
from datetime import datetime, time

def is_within_session(now: datetime, session_range=(time(13, 0), time(17, 0))) -> bool:
    '''
    Check if current time is within active session (default = NY session 13:00–17:00)
    '''
    start, end = session_range
    return start <= now.time() <= end
