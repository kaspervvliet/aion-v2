
import argparse
from tradetool.data import get_latest_data
from tradetool.strategy_config_loader import load_config
from feedback_logger import FeedbackLogger
from entry_scorer import EntryScorer
from strategy_report import StrategyReportGenerator
from evolution_engine import EvolutionEngine
from rolling_memory import RollingMemory
from strategy_visualizer import StrategyVisualizer

def main():
    parser = argparse.ArgumentParser(description="Start de self-learning trading tool op basis van configuratie.")
    parser.add_argument("--config", type=str, default="strategy_config.json", help="Pad naar strategieconfiguratie")
    args = parser.parse_args()

    # Dummy data ophalen (API-ready)
    data = get_latest_data("SOL/USD")

    # Strategie + instellingen laden
    strategy, config = load_config(args.config, data)

    # Uitvoeren
    entries = strategy.find_entries()

    # Entries scoren
    scorer = EntryScorer()
    scored_entries = scorer.score_entries(entries)

    # Performance meten
    performance = strategy.calculate_performance(scored_entries)

    # Log + rapportage
    logger = FeedbackLogger()
    logger.log_entry_feedback(config["strategy_name"], scored_entries, performance)

    reporter = StrategyReportGenerator()
    reporter.generate_html_report(config["strategy_name"], scored_entries, performance)

    visualizer = StrategyVisualizer()
    visualizer.plot_equity_curve(scored_entries, config["strategy_name"])
    visualizer.plot_rr_distribution(scored_entries, config["strategy_name"])

    print(f"Voltooid: {len(scored_entries)} entries gevonden.")
    print("Performance:", performance)

    # Strategie aanpassen met EvolutionEngine
    evo = EvolutionEngine(config)
    new_config = evo.evolve(performance)

    # Log de aangepaste config (optioneel: overschrijven/bewaren)
    import json
    if os.getenv("ENV") != "render":
        with open("adapted_strategy_config.json", "w") as f:
            pass  # toegevoegd om Render-crash te voorkomen
        json.dump(new_config, f, indent=2)
    print("Aangepaste configuratie opgeslagen als adapted_strategy_config.json")

    # Log sessie in RollingMemory
    from confluence_scorer import ConfluenceScorer
    cs = ConfluenceScorer()
    cs.update(scored_entries)
    memory = RollingMemory()
    memory.log_session(performance, cs.summary())
    print("Rolling memory bijgewerkt.")

if __name__ == "__main__":
    main()
