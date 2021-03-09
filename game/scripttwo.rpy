label yeet:
    scene bg pfront
    show bert sad:
        xcenter .7
    b "Hmm... This looks like... A prison."
    hide bert sad
    show bert happy:
        xcenter .7
    b "POGGERS!!!"
    hide bert sad
    show sam:
        xcenter .7
    s "What the fuck is wrong with you? This is serious..."
    hide sam
    show drac ind:
        xcenter .7
    d "Indeed... No time to lollygag, there is a particularly ominous aura here..."
    hide drac ind
    show frog ind:
        xcenter .7
    f "A what? I'm scared, ribbit."

label second:

    scene bg broom
    show bert happy:
        xcenter .7

    b "Woah! we're in a bank I think?"
    b "Let's check down the hallway! It looks like the vault is... Open?!"

    scene bg bdoor with fade
    show bert happy:
        xcenter .7

    b "That's weird... I hear footsteps coming from inside..."

    hide bert happy
    show cydney ind:
        xcenter .75

    o "Oh no... That's scary. Do we have to go? I-"

    hide cydney ind
    show bert happy:
        xcenter .7

    b "Cydney, chill out - I'll let you decide."
    menu:
        b "Should we check the vault?"

        "Yes":
            jump vault

        "No":
            jump stay

label vault:
    b "Okay, follow me..."
    scene black with fade
    o "It's dark in here..."
    o "HEY! Kepp your hands to yourself."
    b "Wait... That wasn't me..."
    b "Kidding, sorry."

    return

label stay:
    b "I think you're right - let's stay here."

    return
