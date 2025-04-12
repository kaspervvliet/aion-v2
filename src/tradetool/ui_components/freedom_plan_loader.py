
import streamlit as st

def load_freedom_plan():
    enabled = st.sidebar.checkbox("📊 Toon Freedom Plan", value=False)
    if enabled:
        from tradetool.ui_components.freedom_plan import freedom_plan_dashboard
        freedom_plan_dashboard()
