let msg = ""
let P1n = 0
let P0n = 0
input.setAccelerometerRange(AcceleratorRange.OneG)
basic.showString("A")
radio.setGroup(1)
radio.setTransmitPower(7)
basic.forever(() => {
    P0n = input.pinIsPressed(TouchPin.P0) ? 1 : 0
P1n = input.pinIsPressed(TouchPin.P1) ? 1 : 0
msg = "a" + pins.map(
    input.acceleration(Dimension.X),
    -2048,
    2048,
    0,
    999
    ) + "," + pins.map(
    input.acceleration(Dimension.Y),
    -2048,
    2048,
    0,
    999
    ) + "," + pins.map(
    input.acceleration(Dimension.Z),
    -2048,
    2048,
    0,
    999
    ) + "," + P0n + "," + P1n
    radio.sendString(msg)
    basic.pause(1)
})
