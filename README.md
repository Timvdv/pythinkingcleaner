# pythinkingcleaner
Library to control ThinkingCleaner devices

## Requirements
- Python >= 3.0

## Install
```
pip install pythinkingcleaner
```

## Example

```python
from pythinkingcleaner import ThinkingCleaner, Discovery
import pprint

discovery = Discovery()
cleaners = discovery.discover()

for device in cleaners:
    print(device.name)
```