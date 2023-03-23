def on_button_pressed_a():
    
    MuseIoT.send_musespeak("KL234", input.light_level(), 0, 0, 0, 0, 0)
    
input.on_button_pressed(Button.A, on_button_pressed_a)


Key = ""
basic.show_number(0)
MuseIoT.initialize_wifi()
basic.pause(5000)
basic.show_number(1)
MuseIoT.set_wifi("KLHOME", "127214529")
basic.pause(10000)
basic.show_number(2)
MuseIoT.connect_muse_data_mqt_tbroker("KL234")
basic.pause(2000)
basic.show_number(3)

