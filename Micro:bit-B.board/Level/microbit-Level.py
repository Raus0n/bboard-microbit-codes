x = 0
y = 0

def on_forever():
    global x, y
    x = input.acceleration(Dimension.X)
    y = input.acceleration(Dimension.Y)
    if x > 32:
        basic.show_leds("""
            . . . # #
                        . . . # #
                        . . . # #
                        . . . # #
                        . . . # #
        """)
    elif y > 32:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        # # # # #
                        # # # # #
        """)
    elif x < -32:
        basic.show_leds("""
            # # . . .
                        # # . . .
                        # # . . .
                        # # . . .
                        # # . . .
        """)
    elif y < -32:
        basic.show_leds("""
            # # # # #
                        # # # # #
                        . . . . .
                        . . . . .
                        . . . . .
        """)
    else:
        basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever)
