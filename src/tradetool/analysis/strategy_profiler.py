
import streamlit as st
import pandas as pd

def profile_strategies(journal_path="trade_journal.json"):
    try:
        df = pd.read_json(journal_path)
    except Exception:
        st.warning("Geen journalgegevens gevonden.")
        return

    if df.empty:
        st.info("Er zijn nog geen entries gelogd.")
        return

    grouped = df.groupby("annotation").agg({
        "rr": ["mean", "count"],
        "confidence": "mean"
    }).sort_values(("rr", "mean"), ascending=False)

    grouped.columns = ["Gemiddelde RR", "Aantal Trades", "Gem. Confidence"]
    st.markdown("## 🧠 Strategieprofiler")
    st.dataframe(grouped.style.format("{:.2f}"))

    best = grouped.iloc[0]
    print("Strategie analyse voltooid")

"
               f"- RR: {best['Gemiddelde RR']:.2f}
"
               f"- Trades: {int(best['Aantal Trades'])}
"
               f"- Confidence: {best['Gem. Confidence']:.2f}")
