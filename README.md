# 5b5t statistics
API wrapper for 5b5t's statistics

`pip install stats5b5t`

*Tested on: Python 3.9*

## Usage
```py
import stats5b5t

stats = api.Statistics()

r = stats.request("uuidhere")

print(stats.kills(r))