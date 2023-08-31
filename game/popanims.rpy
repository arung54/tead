label popwowb:
    play sfx "audio/popwow.mp3" volume .5
    show popwow onlayer overlay:
        xcenter .25
        ycenter .74
        rotate 20
        zoom .5
    #hide popwow
    return

label pophuhb:
    play sfx "audio/pophuh.mp3" volume .5
    show pophuh onlayer overlay:
        xcenter .25
        ycenter .74
        rotate 10
        zoom .5
    return

label poptearb:
    play sfx "audio/poptear.mp3" volume .5
    show poptear onlayer overlay:
        xcenter .215
        ycenter .78
        zoom .5
    return

label poprainb:
    play sfx "audio/poprain.mp3" volume .5
    show poprain onlayer overlay:
        xcenter .18
        ycenter .65
        zoom .6
    return

label popheartsb:
    play sfx "audio/pophearts.mp3" volume .5
    show pophearts onlayer overlay:
        xcenter .18
        ycenter .81
        zoom .6
    return

label popmadb:
    play sfx "audio/popmad.mp3" volume .5
    show popmad onlayer overlay:
        xcenter .19
        ycenter .8
        zoom .6
    return

#######################################################
#######################################################
#######################################################

label popwowo:
    play sfx "audio/popwow.mp3" volume .5
    show popwow:
        xcenter popx
        ycenter .25
        zoom .75
    return

label poptearo:
    play sfx "audio/poptear.mp3" volume .5
    show poptear:
        xcenter popx
        ycenter .275
        zoom .75
    return

#No poprain
label popheartso:
    play sfx "audio/pophearts.mp3" volume .5
    show pophearts:
        xcenter popx
        ycenter .5
    return

label popmado:
    play sfx "audio/popmad.mp3" volume .5
    show popmad:
        xcenter popx
        ycenter .3
    return

label pophuho:
    play sfx "audio/pophuh.mp3" volume .5
    show pophuh:
        zoom .75
        xcenter popx
        ycenter .25
    return

#######################################################
#######################################################
#######################################################


label poptest:
    b "sdrtwesstgs1"
    b "sdrtwesstgs2"
    call popwhuhb from _call_popwhuhb
    b "sdrtwesstgs3"
    b "sdrtwesstgs4"
    call popwowb from _call_popwowb_104
    b "sdrtwesstgs5"
    b "sdrtwesstgs6"
    call poptearb from _call_poptearb_80
    b "sdrtwesstgs7"
    b "sdrtwesstgs8"
    call poptearb from _call_poptearb_81
    b "sdrtwesstgs7"
    b "sdrtwesstgs8"
    call poptearb from _call_poptearb_82
    b "sdrtwesstgs7"
    b "sdrtwesstgs8"
    call poprainb from _call_poprainb
    b "sdrtwesstgs"
    b "sdrtwesstgs"
    call popheartsb from _call_popheartsb_1
    b "sdrtwesstgs"
    b "sdrtwesstgs"
    call popmadb from _call_popmadb
    b "sdrtwesstgs"
    b "sdrtwesstgs"
