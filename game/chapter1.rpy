label chapter1:

    $ camera_reset()
    play music Chalkboards fadein 2.0
    $ renpy.pause(1, hard=True)
    show text "Sarchalen Visual Media Presents: " with dissolve
    $ renpy.pause(2, hard=True)
    scene chapter_screen_1 with fade
    $ renpy.pause(1, hard=True)
    show text "{size=36}Chapter 1. Independence Day" at chaptertitlespot with moveinleft
    $ renpy.pause(3, hard=True)
    scene white with Dissolve(.5)
    scene sky
#START TUTTY BLOCK
    Hiroya "Ah-!"
    Hiroya "Hah..."
    Hiroya "It was just a dream."
    "I rub the back of my neck, easing myself back into a new day."
    "I hate dreams like that. They feel too real, and they trick my gullible brain into reliving old memories."
    Hiroya "Damn it."
    "That dream's more than a figment of my imagination. It's a reminder of the spat I had with my old man."
    "How I ran out of the house, and never looked back. I didn't have a plan or anything. I'd hope I would figure something out along the way."
    Hiroya "Haaahn..."
    "Stretching my arms out in a big yawn, I drink in my surroundings."
    scene bridge below day with Dissolve(.5)
    "Ah, yes. This was the brilliant idea I settled on. Living under a damn bridge."
    "I didn't have much to my name at that point. Whatever I could fit into a bag on my way out of the apartment."
    "Got a sleeping bag, some changes of clothes, and whatever leftovers would tide me over. I wasn't about to go back and look my old man in the eye."
    Hiroya "Smug bastard."
    "Of course he called it. That I'd be under a bridge."
    "He should be able to come out and find me. The fact he hasn't done so yet..."
    "Guess I'm on my own."
    "Whatever. I'll manage. I'm basically an adult."
    "I consider my options — should I get a bite to eat? Find a public shower to freshen up? My uniform's all beat up from last night."
    "I glance up to the passage of the morning sun. Wonder how much time I have."
    "I need to get to school too. I didn't set an alarm. Am I late?"
