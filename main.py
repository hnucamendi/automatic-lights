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
  rand1 = random.randint(0,256)
  rand2 = random.randint(0,256)
  rand3 = random.randint(0,256)
  print(rand1,rand2,rand3)
  # bulb.set_rgb(rand1,rand2,rand3)
  for i in range (3):
    bulb.turn_on(effect="smooth")
    bulb.set_rgb(rand1,rand2,rand3)
    time.sleep(5)
    bulb.turn_off()
    time.sleep(5)

with ThreadPoolExecutor() as ex:
  for bulb in bulbs:
    time.sleep(1.5)
    ex.submit(flicker,bulb)
