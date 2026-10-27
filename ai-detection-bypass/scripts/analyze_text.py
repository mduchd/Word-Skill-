"""
analyze_text.py (Bản Nâng Cấp: Quét Chỉ Số & Ký Tự Cấm AI)
──────────────────────────────────────────────────────────
Phân tích văn bản (tiếng Việt & tiếng Anh) để đo lường các chỉ số AI Detection:
- Độ biến thiên độ dài câu (Burstiness score / Standard Deviation)
- Tỷ lệ câu Ngắn - Trung bình - Dài (so với chuẩn 30-50-20)
- Mật độ từ cấm AI (Transition words, AI vocabulary)
- QUÉT CÁC KÝ TỰ CẤM CỦA AI: Emoji, Dấu gạch ngang Em Dash (—), In đậm lắt nhắt (**...**), Ký tự mũi tên (→, =>)
- Đánh giá chỉ số rủi ro phát hiện AI (AI Risk Index: 0% - 100%)

Cách dùng:
    python analyze_text.py input.txt
    python analyze_text.py input.md
"""

import sys
import re
import math
from pathlib import Path

# Đảm bảo stdout hỗ trợ UTF-8 trên Windows console
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

# Danh sách từ nối / từ đặc trưng AI (tiếng Việt & tiếng Anh)
AI_PATTERNS_VI = [
    r"\bhơn nữa\b", r"\bbên cạnh đó\b", r"\bngoài ra\b", r"\btuy nhiên\b",
    r"\bnhìn chung\b", r"\btóm lại\b", r"\btrong bối cảnh hiện nay\b",
    r"\bđóng vai trò quan trọng\b", r"\bkhông thể phủ nhận\b",
    r"\bthực tế cho thấy rằng\b", r"\bđiều này cho thấy rằng\b",
    r"\bphát triển bền vững\b", r"\bgiải pháp toàn diện\b",
    r"\bcần phải\b", r"\bđáng chú ý là\b"
]

AI_PATTERNS_EN = [
    r"\bfurthermore\b", r"\badditionally\b", r"\bmoreover\b", r"\bdelve\b",
    r"\brobust\b", r"\bleverage\b", r"\bcomprehensive\b", r"\butilize\b",
    r"\bpivotal\b", r"\bfoster\b", r"\btestament\b", r"\bin today's world\b",
    r"\bit is important to\b", r"\bin conclusion\b", r"\bstreamline\b"
]


def split_sentences(text: str) -> list[str]:
    """Tách câu dựa trên dấu câu kết thúc (. ! ? và ngắt dòng)."""
    cleaned = re.sub(r"(TP|PGS|TS|ThS|GS|BS|KS|Th\.|Dr|Prof)\.", r"\1<DOT>", text)
    sentences = re.split(r"[.!?\n]+", cleaned)
    result = []
    for s in sentences:
        s = s.replace("<DOT>", ".").strip()
        if len(s) > 3 and any(c.isalnum() for c in s):
            result.append(s)
    return result


def analyze_burstiness(sentences: list[str]) -> dict:
    """Đo độ biến thiên độ dài câu (Burstiness)."""
    lengths = [len(s.split()) for s in sentences]
    if not lengths:
        return {"avg": 0, "std_dev": 0, "short": 0, "med": 0, "long": 0}

    avg = sum(lengths) / len(lengths)
    variance = sum((x - avg) ** 2 for x in lengths) / len(lengths)
    std_dev = math.sqrt(variance)

    # Phân loại độ dài: Ngắn (<10), Trung bình (10-25), Dài (>25)
    short_cnt = sum(1 for l in lengths if l < 10)
    med_cnt   = sum(1 for l in lengths if 10 <= l <= 25)
    long_cnt  = sum(1 for l in lengths if l > 25)
    total     = len(lengths)

    return {
        "avg": round(avg, 1),
        "std_dev": round(std_dev, 2),
        "short_pct": round(short_cnt / total * 100, 1),
        "med_pct": round(med_cnt / total * 100, 1),
        "long_pct": round(long_cnt / total * 100, 1),
        "lengths": lengths
    }


