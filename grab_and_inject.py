# Grab input input events with dev.grab() and then inject them with UInput

from evdev import UInput, InputDevice, categorize, ecodes

dev = InputDevice('/dev/input/event3')
ui = UInput()

dev.grab()
# when dev.ungrab() ?

for event in dev.read_loop():
    catev = categorize(event)
    if event.type == ecodes.EV_KEY:
        print(categorize(event))
        if catev.keystate == 1:
            ui.write(ecodes.EV_KEY, ecodes.ecodes[categorize(event).keycode], 1)
            ui.syn()
        elif catev.keystate == 0:
            ui.write(ecodes.EV_KEY, ecodes.ecodes[categorize(event).keycode], 0)
            ui.syn()
        elif catev.keystate == 2:
            ui.write(ecodes.EV_KEY, ecodes.ecodes[categorize(event).keycode], 2)
            ui.syn()
