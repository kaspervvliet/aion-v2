
class GPTValidator:
    def __init__(self):
        pass

    def explain_entry(self, entry):
        reasons = []
        if "Sweep" in entry.get("confluences", []):
            reasons.append("deze candle heeft een duidelijke sweep van de vorige low")
        if "FVG" in entry.get("confluences", []):
            reasons.append("er is een fair value gap na de sweep, wat duidt op momentum")
        if "RSI" in entry.get("confluences", []):
            reasons.append("de RSI zat onder de 30, dus we verwachten een retracement")

        rr = entry.get("rr", 0)
        if rr >= 2:
            reasons.append(f"de RR is gunstig ({rr:.2f}) wat het risico waard lijkt")

        if not reasons:
            return "Er zijn geen duidelijke confluences gedetecteerd."

        return "Deze entry is valide omdat " + " en ".join(reasons) + "."

    def explain_all(self, entries):
        for entry in entries:
            entry["gpt_explanation"] = self.explain_entry(entry)
        return entries
