from microbit import display, button_a
messages = ["P","A","U"]
i = 0
while True:
    if button_a.is_pressed():
        if i >= 2:
            i = 0
        else:
            i+=1
        i = 0 if i >= 2 else i+=1
        display.scroll(messages[i])