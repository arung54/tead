
image creditscroll:
    contains:
        "credittext.png"
        xcenter .7
        ycenter 2.0
        linear 40 ycenter -2.0
        repeat

label credits:
    $noside = True
    camera at paralloff
    scene black
    with dissolve
    show frog happy with dissolve:
        xcenter .3
    f "Hiii guys!"
    show creditscroll
    $popx = .3
    call popheartso
    f "It's me, Freddy!"
    f "And woah! Look at that!"
    f "There's some text over there."
    f "I'm not great at reading so I'm not gunna worry about it."
    f "But if you want to read it, go ahead!"
    f "Anyway, that's all from me!"
    f "I'm gunna watch some frog videos on my tablet."
    f "Oh yeah - one more thing!"
    f "Thanks for playing TEAD!"
    hide creditscroll
    hide frog
    with dissolve
    scene black with dissolve
    camera at parallax

label teadcomplete:
    camera at paralloff
    show tead with dissolve
    show screen killuser
    pause 2
    show teadcomplete with dissolve:
        ycenter .92
        xcenter .5
    pause 4
    hide screen killuser
    pause 10
    hide screen killuser

    $ persistent.completedgame = True

    $ MainMenu(confirm=False)()
