input.onButtonPressed(Button.A, function () {
    radio.sendString("")
    hand = randint(1, 3)
    if (hand == 1) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    } else if (hand == 2) {
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `)
    } else {
        basic.showLeds(`
            # . . # #
            . # . # #
            . . # . .
            . # . # #
            # . . # #
            `)
    }
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
})
let hand = 0
radio.setGroup(2)
