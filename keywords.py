import re

def keyword_score(text, keywords):
    if not text or not keywords:
        return 1

    text = text.lower()

    matched = 0
    used_keywords = set()

    for kw in keywords:
        kw = kw.lower().strip()

        # Exact word or phrase match
        pattern = r'\b' + re.escape(kw) + r'\b'
        if re.search(pattern, text):
            matched += 1
            used_keywords.add(kw)

    coverage = matched / len(keywords)

    # Map coverage to 1–5 scale
    if coverage >= 0.9:
        score = 5
    elif coverage >= 0.7:
        score = 4
    elif coverage >= 0.5:
        score = 3
    elif coverage >= 0.3:
        score = 2
    else:
        score = 1

    return score
