basic.showString("Truth or Dare! Press A to play. Press B to pick somebody!", 100)
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    pick_stuff = randint(0, 1)
    if (pick_stuff == 0) {
        basic.showString("Truth")
    } else {
        basic.showString("Dare")
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    basic.clearScreen()
    arrowpoint = randint(0, 3)
    if (arrowpoint == 1) {
        basic.showLeds(`
            . . # . .
                        . . . # .
                        # # # . #
                        . . . # .
                        . . # . .
        `)
        basic.clearScreen()
    } else if (arrowpoint == 2) {
        basic.showLeds(`
            . . # . .
                        . # . . .
                        # . # # #
                        . # . . .
                        . . # . .
        `)
        basic.clearScreen()
    } else if (arrowpoint == 3) {
        basic.showLeds(`
            . . # . .
                        . # . # .
                        # . # . #
                        . . # . .
                        . . # . .
                `)
        basic.clearScreen()
    } else {
        basic.showLeds(`
                    . . # . .
                                . # . # .
                                # . # . #
                                . . # . .
                                . . # . .
                        `)
    }
    
    basic.clearScreen()
})
let arrowpoint = 0
let pick_stuff = 0
