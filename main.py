from yeelight import Bulb
import json
import time

f = open("data.json")
data = json.load(f)

# print(yeelight.discover_bulbs())
# print(data[0]["ip"])

firstLight = data[0]["ip"]
secondLight = data[1]["ip"]
thirdLight = data[2]["ip"]

bulb1 = Bulb(firstLight)
bulb2 = Bulb(secondLight)
bulb3 = Bulb(thirdLight)

def flicker(bulb):
  for i in range (10):
    bulb.turn_on()
    time.sleep(1)
    bulb.turn_off()
    time.sleep(1)


flicker(bulb1)
flicker(bulb2)
flicker(bulb3)
