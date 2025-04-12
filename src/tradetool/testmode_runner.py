
import streamlit as st
import pandas as pd
from datetime import datetime
from tradetool.intelligence.outcome_tracker import record_entry_outcome
from tradetool.intelligence.adaptive_optimizer import adapt_strategy_from_outcomes
from tradetool.intelligence.outcome_analyzer import analyze_outcomes
from tradetool.intelligence.strategy_optimizer import optimize_strategy_thresholds
from tradetool.intelligence.execution_signal_dispatcher import dispatch_execution_signal
from tradetool.models.entry_result import EntryResult
from tradetool.intelligence.macro_regime_detector import detect_market_regime
from tradetool.filtering.session_filter import is_within_session
from tradetool.confluence.htf_bias_filter import htf_bias_filter

st.title("🧪 TESTMODE: System Self-Check")

# Simuleer candles
mock_candles = pd.DataFrame({
    "timestamp": pd.date_range(end=datetime.now(), periods=50, freq="15min"),
    "open": [100 + i*0.5 for i in range(50)],
    "high": [100 + i*0.5 + 1 for i in range(50)],
    "low": [100 + i*0.5 - 1 for i in range(50)],
    "close": [100 + i*0.5 + (1 if i % 2 == 0 else -1) for i in range(50)],
})

# Test regime detection
regime = detect_market_regime(mock_candles)
st.markdown(f"**🌍 Marktregime gedetecteerd:** `{json.dumps(regime, indent=2)}`")

# Test session
now = datetime.now()
session_ok = is_within_session(now)
st.markdown(f"**🕒 Binnen sessie:** `{json.dumps(session_ok, indent=2)}`")

# Test HTF bias
bias_ok = htf_bias_filter("LONG", "bullish")
st.markdown(f"**📈 HTF bias check (LONG + bullish):** `{json.dumps(bias_ok, indent=2)}`")

# Simuleer een entry
entry = EntryResult(
    asset="SOL/USD",
    direction="LONG",
    confidence=0.92,
    rr=2.1,
    reason="sweep + FVG + HTF confluence",
    timestamp=now.isoformat()
)

# Test dispatch + log
st.markdown("**📤 Dispatch testentry...**")
dispatch_execution_signal(entry)

# Log een uitkomst
record_entry_outcome(entry_id="test123", result="TP", realized_rr=2.1)

# Analyse outcomes
st.markdown("**📊 Outcome analyse:**")
stats = analyze_outcomes()
st.json(stats)

# Test optimizer response
st.markdown("**⚙️ Strategy optimizer check:**")
optimize_strategy_thresholds()
adapt_strategy_from_outcomes()
st.success("✅ Testmode completed.")
