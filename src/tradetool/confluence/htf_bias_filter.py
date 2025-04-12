
def htf_bias_filter(entry_direction: str, htf_bias: str) -> bool:
    '''
    entry_direction: "LONG" or "SHORT"
    htf_bias: "bullish", "bearish" or "neutral"
    '''
    if htf_bias == "neutral":
        return False
    if entry_direction == "LONG" and htf_bias == "bullish":
        return True
    if entry_direction == "SHORT" and htf_bias == "bearish":
        return True
    return False
