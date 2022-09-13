
basic.show_string("Truth or Dare! Press A to play. Press B to pick somebody!", 100)
def on_button_pressed_a():
    global pick_stuff
    pick_stuff = randint(0, 1)
    if pick_stuff == 0:
        basic.show_string("Truth")
    else:
        basic.show_string("Dare")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global arrowpoint
    basic.clear_screen()
    arrowpoint = randint(0, 3)
    if arrowpoint == 1:
        basic.show_leds("""
            . . # . .
                        . . . # .
                        # # # . #
                        . . . # .
                        . . # . .
        """)
        basic.clear_screen()
    elif arrowpoint == 2:
        basic.show_leds("""
            . . # . .
                        . # . . .
                        # . # # #
                        . # . . .
                        . . # . .
        """)
        basic.clear_screen()
    elif arrowpoint == 3:
        basic.show_leds("""
            . . # . .
                        . # . # .
                        # . # . #
                        . . # . .
                        . . # . .
                """)
        basic.clear_screen()
    else:
        basic.show_leds("""
                    . . # . .
                                . # . # .
                                # . # . #
                                . . # . .
                                . . # . .
                        """)
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

arrowpoint = 0
pick_stuff = 0