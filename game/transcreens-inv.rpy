screen trainMapInv():
    imagemap:
        ground "trainMAP.png"
        hotspot(25, 19, 396, 278) action [Show("frontCarInv", transition=Dissolve(0.3)), Hide("trainMap")]
        hotspot(22, 329, 450, 148) action [Show("frontCarInv", transition=Dissolve(0.3)), Hide("trainMap")]
        hotspot(447, 20, 394, 276) action [Show("midCarInv", transition=Dissolve(0.3)), Hide("trainMap")]
        hotspot(471, 327, 425, 147) action [Show("midCarInv", transition=Dissolve(0.3)), Hide("trainMap")]
        hotspot(867, 21, 391, 280) action [Show("backCarInv", transition=Dissolve(0.3)), Hide("trainMap")]
        hotspot(909, 320, 315, 157) action [Show("backCarInv", transition=Dissolve(0.3)), Hide("trainMap")]

screen frontCarInv():

    imagemap:
        ground "bg trainFRONT1.png"
        hotspot(479, 196, 327, 101) action [Jump("trainFrontWindow")]
        hotspot(547, 266, 185, 85) action [Jump("trainComputer")]

    imagebutton:
        xalign 1.0
        yalign 1.0
        idle "map.png"
        action [Show("trainMap", transition=Dissolve(0.3)), Hide("frontCarInv")]


screen midCarInv():
    add "bg trainMID.png"
    imagebutton:
        xalign 1.0
        yalign 1.0
        idle "map.png"
        action [Show("trainMap", transition=Dissolve(0.3)), Hide("midCarInv")]

screen backCarInv():
    add "bg trainBACK.png"
    imagebutton:
        xalign 1.0
        yalign 1.0
        idle "map.png"
        action [Show("trainMap", transition=Dissolve(0.3)), Hide("backCarInv")]

label trainComputer:
    scene bg trainfront1
    $train_evidence[0] = True
    n "The computer used to navigate the train. I should add this to my list of evidence."
    if train_evidence[0] and train_evidence[1]:
        n "I think that's everything to find in this room"
    call screen frontCarInv


label trainFrontWindow:
    scene bg trainfront1
    $train_evidence[1] = True
    n "You can't see the tunnel from the front window until it's too late. I should remember that."
    if train_evidence[0] and train_evidence[1]:
        n "I think that's everything to find in this room"
    call screen frontCarInv
