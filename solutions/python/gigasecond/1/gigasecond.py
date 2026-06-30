"""
Determine the date and time one gigasecond after a certain date.
"""
from datetime import timedelta

def add(moment):
    """
    Arg:
      - moment: datetime
    Return datetime 
    """
    return moment + timedelta(seconds=1e9)
