import pandas as pd
from datetime import timedelta

def parse_duration(dur):
    if pd.isnull(dur):
        return timedelta(0)
    dur = str(dur).strip()
    hours = 0
    minutes = 0
    if 'h' in dur:
        hours = int(dur.split('h')[0].strip())
        dur = dur.split('h')[1]
    if 'm' in dur:
        minutes = int(dur.replace('m', '').strip())
    return timedelta(hours=hours, minutes=minutes)
