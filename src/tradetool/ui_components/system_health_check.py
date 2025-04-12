
import streamlit as st
import pandas as pd
from datetime import datetime
from tradetool.intelligence.macro_regime_detector import detect_market_regime
from tradetool.filtering.session_filter import is_within_session
from tradetool.confluence.htf_bias_filter import htf_bias_filter

def show_system_health():
    st.markdown("## 🧠 System Health Check")

    try:
        candles = pd.DataFrame({
            "timestamp": pd.date_range(end=datetime.now(), periods=50, freq="15min"),
            "open": [100 + i*0.5 for i in range(50)],
            "high": [100 + i*0.5 + 1 for i in range(50)],
            "low": [100 + i*0.5 - 1 for i in range(50)],
            "close": [100 + i*0.5 + (1 if i % 2 == 0 else -1) for i in range(50)],
        })

        regime = detect_market_regime(candles)
        session_ok = is_within_session(datetime.now())
        bias_ok = htf_bias_filter("LONG", "bullish")

        checks = {
            "Regime Detection": regime in ["stable", "volatile", "extreme"],
            "Session Filter": session_ok,
            "HTF Bias Filter": bias_ok
        }

        all_ok = all(checks.values())
        if all_ok:
            st.success("✅ Alle systemen operationeel")
        else:
            st.warning("⚠️ Sommige modules geven foutstatus")

        for label, ok in checks.items():
            icon = "✅" if ok else "❌"
            st.markdown(f"- {json.dumps(icon, indent=2)} {json.dumps(label, indent=2)}")

    except Exception as e:
        st.error(f"❌ Systeemcheck mislukt: {json.dumps(e, indent=2)}")
