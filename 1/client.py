#!/usr/bin/python3

import pydbus

bus = pydbus.SessionBus()
bus_object = bus.get("cz.mg.example", "/cz/mg/example")
print(bus_object.Love("Millie"))
dir(bus_object)
