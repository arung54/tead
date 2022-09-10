
label twittergo:

    #camera:
    #    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, -52.0, 0.0)*RotateMatrix(3.0, 0.0, 0.0)

    show black:
        zpos -10000.0
        zzoom True

    show jenny happy:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(650.0, 0.0, -4000.0)*RotateMatrix(0.0, 0.0, 0.0)
    show frog happy:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, -3000.0)*RotateMatrix(0.0, 0.0, 0.0)
    show drac happy:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(650.0, 0.0, -2000.0)*RotateMatrix(0.0, 0.0, 0.0)
    show catherine happy:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, -1000.0)*RotateMatrix(0.0, 0.0, 0.0)
    show bert ind:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(650.0, 0.0, -0.0)*RotateMatrix(0.0, 0.0, 0.0)

    b "hey"
    camera:
        linear 6 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 3748.0)*RotateMatrix(0.0, 0.0, 0.0)
    b "working?"
python:
    '''
    show kaiser ind:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(625.0, 0.0, -472.0)*RotateMatrix(0.0, 0.0, 0.0)

    show lauren happy:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(625.0, 0.0, -472.0)*RotateMatrix(0.0, 0.0, 0.0)

    show sam ind:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(625.0, 0.0, -472.0)*RotateMatrix(0.0, 0.0, 0.0)

    show shahar happy2:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(625.0, 0.0, -472.0)*RotateMatrix(0.0, 0.0, 0.0)

    show sid happy:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(625.0, 0.0, -472.0)*RotateMatrix(0.0, 0.0, 0.0)

    show stella happy:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(625.0, 0.0, -472.0)*RotateMatrix(0.0, 0.0, 0.0)

    b "that's a lot of gamers"
    h "aye"


    screen magiccam:
        add TrackCursor("stellaslut.png", 20)
    screen testxd:
        add "testxd.png" xcenter .5 ycenter .5
    label twitter2:
        scene bg mansionbedroom2 at bg
        #$showchibiR("bert","jenny", "sid", "dan", "sam")
        #$ statusnt("Bar Car", "dan", ch = 1, sun = 3)
        show screen testxd
        camera at parallax
        b "pogchap"
        show sam ind
        b "pogchap"
        b "pogchamp"
    '''
