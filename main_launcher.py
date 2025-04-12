import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import streamlit as st
import json

from tradetool.auto_mode_launcher import run_auto_mode
from tradetool.strategy_config_loader import load_config
from tradetool.gpt_validator import validate_strategy
from tradetool.strategy_report_generator import generate_report
from tradetool.streamlit_dashboard import launch_dashboard

st.set_page_config(page_title="Trading Tool Launcher", layout="wide")

st.title("🚀 Self-Learning Trading Tool – Main Launcher")

menu = st.sidebar.radio("Kies een actie", [
    "🔁 Auto Mode Analyse",
    "📊 Streamlit Dashboard",
    "📑 Strategie Rapport",
    "🤖 GPT Validatie",
])

config = load_config("src/tradetool/configs/strategy_config.json")

if menu == "🔁 Auto Mode Analyse":
    st.subheader("Auto Mode Strategie Analyse")
    run_auto_mode(config)

elif menu == "📊 Streamlit Dashboard":
    st.subheader("Visueel Dashboard")
    launch_dashboard(config)

elif menu == "📑 Strategie Rapport":
    st.subheader("Rapportage Genereren")
    report = generate_report(config)
    st.text(report)

elif menu == "🤖 GPT Validatie":
    st.subheader("Strategie Feedback van GPT")
    feedback = validate_strategy(config)
    st.markdown(f"**GPT Feedback:** {json.dumps(feedback, indent=2)}")
