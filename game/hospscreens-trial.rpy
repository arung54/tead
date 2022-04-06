init python:
    def startHospitalTrial(p1, s1, a1, p2, s2, a2, p3, s3, a3, p4, s4, a4, cS, cE, cL):
        startHospitalTrialTimes(p1, s1, a1, 1.0, p2, s2, a2, 1.0, p3, s3, a3, 1.0, p4, s4, a4, 1.0, cS, cE, cL)

    def startHospitalTrialTimes(p1, s1, a1, t1, p2, s2, a2, t2, p3, s3, a3, t3, p4, s4, a4, t4, cS, cE, cL):
        renpy.music.play("audio/invest1.wav")
        trialAnimation(p1, s1, t1, p2, s2, t2, p3, s3, t3, p4, s4, t4)
        renpy.transition(Dissolve(1.0))
        renpy.call_screen("hospitalTrial", pers1 = p1, statement1 = s1, ag1 = a1, pers2 = p2, statement2 = s2, ag2 = a2, pers3 = p3, statement3 = s3, ag3 = a3, pers4 = p4, statement4 = s4, ag4 = a4, corrS = cS, corrE = cE, corrL = cL)

screen shatteredHosp(lab):
    modal True
    add "shot.png"
    timer 1.0 action [Show("iGotIt", transition=Fade(0.5, 0.0, 0.5), l = lab), Hide("makeyourcase"), Hide("shatteredHosp"), Hide("hospitalTrial"), Hide("hospitalEvidenceTrial"), Hide("pickSpot2"), Hide("pickSpot3"), Hide("pickSpot4"), Hide("chooseCharHospital")]

