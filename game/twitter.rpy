
label twittergo:

    show doors:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-157.0, -126.0, -177.0)*RotateMatrix(0.0, 0.0, 0.0)
    show bert ind:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(500.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    show catherine happy:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1000.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    show drac happy:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1500.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    show frog happy:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(2000.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    show jenny happy:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(2500.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)

    show kaiser ind:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(3000.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)

    show lauren happy:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(3500.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)

    show sam ind:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(4000.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)

    show shahar happy2:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(4500.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)

    show sid happy:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(5000.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)

    show stella happy:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(5500.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)

    b "that's a lot of gamers"
    camera:
        linear 0 pos (0, -100) zpos 0.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 300.0)*RotateMatrix(0, 14.0, 0.0)
    h "aye"
    camera:
        linear 20 pos (5000, -100) zpos 0.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 300.0)*RotateMatrix(0, -14.0, 0.0)
    h "aye"
    h "aye"

screen magiccam:
    add TrackCursor("stellaslut.png", 20)

label twitter2:
    scene bg mansionbedroom2 at bg
    camera at parallax
    b "pogchap"
    show sam ind
    b "pogchap"
    b "pogchamp"
