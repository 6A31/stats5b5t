# 5b5t statistics
API wrapper for 5b5t's statistics

`pip install stats5b5t`

> **Tested on: [Python 3.9](https://www.python.org/downloads/release/python-390)**

## Usage
```py
import stats5b5t

stats = api.Statistics()

r = stats.request("uuidhere")

print(stats.kills(r))
```

## Mudules: api, tools

> **api**
Handles requests and data sorting for you.

> **tools**
Handles debugging and checks for you.
