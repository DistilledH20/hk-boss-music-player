if input.pin_is_pressed(TouchPin.P0):
    pass

def on_forever():
    while input.pin_is_pressed(TouchPin.P1):
        pass
basic.forever(on_forever)
