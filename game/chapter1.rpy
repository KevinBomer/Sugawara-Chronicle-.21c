label chapter1:
    $ camera_reset()
    play music Chalkboards fadein 1.0
    $ renpy.pause(1, hard=True)
    show text "Sugawara Chronicle"
    $ renpy.pause(2, hard=True)\
    scene white with Dissolve(.2)
    scene chapter_screen_1 with Dissolve(.2)
    show logo with Dissolve(.5):
        xalign .5
        yalign .6
        xpos .3
        ypos .5
        zoom .8
    $ renpy.pause(1, hard=True)
    show text "{size=40}{color=#3a47a6}Chapter One \n{size=64}Independence Day" at chaptertitlespot with Dissolve(1.0)
    $ renpy.pause(3, hard=True)


#introduction
    scene sky with dissolve

    Hiroya "Ah-!"

    Hiroya "Oh..."

    Hiroya "It was just a dream."

    "I raise my hand to my cheek. The spot tingles as if it's not sure whether or not it should be signaling pain."

    "I hate dreams like that. They feel too real, and they trick my gullible brain into reliving old memories."

    "That dream's more than a figment of my imagination. It's a reminder of the spat I had with my old man."

    Hiroya "Haaahn..."

    "Stretching my arms out in a big yawn, I drink in my surroundings."

    scene bridge below day with Dissolve(.5)

    "Yup. That's more or less how I ended up here."

    "Living under a damn bridge."

    "I didn't think to bring much with me. Just my school bag, really."

    "I would have liked to have grabbed some stuff from my room at least. A set of clothes, my sleeping bag."

    "Well, at any rate, it's too late for that now."

    "There's no way I can go back and look that smug bastard in the eye."

    "Not that I'd ever want to anyway."

    "That asshole."

    "Whatever. I'll manage."

    "I'm a junior. I'm basically an adult."

    "And this spot isn't too bad. The grass is cool and the autumn breeze is at just the right temperature as it comes in over the water."

    "I glance down at the school uniform I'm still wearing from last night. It's in pretty rough shape from having been slept in, and on the ground, no less."

    "Oh crap, what time is it?"

    "I make a cursory glance to my watch."

    "If I'm late for homeroom again, Miss Hirayama will have my hide!"

    "A disciplinary call to my dad is the last thing I need right now."

    "Hmm."

    "Class hasn't started yet. The school is still a decent way up the road from here, but if I book it, I might just make it before the bell."

    scene bridge sidewalk day with wiperight

    "With no time to lose, I start my run."

    "I try to start off with a quick and steady pace, controlling my breathing like how they teach us to while running track."

    "I'm not exactly in the best shape, but I do have one thing going for me."

    "This is my town. I've lived here all my life."

    "Nobody knows these streets like Hiroya Tachibana!"

    "I reach the end of the road turn down an alleyway. A shortcut through the town's new commercial district."

    scene cafe outside with wiperight

    play sound "sfx/tstep_sidewalk1.ogg"

    "This area is always busy. With so many new businesses springing up left and right, it's no wonder the popularity of this part of town has skyrocketed."

    "I weave my way through the crowd, careful to avoid the traffic."

    "Last thing I need in my life is to get my head smashed in by an oncoming car."

    "Not when I just got my freedom."

    "I break off the street and into another ally."

    play sound "sfx/tstep_sidewalk2.ogg"

    scene street day with wiperight

    "Almost there!"

    "Breathe, breathe..."

    "Aha, yes! The school is just around the corner."

    play sound "sfx/tstep_sidewalk2.ogg"

    scene courtyard empty with wiperight

    "Ah, Finally. I made it to the courtyard."

    "I don’t see any students around. The bell must be seconds from ringing!"

    "I narrow my sights on the far door, the one that leads to my homeroom class."

    "My legs are really starting to cramp up now."

    "I don't know how much longer I can keep up this sprint, but I have to try."

    "Here comes my second wind! Just about there-!"

    #TUTTY BLOCK#
    play sound "sfx/punch.ogg"
    play music SchoolCasual fadein (2)
    Hiroya "Hrk!" with vpunch
    "Just as I turn the corner, I crash right into someone."

    "A girl. A bundle of books fall from her hands down to the ground."

    Hiroya "S-sorry. I-I'll get it."

    "???" "Haa!"

    "In the blink of an eye, the girl lets out a battle cry, kicking her leg high into the air as I bend down."

    Hiroya "!"

    play sound "sfx/punch2.ogg"

    "???" "Yaaa!"

    scene white with vpunch

    Hiroya "guuwhaa'kh!"

    "And without a seconds hesitation, she swings her foot into my exposed gut with the force of a bullet train."

    queue sound "sfx/whril.ogg"
    "With her sheer force of impact, I'm airborne. My whole world spins out of control."
    #This is the sky spinning animation.
    show sky:
        subpixel True xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5 rotate None
        parallel:
            alpha 0
            linear 1.0 alpha 1
        parallel:
            yzoom 2.0
            pause (3.2)
            linear .5 yzoom 1.0
        parallel:
            linear 3.2 rotate 360
        parallel:
            xzoom 2.0
            pause(3.2)
        parallel:
            pause (3.2)
            linear .5 xzoom 1.0
    pause (3.2)
    scene white with hpunch
    "Oh, wait, that's me."
    play sound "sfx/heavy_bag_drop_dirt2.ogg"

    "I crash onto my back, my head turned skyward towards the blinding light."

    "I wince at the bright morning sun."

    "My whole body fills with pain. Right down to my very soul."

    "???" "Are you still breathing?"

    Hiroya "Hn..n."

    scene CG kaori crash with Dissolve (3.0)

    "???" "Oh good. You're not dead."

    "???" "You made some pretty good air-time just now!"

    "The girl leers over me with a quizzical look on her face."

    "She wears a red tie with her uniform. Her blonde hair is pulled into a tight ponytail that blows with the wind."

    "???" "Hey! Stop staring with those dumbstruck eyes and say something!"

    Hiroya "Kaori...Chiba."

    "???" "Huh?"

    scene courtyard empty with dissolve

    Hiroya "You animal! How can you kick me like that?"

    Hiroya "That definitely cost me some hit points."

    show Kaori u shout p1:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            zoom 1.4
            ypos 2.06
            easein 0.15 ypos 1.25
            easein 0.1 ypos 1.3

    Kaori shout "Well {i}excuse me{/i} for acting in self-defence!"

    show Kaori frustrated with Dissolve(.25)

    Kaori "If anything, you should be apologizing for scaring me like that."

    Kaori concerned "I thought you might be some thug out to get me, or something."

    Hiroya "I'm a student! I was just trying to get to my classroom."

    Kaori cool "Hmm."

    Kaori embarrassed "Well I can see that now."

    Kaori frustrated p2 "You just caught me off guard, is all."

    Kaori embarrassed "I may have...overreacted a little."

    Hiroya "You nearly bisected me with your foot!"

    Kaori shout "Oh you're fine. Come on! Up-up on your feet!"

    "To her credit, Kaori lowered to give me a hand and helped me back to my feet."

    Kaori p1 cool "..."

    Kaori speaking "So. I take it you recognize me?"

    Hiroya "Y-yeah, You're Kaori Chiba."

    Hiroya "You're the president of the student council, right? I've seen you at school assemblys and stuff."

    Kaori confused "Hmm."

    "She's staring daggers at me. She has an intense aura about her."

    "She squints her eyes, scanning me from head to toe."

    Kaori p2 cool "Are-are you sure that you're a student here?"

    Hiroya "U-um, I'm Hiroya Tachibana. Room 2A."

    Kaori confused "Tachibana?"

    "That figures."

    "There's no way she'd recognize a relative nobody like me."

    "She seems oddly suspicious of me for some reason."

    Kaori shout "Why were you running like that anyway?"

    Kaori frustrated "Yeah I get it, running to class or whatever."

    Kaori confused p2 "And hey! What's up with your uniform?"

    Hiroya "Huh? My uniform?"

    "I look down at my clothes. I guess my shirt's a little wrinkled, but it's not horrible."

    Kaori frustrated p1 "That uniform represents a lot of history. I would expect a Sugawara student to show a little more pride."

    Hiroya "I don't know. I had a busy morning. Cut me some slack, alrght? I need to go to class now. Hirayama-sensei isn't known for leniency."

    Kaori shocked "Hey, hold on just a minute!"

    Hiroya "What is it?"

    Kaori cool "It’s just a bit strange that I haven't really seen you around school." with dissolve

    Kaori cool "You're not in any clubs, are you?"

    Hiroya "I’m not in any clubs, no."

    Kaori p2 frustrated"I didn't think so. I try to visit each of them regularly. I've never seen you at a meeting."

    Hiroya "Look, I'm just not much of a club person. I have a lot of stuff to deal with and I don't need the extra hassle."

    Kaori shout "That’s unacceptable! Every student should join a club."

    Kaori shocked "It builds character! And relationships that serve as the foundation for a responsible student life!"

    "Jeez, this girl."

    Kaori p1 cool "Consider this an order from your student council president! You {i}will{/i} join a school club while you are a student at Sugawara!"

    Hiroya "Or what? Is that even something the president can do?"

    Kaori shout"I-it's the sentiment that counts! What, is it not enough encouragement for you!?"

    Hiroya "Can I go to class now?"

    Kaori p1 frustrated "I guess."

    Hiroya "Alright then. I'll just be on my way then."

    Kaori p2 shout "Hey..."

    Kaori "I've made a lot of enemies in my time here as president."

    Kaori frustrated "It's hard to know who I can trust."

    Hiroya "Maybe it has something to do with your serious lack of impulse control."

    Kaori shocked "Huh? Is that how I come across to you?"

    Kaori sad2 "Coming from you, someone I just met...that's -"

    "This girl."

    Hiroya "Look. I don't feel one way or another about you, Chiba. I'm just a guy trying to enjoy my school life."

    Kaori speaking "Well then. We may just have to put that to the test." with dissolve

    Kaori speaking p1 "I'm going to need your help with something soon. Be ready for when the time comes."

    Kaori happy "Believe it or not, I actually care about each and every student at this school."

    Kaori caring "As Student body president it is my duty to give each and every student at Sugawara High the best chance at a wonderfull youth experience."

    Kaori speaking "Stick with me and I can make good things happen for you."

    Hiroya "I'll take that under consideration, Chiba."

    Kaori wink "Kaori."

    Hiroya "Um, okay. Kaori then."

    Kaori speaking "Much better."

    Kaori speaking p2 "Now get to class. And join a club while you're at it. Consider it an order from your favorite class president!"

    Kaori wink p2 "Until we meet again. Hi Ro Ya."

    hide Kaori with dissolve

    "She flips her ponytail and walks away just a little too proudly."

    Hiroya "Yeah. Whatever."

    "My head hurts."

    "What was that she said? About making enemies?"

    "Something tells me I should stay far away from her."

    "Kaori."

    scene black with fade

    stop music fadeout 1.0
    play sound "sfx/westminster1.ogg"
    play music Early fadein (5.0)
    queue sound "sfx/tstep_tile1.ogg"
    scene hallway 1 empty with dissolve
    "When I get inside, I go straight upstairs to the classroom."
    play sound "sfx/door_open.ogg"

    "When I get to the door I peek through the window, contemplating wether or not it would be possible to sneak in without Hirayama-sensei noticing."

    "Huh? That's strange."

    "Inside I see my fellow classmates chatting away, wandering around the classroom. Not doing anything in particular."

    "I double check the time on my phone. Class definitely should have started by now."

    "Guess I'll go inside and see what's going on."
    play sound "sfx/door_close.ogg"

    scene classroom with wiperight
    "If I didn't know better, I would think it was break time."
    show Akari vhappy p1 u onlayer master:
        subpixel True xpos 0.5 ypos 1 xanchor 0.5 yanchor 0.0 yoffset 0.0 xzoom -1.0 zoom 1.2 rotate None
        xflip
        bounce

    Akari "Oh you're here! Good Morning, Hiroya!"

    Hiroya "Oh, hey Akari."

    Hiroya "What's going on? Why hasn't class started?"

    show Akari p2 questioning with dissolve

    Hiroya "And dare I ask, what is on your desk?"

    scene CG Akari fruit happy with dissolve

    Akari "Oh this? Just a little snack!"

    "Strawberries, grapes, apple slices, pineapple cubes, and some other fruits are arranged in a circle."

    "No, not just a circle. The fruit pieces seem to be arranged into a shape."

    Hiroya "Hmm. It looks like an animal of some kind."

    Hiroya "A mouse?"

    Hiroya "Oh, wait - it's definitely a cat."

    scene CG Akari fruit questioning with Dissolve(.25)

    Akari "It's not a cat, it's a panda!"

    Akari "See? Look at the ears."

    Hiroya "Yeah, I see it now."

    "I {i}guess{/i} I can see it. Kinda hard to tell when it's just fruit."

    "This weird girl is Akari Miyazaki. She sits next to me in homeroom."

    "Actually, she's been sitting next to me since middle school. I guess we've sort of grown up together, if I think about it."

    "She's always been nice enough to me, and I've got nothing against her or anything but..."

    Hiroya "Akari..."

    Hiroya "Why did you make the panda on your desk? You'll make it sticky."

    Akari "Yeah, but I couldn't make the shape in the box."

    Akari "There's no way it would fit!"

    "...but she's got this bad habit of causing public disturbances."

    "Usually completely obliviously."

    "And to the detriment of others."

    "Namely, me."

    Hiroya "Akari, you're going to get in trouble again."

    scene CG Akari fruit happy with Dissolve(.25)

    Akari "Hey, you came in pretty late today, didn't you? Did something happen?"

    "She totally changes the subject."

    Hiroya "Not really. I woke up late, I guess. I still made it though, didn't I?"

    scene CG Akari fruit questioning with Dissolve(.25)

    Akari "Well you got lucky this time. Hirayama-sensei is late too!"

    Hiroya "So that's why class hasn't started."

    Akari "Hm. I guess so. And you weren't here so I guess I got kinda bored?"

    "I’m hearing what she says, but I just can’t take my eyes off all that fruit."

    "Since walking out on my dad's lame ass dinner, I haven't had a thing to eat."

    "I'm so hungry. I know I shouldn't but..."

    "...but I really wanna eat her panda."

    menu:
        "Ask about your teacher.":
            scene classroom with dissolve
            Hiroya "It’s not like Hirayama-sensei to miss class without any sort of explanation."
            show Akari p2 nervous u at center:
                xflip

            Akari "I hope everything is okay. Someone should go and talk to the principal."
            Akari questioning "Will you come with me?"
            Hiroya "Huh?"
            Akari "To the principal’s office. I want to ask permission to go and check up on her."
            Hiroya "Isn’t that more of a job for the class rep?"
            Akari speaking "But I’m the class rep."
            Hiroya "Since when?"
            Akari p3 "Since Yumi-chan got suspended of course!"
            Hiroya "I don’t recall you being appointed."
            Akari p5 angry2 u "I appointed myself!"
            Hiroya "I {i}really{/i} don’t think that’s how that works."
            Akari p6 angry3 "I make a great class rep. I cleaned the chalkboard and everything."
            Hiroya "Oh. You did?"
            Hiroya "Well, I guess that is something."
            Akari p3 confident "Yeah!"
            Akari questioning p1 "So, will you come to the principal's office with me?" with xflip
            menu:
                    "Yeah I'll come. It's not like anything is happening here.":


                        Akari vhappy"Great!"
                        show Akari nervous u p2 at center with dissolve:
                            xzoom 1
                        Akari "But..."
                        "Why’s she staring so intently at her food panda?"
                        "Ah, she must be wondering if she can eat it all now."
                        Akari questioning" Hey Hiroya, are you hungry?"
                        "Is that even a question?"
                        Akari happy "I brought a little snack today. I would hate for it to go to waste!"
                        Akari "So I'll share it with you, if you like."
                        Hiroya "Akari..."
                        show Akari p2 questioning with dissolve:
                            xflip
                        Akari "Hmm?"
                        Hiroya "Marry me."
                        Akari p2 scheming "Hmm."
                        pause (1)

                        Akari p6 angry2 "Hey! How can you say that over fruit?"
                        hide Akari with dissolve
                        "We spend the next few minutes savoring the sweet fruits laid upon her desk. Normally I would find it a little bit gross, but under the circumstances I decide to ignore that."
                        play sound "sfx/tablewipe.ogg"
                        "With all the pieces gone, Akari uses the side of her hand to wipe the juice back into her lunchbox."
                        Akari "Ah!"
                        "She holds her now dripping hand into the air, as if surprised that it was now covered in fruit juice."
                        show Akari p4 confident u:
                            ypos .09
                            xpos .6
                            xflip
                            pause(.5)
                            linear 1.0 xpos .55
                            pause (.5)
                            linear 2.0 xpos .45
                        Hiroya "No, don't you dare..."
                        hide Akari with hpunch
                        Akari "Hyaa!"
                        play sound "sfx/syrup_hands_slop.ogg"
                        "She slaps her wet sticky hand across the sleeve of my uniform."
                        Hiroya "Nooo, why! That’s gross, Akari!"
                        Akari "That's what you get for mooching!"
                        play sound "sfx/door_open.ogg"
                        "A moment later, the door slides open."
                        "???" "Please take a seat, everyone."
                        hide Akari with dissolve
                        "Ah, Hirayama-sensei showed up."
                        Hirayama "Sorry for the delay, everyone, but break time is over. We have lots to go over today!"
                        "It's the teacher."
                        Hiroya "There she is. I wonder why she was late."
                        Akari "Her hair is messier than usual!"
                        Hiroya "Maybe she got in a fight with another teacher?"
                        Akari "Or a bear!"
                        Hiroya "Bear attack?"
                        Akari "Bear attack!"
                        Hirayama "Miyazaki-san! Tachibana-san! I said class is starting!"
                        Akari "Ach!"
                        play music Chalkboards fadein 2.0
                        scene black with fade

                    "Why don't you just go by yourself?":
                        Akari sad "Awe, but he scares me!"
                        Hiroya "Who? The principal?"
                        Akari nervous "Yeah, a little."
                        Hiroya "I’ve met him, he’s a nice old man. A class rep can’t be afraid of our school’s leader!"
                        Akari p3 frown" But he has that beard!"
                        "She’s scared of his facial hair?"
                        Hiroya "Lots of adults have beards. It’s not scary. It’s a sign of wisdom."
                        Akari p6 angry1 "It looks like something dead."
                        Hiroya "If I grew a beard, would you be scared of me?"

                        Akari p5 angry2 "I would kick it off of you!"
                        Hiroya "That makes no sense."
                        Hiroya "*sigh*"
                        Hiroya "Do you really want me to go with you?"
                        Akari p4 sad "Mhmm."
                        Hiroya "Fine, but if that thing turns out to be alive, don’t expect me to catch it."
                        Akari confident "I’ll use you as a shield!"
                        Hiroya "Fantastic. Let's go."
                        show Akari p2 nervous with dissolve:
                            xflip
                        "But..."
                        "Why’s she staring so intently at her food panda?"
                        "Ah, she must be wondering if she can eat it all now."
                        Akari questioning "Hey Hiroya, are you hungry?"
                        "Is that even a question?"
                        Akari happy "I brought a little snack today. I would hate for it to go to waste!"
                        Hiroya "Akari..."
                        show Akari p2 questioning with dissolve:
                            xflip
                        Akari "Hmm?"
                        Hiroya "Marry me."
                        Akari p2 scheming "Hmm."
                        pause (1)
                        Akari p6 angry2 "Hey! How can you say that over fruit?"
                        hide Akari with dissolve
                        play sound "sfx/door_open_close.ogg"
                        "???" "Take a seat, everyone."
                        "Crap! She actually showed up!"
                        Hirayama "Sorry for the delay, but break time is over. We have lots to go over today!"
                        Hiroya "Quick! We have to get rid of the evidence!"
                        Akari p1 speaking "Right!"
                        hide Akari
                        "Together we shovel the fruit pieces into our mouths as the teacher moves to our side of the room."
                        "I'm so hungry that the fruit just seems to melt away. Delicious!"
                        "Akari on the other hand seems to be struggling to keep up."
                        Hirayama "Tachibana-san! I said class is starting!"
                        "She must have noticed the way I was leaning out of my desk. I scoot away and turn towards the window."
                        "Hirayama-sensei comes towards my desk, and then turns towards Akari."
                        Hirayama "What... is this?"
                        play sound "sfx/tablewipe.ogg"
                        "She wipes her finger across the sticky sweet puddle left behind by the fruit."
                        Akari "Mhff!"
                        "Akari whimpers, her mouth completely stuffed with the fruit panda snack."
                        "She turns away from the teacher, trying desperately to chew."
                        Hirayama "Miyazaki-san..."
                        Akari "Mhffhmmm!"
                        "She tries to apologize, but that's all she can get out."
                        "What a pitiful girl."
                        play music Chalkboards fadein 2.0
                        scene black with fade
        "Ask about the fruit.":
            Hiroya "Hey, Akari?"
            Akari "Hmm?"
            Hiroya "Are you going to eat that?"
            Akari "Well I was going to, but..."
            Akari "But then I started thinking about pandas, and the sweet little pineapple bits."
            scene CG Akari fruit happy with dissolve
            Akari "And they're so pretty when they're laid in a pattern like this."
            Akari "I just want to look at them for awhile."
            "I’m so hungry my stomach is doing backflips."

            Hiroya "Akari, I know our homeroom teacher hasn’t shown up today, but she could still walk in at any moment. You know?"
            scene CG Akari fruit annoyed with dissolve
            Akari "What’s your point?"
            Hiroya "If Hirayama-sensei walks in with that mess on your desk, she’s going to be very angry."
            scene CG Akari fruit questioning with dissolve
            Akari "Hmm."
            "She’s thinking about it."
            scene classroom with wiperight
            "Come on, Akari..."
            "Maybe if I think hard enough, I can telepathically convince her."
            "Give Hiroya food... Give Hiroya food... Do it... DO IT!"
            "JUST DO IT!"
            show Akari u confident p4 at center:
                xflip
                bounce
            Akari "Aha!"
            Akari "Hiroya! I have a favor to ask!"
            Hiroya "Oh, is that so?"
            "Come on, Akari, say it..."
            Akari p3 vhappy "If the teacher walks in, let me hide my snack in your schoolbag!"
            Hiroya "M- maybe I should help you eat it instead..."
            Akari frown p1 "Eh?"
            Hiroya "I mean, you wouldn't want it to spoil or anything, right?"

            Akari scheming p2 "Hmm. Wait a minute! I've seen this look on you before!"
            Akari "Hiroya, you skipped breakfast again, didn’t you!"
            Hiroya "*sigh* It was a tough morning."

            Akari sad p2 "You're so hopeless sometimes."
            Hiroya "So you'll let me eat it then?"
            Akari p1 questioning "If the teacher walks in, you'll get in trouble! But I guess you can."
            Hiroya "Akari."
            Akari p2 "Hmm?"
            Hiroya "Marry me."
            Akari p2 scheming "Hmm."
            pause (.5)
            show Akari p6 angry2:
                bounce
            Akari"Hey! How can you say that over fruit?"
            hide Akari with dissolve
            "I reach over and pick up pick up a grape."
            "It's fresh. Not at all like the preserved kind that comes in a pool of syrup."
            "I plop it into my mouth. It's good. Wonderful even."
            "Without hesitation I reach for another. A pineapple cube."
            "It's sweet and juicy and it's perfectly ripened."
            Hiroya "So...good."
            show Akari u speaking p2 at center with dissolve:
                xflip
                ypos 1.0
                bounce
            Akari "Hey, don't eat them all. Or the panda will lose body parts!"
            "I ignore her. I can't help it."
            "The fruit is wonderful."
            Akari frown "Hey. Hey!"
            "And then it was gone."
            Hiroya "Sorry, Akari."
            Akari nervous "Aww you ate them all! How could you!?"
            Hiroya "I'm sorry..."
            Hiroya "But your panda was really delicious. So thanks."
            Akari sad "You are completely hopeless, Hiroya."

            play sound "sfx/door_open.ogg"
            "The door slides open."
            "???" "Please take a seat, everyone."
            hide Akari with dissolve
            "Ah, Hirayama-sensei showed up."
            Hirayama "Sorry for the delay, everyone, but break time is over. We have lots to go over today!"
            "It's the teacher."
            Hiroya "There she is. I wonder why she was late."

            Akari "Her hair is messier than usual!"
            Hiroya "Maybe she got in a fight with another teacher?"
            Akari "Or a bear!"
            Hiroya "Bear attack?"
            Akari "Bear attack!"
            Hirayama "Miyazaki-san! Tachibana-san! I said class is starting!"
            Akari "Eep!"
            play music Chalkboards fadein 2.0
            scene black with fade

    scene classroom empty with fade
    "Well, now that Hirayama-sensei is back, the classes are back to the norm."
    "Math, English, Literature, the usual subjects."
    "On any other day, classes like these would be a breeze..."
    "...But I was kicked out last night."
    "Well, Akari’s drawing on her notebook, so at least I’m not the only one ignoring the teacher."
    "Maybe I can look for a part-time job after school today."
    "I haven't really worked before, but everyone has to start somewhere."
    "Once I get some money, I'll be in a much better spot."
    "This is easy stuff."
    "I got this!"
    "I say the words in my head over and over in an attempt to psych myself up."
    "Heck yeah, this is gonna be great!"
    Akari "Psst! Hiroya!"
    "Akari leans over, whispering to me."
    Akari "Hey, want to come over later?"
    Hiroya "Huh? I dunno, why?"
    Hirayama "Tachibana! Miyazaki! Again you interrupt my lecture. Care to explain yourselves?"
    Hiroya "Um, no."
    Akari "Sorry, I’ll be quiet!"
    "Way to go, Akari, getting me in trouble as usual."
    play sound "sfx/sms.ogg"
    "*Bzzt*"
    "My phone buzzes."
    "\"So since sensei is back and we can’t talk during class...\""
    play sound "sfx/sms.ogg"
    "*Bzzt*"
    "Damnit Akari."
    "\"I thought I’d text you!\""
    play sound "sfx/sms.ogg"
    "*Bzzt*"
    "\"Anyway, wanna come over for dinner with me and Miyu?. We're making curry tonight! Mom said I could invite you over!\""
    "{i}Dinner{/i}"
    "I press the reply button."
    Hiroya "Food? For free? Hell yeah."
    "And sent."
    $renpy.music.set_volume(0.0, delay=0.2, channel='music')
    #pause(0.2)
    play sound "sfx/sms_akari.ogg"
    pause(1.0)
    $renpy.music.set_volume(1.0, delay=4.0, channel='music')
    "* * *"
    Akari "Oops."
    "And of course she would leave her phone on max volume."
    Hirayama "Miyazaki!"
    Akari "I-I’m so sorry!"
    stop music fadeout 1.0
    play sound "sfx/westminster1.ogg"
    pause (1.5)
    scene hallway 1 empty with wiperight
    pause (2.0)
    play sound "sfx/door_close.ogg"
    #Suzuki introduction scene
    play music Suzukitheme fadein (5.0)
    scene hallway 2 with wipeleft
    "When the lesson ends, I leave the classroom and head downstairs. Akari walks with me until we arrive in the common room for our break period."
    queue sound "sfx/tstep_tile1.ogg"
    show Akari p2 u happy at center with dissolve:
        xpos .5
    Akari "I’m going to look for Miyu-chan! I need to invite her too."
    Hiroya "Right, I hope she can come."
    hide Akari with dissolve
    "I Guess I’ll hit up the vending machine and get my usual bean bun and green tea."
    "Wow, it's 400 yen."
    "I never realized how expensive this was."
    "If I keep buying these for lunch, I'll run out of money in no time!"
    "Nope, I have to stop that train of thought."
    Hiroya "I’m going to get a job!"
    play sound "sfx/coindeposit.ogg"
    queue sound "sfx/vending.ogg"
    "I put the coins in the machine and take my first real meal of the day."
    "I lean up against the wall in my usual spot when..."
    "*THUMP*" with vpunch
    show Suzuki u p1 tough with dissolve
    "Hmm...?"
    "A guy props himself against the wall in front of me. A member of the baseball team if I recall correctly."
    BaseballGuy "Hey, Tachibana! You’re pretty tough, right?"
    Hiroya "Hmm? What?"
    "The way he’s looking at me... is he analyzing me?"
    show Suzuki u p1 questioning with dissolve
    BaseballGuy "Hmm."
    play sound "sfx/toon_poke.ogg"
    Hiroya "Eh!?"
    Hiroya "Did you just poke my arm?"
    show Suzuki u p1 speaking with dissolve
    BaseballGuy "Yep, just as I thought. I bet you could take on anyone at Sugawara, big guy."
    Hiroya "..."
    "How am I supposed to react to this?"
    show Suzuki u p1 confident with dissolve
    BaseballGuy "Say, I don’t suppose you’re any good at swinging are ya?"
    Hiroya "Excuse me?"
    "Is this guy seriously trying to pick a fight?"
    BaseballGuy "Well, are you?"
    Hiroya "Who the hell are you?"
    show Suzuki u p1 shouting with dissolve
    BaseballGuy "Who am I? Who am I!?"
    show Suzuki u p1 confident with dissolve
    BaseballGuy "..."
    show Suzuki u p1 vhappy with dissolve
    BaseballGuy "I guess that just proves it. We've got some serious work to do."
    "This guy’s too close for comfort."
    show Suzuki u p1 speaking with dissolve
    BaseballGuy "Anyway, Kaori-chan told me to come and find you. She seems to think you could be useful to us."
    "Kaori. The girl I ran into this morning."
    Hiroya "Not interested."
    show Suzuki u p2 shouting with vpunch
    BaseballGuy "How can you even say that without hearing our proposition?"

    Hiroya "Let me guess. Kaori Chiba told you that I'm not in any clubs. You've come to recruit me to the baseball team."
    show Suzuki u p2 questioning with dissolve
    pause(.5)
    show Suzuki u p1 vhappy with dissolve
    BaseballGuy "Ahahaha, that's pretty funny!"
    show Suzuki u p1 speaking with dissolve
    BaseballGuy "No, sorry. We've already got plenty enough talent."
    show Suzuki u p1 confident with dissolve
    "BaseballGuy" "Though she did ask me to come and find you. She seems to think we might be able to assist each other, if you'll just hear me out for a sec."
    hide Suzuki with dissolve
    Hiroya "I highly doubt that. We don't know each other and..."
    play sound "sfx/butcherpaper_short.ogg"
    Hiroya "Wait, is that... roast beef?"
    #Show roast beef
    BaseballGuy "Huh? This?"
    "He raises it up so I can see."
    "A perfect home-made roast beef sandwich. With cheese."
    play sound "sfx/butcherpaper.ogg"
    "He peels back the paper a little more. "
    "That little bit of fruit and my bean bun, both of them combined don't even compare."
    BaseballGuy "You know, my folks own the cafe across from the library."
    BaseballGuy "I can give all sorts of delicious meals to the people I like."
    "It smells so good."
    show Suzuki u p2 happy at center:
        bounce
    BaseballGuy "Ah, gotcha! You're drooling like a dog!"
    show Suzuki u p2 vhappy with dissolve
    BaseballGuy "No one can resist Mother's victorious roast beef sandwich!"
    BaseballGuy "I’m sure that if you’ll just hear me out, we could make a trade that would benefit both of us."
    "He tosses me the sandwich, knowing that I had fallen into his trap."
    "It's actually pretty heavy."
    "It actually has a good amount of meat on it!"
    show Suzuki u p1 tough with dissolve
    BaseballGuy "Now listen up, punk! I’m about to fill you in on a top-secret mission."
    Hiroya "*sigh* I guess I have no choice."
    show Suzuki u p2 speaking with dissolve
    BaseballGuy "The name is Suzuki Kisaragi, captain of the baseball team. Star athlete. Recruiting officer. You can get my autograph later."
    hide Suzuki
    Hiroya "Hiroya Tachibana, member of the going home club. Bridge enthusiast. If you ever become famous, expect to see that autograph on Ebay."
    "I take a bite of the sandwich. It's tender. Just right."
    show Suzuki u p1 questioning with dissolve
    Suzuki "Bridge enthusiast? What the hell?"
    show Suzuki u p1 tough with dissolve
    Suzuki "Shut up, never mind that."
    Suzuki "We need your help restoring Sugawara High School’s reputation as an extremely prestigious school."
    Hiroya "Sugawara? Prestigious?"
    "Who does this guy think he’s fooling?"
    show Suzuki u p1 confident with dissolve
    Suzuki "No, really! Hear me out."
    hide Suzuki
    scene black with fade
    play music frozendream fadein (2.0)
    Suzuki "For a while, Sugawara High was famous for its academics and athletics. Students would apply from all over the country to have a chance to graduate from this school."
    Suzuki "Our sports programs were on national television. Our events would even draw spectators in from other cities, just to see what our clubs would put together."
    Suzuki "But..."
    Suzuki "Two years ago, all of that changed."
    Suzuki "A private school, built by one of this town’s oldest and most influential families, was opened our freshmen year."
    Suzuki "For the first year, things were about the same as they had always been."
    Suzuki "But last year, the unthinkable happened."
    queue sound "sfx/thunderclap.ogg"
    scene CG Shizuka dark with fade
    Suzuki "Shizuka Endo. "
    Hiroya "Hmm? Endo?"
    Hiroya "Wait."
    Suzuki "That’s right. The daughter of Mr. Endo. as in Endo Enterprises."
    "Of course I know the name. Everyone knows it."
    "Endo brought the tech industry to this city. Along with factories, stores, offices, you name it."
    "At least half of the real-estate in this town must be owned by Endo by now."

    Suzuki "Some people think Sakura no-Ki Academy was built just for Shizuka. A castle for a princess. Daddy's little princess got her very own private school to rule over."
    Suzuki "She's the class president, club director, hell, she's the top student on top of that."
    Hiroya "That doesn’t sound right. Which people say that? Are you sure your information is good?"
    show Suzuki u p2 shouting:
        xflip
        ypos 0.09
        xpos -.2
        easein (.2) xpos .1
    Suzuki "Shut up and listen!"
    scene black with fade
    scene classroom with dissolve
    show Suzuki u p1 confident with dissolve:
        xpos .6
        ypos 50

    Suzuki "Since Shizuka’s rise to power, there’s been a huge drop in attendance to our school’s events, and applications to this school reached an all-time low."
    Suzuki frown "More importantly, baseball ticket sales dropped."
    Suzuki tough "We had 16 consecutive wins last year! They should be building statues of us!"
    Suzuki "But our turnouts are lower than they've ever been."
    Suzuki questioning "The only possible explanation for the loss in fan attendance..."
    Suzuki questioning p2 "Is that Sakura no-Ki baseball club has stolen our spotlight!"
    Hiroya "Is it possible that you just suck as team captain?"
    show Suzuki shouting p2 at bounce
    Suzuki "No, that's not possible!"
    Suzuki p1 speaking u "Besides, it was Kaori-chan’s conclusion, not mine!"
    "Her again?"
    Suzuki tough "All of it, a dastardly plan by Shizuka Endo to steal the glory from us who've worked for it!"
    Hiroya "Do you actually believe that?"
    Suzuki speaking "Well of course. After all, baseball is the most exciting thing there is."
    Suzuki questioning "It's the most important club at Sugawara. It's only logical she would strike here first!"
    Hiroya "And that's what Kaori told you."
    Suzuki tough "If Kaori-chan says we can do something about it, I intend to!"

    "What a load of crap."

    Hiroya "So, what do you want from me?"
    Suzuki speaking "Oh, nothing much."
    Suzuki happy "Come meet me in the courtyard after school."
    "He points at the thin paper wrapper in my hand, the one which had once contained something delicious."
    Suzuki vhappy "I’ll have another one of those for you when you come."
    "My one true weakness."
    "With that, we make our way to my class."

    "The students start to take their seats. Hojo-sensei enters through the front entrance."
    Suzuki tough "I’ll be near the gates. We’ll fill you in on our top-secret strategy once you get there."
    "Hojo" "Hey you, you're not in this class."
    Suzuki "See you later, buddy!"
    Suzuki "Ciao!"
    hide Suzuki with moveoutright
    "He takes the back exit, in no particular hurry."
    "Why is this school so full of weirdos?"
    "Hojo" "*sigh* Let's get started."
    play music SugarMorning fadein (1.0)
    scene black with fade

    scene classroom empty with dissolve
    "Classes continue as usual. I've pretty much given up on absorbing anything from today's lessons."
    "My head just isn't in the right place for studies right now."
    "This Suzuki guy, the student body president, I barely know either of them."
    "Besides, I’ve got more important things to think about."
    "I wonder if the train station cafe is hiring."
    "I could do a job like that. Go to work afterschool, clean tables and such."
    "I should go talk to the manager. Maybe I can go when--"
    Akari "Psst."
    "Damnit, can't I just get 5 minutes to space out during class!?"
    "Akari leans out of her desk."
    Akari "Hey Hiroya..."
    "Her best attempt at a whisper."
    "I try to ignore her."
    Akari "Psssssssssst!"
    "\"Don't look. Keep your eyes straight ahead. At Hojo-sensei's balding head.\""
    Akari "Hiroooyaaaaaaa!"
    Hiroya "Shush. We’re in class."
    Akari "Hey, so about dinner tonight..."
    "My scolding was completely ineffective."
    "I suppose that's right. I already told Akari I would go to her house after school."
    Akari "I was just talking to Miyu-chan. You'll never guess who she was with!"
    Hiroya "Quiet, you. You'll get me in trouble."
    hide Akari
    Hojo "What was that!?"
    Akari "Ach!"
    "Hojo-sensei barks, but doesn't turn away from the board."
    Hojo "Well, anyway, using what we know about the law of sines..."
    "He returns to the lesson. Akari stares at the teacher's back for a couple seconds, leaning out of her desk to talk again."
    "I try to ignore her again, but she doesn't seem to get the hint."
    Akari "So go on, Guess!"
    Hiroya "I have no idea. Just tell me."
    Akari "So these two girls. Oh! They’re sisters! Umm, they just transferred in and they’re living with Miyu-chan now. My mom always makes too much food - even though she can only make one thing - but it’s really good!"
    "What did I do to deserve this?"
    Akari "And they're coming over tonight! You're going to help me, right?"
    Hiroya "Help? With what? What does this have to do with me?"
    Akari "You should be pleased!"
    Hiroya "Hey, all I agreed to was free curry. What's this you're trying to drag me into?"
    Akari "Dummy! Don't you want to have dinner with a bunch of cute girls?"
    Akari "This could be a great opportunity for you!"
    Hiroya "What am I? A harem protagonist?"
    Akari "Hiroya!"
    hide Akari
    "Hojo" "Miyazaki!"
    Akari "Eep!"
    Hojo "*sigh* You could at least pretend to pay attention, Miyazaki."
    Akari "Yes, sensei!"
    "She says that, but I can clearly see her on her phone."
    play sound "sfx/sms.ogg"
    "*Bzzt*"
    "Of course it’s her. She’s sending me text messages again."
    "\"Back me up on this! Miyu-chan is an introvert! We've got to make sure she becomes friends with her new roommates!\""
    "\"So you’re gonna help me make sure tonight is extra super-duper fun!\""
    "I really do try to understand her reasoning. Sometimes though, she's just in another world."
    "And I actually do really want that roast beef Suzuki was offering."
    "Akari wasn't lying when she said her mother only knows how to make one dish."
    "But still, it seems like she really wants me to be there."
    "I press the reply button."
    menu:
        "Sure, I’ll come over for dinner.":
            "And sent."
            $renpy.music.set_volume(0.0, delay=0.2, channel='music')
            #pause(0.2)
            play sound "sfx/sms_akari.ogg"
            pause(1.0)
            $renpy.music.set_volume(1.0, delay=4.0, channel='music')
            "* * *"
            "*Snap*"
            "The teacher's chalk breaks against the board."
            Hojo "*sigh*"
            "He spins around, his face red with anger."
            "..."
            Akari "Ehehe..."
            "..."
            Hojo "Of course it's you, Miyazaki. Who else could it possibly be!"
            Akari "Ehehe... Well what can you do? Hehe..."
            "..."
            Hojo "Bathroom. Duty."
            Akari "B... b... huh?"
            Hojo "BATHROOM DUUUUUUTYYYYYY!"
            Akari "I’m so sorry!"
            "Saw that coming."
            play music Sugawara fadein (1.0)
            scene black with dissolve
            scene sky with dissolve
            "This is how our days usually go."
            "Me, just trying my hardest to get through the day. Akari can be a bit of a pain sometimes, but she has good enough intentions."
            "She'll pretend to be upset for awhile, but she'll be fine in the end. She's always been that way. I look over to see how she's doing."
            "She's trying her best to glare at me, but I can tell she's holding back a huge smile."
            "You’re not fooling anyone, Akari."
            "I copy down the homework assignment on the board and try my best to focus for the remainder of the period."
            "Akari leaves me alone for the rest of the class, but I know that regardless of her detention, she's looking forward to tonight."
            scene black with fade
            jump Chapter2DinneratAkaris

        "Sorry, I already made plans for tonight.":

            "Aaaand sent."
            $renpy.music.set_volume(0.0, delay=0.2, channel='music')
            #pause(0.2)
            play sound "sfx/sms_akari.ogg"
            pause(1.0)
            $renpy.music.set_volume(1.0, delay=4.0, channel='music')
            "* * *"
            "*Snap*"
            "The teacher's chalk breaks against the board."
            Hojo "*sigh*"
            "He spins around, his face red with anger."
            "..."
            Akari "Ehehe..."
            "..."
            Hojo "Of course it's you, Miyazaki. Who else could it possibly be!"
            Akari "Ehehe, well what can you do? Hehe..."
            "..."
            Hojo "Bathroom. Duty."
            Akari "B-B... huh?"
            Hojo "BATHROOM DUUUUUUTYYYYYY!"
            Akari "I’m so sorry!"
            "Saw that coming."
            play music Sugawara fadein (1.0)
            scene black with fade
            scene sky with dissolve
            "This is how our days usually go."
            "Me, trying my hardest to study, Akari being a bit of a pain, but with good enough intentions."
            "It's not like it's really a big deal anyway. Akari and I can hang out whenever."
            "But I'm actually curious to see just what Suzuki and the president actually have in mind."
            "And they're actually willing to pay me. Even if it's just in food."
            "Still, I can't help but feel a little bit bad for Akari."
            "I look over to see how she's doing."
            "She's facing away from me, with her head down on her desk. Somehow I don't think it's her detention that's bothering her."
            "I'm sure she's read my text by now."
            "I copy down the homework assignment on the board and do my best to ignore her for the remainder of the period."
            "She doesn't try to whisper to me again."
            scene black with fade
            jump Chapter2Rivalry
