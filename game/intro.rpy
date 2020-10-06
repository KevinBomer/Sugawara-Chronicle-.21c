# This is the intro. When you press the start button, the game will begin here.
#used for testing purposes
#label testing:

label start:
    stop music fadeout (2.0)
    scene black with dissolve
    play music delicate

    "In the most quiet part of the night, I walk up the steps to our dingy two-bedroom apartment."
    #sfx unlocking door, open
    "I pull the door open and step inside."
    scene apartment night with squares
    Hiroya "I'm back."
    "The smell of smoke hangs heavy in the air. My nose crincles in response."
    "The room is dark. Some commercial plays on the TV in a low volume."
    "A small collection of beer cans and ramen cups lay near the coffee table. Among them is my father hunched over the table, exhaustedly sucking at the filter of a cigarette."
    Hiroya "Dad..."
    "I call out again."
    Dad "Mm."
    "He stirrs."
    "I drop my schoolbag near the door and stroll over to the kitchen. I peer into the fridge to see about putting a meal together."
    "Let's see."
    "Condiments, some beer, a carton of milk."
    "No combination of ingredients that could ever comprise of a meal."
    "I huff a sigh and close the fridge again."
    Hiroya "Give me some money, Dad. I'll go pick up some sandwiches."
    Dad "Hmph."
    "My father snorts in reply."
    Dad "You see what's on the stove. Eat what we got."
    "He takes the last drag from the cigarette and lets it out with a sigh."
    "I turn back to the kitchen. I see a bowl on the counter covered with a paper napkin."
    "I lift up the napkin with low expectations."
    "Inside, I find a single clump of old, hard steamed rice."
    Hiroya "Hm."
    "I replace the napkin and go back to the living room."

    Dad "They only want spry, young folk working anyway."
    "He reaches for another cigarette, only to find that the box is empty."
    "He glares down into the empty carton."
    Hiroya "Dad, give me some money. I'll go buy some sandwiches from the convenience store."
    "He tosses the carton aside and reaches into his pants pocket."
    "He pulls out another carton of cigarettes."
    Hiroya "Dad!"
    Dad "Do I look like I'm made of money?"
    "His voice is hoarse."
    Hiroya "...Just how much of your unemployment check did you waste on cigarettes?"
    Dad "S'hard work out there, alright? I don't need my good-for-nothing son giving me shit about how I relax."
    Hiroya "It never changes with you, does it?! How long is it going to take for you to pull yourself together?"
    Dad "..."
    Hiroya "We got no food, the house is a mess... when are you gonna pull yourself together!?"
    Dad "Don't you dare preach at me, boy."
    Dad "When you start working 'til your knuckles bleed, you'll be bloody tired all the time too!"
    Dad "Don't kids your age pick up part-time work? Why don't you apply yourself and leave me the Hell alone!?"
    Dad "If only I didn't have you sucking up my hard-earned wages...I wouldn't be in this mess."
    Dad "Parasite. That's all you are."
    Hiroya "..."
    Dad "Huh? H-hey, where're you going? I'm talking to you!"
    Hiroya "...No. I heard exactly what you said."
    Dad "...What's that your grabbing? Are you packing? Hiroya, {i}come here.{/i}"
    Hiroya "No. I'm doing what I should've done ages ago. It's what you always wanted, right?"
    Dad "...Pfft, what? You running away or something? What're you gonna do, live under a bridge for the rest of your life?"
    Hiroya "Tch."
    Dad "Wait, you're serious? What the Hell do you think you're doing, Hiroya!?"
    Hiroya "I'm leaving this crummy apartment behind. I'm leaving you behind."
    Hiroya "You can't support a family, you can barely support yourself!"
    Hiroya "You never wanted a son anyway! You said so yourself!"

    Dad "Hiroya! No. You know what, fine."
    Dad "You think you'll do that much better on your own? Well go on then!"
    Dad "Get out of my house, you ungrateful punk."

    "Fine. That's what I'll do then. I'll leave my pig of a father once and for all. I'll make my own way from now on."
    "I grab just a few things and throw them into my schoolbag."
    Hiroya "...Good for nothing pig. You know this is exactly why Mom left you."
    "I head for the door."
    #sfx cloth rustling (like a backpack being roughly grabbed/tugged at
    Hiroya "Hn!"
    "He grabs me from behind."
    Hiroya "Let go of my backpack, asshole!"
    "I tug and pull with all my might. But he just won't give up."
    Hiroya "Let!..."
    Hiroya "LET GO OF ME!"
    #sfx whoosh
    "{b}WHOOSH!{/b}"
    #if we have a bg a screen shake for impact might be good
    #sfx impact
    "{b}THUD!{/b}"
    #sfx collapse on floor
    "I hit him."
    Dad "Ungh."
    "I turn around. He looks like he stumbled a bit. He moved his hand away from his face. There was blood on his nose."
    Dad "Ah... pull a cheap shot on your old man!?"
    Hiroya "Urk!"
    "He's got me by the collar! I can't escape!"
    Hiroya "Ah!"
    "His eyes are no longer that of a tired salaryman. There was something else there now."
    "Something vicious."
    "He's got me pinned against the wall."
    Dad "You got {i}no idea{/i} what you're doing, you mouthy little brat! You got no money, no plan, and where were you even going to run off to!?"
    Dad "Answer me, boy!"
    Hiroya "Anywhere but with you."
    #sfx dull hit
    "Pulling my head back, I bash my head against his. He doesn't let go."
    Dad "Ah! Smarmy {i}prick!{/i}"
    #sfx swing
    Dad "Before you go..."
    Dad "I'll just leave you with this."
    "The last thing I see is his scarred knuckles making a beeline towards my face."
    "I close my eyes tight and brace for the impact."
    scene black with vpunch
    play sound "sfx/heavy_bag_drop_dirt2.ogg"


    stop music fadeout 2.0
    $ renpy.pause (3, hard = True)

    jump chapter1
