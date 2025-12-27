import re

def fluency_score(spoken_text, duration=30):
    if not spoken_text or not spoken_text.strip():
        return 1

    text = spoken_text.lower().strip()
    words = text.split()
    word_count = len(words)

    if word_count < 5:
        return 1

    # Words per minute
    wpm = (word_count / duration) * 60

    # Filler words reduce fluency
    filler_words = ['um', 'uh', 'like', 'you know', 'actually']
    filler_count = sum(text.count(fw) for fw in filler_words)

    # Repetition penalty (same word repeated continuously)
    repetitions = sum(
        1 for i in range(1, len(words)) if words[i] == words[i - 1]
    )

    # Base score from WPM
    if 120 <= wpm <= 160:
        score = 5
    elif 100 <= wpm < 120 or 160 < wpm <= 180:
        score = 4
    elif 80 <= wpm < 100:
        score = 3
    elif 60 <= wpm < 80:
        score = 2
    else:
        score = 1

    # Penalties
    if filler_count >= 3:
        score -= 1

    if repetitions >= 3:
        score -= 1

    # Clamp score
    return max(1, min(5, score))
