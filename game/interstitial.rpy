label interstitial:
    scene white with Dissolve(.2)
    stop music fadeout 1.0
    scene chapter_screen_1 with Dissolve(.2)
    show logo with Dissolve(.5):
        xalign .5
        yalign .6
        xpos .3
        ypos .5
        zoom .8
    $ renpy.pause(2, hard=True)
    scene bridge sidewalk night with dissolve
    "Darkness makes for good cover. It's easier for me to wander without having to watch my back all the time, in case anyone happens to be watching."
    "Following the familiar bends, I make it back to my bridge."
    "???""Who's there?!"
    "I stop in my tracks. There's two guys across the road lurking near my spot, dressed in all black. Are they police?"
    "...No. No, I recognize those uniforms."''
    "I can't make out much. Theres two of them. One is sort of tall. The other, sort of round."
    "The round one" "Hey. He's talking to you!"
    "The two guys start walking over. Slowly, but with menace."
    "As they step into the light I can see them more clearly. It's just as I thought."
    "They're wearing Sakuranoki uniforms."
    "Great. Some thugs from our rival school are here to give me a hard time."
    "Damn that girl."

    "The tall one" "We heard there was some chump settin' up out here."
    "The round one" "And whaddya' know. He's from Sugawara too."
    "The tall one" "Our lucky day."
    "Hiroya" "*sigh* I should have known. Where theres a bridge, there's bound to be trolls."
    "The round one" "Oh. Smart guy, huh?"
    "Hiroya" "I don't want any trouble."
    "The tall one" "Well the thing is, we're gonna' have a hard time believing that after that shit you guys pulled on our field the other day."
    "The round one" "How dare you embarrass us in front of Shizuka!"
    "Oh. That's what this is about. The baseball guy from the other day. Damn both of them."
    "The tall one" "I'd reckon that the whole lot of you deserves some discipline."
    Hiroya "Look, if you're here to mug me or whatever, I don't have any money."
    "The round one" "You know what happens to barn animals who step outta line?"
    "The tall one" "They brand 'em, and make an example of them for everyone else."
    Hiroya "Well, I'm glad the boys at Sakura no Ki are learning all about husbandry. Farming's a good vocation."
    "The round one" "...what?"
    "The tall one" "...I'm gettin' sick of seeing your dumb face!"
    "The round one" "Let's Teach 'im a lesson."
    "The bigger of the two clenched his fist so tightly I could hear his knuckles crack. This wasn't good, but I had nowhere else to run."
    "I guess it can't be helped."
    "I raise my fists defensively as the big guy comes at me with a hook."
    "I go low, aiming for his exposed gut."
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.05
            linear 0.1 zoom 1.0
    "The tall one" "Oof!"
    "He keels forward, wincing and glares at me. I go for another hit while he's flinching."
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.05
            linear 0.1 zoom 1.0
    "The round one" "C'mon!"
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.05
            linear 0.1 zoom 1.0
    "Not to be left out, the round guy tackles me from the side, bowling me over to the ground"
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.05
            linear 0.1 zoom 1.0
    "I wrestle with him for a short moment. I almost get him in a hold. He slips out and pushes me back down to the pavement."
    "I bounce back to my feet. The tall one is holding his stomach, still reeling from my first hit."
    Hiroya "Oh no. Did a little punch like that really hurt? I had expected better from students of the prestigious Sakura no Ki."
    "The tall one" "Tch. We were only gonna leave you with a few bruises, but now you really did it."
    "He reached into his pocket and pulled out something I didn't quite recognize."
    "It was only when I heard the tell-tale sound of a spring-loaded mechanism that I realized he had pulled out a switchblade."
    "This is really bad."
    "Maybe I should cut my losses and run."
    "I back up a bit, trying to put some distance between me and these thugs."
    "But I feel something hard press against my lower back."
    "I turn my head to look behind me. I'm not met with another hooligan, thankfully."
    "Just a guard rail overseeing the river. And it was quite a drop."
    "The tall one" "Heheh. Now I got you."
    "The round one" "Squeal like a pig for us. Nobody's comin' to save you."
    Hiroya "...?"
    "I look down over the railing at the dark water down below."
    "Just for an instant I thought I saw something in the water."
    "No, it has to be a trick of the moonlight."
    "The guy with the knife comes closer to me."
    "I can't help but look again, back over the rail"
    "The round one" "Hey! Look me in the eye when I'm killing you!"
    Hiroya "Something's... in the water. Some kind of light."
    "The light stirs back and forth as I watch it. Suddenly, it stops. I don't understand."
    "So what's this I'm seeing? Am I going crazy?"
    "The tall one" "Are you screwing with me, punk!? Are you stupid or something?!"
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.25
    "The guy with the knife grabs my collar, and forces my attention back to him."
    "The round one" "Maybe I'll throw you down there too if it's so interestin', huh!?"
    #sfx
    "Behind me, there was a splash. It sounded as if somebody had dived into the river, but..."
    "The tall one" "...What the fuck is that?!"
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1.25
            linear 0.1 zoom 1.0
    #sfx whoosh
    "I can feel a bright flash of light behind me."
    "Losing the grip on my shirt, the round one staggered back."
    "The round one" "What!? Shit get away from it!"
    "The tall one" "L-look!"
    "I turn my head and I see it. But what...is it?"
    "A translucent essence floating still over the water. A formless mass of a silvery sort of liquid, surrounded in a beam of otherworldly white light."
    "It quivers and shifts, giving it some kind of form."
    "The longer I stare, the more I'm convincing myself that it looks, ever so vaguely... humanoid. And more humanoid by the second."
    Hiroya "What is that?"
    "The tall one" "It's an alien!"
    "The round one" "...You serious, dude? Let's just-"
    "The thing rushes forward, fluid, as if it were made from the water itself."
    "It flys over my head, not at me, but at my attackers from Sakuranoki."
    "Reacting, they raise their fists"
    "The round one" "Get it! Just grab it and hold it! I'll get my knife and slit its throat, wherever the hell it is!"
    "The tall one" "O-okay!"
    "The bigger guy lurched forward, his arms reaching out for a bear hug."
    "...But his arms simply slipped right through it."
    "The tall one" "...Huh?"
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.05
            linear 0.1 zoom 1.0
    #sfx slash
    "The tall one" "Ahh! My back!"
    "Invisible to the eye, some part of the silvery mass rapidly descended upon his back, causing him to collapse to the ground."
    "He scrambled forward, and stood back up."
    "The round one" "What're you doing!? Just grab it!"
    "The bigger guy went forward again."
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.05
            linear 0.1 zoom 1.0
    #sfx slash
    "But he stopped midpace, a similar look on his face as when I hit him in the gut."
    "He leaned forward and made a swing at the ghostly figure."
    "And with a rapid movement, the figure was behind him again."
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1
            linear 0.1 zoom 1.05
            linear 0.1 zoom 1.0
    #sfx slash
    "The tall one" "OOF! M-my back!"
    "The round one" "Grr... got it!"
    "By the time the smaller guy clamored for his knife, his bigger buddy had been bested, sprawled onto the ground. Realizing this, the smaller guy's face turned pale."
    "The round one" "What the hell is... damn it!"
    "His exclamations were left to the corner of my eye. I had been gazing at the ghostly form for some time in awe."
    "And I thought I could make out a human. ...No, I definitely did."
    "It was a girl. She was garbed in a wispy white nightgown, clutching a sword. It was still sheathed, holding it above the larger man that had collapsed to the ground."
    "Her hair was a pale, ivory white, moving on its own as if lifted by the wind. Her eyes had a sharp gaze, punctuated by her red irises."
    "She looked over to me, and our eyes met. Her eyes widened upon looking at me, concern washing over her face."
    "...I could see my reflection in them. And I could see the shorter man had grabbed my side in my dazed confusion, holding a knife up against my stomach."
    "The round one" "Alright, you spooky ghost alien {i}thing!{/i} One more move and this guy's guts are going all over the pavement!"
    "She scowled silently, lowering her body into a combat stance. My eyes widened, not sure what she was thinking."
    "Her hand tightened against the grip of her katana. My eyes stared at it with growing concern."
    Hiroya "Wait, don't-"
    "In the blink of an eye, she rushed forward, moving too fast for either of us to see."
    #sfx shove
    Hiroya "Oof!"
    "I felt a powerful impact against my chest. She was moving so fast, it took me a second to realize what had happened."
    show sky night with squares
    "By the time I realized that she had rammed into me, I was already falling over the guardrails."
    "My body flipped from the impact, and all I could make out was my own reflection, rapidly travelling towards me, illuminated by the moon above."
    "It was getting close. I knew then that I was going to land in the river."
    "I close my eyes, bracing for impact."
    "So this is how I'm going to die..."
    scene black with fade
    $ renpy.pause(1, hard=True)
    show text "Sugawara Chronicle"
    $ renpy.pause(2, hard=True)
    #sfx splash
    #prolly open the next scene with him screaming idk
    return
