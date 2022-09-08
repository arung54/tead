#twittertesting
screen object_screen():
    key "K_UP" action Return("u")
    key "repeat_K_UP" action Return("u")
    key "K_DOWN" action Return("d")
    key "repeat_K_DOWN" action Return("d")
    key "K_LEFT" action Return("l")
    key "repeat_K_LEFT" action Return("l")
    key "K_RIGHT" action Return("r")
    key "repeat_K_RIGHT" action Return("r")

    add "images/bertfrlg2.png" anchor (1.0, 0.0) pos (object_posx, object_posy)

# The game starts here.
label twitter:

    $ object_posx = 200
    $ object_posy = 200

    show screen object_screen

    label move_loop:
        $ res = ui.interact()
        if res == "l":
            $ object_posx -= 5
        elif res == "r":
            $ object_posx += 5
        elif res == "u":
            $ object_posy -= 5
        elif res == "d":
            $ object_posy += 5

        jump move_loop
