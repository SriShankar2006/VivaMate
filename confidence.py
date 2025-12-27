import re

def confidence_score(spoken_text, total_time=30):
    if not spoken_text or not spoken_text.strip():
        return 1

    text = spoken_text.lower().strip()
    words = text.split()
    word_count = len(words)

    # Estimated speaking duration (150 WPM ≈ 2.5 words/sec)
    speech_duration_est = word_count / 2.5
    ratio = speech_duration_est / total_time

    # Filler words reduce confidence
    filler_words = ['um', 'uh', 'like', 'you know', 'actually']
    filler_count = sum(text.count(fw) for fw in filler_words)

    # Assertive words increase confidence
    assertive_words = [
        'is', 'are', 'will', 'can', 'does', 'clearly',
        'definitely', 'important', 'main'
    ]
    assertive_count = sum(text.count(w) for w in assertive_words)

    # Base score from speaking ratio
    if ratio >= 0.8:
        score = 5
    elif ratio >= 0.6:
        score = 4
    elif ratio >= 0.4:
        score = 3
    elif ratio >= 0.2:
        score = 2
    else:
        score = 1

    # Penalties
    if word_count < 10:
        score -= 1

    if filler_count >= 3:
        score -= 1

    # Bonus
    if assertive_count >= 3:
        score += 1

    # Clamp score between 1 and 5
    return max(1, min(5, score))
