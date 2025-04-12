
# Self-Learning Trading Tool

Deze trading tool gebruikt Smart Money Concepts, Sweep + FVG entries, en zelflerende modules zoals feedback logging en entry scoring.

## 🚀 Functionaliteiten

- ✅ Strategy framework met class-based structuur
- ✅ CLI launcher met argparse
- ✅ Entry scoring + confidence indicator
- ✅ Feedback logging voor zelflerend vermogen
- ✅ HTML rapportage + visualisaties (equity curve, RR-verdeling)
- ✅ Unittest modules voor strategie, data en scorer

## 🔧 Gebruik

```bash
python auto_mode_launcher.py --symbol SOL/USD --strategy SweepFVGStrategyV1 --interval 15m
```

## 📊 Voorbeeld Output

### Equity Curve
![Equity Curve](charts/SweepFVGStrategyV1_equity_TIMESTAMP.png)

### RR Distributie
![RR Distributie](charts/SweepFVGStrategyV1_rr_dist_TIMESTAMP.png)

## 📁 Structuur

```
├── auto_mode_launcher.py
├── strategy_class_based.py
├── strategy_manager.py
├── strategy_visualizer.py
├── strategy_report.py
├── feedback_logger.py
├── entry_scorer.py
├── data.py
├── tests/
│   ├── test_strategy.py
│   ├── test_data.py
│   └── test_scorer.py
```

## 🧪 Testen

```bash
python -m unittest discover tests
```

## 📝 Logs

Alle feedback logs worden opgeslagen in `/logs`, rapportages in `/reports`, en charts in `/charts`.

---

# Self-Learning Crypto Futures Trading Tool

Deze tool analyseert realtime crypto futures markten (zoals SOL/USD) via de Kraken API met behulp van Smart Money Concepts (SMC) en technische indicatoren. De tool is gebouwd voor maximale autonomie, schaalbaarheid en inzicht.

## 🔧 Functionaliteiten

- ✅ Volledige automatisering van signalen (Sweep, FVG, BOS/CHoCH, OB, RSI)
- ✅ Confidence scoring en performance logging
- ✅ Telegram alerts met entry, TP, SL, RR
- ✅ Zelflerende strategie-adaptatie o.b.v. winst/verlies
- ✅ Equity curve visualisatie en strategy profiler
- ✅ Multi-asset scanning (bijv. SOL, ETH, BTC)
- ✅ Streamlit-dashboard met Apple-achtige stijl
- ✅ Replay engine voor historische training

## 🚀 Gebruik (lokale setup)

1. Clone of unzip de repository:
```bash
unzip my_trading_tool_final.zip
cd my_trading_tool_final
```

2. Installeer afhankelijkheden:
```bash
pip install -r requirements.txt
```

3. Start het dashboard:
```bash
streamlit run dashboard/dashboard.py
```

## 🧠 Voorwaarden & Input

- Zorg voor candle data met kolommen: `timestamp, open, high, low, close`
- Voeg jouw `get_latest_data(symbol)` en `analyze(data)` toe aan `strategy.py`
- Vul jouw Telegram bot token en chat_id in `auto_mode_launcher.py`

## 📂 Mappenstructuur

```
core/              # Strategie-logica
visualization/     # Replay en equity charts
notifications/     # Telegram integratie
dashboard/         # Streamlit UI
auto_mode_launcher.py  # Main auto script
```

---

Deze tool is gebouwd voor serieuze daytraders en strategie-ontwikkelaars. Gebruik hem verstandig. ✌️
