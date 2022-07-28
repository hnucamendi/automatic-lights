from yeelight import Bulb
from concurrent.futures import ThreadPoolExecutor
import random
import json
import time

f = open("data.json")
data = json.load(f)

bulb1 = Bulb(data[0]["ip"])
bulb2 = Bulb(data[1]["ip"])
bulb3 = Bulb(data[2]["ip"])

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
    bulb.turn_on(effect="smooth")
    bulb.set_rgb(255,255,255)
    time.sleep(1)
    bulb.turn_off()
    print(i)

with ThreadPoolExecutor() as ex:
  for bulb in bulbs:
    time.sleep(1.5)
    ex.submit(flicker,bulb)
