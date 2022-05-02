radio.onReceivedNumber(function (receivedNumber) {
    you_3 = receivedNumber
})
input.onGesture(Gesture.Shake, function () {
    Yo_3 = 0
    you_3 = 0
    Yo_3 = randint(1, 3)
    if (Yo_3 == 1) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
    } else if (Yo_3 == 2) {
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
    radio.sendNumber(Yo_3)
    basic.pause(1000)
    basic.clearScreen()
    if (you_3 == 1 && Yo_3 == 2 || (you_3 == 2 && Yo_3 == 3 || you_3 == 3 && Yo_3 == 1)) {
        basic.showString("GANASTE!")
    } else if (Yo_3 == you_3) {
        basic.showString("EMPATE!")
    } else {
        basic.showString("PERDISTE!")
    }
})
let Yo_3 = 0
let you_3 = 0
radio.setGroup(13)
let count = 6
for (let index = 0; index < 5; index++) {
    count += -1
    basic.showNumber(count)
    basic.pause(500)
}
basic.showString("Pvp :v")
