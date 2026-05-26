#  1) Convert a series of date-strings to a timeseries?

import pandas as pd

dates = ['2026-05-26','2020-05-27','2026-05-28']

ts = pd.to_datetime(dates)
print(ts)
print(type(ts))