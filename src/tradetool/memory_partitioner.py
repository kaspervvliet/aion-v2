
class MemoryPartitioner:
    def __init__(self, training_data, live_data):
        self.training_data = training_data
        self.live_data = live_data

    def separate_data(self):
        """
        Scheidt backtest-data (training) van live-data.
        Dit zorgt ervoor dat de modelupdates alleen op live-data gebeuren.
        """
        print("Seperating training and live data...")
        return self.training_data, self.live_data

    def get_live_data(self):
        return self.live_data

    def get_training_data(self):
        return self.training_data
