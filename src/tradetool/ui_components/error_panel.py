
import streamlit as st
import json
import os
from datetime import datetime

def show_error_log_panel(max_entries=5):
    st.markdown("## ❗ Systeemfouten (laatste fouten)")

    log_path = "logfile.json"
    if not os.path.exists(log_path):
        st.success("✅ Geen fouten geregistreerd.")
        return

    with open(log_path, "r") as f:
        logs = json.load(f)

    if not logs:
        st.success("✅ Geen fouten geregistreerd.")
        return

    recent_logs = logs[-max_entries:]
    for entry in reversed(recent_logs):
        st.markdown(f"""**🕒 Tijd:** `{entry["timestamp"]}`  
**📍 Context:** `{entry["context"]}`  
**❌ Fout:** `{entry["error"]}`""")
"
                    f"**📍 Context:** `{entry['context']}`  
"
                    f"**❌ Fout:** `{entry['error']}`")
        with st.expander("🧠 Stacktrace"):
            st.code(entry["trace"], language="python")
