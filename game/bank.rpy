label bankGo:
    $dan = False
    $ftecounter = 8
    scene black
    $mood = "sad"
    bi "Two more people dead..."
    bi "Shahar... and Dracula."
    bi "No, Vladamir."
    bi "Despite everything, I don't hate him."
    $mood = "ind"
    bi "I can't hate him."
    bi "None of us here have options, all we can do is keep pushing forward."
    bi "I won't let them, or anyone else, die in vain."
    bi "..."
    bi "I can feel myself slowly come to."
    show bg banklobby with dissolve
    $ statusnt("???", "bert", ch=4, sun=2)
    $showchibint("freddy, jenny, lauren, sid")
    show sid ind with dissolve
    i "yo!"
    i "why the fuck chibis not working"