screen chooseCharHospital(ans, correctLabel, midText):
    add "debatescroll" at cczoom
    imagemap:
        ground "lineup3dead.png"
        hotspot(46, 70, 172, 257):
            if ans == "bert":
                action [Function(shatterNoise), Show("shatteredHosp", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(243, 89, 164, 237):
            if ans == "catherine":
                action [Function(shatterNoise), Show("shatteredHosp", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(438, 61, 180, 262):
            if ans == "dan":
                action [Function(shatterNoise), Show("shatteredHosp", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(648, 48, 231, 275):
            if ans == "dracula":
                action [Function(shatterNoise), Show("shatteredHosp", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(921, 131, 148, 196):
            if ans == "froggy":
                action [Function(shatterNoise), Show("shatteredHosp", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(1104, 70, 112, 255):
            if ans == "jenny":
                action [Function(shatterNoise), Show("shatteredHosp", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(50, 423, 164, 275):
            if ans == "kaiser":
                action [Function(shatterNoise), Show("shatteredHosp", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(258, 446, 154, 246):
            if ans == "lauren":
                action [Function(shatterNoise), Show("shatteredHosp", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(477, 457, 107, 234):
            if ans == "sam":
                action [Function(shatterNoise), Show("shatteredHosp", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(674, 413, 168, 279):
            if ans == "shahar":
                action [Function(shatterNoise), Show("shatteredHosp", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(887, 436, 163, 256):
            if ans == "sid":
                action [Function(shatterNoise), Show("shatteredHosp", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(1093, 432, 132, 260):
            if ans == "stella":
                action [Function(shatterNoise), Show("shatteredHosp", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
    text midText xalign 0.5 yalign 0.5

screen hospitalEvidenceTrial(s, e, l):
    modal True
    add "eviscroll"
    if s == -1:
        imagemap:
            ground "evidenceuinb.png"
    else:
        imagemap:
            ground "evidenceui.png"
            hotspot(35, 29, 144, 75) action [SetVariable("currEvidence", -1), Hide("hospitalEvidenceTrial")]
    vbox xalign 0.15 yalign 0.75 spacing 18:
        textbutton "Guards' Accounts" style "button_text" action SetVariable("currEvidence", 0)
        textbutton "Computer" style "button_text" action SetVariable("currEvidence", 1)
        textbutton "Bottle of Medical Glue" style "button_text" action SetVariable("currEvidence", 2)
        textbutton "Rules of the Hospital" style "button_text" action SetVariable("currEvidence", 3)
        textbutton "Baseball Bat" style "button_text" action SetVariable("currEvidence", 4)
        textbutton "Stepstool" style "button_text" action SetVariable("currEvidence", 5)
        textbutton "Cleaning Supplies" style "button_text" action SetVariable("currEvidence", 6)
        textbutton "Closet Rules" style "button_text" action SetVariable("currEvidence", 7)
        textbutton "State of the Body" style "button_text" action SetVariable("currEvidence", 8)
        textbutton "Glass Shards" style "button_text" action SetVariable("currEvidence", 9)
        textbutton "Pipe in the Hallway" style "button_text" action SetVariable("currEvidence", 10)
        textbutton "Order of the Cells" style "button_text" action SetVariable("currEvidence", 11)
        textbutton "Sid's Account" style "button_text" action SetVariable("currEvidence", 12)
    fixed xmaximum 580:
        if currEvidence == 0:
            image "ev3 guards.png" xcenter 800 yalign 0.1
            text "Sam claims to have woken up before the intercom went off and stared out the door on the guard side of his door until morning. Sam didn't see or hear anything until Lauren showed up to get Sam out of the cell. Lauren claims she left her cell as soon as possible and waited outside Sam's cell." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 1:
            image "ev3 computer.png" xcenter 800 yalign 0.1
            text "The computer in the security room has several features: \n1) A camera viewing the cafeteria\n2) Controlling the lights\n3) Cycling hot water through plumbing\n4) Changing the temperature throughout the building" xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 2:
            image "ev3 glue.png" xcenter 800 yalign 0.1
            text "The bottle of medical glue in the first aid kit had a bit of residue on the nozzle. According to the instructions, medical glue is used for sealing glue and hardened medical glue can be cleaned up by applying a towel dipped in near-boiling water." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 3:
            image "ev3 rules.png" xcenter 800 yalign 0.1
            text "The rules of the hospital state \n1) Two guards are appointed every day\n2) During the day, we cannot be in our cells\n3) At night, we must be in our cells\n4) No one may enter another person's cell\n5) Guards cannot be on the patients' side of the floor and vice-versa\n6) Guards are responsible for feeding patients" xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 4:
            image "ev3 stool.png" xcenter 800 yalign 0.1
            text "The baseball bat was still in the closet and looked like it was in mint condition." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 5:
            image "ev3 stool.png" xcenter 800 yalign 0.1
            text "There is a stepstool in the supply closet, but the highest step is only a few feet off the ground." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 6:
            image "ev3 cleaning.png" xcenter 800 yalign 0.1
            text "The closet has a number of cleaning supplies, including ammonia, bleach, ethanol, and hydrogen peroxide." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 7:
            image "ev3 closet.png" xcenter 800 yalign 0.1
            text "The closet has two rules: \n1) Return everything to where it once was\n2) Do not leave the supply closet lights on" xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 8:
            image "ev3 body.png" xcenter 800 yalign 0.1
            text "Shahar's corpse was found kneeling, with his forehead resting against a bar of his cell. His forehead is bleeding where it touches the bar, and the blood is running down the bar. No other injuries are visible." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 9:
            image "ev3 shards.png" xcenter 800 yalign 0.1
            text "A number of glass shards were found in front of Shahar's corpse." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 10:
            image "ev3 pipes.png" xcenter 800 yalign 0.1
            text "Several pipes run along the ceiling of the hallway where Shahar's body was found, roughly twelve feet off the ground." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 11:
            image "ev3 cells.png" xcenter 800 yalign 0.1
            text "From left to right, the order of the cells is: Lauren, Sam, Dracula, Freddy, Jenny, Bert, Sid, Shahar." xcenter 800 yanchor 0.0 ypos 330

        if currEvidence == 12:
            image "ev3 sid.png" xcenter 800 yalign 0.1
            text "Sid woke up in the middle of the night with a bad cough. There were no signs of illness prior to today." xcenter 800 yanchor 0.0 ypos 330

    if currEvidence >= 0:
        if (s == statement or s == -1) and (e == currEvidence or (type(e) is list and currEvidence in e)):
            imagebutton:
                idle "usethis.png"
                xalign 0.66
                yalign 0.9
                action [Function(shatterNoise), Show("shatteredHosp", lab = l)]#, Hide("hospitalTrial"), Hide("hospitalEvidenceTrial"), Jump(l)]
        else:
            imagebutton:
                idle "usethis.png"
                xalign 0.66
                yalign 0.9
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]

#pers = prefix for the ___face.png you want to show
#statement is text that appears on the screen
#ag = 1 if you can agree, -1 if you can refute, and 0 if you can't interact

screen hospitalTrial(pers1, statement1, ag1, pers2, statement2, ag2, pers3, statement3, ag3, pers4, statement4, ag4, corrS, corrE, corrL):
    modal True
    add "debatescroll"
    add "debateui.png"
    vbox xalign 0.06 ypos 190 spacing 20:
        imagebutton:
            idle pers1+"face.png"
        imagebutton:
            idle pers2+"face.png"
        imagebutton:
            idle pers3+"face.png"
        imagebutton:
            idle pers4+"face.png"
    if statement >= 0:
        add "expoint.png" xpos 0.28 ypos 175+127*statement at exzoom
    fixed xmaximum 750:
        textbutton statement1 xpos 0.64 xanchor 0 ypos 190 yanchor 0 style "button_text" action [SetVariable("statement", 0), SetVariable("agree", ag1)]
        textbutton statement2 xpos 0.64 xanchor 0 ypos 317 yanchor 0 style "button_text" action [SetVariable("statement", 1), SetVariable("agree", ag2)]
        textbutton statement3 xpos 0.64 xanchor 0 ypos 444 yanchor 0 style "button_text" action [SetVariable("statement", 2), SetVariable("agree", ag3)]
        textbutton statement4 xpos 0.64 xanchor 0 ypos 571 yanchor 0 style "button_text" action [SetVariable("statement", 3), SetVariable("agree", ag4)]
    imagebutton:
        idle "evidenceicon.png" at evizoom
        xpos 0.398
        yalign 0.0225
        action [Show("hospital_evidence", transition=Dissolve(0.3))]
    if agree == 1:
        if corrS == statement and corrE == -1:
            imagebutton:
                idle "agree.png"
                xpos 0.55
                yalign 0.04
                action [Function(shatterNoise), Show("shatteredHosp", lab = corrL)]#, Hide("hospitalTrial"), Hide("hospitalEvidenceTrial"), Jump(l)]
        else:
            imagebutton:
                idle "agree.png"
                xpos 0.55
                yalign 0.04
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]

    else:
        imagebutton:
            idle "agreegrey.png"
            xpos 0.55
            yalign 0.04

    if agree == -1:
        imagebutton:
            idle "refute.png"
            xpos 0.775
            yalign 0.04
            action [Show("hospitalEvidenceTrial", transition=Dissolve(0.2), s = corrS, e = corrE, l = corrL)]
    else:
        imagebutton:
            idle "refutegrey.png"
            xpos 0.775
            yalign 0.04