#END TUTTY
    "I make a cursory glance to my watch. My eyes widen in surprise."
    "Oh crap, what time is it? I'm gonna be late."
    "Unless, if I make a break for it, I can still make it to school on time!"
    "Thank goodness I’m still wearing yesterday’s school uniform. I've gotta book it."

    scene bridge sidewalk day with fade
    "I'm not exactly used to taking this route to school, but the familiar architecture of the town serves as solid guide posts."
    Hiroya "I take a left here."
    "Yeah, I can do this. I'm on my own now, I'd be an idiot if I couldn't find my way around town!"

    play sound "sfx/tstep_sidewalk1.ogg"
    scene cafe outside with fade
    "I make my best effort to run as fast as I can, steadily breathing in through my nose and out through my mouth."
    "My eyes dart from side to side. I'm careful to avoid traffic."
    "Last thing I need in my life is to get whallopped and forced back into my father's two-faced care."

    play sound "sfx/tstep_sidewalk2.ogg"
    scene street day with fade
    "Almost there!"
    "Breathe, breathe..."
    "Aha, yes! The gate is still open!"
    play sound "sfx/tstep_sidewalk2.ogg"
    scene courtyard empty with fade

    "I don’t see any students standing around outside. The bell must be seconds from ringing!"
    "I have to go faster. My eyes narrow on the far door, the one that would lead to my homeroom class."
    "Breathe, breathe..."
    "I don't know how much longer I can keep up this sprint, but I have to try."
    "Here comes my second wind! Just about there-!"

    #TUTTY BLOCK#
    play music SchoolCasual fadein (.2)
    Hiroya "Oof!" with vpunch
    #show Kaori u shocked p1

    "???" "!?"
    "A girl. I ran right into her."
    Hiroya "S-sorry, I wasn't watching where I was going-"
    show Kaori u shout p1
    "???" "Haa!?"
    hide Kaori
    Hiroya "!"
    #sfx kick
    scene white with vpunch

    "In the blink of an eye, the girl let out a battle cry, swinging her leg as she turned to face me."
    Hiroya "OOF!"
    "And pounded it into my exposed gut with the force of a bullet train - I didn't have a second to react."
    $ ("With her sheer force of impact, I'm flung ten feet into the air. The world was spinning out of control!")
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
    "Oh, wait, that was me."
    play sound "sfx/heavy_bag_drop_dirt2.ogg"
    "With a rough landing, I land on my back, gazing up towards the sky with a stunned look."
    #scene black with dissolve
    "I winced, trying to keep the sun out of my eyes. My back arced slightly, throbbing with pain."
    "Everything hurt down to my very soul. Thank goodness I didn't land on pavement, or I might've actually needed a hospital."
    "???" "Are you still breathing?"
    Hiroya "Huh?"
    scene CG kaori crash with Dissolve (3.0)

    "The girl was leering over me with a quizzical look on her face."
    "???" "Oh good."
    "???" "You made some pretty good air-time just now!"
    Hiroya "That voice..."
    "Of course. Now I recognized her."
    Kaori "Hey! Stop staring with those dumbstruck eyes and say something!"
    Hiroya "Kaori... Chiba?"

    menu:
        "Why would you do that!?":
            scene courtyard empty with dissolve
            show Kaori u shout p1 with dissolve
            Kaori "Well {i}excuuuse me{/i} for acting in self-defence!"

            Kaori frustrated "If anything, you should be apologizing to me! You got the jump on me!"
            Kaori confused "Besides, you're huge! I thought you were some thug out to get me!"
            Hiroya "S-Sorry?"
            Kaori cool"Hmm."
            Kaori speaking "That's better! Apology accepted."
            "Well ok then. That was easy."

        "Sorry, I wasn't watching where I was going.":
            scene courtyard empty with dissolve
            show Kaori u shout p1 with dissolve
            Kaori glaring "Yeah, I can tell!"
            Kaori frustrated "I guess I can accept your apology... this time."
            Kaori happy "Keep your eyes open next time. You could really hurt someone, y'know?"
            Hiroya "{i}Me!?{/i} You nearly bisected me with your foot!"
            Kaori consoling "Oh you're fine. Come on! Up-up on your feet!"


    show Kaori u glaring p2 with dissolve
    "To her credit, Kaori lowered to give me a hand and helped me back to my feet."
    Kaori cool "..."
    "She was staring daggers at me. She had an intense aura about her."
    Kaori shout "So. I take it you recognize me?"

    Hiroya "Y-yeah, of course. Kaori Chiba from 3A, student council president."
    Kaori speaking "Good! Then we don't need to drag out introductions."
    Kaori confused "Hmm."
    "She squint her eyes to gaze at me. I guess she wouldn't recognize a relative nobody like me."
    Kaori "Are you a new student or something?"
    Hiroya "U-um, I'm Hiroya Tachibana. Room 2A."
    Kaori shocked "I-I knew that. of course. Tachibana."
    "Her mouth flattened as she studied me all over."

    Kaori glaring "Why were you running like that anyway?"
    Kaori frustrated "I mean, I can understand your eagerness to get into the classroom."
    Kaori confused p2 "But you look like you were raised in a barn. What's with your uniform?"
    "I look down at my uniform. I guess it's a little wrinkled, but it's not horrible."
    Kaori frustrated p1 "That uniform represents a lot of history. Show a little pride, will you?"
    Hiroya "Well, it was {i}nice{/i} to meet you, Chiba, but I really have to get to class now."
    Kaori shocked "Hey, hold on just a minute!"
    show Kaori glaring with dissolve
    menu:
        "Tell her you have to go.":
            Hiroya "Sorry, I really can’t be any later than I already am. Hirayama-sensei isn’t known for leniency."
            Kaori "Haaah, {i}fine.{/i} You're right."
            Kaori "Do straighten up that uniform before you go in though."
            # consider it a favor from your favorite student body president!
            hide Kaori with dissolve
            "She walks past me and out of the building, leaving me alone in the school entrance."
            "I sigh. What a strange person."
            scene black with fade

        "Chat with Kaori a bit longer.":
            Hiroya "What is it?"
            Kaori cool "It’s just a bit strange that I haven't really seen you around school." with dissolve
            Kaori cool "You're not in any clubs, are you?"
            Kaori speaking "I visit each of them regularly, but I don’t think I’ve ever seen you at a meeting."
            Hiroya "I’m not in any clubs, no."
            Kaori frustrated "That’s unacceptable! Every student should join a club."
            Kaori shocked "It builds character! And relationships that serve as the foundation for a responsible student life!"
            Hiroya "Yeah, I guess I really just haven’t had the time."
            "That’s not entirely true. It’s not like I’ve had any other responsibilities. I guess I’m just not really that much of a club person."
            Kaori p1 cool "Consider this an order from your student council president! You {i}will{/i} join a school club while you are a student at Sugawara!"
            Hiroya "Or what? Is that even something the president can do?"
            Kaori shout"I-it's the sentiment that counts! What, is it not enough encouragement for you!?"
            Hiroya "I-I guess I'll think about it."
            show Kaori frustrated with dissolve
            hide Kaori with dissolve
            with vpunch

            Hiroya "Ow! What was that punch for?"
            show Kaori u shout p2 at leftoffset2 with moveinleft
            Kaori "Stop looking so sad too! And get to class!"
            Hiroya "Seriously?"
            Kaori happy p1 "Yes! We will meet again. I hope to see you in a club by then. For your sake." with dissolve

            Kaori wink "Toodles~"
            hide Kaori with moveoutleft
            "She flips her ponytail and walks away just a little too proudly."
            "My arm hurts..."
            scene black with fade

    stop music fadeout 1.0
    play sound "sfx/westminster1.ogg"
    play music Early fadein (5.0)
    queue sound "sfx/tstep_tile1.ogg"
    scene hallway 1 with dissolve
    "When I get inside, I go straight to the classroom."
    play sound "sfx/door_open.ogg"
    "Huh? Why is everyone standing around?"
    "That’s odd. Class definitely should have started by now."
    "Guess I'll see what's going on."
    play sound "sfx/door_close.ogg"
    scene classroom with wiperight
    "If I didn't know better, I would think it was break time."
    show Akari vhappy p1 u at rightoffset:
        ypos .09
        xflip
        bounce
    Akari "Hey Hiroya!"
    Hiroya "Akari, why hasn't class started?"
    show Akari p2 questioning with dissolve
    Hiroya "And dare I ask, what is on your desk?"
    scene CG Akari fruit happy with dissolve
    Akari "Oh this? Just a little snack!"
    "Strawberries, grapes, apple slices, pineapple cubes, and some other fruits are arranged in a circle."
    "No, not just a circle. It's an animal of some kind. A fox maybe?"
    "Oh, wait - it's definitely a kitty."
    Akari "It's a panda!"
    scene CG Akari fruit questioning with dissolve
    Akari "Can't you tell?"
    Hiroya "Yeah, I can see that."
    "I {i}guess{/i} I can see that."
    Hiroya "Why is it on your desk, though? You'll make it sticky."
    Akari "Yeah, but I couldn't make the shape in the box."
    Hiroya "Akari, you're going to get in trouble again."
    scene CG Akari fruit happy with dissolve
    Akari "I’m glad you came to school today! I was getting a little worried."
    "She totally changes the subject."

    Hiroya "Yeah, I had a bit of a rough night. Though with all the ‘studying’ getting done here it looks like I could have taken the day off."
    scene CG Akari fruit questioning with dissolve
    Akari "It’s been a pretty easy day so far. Hirayama-sensei never showed up for homeroom today."
    "I’m hearing what she says, but I just can’t take my eyes off all that fruit."
    "I'm so hungry..."
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
            Hiroya "I don’t recall you being appointed. Also, what kind of class rep gets suspended?"
            Akari p5 angry2 u "I appointed myself!"
            Hiroya "I {i}really{/i} don’t think that’s how that works."
            Akari p6 angry3 "You’re mean, Hiroya."
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
            "Come on, Akari, saaay it..."
            Akari p3 vhappy "If the teacher walks in, let me hide my snack in your schoolbag!"
            Hiroya "M- maybe I should help you eat it instead..."
            Akari frown p1 "Eh?"
            Hiroya "I mean, you wouldn't want it to spoil or anything, right?"

            Akari scheming p2 "Hmm. Wait a minute! I've seen this look on you before!"
            Akari "Hiroya, you skipped breakfast again, didn’t you!"
            Hiroya "*sigh* ...It was a tough morning."

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
            "It's sweet and perfect and just the right texture."

            show Akari u speaking p2 at center with dissolve:
                xflip
                ypos 1.0
                bounce
            Akari "Hey, don't eat them all. Or the panda will lose body parts!"
            "I ignore her. I can't help it."
            "The fruit is wonderful."
            Akari frown "Hey. HEY!"
            "And then it was gone."
            "Crap."
            Hiroya "Sorry, Akari."
            Akari nervous "Aww you ate them all! How could you!?"
            Hiroya "I'm sorry..."
            Hiroya "But it was really good. So thanks."
            Akari sad "You are completely hopeless, Hiroya-kun."
            
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
    "Well, Akari’s drawing on her notebook, so at least I’m not the only one igoring the teacher."
    "Maybe I can look for a part-time job after school today."
    "I haven't really worked before, but everyone's got to start somewhere."
    "Once I get some money, I'll be in a much better spot."
    "This is easy stuff."
    "I got this!"
    "This is what I tell myself over and over, in an attempt to psych myself up."
    "Heck yeah, this is gonna be great!"

    Akari "Psst! Hiroya!"
    "She leans over, whispering to me."
    Akari "Hey, want to come over later?"
    Hiroya "I don’t mind, but don’t you think we should talk about this after class-"
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
    "Aaand sent."
    $renpy.music.set_volume(0.0, delay=0.2, channel='music')
    #pause(0.2)
    play sound "sfx/sms_akari.ogg"
    pause(1.0)
    $renpy.music.set_volume(1.0, delay=4.0, channel='music')
    "*BING*"
    Akari "Oops."
    "And of course she would leave her phone on max volume."
    Hirayama "Miyazaki!"
    Akari "I-I’m so sorry!"
    scene black with fade
    stop music fadeout 1.0
    play sound "sfx/westminster1.ogg"
    play music Suzukitheme fadein (5.0)
    #Suzuki introduction scene

    scene hallway 2 with dissolve
    play sound "sfx/door_close.ogg"
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
    "*THUMP*"
    "Hmm...?"
    "A guy props himself against the wall in front of me. A member of the baseball team if I recall correctly."
    show Suzuki u p1 tough with dissolve
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
    show Suzuki u p2 shouting with dissolve
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
    "Endo brought the tech industry to this city. Along with factories, real estate, and new business to boot."
    "At least half of the buildings in this town must be owned by Endo by now."

    Suzuki "Some people think Sakura no-Ki Academy was built just for Shizuka. A castle for a princess. Daddy's little princess got her very own private school to rule over."
    Suzuki "She's the class president, club director, hell, she's the top student on top of that."
    Hiroya "Thaaat doesn’t sound right. You sure your information’s good?"
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
    Suzuki questioning p2 "Is that Sakura no-Ki baseball club has stolen our spotlight! Slipped right in on top of us I tell you!"
    Hiroya "Is it possible that you just suck as team captain?"
    show Suzuki shouting p2 at bounce
    Suzuki "No, that's not possible."
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
    Akari "Don’t give me that."
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
            "Aaaand sent."
            $renpy.music.set_volume(0.0, delay=0.2, channel='music')
            #pause(0.2)
            play sound "sfx/sms_akari.ogg"
            pause(1.0)
            $renpy.music.set_volume(1.0, delay=4.0, channel='music')
            "*BING*"
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
            "*BING*"
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
