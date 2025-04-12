from tradetool.ui_components.error_panel import show_error_log_panel
from tradetool.ui_components.system_health_check import show_system_health

import streamlit as st
from datetime import datetime
import pandas as pd

from tradetool.ui_components.strategy_ui import strategy_control_panel
from tradetool.models.entry_result import EntryResult
from tradetool.intelligence.execution_signal_dispatcher import dispatch_execution_signal
from tradetool.strategies.sweep_fvg import sweep_fvg_strategy
from tradetool.strategy_registry import get_registered_strategies
from tradetool.confluence.htf_bias_filter import htf_bias_filter
from tradetool.filtering.session_filter import is_within_session
from tradetool.intelligence.macro_regime_detector import detect_market_regime

st.set_page_config(page_title="Auto Mode Dashboard", layout="wide")
st.title("🧠 AUTO MODE CONTROL CENTER")
show_system_health()
show_error_log_panel()

strategy_name, conf_threshold, rr_threshold = strategy_control_panel()

mock_data = {
    "candles": pd.DataFrame({
        "timestamp": pd.date_range(end=datetime.now(), periods=50, freq="15min"),
        "open": [100 + i*0.5 for i in range(50)],
        "high": [100 + i*0.5 + 1 for i in range(50)],
        "low": [100 + i*0.5 - 1 for i in range(50)],
        "close": [100 + i*0.5 + (1 if i % 2 == 0 else -1) for i in range(50)],
    })
}

htf_bias = "bullish"
now = datetime.now()

# Detecteer marktomstandigheden
regime = detect_market_regime(mock_data["candles"])

if regime == "extreme":
    st.warning("🌪️ Marktregime: EXTREME – Auto Mode gepauzeerd.")
    st.stop()
elif regime == "volatile":
    st.info("⚠️ Marktregime: VOLATILE – Alleen high-confidence entries worden toegelaten.")
else:
    st.success("✅ Marktregime: STABLE")

# Analyse en entry-logica
strategies = get_registered_strategies()
strategy_func = strategies[strategy_name]
result = strategy_func({}, mock_data)

if not result or "entries" not in result or not result["entries"]:
    st.info("📭 Geen entry gevonden door deze strategie.")
else:
    for entry in result["entries"]:
        if entry["confidence"] >= conf_threshold and entry["rr"] >= rr_threshold:
            e = EntryResult(
                asset=entry["asset"],
                direction="LONG",
                confidence=entry["confidence"],
                rr=entry["rr"],
                reason=result.get("bias", "Bias onbekend"),
                timestamp=now.isoformat()
            )

            if not htf_bias_filter(e.direction, htf_bias):
                st.warning("⛔ Entry geweigerd door HTF-bias mismatch.")
                continue

            if not is_within_session(now):
                st.warning("⏱️ Entry buiten actieve sessie.")
                continue

            st.success("🎯 ENTRY GEVONDEN!")
            st.markdown(
                f"- **Asset:** `{e.asset}`\n"
                f"- **Confidence:** `{e.confidence}`\n"
                f"- **RR:** `{e.rr}`\n"
                f"- **Bias:** `{e.reason}`\n"
                f"- **Tijd:** `{e.timestamp}`"
            )

            dispatch_execution_signal(e)
        else:
            st.warning("⚠️ Entry afgewezen – onvoldoende confidence of RR.")
