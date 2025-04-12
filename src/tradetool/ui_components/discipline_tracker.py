
import streamlit as st
import json
import os
from datetime import date

LOG_PATH = "discipline_log.json"

def load_log():
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            return json.load(f)
    return {}

def save_log(log):
    if os.getenv("ENV") != "render":
        with open(LOG_PATH, "w") as f:
            pass  # toegevoegd om Render-crash te voorkomen
        json.dump(log, f, indent=2)

def show_discipline_tracker():
    st.markdown("## ✅ Discipline Tracker")
    today = str(date.today())

    log = load_log()
    today_log = log.get(today, {
        "only_ai_entries": False,
        "followed_tp_sl": False,
        "no_emotional_trades": False,
        "respected_risk": False
    })

    st.markdown(f"### 📅 Vandaag: {json.dumps(today, indent=2)}")

    with st.form("discipline_form"):
        ai = st.checkbox("Alleen AI-entries genomen", value=today_log["only_ai_entries"])
        tp = st.checkbox("SL/TP exact opgevolgd", value=today_log["followed_tp_sl"])
        no_emotion = st.checkbox("Geen emotionele trades", value=today_log["no_emotional_trades"])
        risk = st.checkbox("Risk management gerespecteerd", value=today_log["respected_risk"])

        submitted = st.form_submit_button("Opslaan")
        if submitted:
            log[today] = {
                "only_ai_entries": ai,
                "followed_tp_sl": tp,
                "no_emotional_trades": no_emotion,
                "respected_risk": risk
            }
            save_log(log)
            st.success("✅ Gedragslog opgeslagen!")
