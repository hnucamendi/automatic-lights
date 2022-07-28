from yeelight import Bulb
from concurrent.futures import ThreadPoolExecutor
import random
import json
import time

f = open("data.json")
data = json.load(f)

firstLight = data[0]["ip"]
secondLight = data[1]["ip"]
thirdLight = data[2]["ip"]

bulb1 = Bulb(firstLight)
bulb2 = Bulb(secondLight)
bulb3 = Bulb(thirdLight)

bulbs = [
  bulb1,
  bulb2,
  bulb3
]

def flicker(bulb):
  # rand = random.Random(31)
  rand = 3
  for i in range (rand):
    bulb.turn_on()
    # time.sleep(1)
    bulb.turn_off()
    # time.sleep(1)

with ThreadPoolExecutor() as ex:
  for bulb in bulbs:
    ex.submit(flicker,bulb)
