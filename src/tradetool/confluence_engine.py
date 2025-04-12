
class BaseConfluence:
    def __init__(self, data):
        self.data = data

    def check(self, index):
        raise NotImplementedError("check() moet worden geïmplementeerd door subclasses.")


class SweepDetector(BaseConfluence):
    def check(self, index):
        if index < 1:
            return False
        return self.data[index]["low"] < self.data[index - 1]["low"]


class FVGDetector(BaseConfluence):
    def check(self, index):
        if index < 2:
            return False
        c1 = self.data[index - 2]
        c2 = self.data[index - 1]
        c3 = self.data[index]
        return c2["low"] > c1["high"] and c2["low"] > c3["high"]


class RSIDetector(BaseConfluence):
    def __init__(self, data, threshold=30):
        super().__init__(data)
        self.threshold = threshold
        self._calculate_rsi()

    def _calculate_rsi(self, period=14):
        import pandas as pd
        df = pd.DataFrame(self.data)
        delta = df["close"].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / (loss + 1e-10)
        self.rsi = 100 - (100 / (1 + rs))
        self.rsi = self.rsi.fillna(50).tolist()

    def check(self, index):
        return self.rsi[index] < self.threshold
