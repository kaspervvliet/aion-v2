
# 🧠 AI Trading Tool – Self-Learning Strategy Engine

Deze tool is ontworpen om jou te voorzien van 100% autonome signalen: entries, TP/SL en RR worden bepaald door AI — op basis van confluence, bias, confidence en performance learning.

⚠️ **De AI plaatst geen orders. Jij behoudt de controle.**

---

## 🔧 Belangrijkste Modules

| Module | Omschrijving |
|--------|--------------|
| `auto_mode_dashboard.py` | Streamlit-dashboard voor live signalen |
| `strategy_registry.py` | Registreert strategieën via decorator |
| `strategies/` | Bevat je strategie-plug-ins (zoals Sweep + FVG) |
| `ui_components/` | Visuele onderdelen zoals stats, pipeline, buttons |
| `intelligence/` | GPT-annotatie, scorer, optimizer, execution dispatcher |
| `analysis/` | Profiler, equity visualizer |
| `performance/` | Async scanner, cache engine |
| `notifications/` | Telegram alerts |
| `models/` | `EntryResult` dataclass |

---

## 📦 Installatie

```bash
git clone <repo-url>
cd final_trading_tool
pip install -e .
cp .env.example .env
```

Vul je `.env` in met:
- OpenAI API key
- Telegram bot token & chat ID
- (eventueel Kraken/Blofin keys in de toekomst)

---

## 🚀 Gebruik

```bash
streamlit run src/tradetool/auto_mode_dashboard.py
```

---

## ✅ Features

- Auto-signalering op basis van SMC / Sweep / FVG
- GPT-uitleg bij entries
- Trade journal logging
- Realtime bias + RR filtering
- Strategy optimizer op basis van eigen performance
- Telegram notificaties
- Replay engine en equity visualizer