def find_ai_keywords(text: str) -> dict:
    """Quét các từ khóa có nguy cơ bị detector bắt."""
    lower_text = text.lower()
    matches = {}
    for pat in AI_PATTERNS_VI + AI_PATTERNS_EN:
        found = re.findall(pat, lower_text)
        if found:
            word = pat.replace(r"\b", "")
            matches[word] = len(found)
    return matches


def find_ai_symbols(text: str) -> dict:
    """Quét các ký tự đặc trưng mà AI hay lạm dụng."""
    symbols_found = {}

    # 1. Quét Emoji
    emojis = re.findall(r"[\U00010000-\U0010ffff]|[\u2600-\u27ff]", text)
    if emojis:
        symbols_found["Emoji"] = len(emojis)

    # 2. Dấu gạch ngang dài Em Dash (—) hoặc En Dash (–)
    em_dashes = text.count("—") + text.count("–")
    if em_dashes > 2:
        symbols_found["Dấu gạch ngang Em Dash (—/–)"] = em_dashes

    # 3. Ký tự mũi tên suy luận
    arrows = len(re.findall(r"→|=>|->|⇒", text))
    if arrows > 0:
        symbols_found["Ký tự mũi tên (→, =>)"] = arrows

    # 4. In đậm lắt nhắt giữa câu (**...**)
    inline_bolds = len(re.findall(r"[^\n#]+\*\*[^*]+\*\*", text))
    if inline_bolds > 3:
        symbols_found["In đậm lắt nhắt giữa câu (**...**)"] = inline_bolds

    # 5. Dấu & viết tắt
    ampersands = len(re.findall(r"\b\w+\s*&\s*\w+\b", text))
    if ampersands > 0:
        symbols_found["Dấu '&' viết tắt"] = ampersands

    return symbols_found


def calculate_risk(burst: dict, keywords: dict, symbols: dict, total_words: int) -> tuple[int, list[str]]:
    """Tính điểm rủi ro AI (0% - 100%) và đưa ra cảnh báo."""
    risk = 0
    feedback = []

    # 1. Đánh giá Burstiness
    if burst["std_dev"] < 4.5:
        risk += 30
        feedback.append("[!] Câu có độ dài quá đều nhau (StdDev < 4.5). Cần đan xen câu rất ngắn (<8 từ) và câu ghép dài.")
    elif burst["std_dev"] < 6.5:
        risk += 15
        feedback.append("[*] Độ biến thiên độ dài câu ở mức trung bình. Nên thêm 1-2 câu ngắn tạo nhịp ngắt.")
    else:
        feedback.append("[OK] Độ biến thiên câu (Burstiness) tốt, tự nhiên như người viết.")

    # 2. Đánh giá tỷ lệ câu ngắn
    if burst["short_pct"] < 15:
        risk += 15
        feedback.append("[!] Quá ít câu ngắn (<15%). Văn bản thiếu nhịp thở tự nhiên, dễ bị cờ là do AI viết.")

    # 3. Mật độ từ khóa AI
    total_ai_words = sum(keywords.values())
    density = (total_ai_words / max(total_words, 1)) * 100
    if density > 1.5:
        risk += 30
        feedback.append(f"[!] Mật độ từ cấm AI cao ({round(density, 2)}% từ ngữ lặp đi lặp lại: {list(keywords.keys())[:5]}).")
    elif density > 0.8:
        risk += 15
        feedback.append(f"[*] Xuất hiện nhiều từ nối/từ vựng AI đặc trưng ({round(density, 2)}%).")

    # 4. Đánh giá Ký tự cấm AI
    if "Emoji" in symbols:
        risk += 30
        feedback.append(f"[NGHIÊM TRỌNG] Phát hiện {symbols['Emoji']} emoji trong văn bản. Báo cáo học thuật/công vụ tuyệt đối KHÔNG dùng emoji!")
    if "Dấu gạch ngang Em Dash (—/–)" in symbols:
        risk += 15
        feedback.append(f"[!] Lạm dụng {symbols['Dấu gạch ngang Em Dash (—/–)']} dấu gạch ngang Em Dash (—). Tiếng Việt người thật hay dùng dấu phẩy hoặc ngoặc đơn.")
    if "In đậm lắt nhắt giữa câu (**...**)" in symbols:
        risk += 15
        feedback.append(f"[!] Phát hiện {symbols['In đậm lắt nhắt giữa câu (**...**)']} cụm in đậm lắt nhắt giữa câu. Người thật chỉ in đậm tiêu đề hoặc số liệu tổng.")
    if "Ký tự mũi tên (→, =>)" in symbols:
        risk += 10
        feedback.append(f"[*] Phát hiện {symbols['Ký tự mũi tên (→, =>)']} ký tự mũi tên. Hãy thay bằng chữ 'dẫn đến' hoặc 'từ đó'.")

    # Giới hạn risk từ 0 đến 100
    risk = min(max(risk, 5), 95)
    return risk, feedback


