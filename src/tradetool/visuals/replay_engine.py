
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

def replay_candles(candles: pd.DataFrame, entry_index: int = None, delay=0.3):
    st.markdown("## 🔁 Entry Replay Engine")
    max_index = len(candles)
    play = st.button("▶️ Start Replay")
    step = st.slider("⏩ Speed (sec)", 0.1, 1.0, delay)

    if play:
        chart_placeholder = st.empty()
        for i in range(30, max_index + 1):
            subset = candles.iloc[:i]
            fig, ax = plt.subplots()
            ax.plot(subset["timestamp"], subset["close"], label="Close")
            if entry_index and i >= entry_index:
                ax.axvline(x=candles.iloc[entry_index]["timestamp"], color="green", linestyle="--", label="ENTRY")
            ax.set_title("Candle Replay")
            ax.legend()
            chart_placeholder.pyplot(fig)
            time.sleep(step)
