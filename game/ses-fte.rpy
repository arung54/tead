#Julian

#Mansion 2
label sesAsk0:
    ses "Meow!"
    bi "...I could hang out with Sesame."
    menu:
        "Spend time with Sesame?":
            j "Sure!"
            jump sesang
        "I'd be crazy to talk to a cat...":
            hide sesame with dissolve

label sesHang:
    ses "Meow!"
    jump postFTEHandler
