screen chooseCharPent(ans, correctLabel, midText):
    add "debatescroll" at cczoom
    imagemap:
        ground "lineup.png"
        hotspot(46, 70, 172, 257):
            if ans == "bert":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(243, 89, 164, 237):
            if ans == "catherine":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(438, 61, 180, 262):
            if ans == "dan":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(648, 48, 231, 275):
            if ans == "dracula":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(921, 131, 148, 196):
            if ans == "froggy":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(1104, 70, 112, 255):
            if ans == "jenny":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(50, 423, 164, 275):
            if ans == "kaiser":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(258, 446, 154, 246):
            if ans == "lauren":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(477, 457, 107, 234):
            if ans == "sam":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(674, 413, 168, 279):
            if ans == "shahar":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(887, 436, 163, 256):
            if ans == "sid":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
        hotspot(1093, 432, 132, 260):
            if ans == "stella":
                action [Function(shatterNoise), Show("shatteredMans", lab = correctLabel)]
            else:
                action [Function(errorNoise), Show("tryAgain", transition=Dissolve(0.2))]
    text midText xalign 0.5 yalign 0.5
