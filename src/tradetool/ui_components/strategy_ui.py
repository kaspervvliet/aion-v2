
import streamlit as st
from tradetool.strategy_registry import get_registered_strategies

def strategy_control_panel():
    strategies = get_registered_strategies()
    strategy_name = st.selectbox("📌 Kies strategie", list(strategies.keys()))
    confidence_threshold = st.slider("🎯 Min. confidence", 0.0, 1.0, 0.5, 0.05)
    rr_threshold = st.slider("📈 Min. risk/reward", 0.5, 5.0, 1.5, 0.1)
    return strategy_name, confidence_threshold, rr_threshold
