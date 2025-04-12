
import streamlit as st
import pandas as pd
from datetime import date
import json
import os

def freedom_plan_dashboard():
    st.markdown("# 💸 Freedom Plan Dashboard")
    st.markdown("Stel je eigen pad naar financiële vrijheid samen.")

    # Gebruiker kiest doel en looptijd
    start_balance = st.number_input("Startkapitaal (€)", value=500, min_value=100)
    target_balance = st.number_input("Doelkapitaal (€)", value=200000, min_value=start_balance + 100)
    months = st.slider("Looptijd (maanden)", min_value=6, max_value=36, value=12)

    # Bereken maandelijkse groeifactor
    growth_rate = (target_balance / start_balance) ** (1 / months) - 1

    # Equity groeipad berekening
    balances = [start_balance]
    for i in range(months):
        new_balance = balances[-1] * (1 + growth_rate)
        balances.append(new_balance)

    df = pd.DataFrame({
        "Maand": list(range(0, months + 1)),
        "Verwachte Balans (€)": [round(b, 2) for b in balances]
    })

    st.line_chart(df.set_index("Maand"))

    # Maanddoelen
    st.markdown("## 📆 Maandelijkse doelen")
    for i in range(1, months + 1):
        target = round(balances[i], 2)
        st.markdown(f"**Maand {json.dumps(i, indent=2)}:** streefbalans **€{json.dumps(target, indent=2)}**")

    # Discipline visualisatie
    st.markdown("## ✅ Discipline Check Historie")
    LOG_PATH = "discipline_log.json"
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r") as f:
            log = json.load(f)
        heat_data = {
            date: sum(1 for v in checks.values() if v)
            for date, checks in log.items()
        }
        df_heat = pd.DataFrame(list(heat_data.items()), columns=["Datum", "Aantal Vinkjes"])
        df_heat["Datum"] = pd.to_datetime(df_heat["Datum"])
        df_heat = df_heat.set_index("Datum").resample("D").sum().fillna(0)
        st.bar_chart(df_heat)
    else:
        st.info("Nog geen discipline-activiteit geregistreerd.")
