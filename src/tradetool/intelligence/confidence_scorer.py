
def score_entry(entry_result):
    score = 0
    reasons = []

    if entry_result.confidence > 0.8:
        score += 2
        reasons.append("Hoge confidence")
    if entry_result.rr >= 2.0:
        score += 2
        reasons.append("Sterke RR")
    if "bias" in entry_result.reason.lower():
        score += 1
        reasons.append("Bias confluence")
    if entry_result.rr < 1.0:
        score -= 1
        reasons.append("RR onder de 1")

    return score, reasons
