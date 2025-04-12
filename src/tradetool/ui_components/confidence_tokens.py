
import streamlit as st

def show_confidence_level(level):
    if level == "low":
        st.markdown("🔘 **Confidence: Laag**")
    elif level == "medium":
        st.markdown("🟡 **Confidence: Gemiddeld**")
    elif level == "high":
        st.markdown("🟢 **Confidence: Hoog 🔥**")
    else:
        st.markdown("⚪ **Confidence: Onbekend**")
