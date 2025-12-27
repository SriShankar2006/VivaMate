import re

def clarity_score(spoken_text):
    if not spoken_text or not spoken_text.strip():
        return 1

    text = spoken_text.lower().strip()

    # Split sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if len(s.split()) >= 4]

    if not sentences:
        return 1

    sentence_count = len(sentences)

    # Average sentence length
    avg_words = sum(len(s.split()) for s in sentences) / sentence_count

    # Filler words check
    filler_words = ['um', 'uh', 'like', 'you know', 'actually']
    filler_count = sum(text.count(fw) for fw in filler_words)

    # Base score from sentence count
    if sentence_count >= 4:
        score = 5
    elif sentence_count == 3:
        score = 4
    elif sentence_count == 2:
        score = 3
    else:
        score = 2

    # Adjust score based on clarity factors
    if avg_words < 5 or avg_words > 25:
        score -= 1

    if filler_count >= 3:
        score -= 1

    # Clamp score between 1 and 5
    return max(1, min(5, score))
