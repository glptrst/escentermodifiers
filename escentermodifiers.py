from evdev import UInput, InputDevice, categorize, ecodes

dev = InputDevice('/dev/input/event3')

for event in dev.read_loop():
    if event.type == ecodes.EV_KEY:
        # print(categorize(event))
        # categorize(event).keycode # => 'KEY_BLABLA'
        # categorize(event).keystate # => 0=up, 1=down, 2=hold 
        catev = categorize(event)
        if catev.keycode == 'KEY_RIGHTCTRL' and catev.keystate == 0:
            print('right ctrl UP')
        if catev.keycode == 'KEY_RIGHTCTRL' and catev.keystate == 1:
            print('right ctrl DOWN')
        if catev.keycode == 'KEY_RIGHTCTRL' and catev.keystate == 2:
            print('right ctrl HOLD')
