
class MissedEntryLogger:
    def __init__(self):
        self.missed_entries = []

    def log_missed_entry(self, reason, setup, timestamp):
        """
        Logt waarom een entry niet is genomen (bijv. RR te laag, confidence mismatch).
        """
        missed_entry = {
            "timestamp": timestamp,
            "setup": setup,
            "reason": reason
        }
        self.missed_entries.append(missed_entry)
        print(f"Missed entry logged: {reason} at {timestamp}")

    def get_missed_entries(self):
        """
        Haal de gelogde missed entries op.
        """
        return self.missed_entries

    def clear_missed_entries(self):
        """
        Wis de gelogde missed entries.
        """
        self.missed_entries = []
