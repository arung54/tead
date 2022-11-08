

screen fishing():
    add "bg fishing.png" xcenter .5 ycenter .5 zoom 2
    timer .01 action Show("getready")

screen getready():
    add "danfish" xcenter .91 ycenter .99
    add "fishingrod" xcenter .93 ycenter .975
    vbox:
        align (.5, .3)
        textbutton "   Go fishing for a bit?":
            text_color "#444444" text_hover_color "#000000" action [Hide("getready"),Show("fishgo")]
        textbutton "Skip fishing for tonight.":
            text_color "#444444" text_hover_color "#000000" action QuickSave(2)

screen fishgo():
    add "getready1.png" xcenter .5 ycenter.33
    add "danfish" xcenter .91 ycenter .99
    add "fishingrod" xcenter .93 ycenter .975
    timer 2.0 action [Hide("fishgo"), Show("fishspeed1a")]

screen fishspeed1a():
    add "fish3.png" xcenter .5 ycenter.33
    add "danfish" xcenter .91 ycenter .99
    add "fishingrod" xcenter .93 ycenter .975
    timer 1.0 action [Hide("fishspeed1a"), Show("fishspeed1b")]
screen fishspeed1b():
    add "fish2.png" xcenter .5 ycenter.33
    add "danfish" xcenter .91 ycenter .99
    add "fishingrod" xcenter .93 ycenter .975
    timer 1.0 action [Hide("fishspeed1b"), Show("fishspeed1c")]
screen fishspeed1c():
    add "fish1.png" xcenter .5 ycenter.33
    add "danfish" xcenter .91 ycenter .99
    add "fishingrod" xcenter .93 ycenter .975
    timer 1.0 action [Hide("fishspeed1c"), Show("fishspeed1f")]
screen fishspeed1f():
    add "danfish" xcenter .91 ycenter .99
    #add "danwow" xcenter .91 ycenter .99
    add "fishingrodhooked" xcenter .93 ycenter .975

    imagebutton:
        idle "REEL!!!.png"
        xcenter .5
        ycenter.4
        action [Hide("fishspeed1f"), Show("fishreeling")]
    timer 3 action [Hide("fishspeed1f"), Show("fishgotaway")]

screen fishreeling():
    add "danfish" xcenter .91 ycenter .99
    #add "danwow" xcenter .91 ycenter .99
    add "fishingrodhooked" xcenter .93 ycenter .975
    timer 1.0 action [Hide("fishreeling"), Show("resultsfish")]

screen resultsfish():
    add "danjumping" xcenter .42 ycenter .512
    #add "fishingrod" xcenter .93 ycenter .975
    text "You caught a fish!" xcenter .62 ycenter .3 color "#222222"
    add "fishcatch1.png" xcenter .62 ycenter .52
    textbutton "   Continue":
        xcenter .62 ycenter .72 text_color "#222222" text_hover_color "#444444" action [Hide("resultsfish"),Show("getready")]

screen fishgotaway():
    add "danfish" xcenter .91 ycenter .99
    #add "fishingrod" xcenter .93 ycenter .975
    text "It got away..." xcenter .5 ycenter .4 color "#444444"
