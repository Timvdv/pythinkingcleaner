from pythinkingcleaner import ThinkingCleaner, Discovery
import pprint

discovery = Discovery()
cleaners = discovery.discover()

for device in cleaners:
    print(device.name)