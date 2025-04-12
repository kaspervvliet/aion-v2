
from tradetool.models.entry_result import EntryResult
from tradetool.notifications.telegram_alert import send_telegram_alert
from tradetool.intelligence.gpt_annotator import annotate_entry
from tradetool.intelligence.trade_journal import log_entry
from tradetool.intelligence.confidence_scorer import score_entry

def dispatch_execution_signal(entry: EntryResult):
    # Analyseer entry
    score, score_reasons = score_entry(entry)
    annotation = annotate_entry(entry)
    if annotation.startswith('BLOCKED_TAG'):
        print(f'⛔ Entry genegeerd: tag {annotation.split("::")[1]} is tijdelijk geblokkeerd.')
        return

    # Alleen doorgaan bij voldoende score
    if score >= 3:
        log_entry(entry, annotation)
        send_telegram_alert(entry)
        print("✅ Entry doorgestuurd:")
        print(f"Asset: {entry.asset}, Direction: {entry.direction}, Confidence: {entry.confidence}, RR: {entry.rr}")
        print(f"Reden: {entry.reason}")
        print(f"Score: {score} → {'; '.join(score_reasons)}")
        print(f"Annotatie: {annotation}")
    else:
        print("❌ Entry afgewezen op basis van te lage score.")
        print(f"Score: {score} → {'; '.join(score_reasons)}")
