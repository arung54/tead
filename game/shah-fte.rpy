
label shahAsk0:
    scene bg trainmid
    show shahar ind with dissolve
    h "Y'arr, if you think about it, a train is just a pirate ship on land."
    ni "...yeah, I should go talk to Bert instead of this guy."
    call screen midCar

label shahAsk1:
    scene bg trainmid
    show shahar ind with dissolve
    h "Land ho!"
    h "Wait, no, that's just a mirage..."
    blank "Should I talk to Shahar?"
    menu:
        "Spend time with shah":
            h "Arr laddy, you've made a good choice!"
            ni "...have I?"
            jump shahHang
        "Maybe later":
            hide shahar with dissolve
            call screen midCar

label shahHang:
    if fte_shah == -1:
        h "Y'arr, Dan, what can I do for ye?"
        n "Do you really have to talk like that?"
        h "Talk like what, mate?"
        n "Like... you know, not normally."
        h "Lad, this is normal talk for me!"
        n "You know you talk like a pirate, right?"
        h "Because I am a pirate!"
        n "You're not though."
        h "What do ye mean? If I'm not a pirate, why are my memories all of the seas?"
        h "Plundering ports and arguing over how to split bounties, those were the days..."
        n "Pirates don't really exist they way you seem to think they do."
        n "They usually just attack rich people's ships and take their belongings."

    $fte_shah += 1
    $ftecounter += 1
    hide shahar with dissolve

    if ftecounter - 1 == 1:
        call screen frontCar #replace w/ jump to after FT2
