
class EntryScorer:
    def __init__(self, thresholds=None):
        # thresholds bepaalt wat een 'goede' RR of winstkans is
        self.thresholds = thresholds or {"min_rr": 1.5, "min_confidence": 0.7}

    def score_entries(self, entries):
        scored = []
        for entry in entries:
            rr = entry.get("rr", 0)
            confidence = self._calculate_confidence(rr)
            scored.append({
                **entry,
                "confidence_score": confidence,
                "is_valid": confidence >= self.thresholds["min_confidence"],
                "reason": self._get_reason(confidence, rr)
            })
        return scored

    def _calculate_confidence(self, rr):
        # Placeholder: linear scaling van RR naar confidence score
        return min(1.0, max(0.0, rr / 2.5))  # bijv. RR 2.5 = 100% vertrouwen

    def _get_reason(self, confidence, rr):
        if confidence < 0.3:
            return "RR te laag"
        elif confidence < 0.7:
            return "Beperkte winstverwachting"
        else:
            return "Sterke setup"
