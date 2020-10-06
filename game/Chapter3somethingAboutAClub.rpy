label Chapter3somethingAboutAClub:
    play music SugarMorning fadein 1
    $ renpy.pause(1, hard=True)
    scene chapter_screen_1 with dissolve
    $ renpy.pause(.5, hard=True)
    show text "{size=40}Chapter 3: Something About a Club" at chaptertitlespot with easeinleft
    $ renpy.pause(2, hard=True)
    scene white with dissolve
    scene classroom empty
    "I'm back in Hirayama-sensei's class. The day's been pretty uneventful thus far."
    "It's near the end of the period and Hirayama-sensei is passing around the results from yesterday's pop quiz."
    "..."
    "I guess I can say I've had a good morning so far."
    "I woke up early, still full from the cooking Akari and her mother so graciously provided for me. Free of charge at that."
    "My back and shoulders weren't as sore as they were yesterday. Maybe I'm finally getting used to this lifestyle."
    "There was a cool breeze out today. A welcome sign that winter was on it's way."
    "I decided to use my spare time in the morning to pay a visit the school's athletics building."
    "The school is pretty lackluster in most areas, but the sport's facilities are actually decent."
    "The main building has an indoor pool, two gyms, and a multipurpose section where they hold the judo and wrestling classes, along with boys' and girls' locker rooms towards the back."
    "Outside there's the baseball field, archery club, running track, tennis court, and a grassy area that's usually used for the soccer team, but also where the school would host various outdoor events."
    "None of these areas are new, or particularly fancy. But more than adequate."

    #Scene change to gym or something athletic

    scene white with dissolve
    scene sky

    "When I got to the athletics building, I went straight for the locker room and retrieved my PE uniform from my locker."
    "There wasn't anyone else there. I figured this was a good opportunity to get cleaned up."
    "I headed for the showers and turned the water up nice and hot."
    "I took my school uniform in with me too. Not wearing it, obviously."
    "But I took it into the shower with me and sprayed it down. It's the best I could do for now."
    "It's a shame we don't have a bath here at the school."
    "...actually"
    "we do have a pool..."
    "..."
    "Nah. Better not."

    "Of course when I got out, my uniform was soaked. Clean, but soaked."
    "I threw on my PE outfit instead and hung my shirt and slacks near the window to dry."
    "So I decided to do a few laps around the track to pass the time. Hopefully my uniform would be dry enough before class."

    scene classroom empty with squares

    Hirayama "Tachibana-san. Your results."
    Hiroya "Yes, ma'am. Thank you, ma'am."
    "She hands me the paper. She seems to stop at my desk for a moment and before I know it, she pokes a long, skinny finger into my shoulder."
    "Damn."
    Hirayama "Hey Tachibana-san, is your entire uniform slightly wet?"
    Hiroya "Y-Yes, ma'am."
    Hirayama "Hmm, do I want to know why?"
    Hiroya "Not particularly, no."
    Hiroya "...Ma'am."
    "I nod my head slightly in deferment. With a scoff, Hirayama-sensei moves to the next desk in the row."
    show Akari u p1 scheming at rightoffset with dissolve:
        yanchor -.1
        xflip

    Akari "Eeeh?"
    Hiroya "It's nothing!"
    hide Akari with moveoutright

    #sfx paper rustle
    "I rustle the sheet of paper in my hands to flip it over."
    "Red markings were scattered around sparsely. My mouth flattens, surveying the results."
    Hiroya "Hmm."
    "In the top of the corner, I see my grade."
    "{b}{color=#f00000}B-{/color}{/b}"
    Hiroya "Well, it's not {b}bad{/b}, but it's not particularly {i}good{/i} either..."
    "I sigh to myself, lowering the paper back to my desk. I guess I can't call myself an A-student anymore. That's a bummer."
    "Though I guess I have a bit of a handicap now. Hard to mind your studies when you're starving, cold, and out on the streets. Maslow's hierarchy of needs, or something."
    "And with that, my newly found confidence in myself disappeared in an instant."
    "I wonder how Akari did."

    show Akari u sad p2 at rightoffset with dissolve:
        xflip
        yanchor -.1
    "Glancing over across the desks, I get a look at Akari's face."
    "The color is drained from her face, communicating just about everything I need to know."
    Hiroya "Hey, Akari, you doing alright over there?"
    Akari speaking "Ah-"
    Akari happy "F-fine, fine! How'd you do?"
    Hiroya "Not amazingly. Want me to look over your-"
    Akari frown "Ah, no need! I did fine!"
    show Akari u sad p2 with dissolve
    "Akari pulled her test closer to her chest. Subtlety wasn't her strongest point."
    Hiroya "I can see the red ink bleed through the paper, y'know."
    Akari questioning "R-really?"
    show Akari u angry2 p5 at rightoffset with dissolve
    Akari "Curse you, Hirayama-sensei..."
    Hiroya "That's a lot of red, too. S'like a grisly murder scene happened all over your test scores."
    Akari angry3 "Weeeh, don't remind me!"
    Akari angry1 "She should really use a pencil crayon instead! It's more subtle and elegant!"
    Hiroya "I don't really think that's the issue here, Akari."
    "She pouted, puffing her cheeks out in response."
    Akari u angry1 p6 "It's a conspiracy! Hirayama-sensei gives preferential treatments to the boys!"
    Hiroya "That's a new one."
    Akari "Yeah! She's a lonely thirty-something bachelorette who thinks she can honey up a new boy toy with good grades!"
    Akari angry3 "It's sexism is what it is!"
    Hiroya "What are you even..."
    Hiroya "N-nevermind, you should keep your voice down! She'll hear you!"
    Akari u sad p2 "Nnnnn."
    "With a groan, she slumped against her desk."
    show Akari u frown p2 with dissolve
    Hiroya "You're gonna see her after class, right? She could give you a few pointers on the material."
    Akari "History sucks, why do I have to memorize what a bunch of old dudes said and did?"
    Hiroya "You don't have to memorize every little detail. Just the big picture is fine."
    Akari "She probably thinks I'm dumb. Everyone does."
    Hiroya "Hey, hey, you aren't stupid, Akari."
    "She seems more bummed out than usual. I should say something."

    menu:
        "You need to try harder.":
                Hiroya "If you studied more regularly, the tests wouldn't be as rough."
                Akari "Hmph! What do you know, Hiroya? You didn't even do well."
                Hiroya "Hey, I'm just trying to help."
                Akari "If just studying would work, I wouldn't be doing so bad."
                "Akari looks away, muttering under her breath."
                Akari "I'm tired of people thinking I'm some idiot girl."
                "I didn't quite catch her last comment."
                "Even so, I drop it. It feels like I only managed to discourage her further."

        "Watch more documentaries.":
                Hiroya "You watch any documentaries on this stuff? They do a pretty decent job of boiling down the subject matter."
                Akari speaking "I watch a few movies! Wait, should I have been taking notes watching the old samurai movies?"
                Hiroya "W-well, there's a difference between Hollywood stuff and actual-"
                Akari vhappy p3 "Wow! History was {i}super{/i} violent!"
                "Well, that perked her back up at least."
                Akari "Documentaries, huh? I guess I never really thought of that."
                "Hmm. I didn't expect her to take the suggestion seriously."

        "You can always get help.":
                Hiroya "If you need a hand with the material, I could study with you."
                Akari questioning "Eh? You'd do that for me?"
                Hiroya "Well, yeah. If I have time, but I'm sure I could make time for it."
                Akari happy p3 "Really? I don't wanna slow you down or anything. Mister A-student and all."
                Hiroya "Well, not anymore..."
                Akari "Oh! Right! You've come back down to Earth with the rest of us!"
                Akari vhappy "It's okay, Hiroya! I'll help you restore your honor."
                Hiroya "What? But I was just - you were-"
                show Akari u scheming p1 with dissolve
                "Akari mouths the words 'B minus' with a sly grin."
                Hiroya "Okay. Fair enough."
                "Akari always struggled in her studies. I feel I could be a better friend and help her out more."
                "It's only fair, since she feeds me on a regular basis."

    Hiroya "Anyway, besides that, you shouldn't get so bummed out over a test result. It's just a number."
    Hiroya "If it means anything, I think you can be pretty clever. Remember that book report you had to do for Japanese Literature?"
    show Akari u questioning p1 with dissolve
    Akari "The one where we had to read out loud and stuff?"
    Hiroya "Yeah. You got more into it than anyone else. And the way you delivered those lines was always really fun."
    Hiroya "Compared to that Hirotada kid."
    Akari frown p2 "Oh, yeah, him! He always does this droooning monotone! I couldn't stay awake for it!"
    Akari "And it had to be a morning class too. Yaaaawn."
    Hiroya "Yeah, and the book report you delivered was super intense too."
    Akari happy p1 "Heheh! I got lucky, the teacher let me present on a {i}graphic novel{/i}. Still counts!"
    Hiroya "Yeah. Just need to find things where you can apply yourself."
    Hiroya "Maybe history can be another one of those things. Just need to view it in a different way."
    Akari sad "It's hard. Hirayama-sensei doesn't seem thrilled about lectures."
    Hiroya "She's difficult, yeah."
    Akari "I'll talk to her after class. See if I can do any better."
    Akari happy p1 "Thanks Hiroya! You're a good friend."
    Hiroya "Sure thing. You want me to wait outside?"
    Akari vhappy p3 "Yeah! Lunch is next, so we can sit together!"
    Hiroya "Alright, that's settled then."
    "My eyes glance up towards the clock. Almost time for lunch."
    "Akari and I confirm our plans, before turning back to our desks. I move to pack my things up."
    hide Akari with dissolve
    #sfx bellring
    "By the time the bell rang, I was already on my way towards the door. Akari was ready as well, though she made a beeline towards the teacher's desk."
    play music Suzukitheme fadein 1

    scene hallway 1
    "I lean next to the door, staring ahead through a window overlooking the Sugawara campus."
    "It's a peaceful sight. I can make out a few students tossing a frisbee back and forth. Students gathered into their usual groups for the lunch period."
    "Leaves blow over the pavement in waves. It won't be long before this whole place is covered in white."
    "For the most part, the teachers don't really care what we students do during lunch."
    "I'll usually find a bench somewhere and eat my usual vending machine bread, though the past few days have been a shakeup of that routine."
    "I'd hate to mooch off of Akari again, but it may be necessary."
    show Suzuki u questioning p1 with moveinleft
    Suzuki "Hey, big guy! Yo!"
    "I guess peace has its price."
    Hiroya "Suzuki? What're you doing out here?"
    Suzuki shouting p2 "I was waiting {i}aaaaall{/i} morning to give you a piece'a my mind, okay?"
    Suzuki "So just park your ass right there and let's let it all hang out!"
    Hiroya "I mean, I wasn't going anyway. Waiting for a friend."
    Hiroya "And I didn't really wanna fight you."
    Suzuki questioning p1 "Eh? What's this about a fight? We were just gonna chat, mano-a-mano, yeah?"
    Hiroya "Hey, if this is about that thing that happened yesterday, I'm sorry, I had other plans."
    Suzuki shouting "Damn straight, you're sorry! This is important business!"
    Hiroya "Well you guys {i}did{/i} push it on me at a moment's notice."
    Hiroya "Hopefully you guys at least managed without me. How'd it go anyway, With the whole 'saving the school' angle?"
    Suzuki frown "Nnnng."
    "He looks visibly upset."
    Hiroya "Did something happen?"
    Suzuki shouting "Nothing happened!"
    "Something {i}definitely{/i} happened."
    Suzuki u tough p1 "You don't just stick your nose up when the Student Council President summons you!"
    Suzuki u speaking "In any other circumstance I'd call that ballsy, actually."
    Hiroya "I'm glad that I've earned your admiration and respect."
    Suzuki u shouting p2 "D-don't take my words out of context! I'm still mad!"
    Hiroya "If you gave me notice next time, I could help out with the stuff you and Kaori are up to, but you didn't, soooo..."
    show Suzuki p2 at bounce
    Suzuki "But we have to defend Sugawara's honor! Our cause is {i}noble!{/i}"

    #sudden akari appearance
    show Akari u vhappy p3 onlayer master:
        subpixel True xpos 0.34 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos -0.26
            ease_quad 1.0 xpos 0.3
    show Suzuki u shouting p2 onlayer master:
        subpixel True xpos 0.62 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.5
            ease_quad 1.0 xpos 0.7
    Akari "Yeah! Die with honor! Live forever in glory!"
    Suzuki p1 "Eh? What!?"
    Hiroya "What was that? Were you quoting a samurai movie?"
    Akari u nervous p2 "Mm? I thought that was a thing, so I wanted to join in. Did I read the conversation wrong?"
    Suzuki questioning "Oh, is she your {i}friend{/i} that you {i}ditched{/i} me for, Hiroya??"
    show Akari u angry1 p5 at bounce
    Akari "Eh?"
    Akari angry2 "The friend thief has returned!"
    Hiroya "Eh, you're fine, Akari. We didn't really talk about anything important."
    Akari happy p4 "Oh, okay! Hirayama-sensei recommended some extra reading I could do."
    Hiroya "That's surprisingly helpful of her. Glad she wasn't too rough on you."
    Suzuki shouting "H-hey, don't ignore me!"
    Akari "Yeah, she can be pretty nice one-on-one! Okay, you ready to go?"
    Hiroya "Sure thing. I worked up a bit of an appetite already."
    Akari u frown p4 "Hey wait! Where's your lunch!"
    Hiroya "Nevermind that."
    #hide sprites
    hide Akari with dissolve
    hide Suzuki with dissolve
    "Turning around, we make our way to the stairwell at the end of the hall."
    Suzuki "Is this what it feels like to have a friend taken from you? Bummer, man..."

    scene hallway 2 at xflip with squares

    "We descend to the main foyer, and take a hard right into the main dining area. Students are flowing into the cafeteria in waves."
    Hiroya "We should probably call dibs on our seats before we get food."
    show Akari u sad p4 with dissolve
    Akari "Eh? But if we're too slow, all the chocolate milk will be gone before we get there!"
    Hiroya "They sell chocolate milk everywhere. Isn't there like a corner store across the street anyway?"
    Akari confident "School milk is better!"
    Hiroya "Are you saying that because it comes in cute packaging?"
    Akari nervous "I-it's funny. And they come with jokes on the side."
    Akari vhappy "Liiike... okay! Why do cows have hooves instead of toes?"
    Hiroya "Because they lactose."
    Akari frown "Because they - aww."
    Hiroya "They reprint the same six jokes across all the cartons, Akari. Everyone's memorized them."
    Akari questioning "They're really funny though, right?"
    Hiroya "Suuure."
    hide Akari with dissolve
    "My eyes drift about, scanning the room for an empty pair of seats."

    #cg?
    "My eyes spot a familiar face, sitting alone towards the end of the dining area."
    Hiroya "Hey, Akari? Isn't that Yukiko over there?"
    Akari "Hm? Oh, yeah! I almost forgot she transferred here!"
    Hiroya "Good to know you think about your friends. She's a first year now, right?"
    Akari "Mmhm! We should go sit with her!"
    Hiroya "Sure. It doesn't look like she's made that many friends yet..."
    "Navigating the aisles, we slowly make our way over to where Yukiko's seated."
    "Something's a little off about Yukiko, though. It was harder to tell from the other side of the dining hall, but getting a little closer, I could see the look on her face."
    Hiroya "What's that face she's making?"
    Akari "Mm? What face?"
    Hiroya "She's kind of staring. Intensely."
    "I point in front of her. She's paying close attention to what a group of students are talking about at a nearby table."
    Akari "Oh, that? She must be thinking really hard about something!"
    Hiroya "She looks like she's about to make a move to kidnap the emperor."
    Akari "Eh? She couldn't get away with that, she's just a kid!"
    Hiroya "N-Nevermind."
    "Yukiko's scheming expression aside, Akari and I head over to her."


    show Akari u vhappy p3 onlayer master:
        xflip
        subpixel True xpos 0.65 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 rotate None
        parallel:
            xpos 1.22
            linear 1.0 xpos 0.65
    show Yukiko u curious p2 onlayer master:
        subpixel True xpos 0.35 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            yzoom 1
            easein_cubic 1.0 yzoom 1.0
        parallel:
            xpos -0.14
            easein_cubic 1.0 xpos 0.35
        parallel:
            xzoom 1
            easein_cubic 1.0 xzoom 1.0
        parallel:
            xoffset 0
            easein_cubic 1.0 xoffset 0
    Akari "Heeeyyy! Yukikooo!"

    show Yukiko u smile happy p1 onlayer master:
        xflip
        subpixel True xpos 0.35 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 rotate None
    Yukiko "Mm? Oh, hey guys!"
    Hiroya "Long time no see."
    show Akari u confident p1:
        xflip
    show Yukiko u smile sweet p1:
        xflip
    "We take our seats on opposite sides of her. Yukiko has a thermos nearby, along with a plateful of curried rice. I recognized it from dinner last night."
    "It was quite fragrant. Doubly so when Akari unpacked her own lunch - the same curried rice."
    "I should've thought to ask for a share, but it's not like I have a good way to store it anymore. Damn."
    Akari "How's your first day of school so far, Yukiko?"
    Yukiko smile happy "Ohhh, pretty average. Everyone's being super nice to me because I'm the new kid, soooo I think I'm getting along just fine."
    Akari "Well that's good! Your big sis Akari'll be here if you need help making friends and getting settled in, okay?"
    Yukiko speaking questioning "We aren't sisters, though?"
    Hiroya "Where {i}is{/i} your sister anyway? Izumi?"
    Yukiko frown p2  "Oh, she's staying home again."
    show Akari u nervous p4:
        xflip
        dissolve
    "Yukiko's cheerful face turned morose. A look of mild concern flashed over Akari's face."
    Akari "She didn't come after all? Is she still in her room?"
    Yukiko speaking annoyed p1 "Where else would she be? She just spends all day in there anyway."
    Yukiko "It was me who had to check up on her! She wasn't even sick, she just wants to sleep all the time."
    Yukiko "Pale as a ghost too. She really needs to get some sunlight. Or a boyfriend."
    Akari vhappy p3 "M-maybe she's a vampire! Like, {i}I vanna suck your blaaahd~{/i}"
    Hiroya "If she had a bedsheet over her, she'd probably look more like a ghost."
    Yukiko smile happy p1 "Man, you guys really are dorks, huh?"
    Akari "Oh! I know!"
    Akari "Why don't you join a school club, Yukiko? It's the fastest way to make new friends!"
    Yukiko speaking surprised "Whoa, okay, you're changing gears a little too fast for me, uhhh..."
    Hiroya "It's a good idea, though. If you don't have a lot of friends around the school, finding people with common interests is a good way to start."
    Akari confident "Mmhm! I'm in the Cooking Club! I'm not very good at math, but I can read a recipe pretty good!"
    Hiroya "Pretty well."
    Akari "And when you're good enough, you don't even need a recipe!"
    "Ignored."
    Yukiko suspicious p2 "Mm, I dunno. Thinking about it. None of the clubs have really grabbed my attention yet."
    Yukiko "I didn't really do clubs at my last school either. But it was a small school, so everyone knew each other anyway."
    Hiroya "Sugawara is pretty big, though. You sure you'll get by fine?"
    Yukiko smile confident p1 "Probably! I'm kind of a badass like that! An exceptional case of raw charisma in my family!"
    "Part of me wondered if she got all the charisma in the family. It sounded like Izumi had none of it."
    Yukiko "Hey, you two, pitch me a few clubs. I'll solicit any suggestions!"
    Akari vhappy p4 "Ooh! Okay, okay, join me in the Cooking Club! We can be baking besties!"
    Yukiko speaking serious "You want me to cook?"
    Akari "Yeah! Cooking is awesome!"
    Yukiko "I can read the packaging on a bag of ramen. I think my culinary reservoir is deep enough as it is."
    Akari questioning "Th-that's not real cooking though."
    Yukiko smile confident "Hiroya! Hit me with your best shot!"
    Hiroya "Um, okay, let me think."

    menu:
        "Newspaper Club":
                Yukiko "Hmmm. I could see myself being a journalist."
                Yukiko "Stalking people relentlessly until they spill the beans, getting the dirt on someone's love life, getting paid the big bucks for dirty pictures..."
                Akari nervous "I-it's the school paper, not a tabloid magazine!"
                Yukiko speaking annoyed "It's not like {i}professional journalism{/i} is supposed to be a draw anymore."
                Yukiko questioning "Say, you think they'd let me read the morning announcements? I have a great personality for that!"
                "Yukiko really got fired up over the idea of reaching out to a bigger audience."
        "Anime Club":
                Yukiko speaking questioning "Oh boy. Those things attract the most desperate kinds of people. Aren't those shows for kids?"
                Yukiko "Like, little kids. Babies."
                Hiroya "A lot would beg to differ on that point."
                Yukiko "Well, I'll think about it. Nothing wrong with being passionate about something!"
                Yukiko "Maybe it'll surprise me."
                Hiroya "Yeah, that's a good mentality to have."
        "Art Club":
                Yukiko frown p2 "Like painting and stuff? That's more Izumi's thing."
                "She gets quiet."
                Akari happy "Um, so maybe the Cooking Club, then?"
                Yukiko smile attitude "Don't wanna hear it, Akari!"
                #kinda joking/friendly, not mad at Akari
                "She perked up, so I guess it's fine."
                "Akari's cooking club strategy isn't a bad one though, especially for starving kids like myself."

    Yukiko smile confident p1 "Alright, got some ideas, but let's hear another! C'mon, Hiroya!"
    "Really? She wants more? Okay, uhh..."

    menu:
        "AV Club":
                Yukiko speaking questioning "Mm? Like a roadie?"
                Hiroya "The drama club holds annual shows, I recall. They usually have AV club on hand with tech support."
                Yukiko smile happy "I'd be okay with that! I'm not a great actress, but I always thought the theatre was pretty cool."
                Akari vhappy p3 "You could put on a light show! Or do sound stuff for an idol performance!"
                Yukiko vhappy "Oh, does Sugawara have an idol troupe too? I hear that's been trending up and up!"
                Akari "I think Miyu pitched it to the Student Council President before, but it got vetoed. Miyu told me Kaori wanted to see a talent before giving a vague idea the O.K."
                Hiroya "That's a shame. It'd be a good way to draw attention to the school. And maybe more students would enroll..."
                Yukiko "Saving the school with the power of idols? What a novel idea!"
                "Well, Kaori was right that we need talent before we can go all in on that type of thing."
        "Book Club":
                Yukiko speaking annoyed "Ehhh, maybe. Depends on the books they read."
                Yukiko "If it's a crusty old novel about some high-bred harlot feeling sad about her dead husband, {i}yaaawn{/i}."
                Akari questioning "What kind of stuff do you like, Yukiko?"
                Yukiko smile happy "Oh, I'm super into occult, supernatural stories lately!"
                Yukiko "It's pretty interesting stuff, actually. There are so many different takes on the same myths and legends."
                Hiroya "You don't believe in that stuff, do you?"
                Yukiko "Nah, I just happened to find some of Izumi's books on ghosts and stuff, and I've been reading them ever since."
                Akari vhappy "So you guys {i}do{/i} have something in common."
                show Yukiko pout with dissolve
                "Yukiko shrugs."
                Yukiko "Yeah, I guess."
        "Archery Club":
                Yukiko speaking surprised "Ohhhh no, you don't want me anywhere near a bow and arrow! I'm not about to be held criminally liable for anything!"
                Akari questioning "Eh? What're you talking about?"
                Yukiko "You know they're a {i}weapon{/i} right? You could really hurt someone! I don't want someone's death on my hands..."
                Hiroya "I'm pretty sure they have training bows. Those are harmless."
                Yukiko smile happy "Mm? Ohhh, right, those. Okay, might be fun! I'll think about it!"
                "She changes her tune remarkably fast."

    Yukiko smile happy "Mmkay! Thanks guys! You've given me a lot to think about!"
    Akari happy p3 "Really? I was gonna pitch some sports clubs too."
    Yukiko frown p2 "Ehhh, physical exercise isn't my jam. Plus I hear the baseball team's a dumpster fire, so I don't wanna get anywhere near that."
    Hiroya "Oof, don't say that around Suzuki, he'd throw a fit."
    Yukiko "Who? No, that's not important right now."
    Yukiko smile happy "The real challenge is to pick one out. Hmmm..."
    Yukiko "Aw nuts, so many options! I can't pick just one."
    Hiroya "If you're so conflicted, why don't you just pick one at random?"
    Hiroya "And if you don't like it, well, you can drop it and try another. Seems pretty simple to me!"
    Akari vhappy "Yeah! Except Cooking Club. When you come to Cooking Club, you're a member for life!"
    Yukiko speaking surprised "Huh. Not actually a bad idea."
    Yukiko smile vhappy "I underestimated you, Hiroya! I thought you were the brawn-over-brains type!"
    Hiroya "What? I'm a straight-A student."
    Akari scheming "{i}Was{/i} a straight-A student."
    Hiroya "H-hey, you don't have to bring that up in front of her!"
    Yukiko speaking serious p1 "And you're one to talk, Akari. How many tutors did you go through over the summer?"
    Akari nervous p2 "H-hey! I'm a good learner! I just buckle under pressure."
    "Clearly uncomfortable with the subject, Akari quickly changes topics."
    Akari questioning "Hey, Hiroya, did you bring anything to eat?"
    Hiroya "...No, I, uh, had a big breakfast. Think that's holding me over for now."
    Akari "Well, you should be snacking regularly through the day."
    Hiroya "I mean, I already tried it. I was at your house for dinner last night."
    Hiroya "Besides, it's your lunch, I shouldn't be mooching off you."
    Yukiko smile vhappy p2 "Well! If you're hungry, you can have a few bites of {i}myyy{/i} rice. Just to get you by!"
    "Yukiko slid her dish over to me with an inviting smile."
    Hiroya "You sure?"
    Yukiko "It's cool! You can pay me back later!"
    Hiroya "Alright. Thanks."
    "My cheeks flushed slightly as Yukiko beamed at me with her smile."
    "She seems like a nice girl."
    Akari speaking p1 "Ah, better eat quick, lunch is almost over!"
    Hiroya "Crap, you're right!"
    "I shovel a few more forkfuls into my mouth, the deluge of savory flavours mixing together to massage my palate. It was really quite good, and held up well even as leftovers."
    "Pity I couldn't enjoy it for longer."
    Hiroya "Great. So we're all meeting at the usual place?"
    Akari questioning p2 "I got Cooking Club today! Yukiko, you {i}suuure{/i} you don't wanna check it out?"
    Yukiko speaking questioning p1 "Well, I already said I was going to give all the clubs a fair shake, so..."
    Yukiko smile vhappy "Alright. I'll give it a shot. Where's it usually held?"
    Akari vhappy "Room 220! I'll send you a text after class, okay?"
    Yukiko "Groovy. What'll you be up to Hiroya?"
    Hiroya "Usually I just hang out in the courtyard. Sometimes the student council lets Miyu free early and we hang out then."
    Yukiko confident "Ah, yes. Still using you as a training dummy for her fortune-telling stuff?"
    Hiroya "She's getting better at it!"
    Yukiko vhappy "Enjoy it while you can! Before long she'll be demanding ten thousand yen a session!"
    Akari p1 "Eh!? Really?"
    Yukiko "It's what I always tell her! You gotta ask what you think your services are worth!"
    Hiroya "I thiiink you're looking into it a bit too much. It's just a hobby."
    Yukiko "An under-monetized hobby. It's okay, she'll warm up to it!"
    "After some more good-natured gabbing, we pack up our things and disperse for our afternoon classes."

    scene classroom

    "Students begin to trickle back into the classrooms for afternoon lectures. Next is math class."
    "Akari fumbles through her knapsack. I assume she's trying to find her textbook."
    "The same one that keeps vanishing periodically. And fairly predictably, every other week."
    "With a defeated sigh, I loan her my own. She accepts it graciously."
    "Watching her squirm is incredibly distracting, so I can survive an hour without my textbook. My grades are good enough that Hojo-sensei doesn't particularly object."
    "Glancing around the room, bored and ready for class to start, I see one of my male classmates pace over to a classmate's desk. The girl had beckoned him over."
    "My mouth flattens again. This has been a recurring soap opera that much of the class room has quietly been keeping up with."
    "The recurring saga of Touma and Aoi, two childhood best friends. Their relationship has been a hushed topic of gossip within the rest of the class."
    "Usually I opted to mind my own business, but when there was nothing else on, I listened in on the gossip and drama that filled the air."

    Aoi "Hey, Touma-kun! I got a business proposition for you!"
    Touma "Huh? What's up, do you need a study partner?"
    Aoi "Nah, I think I'm getting the material a bit better! It's way better when you teach me! Hojo-sensei gets a little frustrated with all my questions, y'know?"
    Touma "Heheh, no kidding."
    "It's been a source of speculation as to what their study groups actually entail. Touma-kun has a waiting list of people asking to join."
    "Though at least a few of those on the list just want to be a fly on the wall for whatever happens between those two. Sheesh."
    Aoi "The annual harvest festival's next week, did you hear?"
    Touma "Oh, really? I guess it just slipped my mind."
    Aoi "There's gonna be rides, and food booths, and a haunted house! They're going all out this year!"
    Touma "A haunted house? Those are so tacky though."
    Aoi "Eh, a little. But they're gonna be holding a curry contest too!"
    Aoi "I heard that they're bringing back the Esophagus Exploder! It was so spicy it sent a man to the hospital, like, five years ago!"
    Touma "That's actually pretty metal. Too bad I'm no good with spicy food."
    Aoi "Heheh! Anyway, you free next week? We should {i}totally{/i} go!"
    Touma "Hmm? I think I'm free. Who else is coming?"
    Aoi "Why would I invite anyone else to our date?"
    Touma "Right, that makes sense - wait, a what now?"
    "Touma took a step back, turning red."
    Aoi "Haha! You're cute when you get all flustered like that!"
    "Aoi rested her head in her hand and crossed her legs, smirking as she did and utterly oblivious to the multitude of eyes staring at them."
    Aoi "But no, I'm super serious, we should head over, it'll be fun!"
    Aoi "Please come? After Debate Club on Wednesday, I'm super free to hang out!"
    Touma "J-Just the two of us?"
    Aoi "Mm? Did you have other plans, Touma-kun?"
    Touma "N-no, it's just... you, and me, and we, and..."
    Touma "I-it... it might be fun?"
    Aoi "Ohhh, you're exciiiited! Okay, it's settled, then! I'm gonna look into it a bit more, okay?"
    Touma "A-ah... uh... o-okay!"
    "Touma sputtered a response as Aoi hurried back to her desk, excitedly swiping at her phone. I assume she's still doing research on the festival."
    "Touma's jaw opened and closed by itself as he tried to process exactly what happened. A hushed silence fell over the classroom."
    "He slumps over onto his desk. One could only imagine what he was thinking right now."
    Suzuki "How does a guy like {i}that{/i} seduce a girl like {i}that{/i} without even trying...?"
    Hiroya "Eh?"
    show Suzuki u questioning p1 with dissolve
    "I glance behind me, only to see Suzuki seated at the desk behind mine."
    Hiroya "ACK!"
    "And he was leaning so far forward my head nearly collided with his."
    Hiroya "Suzuki!? What are you doing here? You aren't in this class!"
    Suzuki "Oh, {i}now{/i} you wanna talk to me. Some bro you are..."
    Suzuki "Oh well. I'll find it in my heart to forgive you. This time."
    Hiroya "I'm touched. Seriously though, what's going on? Akari, you seeing this?"
    "Akari glanced over to survey Suzuki."
    $all_moves(camera_check_points={u'rotate': [(-5640, 0, u'linear')]}, layer_check_points={}, subpixel=True, **{})
    show classroom onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.5
            ease 1.0 xpos 0.43
        parallel:
            ypos 1.0
            ease 1.0 ypos 1.22
        parallel:
            zoom 1.0
            ease 1.0 zoom 1.22
    show Akari u frown p1 onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            yzoom 1
            ease 1.0 yzoom 1.0
        parallel:
            xpos 1.18
            ease 1.0 xpos 0.75
        parallel:
            xzoom -1.22
            ease 1.0 xzoom -1.0
        parallel:
            zoom 1
            ease 1.0 zoom 1.22
        parallel:
            ypos 1.0
            ease 1.0 ypos 1.22
    show Suzuki u questioning p1 onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            yzoom 1
            ease 1.0 yzoom 1.0
        parallel:
            xpos 0.5
            ease 1.0 xpos 0.26
        parallel:
            xzoom 1
            ease 1.0 xzoom 1.0
        parallel:
            zoom 1
            ease 1.0 zoom 1.22
        parallel:
            ypos 1.0
            ease 1.0 ypos 1.22
    Akari "I think I saw him come in through the back door. Friend thief guy, right?"
    Suzuki shouting "I'm no thief!"
    Hiroya "If you saw him, you could've given me some kind of advance warning."
    Akari "I'm not your mom."
    Hiroya "Really, what's this guy doing in our class?"
    Suzuki "I-I have a name, you know!"
    Akari "Yeah, yeah. You're Suzuki Kisaragi, Captain Ace Supreme of the Sugawara Baseball Team, right?"
    Suzuki "Oh shit, you {i}do{/i} remember! And the full title! Finally, someone that knows what's up!"
    Suzuki "Hiroya, bro, you're slick, y'know? You know how to pick out the best girls!"
    Hiroya "What in god's name do you mean by that?"
    Akari angry1 p5 "Don't go getting cozy with me just like that! You couldn't steal Hiroya from me, so now you're trying to steal me from him?"
    Akari "Ha! Well it won't be that easy! If you thought joining 2C would make it a cakewalk to separate us, you were wrong! Dead wrong!"
    Hiroya "Wait, wait wait wait, how do you know he's going to join our class? He's got his own."
    Akari "I mean, why else would he come here and sit at a desk? He's here for class, right?"
    Suzuki speaking "Akari catches on quickly. Keep it quiet though, I'm on a secret mission."
    Akari questioning p4 "A secret mission?"
    "I groan audibly in response. Again with this crap. And it looks like Akari might get strung along."
    Hiroya "Secret mission, what the hell."
    Suzuki "Yup. It's of critical importance. Honestly, you two shouldn't know about it, but I guess I can trust you two."
    Akari sad p1 "Hmm, I still suspicious of you, but... go on."
    Hiroya "Akari, don't listen to this idiot."
    Akari questioning "But what if he's really on a secret mission?"
    "I exhale out of my nose so forcefully it feels like I'm physically deflating."
    Suzuki "I can't tell you exactly what I'm here to do, but it's top priority."
    Suzuki "You could even say that the fate of the school rests squarely on my broad shoulders. It's a ton of responsibility."
    Hiroya "Whatever you say, dude."

    "It was then that Hojo-sensei entered through the front doors, and the rest of the students rushed back to their seats."
    "He looked around to make sure everyone was paying attention, then cleared his throat with an air of presumptuous formality."
    Hojo "Ahem. Good afternoon class. It has been brought to my attention that we have a new student in our class."
    Hojo "Suzuki Kisaragi. Come to the front and introduce yourself. Quickly now, I don't have all day."
    show classroom onlayer master:
        subpixel True xpos 0.43 ypos 1.22 xanchor 0.5 yanchor 1.0 zoom 1.22 rotate None
        parallel:
            xpos 0.43
            linear 1.0 xpos 0.5
        parallel:
            ypos 1.22
            linear 1.0 ypos 1.0
        parallel:
            zoom 1.22
            linear 1.0 zoom 1.0
    show Akari u questioning p1 onlayer master:
        subpixel True xpos 0.75 ypos 1.22 xanchor 0.5 yanchor 1.0 xzoom -1.0 zoom 1.22 rotate None
        parallel:
            xpos 0.75
            linear 1.0 xpos 1.17
    show Suzuki u happy p1 onlayer master:
        subpixel True xpos 0.26 ypos 1.22 xanchor 0.5 yanchor 1.0 zoom 1.22 rotate None
        parallel:
            xpos 0.26
            linear 1.0 xpos 0.5
        parallel:
            zoom 1.22
            linear 1.0 zoom 1.0
        parallel:
            ypos 1.22
            linear 1.0 ypos 1.0
    "Flashing me a knowing smirk, Suzuki strutted to the front of the class."
    Suzuki speaking p2 "The name's Suzuki Kisaragi, Captain Ace Supreme of the Sugawara Baseball Team!"
    Suzuki happy "Let's all do our best to kick inertia to the curb, do our best all of the time, and make Sugawara the best damn school it can be!"
    "Suzuki was charismatic and already had a reputation with most of the students in the class."
    "While Hojo gave him a dirty eye over his swearing, Suzuki had earned himself a polite round of applause."
    hide Suzuki with dissolve
    "With a hearty smile and wave, he returned to his seat."
    Hojo "Well, with that out of the way, we can return to our lessons. Today we'll be learning about quadratic parabolas."
    "Our afternoon classes go on relatively normally. Hojo-sensei begins his lecture."
    Hojo "You can see how the graphs curve elegantly across the chart. Perfectly, uniformly. Mm, exquisite."
    Akari "Wow! Hojo-sensei is really into curves!"
    Hiroya "..."

    #timeskip

    scene courtyard with dissolve

    "After a mildly uncomfortable lecture with Hojo-sensei, the bell rang to signal the end of today's classes."
    "Akari had Cooking Club, Suzuki had baseball practice, and Miyu had her student council responsibilities. So I was left to my own devices on most days."
    "Usually I'd just head straight home, but I didn't exactly have a home to return to anymore. Plus, if I left before everyone else, Akari would throw a fit."
    "So here I was, in the courtyard, idly waiting for time to pass."
    Hiroya "I could probably grab a snack from the vending machines. Except I'm broke, so maybe not."
    "I mused aloud to myself, alone on this bench."
    "I need a hobby. Maybe I should join a club after all..."
    #sfx buzz
    "My phone vibrates in my pocket. I got a text message."
    "I take a look at it. It's from Miyu..."
    Hiroya "'Can't make it. This meeting's going late. I'll catch up with you guys tomorrow.'"
    Hiroya "Well, that sucks."
    "With a sigh, I pocket my phone. If Suzuki was any indication, Kaori is probably plotting something."
    "I heard some of the war stories from Miyu, but she's always spoken about her in a respectful tone. Miyu isn't one to raise her voice in general, though."
    "Either way, Miyu isn't joining me, so I guess it's just Akari I'll be waiting for."
    "Leaning back against the bench, I figure now's a good time for a nap. The atmosphere in the courtyard's much preferred to the crummy bridge."


    show black onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            ypos 0.0
            linear 0.5 ypos 1.0
    "I close my eyes, ready for a power nap..."

    #we should do something with izumi stuff during the nap but idk what
    #Mono's got you covered

    Yukiko "Heeey! Hiroyaaa!"
    Hiroya "Ngh... huh?"
    show Yukiko u curious p2 behind black
    show black onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            ypos 1.0
            linear 2.0 ypos 0.0
    "Slowly opening my eyes, I find myself face to face with Yukiko. She was staring at me with her curious wide gaze."
    hide black
    Yukiko "You okay, man? You were stirring in your sleep."

    menu:
        "How long were you watching?":
            Hiroya "It's a little creepy, yanno?"
            Yukiko smile happy "Not long. Got here about five minutes ago. I thought I saw something, but..."
            Yukiko speaking questioning "Well, then I saw you, looking so peaceful..."
            Yukiko smile eyesclosed "...And snoring like a lumberjack. Whew."
            Hiroya "Sh-shut up. How long was I out for?"
            "I glance at my watch. Not much longer than thirty minutes, it looked like."
            Yukiko "Hey, weird question, but did you see anyone else out here before you fell asleep?"
            Hiroya "I wasn't really paying attention, but I think everyone had either gone home or to a club."
            Yukiko "Right, that makes sense."
        "I had a dream.":
            Yukiko speaking questioning "Oh yeah? Anything interesting?"
            Hiroya "Not interesting, just weird."

        "Why'd you wake me up?":
            Hiroya "Did something happen?"
            Yukiko smile happy "No, not really! I was just bored."
            Hiroya "You were {i}bored?{/i}"
            Yukiko eyesclosed "Yeah, I just tried three different clubs, and they were all hot garbage."
            Hiroya "Woah, you hit three clubs in one day?"
            Yukiko speaking serious "Yeah, I can't just sit around all day and do nothing like {i}some{/i} people I know."
            "She gave me a knowing look. That cut deep."

    Yukiko speaking questioning p1 "Why are you napping out here, anyway? Don't you have any clubs to go to?"
    Hiroya "Nah. Never joined a club. Usually I just wait until the girls are done with their stuff."
    Yukiko "Really. Hm, interesting."
    "Yukiko nodded her head."
    Hiroya "Anyway, I'm fine now. How're you? No luck with the clubs?"
    Yukiko pout p1 "Nope. Haven't found a good fit yet."
    Hiroya "Ah well. I'm sure if you keep looking, you'll find a club that fits."
    Yukiko poutyblush "I'm not so sure."
    Hiroya "Come on, don't get discouraged so soon!"
    Yukiko upset "It's not that, it's just that..."
    Yukiko "It's hard, like, I'm not sporty enough for the sports clubs, and I'm not nerdy enough for the nerdy clubs..."
    Hiroya "Did you take up Akari on her offer to check out Cooking Club?"
    Yukiko "Ohhh."
    Hiroya "'Ohhh'?"
    Yukiko speaking serious "The less said about what happened in Cooking Club today, the better."
    Hiroya "Where's Akari, anyway? She's later than usual..."
    Yukiko smile happy "Dunno! I hope she survived!"
    Hiroya "Survived? Survived what?"
    Yukiko eyesclosed p2 "Don't worry about it! Ya know, the initial blast isn't bad!"
    Yukiko speaking serious "It's the fallout you have to worry about."
    Hiroya "You're not easing my concerns, Yukiko!"
    Yukiko smile eyesclosed "Oh, don't be such a baby. She's fine, she texted me and everything."
    Yukiko vhappy p1 "Anyway! No luck going through the existing clubs, but I think I got an even better idea!"
    Yukiko "I think I'll start my own club! Whaddya think?"
    Hiroya "Your own club? Isn't there like, a whole approval process?"
    Yukiko speaking questioning "Yeah, about that. I was reading over my student handbook. Right here, see?"
    "As if ready for this conversation, she held her book aloft, presenting it before me."
    Yukiko "I did some reading up on the whole approval process. Turns out you need to talk to Student Council about it, buuut..."
    Yukiko "They're {i}super{/i} laissez-faire about this stuff. So long as it has 'significant student interest', you got carte blanche to do whatever~"
    Hiroya "Well, you still need, like, approval, right? The president's a tough one to crack."
    Yukiko "Yeaaah, that's the sucky part. You also need a teacher supervisor, so I gotta rub someone's back there."
    Yukiko "But I think I could get away with something! It's all about persuasion."
    "Damn. Yukiko could be quite conniving when she wants to be."
    Hiroya "You sure you wanna start an all-new club? Sounds like a lot of work."
    Yukiko smile vhappy "It'll be great! C'mon, Hiroya, back me up!"
    show Yukiko u smile vhappy p1 onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.5
            linear 1.0 xpos 0.35
        parallel:
            xzoom 1
            linear 1.0 xzoom -1.0
    show Akari u vhappy p3 onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 rotate None
        parallel:
            xpos 1.21
            linear 1.0 xpos 0.65
    Akari "Yeah, Hiroya! You gotta support your friends!"
    Hiroya "Wha- Akari!? When did you get here?"
    Akari "Just now! Sorry it took so long, I was cleaning and sterilizing the kitchen."
    Hiroya "Oh, right, the incident. Uhh, are you okay? Can you walk?"
    Yukiko smile attitude p2 "She's fiiiine. Don't make such a big deal out of it."
    Akari happy p2 "Yeah! I mean, I went cross-eyed for about fifteen minutes, but after that I was hunky-dory!"
    Hiroya "Wait, what."
    Yukiko confident "I'm sure she's fiiiine! Anyway, let's talk about my thing!"
    "Her repeated insistence that Akari is 'fiiiine' is concerning, but I decide that pushing the issue would be a waste of energy."
    Yukiko smile vhappy p1 "Do I have both of you signed on for tentative interest to my amazing club experience?"
    Hiroya "What? No, what are you-"
    Akari vhappy p3 "I'm game! Yukiko has a lot of great ideas!"
    Hiroya "What? You're already in Cooking Club, don't let Yukiko pressure you into joining another!"
    Akari questioning p2 "Huh? But we're friends! I wanna support my friends as much as I can!"
    Yukiko smile confident p2 "Speaking of, Hiroya, you're not involved in any clubs right now, are you?"
    Hiroya "That has nothing to do with anything!"
    Yukiko speaking annoyed "If you {i}really{/i} think about it, doesn't that make you kind of a hypocrite? Pressuring me into joining a club and all."
    Akari confident p3 "Yeah, Yukiko! Low blow!"
    Hiroya "B-but Akari, you were also telling her to join a club!"
    Akari scheming "I'm actually in a club, though."
    Hiroya "Grr... Alright, I'll humor you guys for now. But I'm not making any promises."
    Yukiko smile vhappy p1 "Hooray! We're friends, so we're all in this together now!"
    Yukiko "Though I didn't think of a name yet. Lot of the good ones are already clubs."
    Akari happy p4 "Oh! If we need a club name, I already thought of one!"
    Akari "C'mon, c'mon, Miyu said they're still in a meeting! We can pitch it right now!"
    Yukiko speaking questioning "What? Aren't you going to tell us-"
    Akari p1 "It'll be okay! Miyu will have our backs! But we gotta run for it!"
    hide Akari with easeoutright
    show Yukiko u speaking questioning p1 onlayer master:
        subpixel True xpos 0.35 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 rotate None
        parallel:
            xpos 0.35
            linear 1.0 xpos 0.5
    Hiroya "I doubt they're open to pitches while they're holding a meeting."
    "Akari was already sprinting off towards the school building. Yukiko gave me a quizzical look."
    Yukiko "You have any idea what she's thinking?"
    Hiroya "I don't know if even Akari knows what she's thinking. C'mon, I'll show you where the student council meets."
    "Picking up the pace to a jog, we make our way over with godspeed-"
    Yukiko surprised "Hah, hah... slow dooown... I'm running outta breath..."
    Hiroya "What? Already?"
    Yukiko "I told you, I'm not... sporty enough... I don't like running."
    "-Or as quickly as reasonably feasible."


    #Mono start here
    scene student council
    "When we arrived, the door to the student council room was already open. Akari must've beaten us there."
    show Akari u speaking p4 onlayer master:
        subpixel True xpos 0.65 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 rotate None
        parallel:
            xpos -0.26
            linear 1.0 xpos 0.7
    Akari "If you just give me a second-"
    Kaori "That doesn't excuse the fact that you're-"
    "She sees us at the door."
    show Kaori u shout p1 onlayer master:
        subpixel True xpos 0.35 xzoom -1.0 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos -0.16
            linear 0.25 xpos 0.3
    Kaori "H-HEY! You can't just walk in here, we're having a meeting! This is official student council business!"
    show Kaori u shout p1 onlayer master:
        subpixel True xpos 0.3 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 rotate None
        parallel:
            xpos 0.3
            linear 1.0 xpos 0.25
    show Yukiko u speaking surprised p1 onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            ypos 1.97
            linear 1.0 ypos 1.0
    show Akari u speaking p4 onlayer master:
        subpixel True xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 rotate None
        parallel:
            xpos 0.7
            linear 1.0 xpos 0.75
    Yukiko "But what we're here for {i}is{/i} student council business! That means you have to listen to us!"
    Hiroya "Yukiko, that's Kaori Chiba. You probably shouldn't talk to her like that; she's the president."
    Yukiko pout "Sure I can! This is a free country, I have rights!"
    Hiroya "It's not about rights, it's about being diplomatic and not breaking down the door."
    Akari speaking p1 "The door's fine! I was very careful running in here!"
    Akari confident "A-anyway, we're all here to propose a new school club! Can we have everyone's attention?"
    Kaori "This is patently ridiculous! We were just in the middle of-"
    $all_moves(camera_check_points={u'y': [(799, 0, u'linear')], u'x': [(106, 0, u'linear')]}, layer_check_points={}, subpixel=True, **{})
    show Yukiko u pout p1 onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.5
            linear 1.0 xpos 0.65
    show Kaori u shout p1 onlayer master:
        subpixel True xpos 0.25 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 rotate None
        parallel:
            xpos 0.25
            linear 1.0 xpos 0.35
    show Akari u confident p1 onlayer master:
        subpixel True xpos 0.75 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 rotate None
        parallel:
            xpos 0.75
            linear 1.0 xpos 0.85
    show Miyu u speaking onlayer master behind Kaori:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos -0.23
            linear 1.0 xpos 0.15
    Miyu "Kaori, while I empathize with your frustration, our mandate was to give the student body a voice."
    Kaori "It's not about giving the student body a voice, it's that we're having an important meeting and that there's a policy for making appointments."
    Miyu "I think we should hear them out. It's not like we can't postpone this meeting, and if I may say so, I'm in need of a break."
    Kaori glaring "I guess a break might indeed be in order."
    Kaori "Alright. Five minutes. Five minutes is all I can spare to indulge you. C'mon, let's hear it."
    Yukiko smile vhappy "Thanks Miyu! You're a total badass!"
    Miyu u nervous "I - o-okay."
    show Yukiko u smile vhappy p1 onlayer master:
        subpixel True xpos 0.65 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.65
            linear 1.0 xpos 0.5
    show Akari u confident p1 onlayer master:
        subpixel True xpos 0.85 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 rotate None
        parallel:
            xpos 0.85
            linear 1.0 xpos 0.75
    show Kaori u glaring p1 onlayer master:
        subpixel True xpos 0.35 ypos 1.0 xanchor 0.5 yanchor 1.0 xzoom -1.0 rotate None
        parallel:
            xpos 0.35
            linear 1.0 xpos 0.25
    show Miyu u speaking onlayer master:
        subpixel True xpos 0.15 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.15
            linear 1.0 xpos -0.16
    "Miyu lowered herself back into her seat. All eyes were on Yukiko, Akari, and myself."
    hide Miyu
    Hiroya "So, uh... Akari? You wanted to lead?"
    Akari p3 "Yep! So here's my pitch."
    Akari "I'd like to bring to Sugawara..."
    "Akari pauses for dramatic effect."
    Akari "...the Manga Club!"
    "I had forgotten how open she is with her interests."
    Yukiko speaking questioning "What."
    Kaori shocked "A Manga Club? Why would we need a-"
    Miyu "K-Kaori, let her talk. She - she might be going somewhere with this."
    show Kaori u frustrated p1 with dissolve
    "With a heavy sigh, Kaori folded her arms, patiently waiting to hear the rest. Miyu sure has a way with this girl."
    Akari "Manga is a medium that doesn't get enough recognition. These day, kids sit around watching anime, with no regard for the source material!"
    Hiroya "Not everything is based on a manga."
    Akari vhappy "Silence in the peanut gallery!"
    Kaori speaking "Don't we already have an Anime Club? This sounds like an Anime Club."
    Akari angry2 p5 "You take that back! Anime and manga are completely different forms of storytelling, and to lump them together would be like... like... lumping together panda bears and red pandas!"
    Hiroya "Akari, don't get too worked up."
    Akari angry1 p6 "I'm not worked up, you're worked up!"
    Akari "Students of Sugawara deserve a place to gather and discuss their favorite manga!"
    Miyu "Th-that sounds nice and everything, but-"
    Juichi "But what's the point, exactly? Are you suggesting an expansion upon the Anime Club to include manga?"
    Akari "Did I say Anime and Manga Club? No! I said Manga Club!"
    Akari "Juichi! I know you'd appreciate this. I saw you reading that Magical Girl Nanako during lunch-"
    Juichi "Hey, keep quiet about that! It, um, was a friend's."
    Kaori glaring "..."
    Juichi "Anyway, as Kaori has said, we're in the middle of a meeting."
    Akari "Also! I brought this man, who wants to make a statement on the heated subject of manga!"
    Hiroya "Wha- I didn't agree to anything like-"
    Akari "So, Hiroya! What is your take on the embattled landscape of manga?"
    "Oh no, she's putting me on the spot. What do I say?"
    menu:
        "I support it.":
            Hiroya "I, uh... support the club? I guess manga is pretty cool."
            Hiroya "I've got a few at home, but I mean, who doesn't have at least a couple?"
            Akari angry2 p5 "This is a man who votes on the issues!"
            Akari confident p3 "And he votes well, no less. Good job, Hiroya!"
            Hiroya "Remind me why I hang out with you."
            Akari vhappy "Because you love me."
            Hiroya "Whatever you say."
        "Thank you for your time.":
            Hiroya "Uh... thanks for your time, Kaori. This couldn't have been possible without your, uh, infinite patience."
            show Akari u questioning p1 with dissolve
            Kaori "..."
            Juichi "She's flattered, Hiroya."
            Yukiko speaking surprised "Oh. Hard to tell. She looks filled with seething rage more than anything..."
            Hiroya "Th-the Manga Club would not be possible without the hard work of the student council."
            Hiroya "...Uh, give yourselves a hand? Guys?"
            "After a cautious pause, polite applause filled the room."
            "Kaori was the only one not clapping."
        "Make a campaign promise.":
            Hiroya "If the Manga Club is funded, we promise to, uh..."
            Hiroya "...to realize society's dream of genetically engineered catgirls."
            show Akari u questioning p1 with dissolve
            Yukiko pout "Well, someone's not great under pressure."
            Hiroya "I don't see you helping out!"
            Miyu "W-we don't have the budget for genetic engineering! We don't have a genetic engineering lab either!"
            Juichi "You guys wouldn't want to engineer slime girls instead...?"
            "The room went silent in response, and all eyes were on Juichi. He tried to retreat further back into his seat."
            Juichi "...Chihiro, could you, uh, strike that from the record?"
            #sfx keyboard typing
            "A bespectacled girl off to the side clacked away at her keyboard in response to his request. Hoo boy."

    Kaori cool "Tch. This is {i}ridiculous{/i}, I'm not approving this-"
    Yukiko speaking serious "You can't do that!"
    "With a forceful slam, Yukiko spread the student handbook across the table, its impact echoing in the cramped room."
    Kaori shout "What!? What are you even-"
    Yukiko "Chapter 15, Article 11.4, Line 4."
    Yukiko "If a club has demonstrably sufficient student interest and has adhered to the application process, it is the student council's duty to authorize it as an official club with access to school funding."
    Yukiko "It's in the rules! You can't just say no just because you don't like the idea! Because that's called fascism!"
    Juichi "She's exaggerating a bit, but the documentation is fairly clear on the matter."
    Kaori concerned "Ugh, Juichi, you cockroach, don't take {i}their{/i} side. Miyu, you agree this is insanity, right?"
    Miyu "I-I don't have an opinion, I just work here..."
    Kaori "Ugh."
    "Kaori glanced at Yukiko with a look of annoyance, before lowering her head. She looked defeated."
    Kaori embarrassed "...And do you have your forms and your signatures?"
    Yukiko speaking surprised "...Aaaah, still working on that."
    Kaori frustrated "...Of course you don't. Joy."
    Kaori cool "I don't have time for this. Miyu! You have their form?"
    Miyu "R-right here!"
    "Miyu slid a blank form over, smiling triumphantly as she did."
    Kaori "Fill this out, get your eight stupid signatures, and we'll..."
    Kaori embarrassed "...I'll sign off on your stupid comic club-thing."
    Akari vhappy "Yaaay! Thank you, Kaori! You're the best president ever!"
    Kaori "W-Well, I try."
    Kaori happy "I mean, yes, of course. The best there ever was. Now buzz off, we have important matters to discuss."
    "The three of us nodded and gave an appreciative bow before ducking back out into the hallway."
    hide Kaori with dissolve
    hide Akari with dissolve
    hide Yukiko with dissolve
    Kaori "And close the door behind them!"
    #sfx door slam
    Kaori "..."
    Kaori "Alright, let's review our plan of attack against Sakura no Ki."
    Miyu "Kaori... you {i}really{/i} have to let this go..."

    scene hallway 1 empty with dissolve

    show Yukiko u smile vhappy p1 at rightoffset with dissolve
    Yukiko "Holy crap guys, we did it!"
    show Akari u vhappy p1 at leftoffset with dissolve
    Akari "Yukiko, you were amazing! The way you stared her down with the rulebook! It was chilling!"
    Yukiko "Not as good as your impassioned speech! Thanks to you, we reached their hearts AND their minds!"
    Akari "Omigosh, you really think so? Really?"
    Yukiko speaking questioning "Well, probably not... they looked confused more than anything, I was just trying to be supportive."
    Akari questioning "Oh, well, huh."
    Akari happy "Well it was really fun! I'm glad you guys are supporting me too!"
    Hiroya "Man, Akari, you can bounce back from anything."
    Yukiko smile confident "Alright, alright, c'mon, signatures, signatures! Let's get the ball rolling!"
    "Taking out a pen from her pocket, she brings us all together to scribble down our names."
    Yukiko "That's three down! We need five more, right?"
    Hiroya "Might be a challenge. Dunno what kind of people would openly join the Manga Club when the Anime Club already has such a bad rep."
    Akari happy "Let's ask Miyu when she's out of her meeting!"
    Hiroya "You sure? We've put her under enough pressure already."
    Yukiko "She's a total pushover, I'm sure it'll be fiiine."
    Akari "What about your sister?"
    Hiroya "Can she sign if she's never come to school?"
    Yukiko "Izumi is technically a student at Sugawara."
    Akari "Oh, really? I hope she gets well soon, it'd be nice if she hung out with us."
    Yukiko "I'll take this form home with me tonight, see if I can get her to do something. For once."
    Akari "W-Well, if she does, we're over halfway there right?"
    Hiroya "Things are looking up. You guys wanna head back now?"
    Yukiko vhappy "Yeah. If you spend too much time at school people start calling you a nerd. I don't need that to be what people think of when they think 'transfer student.'"
    Akari confident "Too bad Miyu can't come with us... but I guess we'll see her tomorrow!"
    Hiroya "Alright, let's go."
    hide Akari with dissolve
    hide Yukiko with dissolve
    "We agreed to meet up in the courtyard again after gathering our stuff at our lockers."

    scene street day with dissolve

    "Before long, we were back on the streets. Yukiko's eyes were drifting from side to side."
    "Vendors, eateries, and retail outlets flanked the street on both sides. She had a hungry look in her eye."
    show Yukiko u speaking questioning p1 at rightoffset with dissolve
    Yukiko "Man, I haven't been out here before. There're sooo many people out here! A lot of them seem to be heading to Drifter's Grill."
    Hiroya "It gets busy at this time of day. I have heard some good stuff about Drifter's Grill, though."
    Yukiko smile vhappy "We should get a bite to eat right now! I could go for a steak."
    show Akari u speaking p2 at leftoffset with dissolve
    Akari "Yukiko, we have leftovers. And they're still good!"
    Yukiko upset "But steaaak..."
    Hiroya "I'm voting for the rice. Steak is expensive."
    Yukiko pout "Aw, okay. I guess I'm outnumbered."
    Hiroya "So you guys are gonna mooch some signatures off friends and family?"
    Akari vhappy p1 "Yep, that's the plan."
    Yukiko speaking questioning "We've got Miyu and maybe Izumi, but beyond that, it'll take some convincing."
    Yukiko smile happy "Well, I suppose we can deal with that tomorrow."
    Yukiko "Anyway, Hiroya, thanks for your help. Are you coming to Akari's too?"
    Akari "We got huge heapings of curry rice leftover! We gotta finish it off!"
    Hiroya "Actually, uh..."
    "I have to check up on my camp under the bridge, but I can't let the girls know. Gotta think of something quick."
    Hiroya "It's getting a little late, and I have a thing with the folks. Sorry, I can't stay for food."
    Akari questioning p2 "Huh. You never turn down food."
    Akari nervous "Is it that bad?"
    Hiroya "Huh? N-no, I just have something to do, that's all."
    "I try to cover up my reaction to Akari's piercing question. She looks back with a look of mild concern, before Yukiko intervenes."
    Yukiko vhappy "Hey, the big guy has places to be. We'll see him tomorrow, alright?"
    Yukiko "And by then we'll have this thing aaaaall filled out! It'll be a hella cool surprise!"
    Akari happy "Yeah, you're right. See you around, Hiroya!"
    Hiroya "Later."
    hide Akari with dissolve
    hide Yukiko with dissolve
    "The other two turned a corner and split off from me."
    Hiroya "I'm sorry, Akari."
    "Muttering to myself, I keep going the way I was going. Going the scenic route was the best way to get to the bridge, and to throw them off my scent in the process."

    scene bridge below day with dissolve
    "Before too long, I made it to the bridge. I hid most of my stuff in the bushes apart from the concrete."
    "To my great relief, they were still there. Lucky, too. I often hear of shady folk passing through here, and they'd be easy pickings for someone desperate."
    "...This is far from an ideal living situation, but without income I'm stuck with it."
    "I rise up to my feet, quickly shuffling back over to the main roads. I don't want to arouse suspicion while it's still bright out."

    scene street day with dissolve
    "I try and keep my rounds around town casual. Don't want to expend too much energy."
    "I don't know how much longer I can keep up this charade. Someone's eventually going to notice me sleeping under the bridge."
    "And if they don't catch that, well... I might get caught showering at school. Need to figure out something for that."
    "They have bathhouses, but those are mostly for old people and families. If they saw some kid in a Sugawara uniform mulling about, it'd raise questions."
    "That doesn't account for issues like getting food. I really don't want to start picking out of the trash; I don't care how good that steak is."
    "I could try farming along the bridge, but that'd probably raise more suspicion. Scratch that."
    "I just don't want the girls to find out. If they found out, they'd call me ridiculous for what I did. For running out on my old man."
    "Well, I'm basically an adult now. I can handle this. I've handled it well enough so far. Just need to figure out a plan."
    "A realistic plan. One without scavenging for leftovers and garbage."
    "I can risk the bathhouses though. Bathhouses are honestly pretty alright."
    "I make my paces around the block, stopping here and there to get a feel for my surroundings. Making a mental list of the resources available to me."

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
    show bridge sidewalk night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            ypos 1.0
            linear 1.0 ypos 2.0
    show sky night onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            ypos 0.0
            linear 1.0 ypos 1.0
    "By the time I realized that she had rammed into me, I was already falling over the guardrails."
    "My body flipped from the impact, and all I could make out was my own reflection, rapidly travelling towards me, illuminated by the moon above."
    "It was getting close. I knew then that I was going to land in the river."
    "I close my eyes, bracing for impact."
    "So this is how I'm going to die..."
    #sfx splash
    #prolly open the next scene with him screaming idk
    return