def main():
    if len(sys.argv) < 2:
        print("Sử dụng: python analyze_text.py <duong_dan_file>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"Lỗi: Không tìm thấy file {file_path}")
        sys.exit(1)

    text = file_path.read_text(encoding="utf-8")
    words = text.split()
    sentences = split_sentences(text)

    if not sentences:
        print("Văn bản quá ngắn để phân tích.")
        sys.exit(0)

    burst = analyze_burstiness(sentences)
    keywords = find_ai_keywords(text)
    symbols = find_ai_symbols(text)
    risk, feedback = calculate_risk(burst, keywords, symbols, len(words))

    print("\n" + "=" * 60)
    print(" KẾT QUẢ PHÂN TÍCH CHỈ SỐ AI DETECTION & KÝ TỰ CẤM")
    print("=" * 60)
    print(f"  Tổng số từ: {len(words)} từ | Tổng số câu: {len(sentences)} câu")
    print(f"  Độ dài câu trung bình: {burst['avg']} từ/câu")
    print(f"  Độ biến thiên câu (Burstiness StdDev): {burst['std_dev']} (Chuẩn người viết: > 7.0)")
    print(f"   • Câu ngắn (<10 từ): {burst['short_pct']}% (Khuyến nghị: 25-30%)")
    print(f"   • Câu trung bình (10-25 từ): {burst['med_pct']}% (Khuyến nghị: 45-55%)")
    print(f"   • Câu dài (>25 từ): {burst['long_pct']}% (Khuyến nghị: 15-20%)")

    print("\n TỪ KHÓA / TỪ NỐI AI ĐƯỢC PHÁT HIỆN:")
    if keywords:
        for w, count in keywords.items():
            print(f"   - '{w}': xuất hiện {count} lần")
    else:
        print("   [OK] Không phát hiện từ khóa AI đặc trưng.")

    print("\n KÝ TỰ & DẤU CÂU CẤM ĐƯỢC PHÁT HIỆN:")
    if symbols:
        for s, count in symbols.items():
            print(f"   - {s}: {count} lần")
    else:
        print("   [OK] Không phát hiện emoji, mũi tên hay ký tự AI cấm.")

    print("\n" + "-" * 60)
    print(f" CHỈ SỐ RỦI RO BỊ AI DETECTOR PHÁT HIỆN: {risk}%")
    if risk >= 60:
        print("   [NGUY CƠ CAO] - Cần dọn dẹp ký tự cấm và viết lại theo chiến lược Full Paraphrase.")
    elif risk >= 35:
        print("   [NGUY CƠ TRUNG BÌNH] - Nên xóa các ký tự thừa, chỉnh sửa các câu nối và đan xen câu ngắn.")
    else:
        print("   [AN TOÀN] - Văn phong tự nhiên, perplexity, burstiness & ký tự đạt chuẩn.")

    print("\n KHUYẾN NGHỊ CHỈNH SỬA:")
    for fb in feedback:
        print(f"   {fb}")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
