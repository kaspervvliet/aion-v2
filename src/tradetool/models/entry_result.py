
from dataclasses import dataclass

@dataclass
class EntryResult:
    asset: str
    direction: str
    confidence: float
    rr: float
    reason: str
    timestamp: str
