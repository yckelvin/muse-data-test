input.onButtonPressed(Button.A, function on_button_pressed_a() {
    MuseIoT.sendMusespeak("ML1234", input.lightLevel(), 0, 0, 0, 0, 0)
})
basic.showNumber(0)
MuseIoT.initializeWifi()
basic.pause(5000)
basic.showNumber(1)
MuseIoT.setWifi("wifi-name", "password")
basic.pause(10000)
basic.showNumber(2)
MuseIoT.ConnectMuseDataMQTTbroker("ML1234")
basic.pause(2000)
basic.showNumber(3)
