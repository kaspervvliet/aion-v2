
import streamlit as st

def show_pipeline(stage):
    stages = ["📡 Scan", "🧠 Analyse", "🎯 Signal", "📬 Alert", "📓 Learning"]
    highlight = {s: "**" + s + "**" if s == stage else s for s in stages}
    flow = " → ".join([highlight[s] for s in stages])
    st.markdown(f"### 🚦 Status: {flow}")
