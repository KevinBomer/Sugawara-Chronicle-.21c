#Fixed some syntax errors that kept the file from being able to be launched in game.
#Redid ALL of the conversation syntax for expression changes.
#Commented outbackgrounds that didn't exist and just put plain black background.
#Fixed the broken Boolean code.
#ch3night wasn't declared. So I declared the label where I believe it starts.
#Did my best with the poses for the last like 200 lines, because there were none.
#WOLF: Check  ..., ?, ?, !?, !?, !??, !?, .~, ...~, ~, ?~

#this needs to be put in the init for the boolean in this chapter to work properly. I don't know why but it won't work if it isn't declared beforehand.
init:
    $ fan = False

label Chapter3Kaori:

    $ renpy.pause(1, hard=True)
    scene chapter_screen_1 with dissolve
    $ renpy.pause(1, hard=True)
    show text "{size=36}Chapter 3: Licking Our Wounds" at chaptertitlespot with moveinleft
    $ renpy.pause(2, hard=True)

    scene street day with dissolve
    "Defeated, and with their heads hung low, our troops spilled out into the streets."
    "Yet there was a curious murmuring among their ranks. Several of them were casting glances towards Kaori."
    "A sullen look was on her face. I catch up to her to catch up with her."
    show Kaori u frustrated p1 with dissolve
    Hiroya "Hell of a game, wasn't it?"
    Kaori "...I guess."
    Hiroya "You don't look happy."
    Hiroya "Well, I mean, losing sucks in general, but..."
    Kaori "No kidding."
    hide Kaori with dissolve
    "Lost for words, I glance ahead."
    "It occurs to me that we all missed the right turn that'd take us back to Sugawara."
    "I glance back to Kaori, confused."
    show Kaori u frustrated p1 with dissolve:
        align (0.4, 1.0)
    Hiroya "Hey, Kaori, we're going the right way, right?"
    Kaori "Yup."
    Hiroya "But the school's back in that direction, right?"
    Kaori "Yup"
    Hiroya "Huh."
    Hiroya "So why aren't we going back to school?"
    show Suzuki bb frown p2 with easeinright:
        align (0.8, 1.0)
    Suzuki "Kaori said that she'd pay for lunch for the whole baseball team after the game."
    Hiroya "The {i}whole{/i} team?"
    Suzuki "It was the only way to convince everyone to come out for an exhibition."
    Hiroya "Isn't that a little exorbitant?"
    Kaori u shout p1 "It'd be fine if your boys actually came out to play! That was {i}embarrassing!{/i}"
    Suzuki bb shouting p1 "H-hey, I ain't pleased about this neither!"
    Kaori shout "What was all that hot air about going 16-0!? That was last year!"
    Kaori "I expect better! Sugawara expects better!"
    Suzuki bb shouting p2 "Why are you takin' the piss out of me!? You can't honestly be blaming me!"
    Kaori "You're the captain, right? Act like it!"
    "They were getting into a full-on shouting match in the middle of the streets."
    "Bystanders were staring at us with concern. And so were several of the players."
    "Should I get involved...?"
    menu:
        "Break it up":
            "This is ridiculous. I'm gonna give them a piece of my mind."
            Hiroya "Hey! Knock it off you two!"
            show Kaori u shout p1 with dissolve
            show Suzuki bb frown p2 with dissolve
            Hiroya "Losing sucks, but you guys are friends, right?"
            Hiroya "Bickering won't solve anything, so let's just take it down a notch."
            Hiroya "We can figure out what we can do better next time."
            Kaori u cool p1 "Tch."
            Suzuki "You got some nerve talking to me like that, buddy..."
            Suzuki bb happy p1 "...I like it! You got chutzpah~"
            Hiroya "What?"
            Kaori "Whatever. We'll talk more at the restaurant."
            Kaori "...Sorry."
            "Kaori didn't seem happy about being talked down to, but she had been pacified for now. Thank goodness."
            jump arriveToEat
        "Let it play out":
            "I'm still a bit too new to this group, and I get the impression they argue a lot."
            "So I remain on standby. Maybe they can sort it out themselves."
            Kaori "And what's with the spitting into your glove thing!?"
            Suzuki "What spitting thing!? Is that {i}really{/i} something to object over?"
            Kaori "It's unsanitary! We're supposed to represent Sugawara, and it's such a vulgar display."
            Suzuki "It-it's tradition! Everyone does it! The guys from Endo were doing it!"
            Kaori "Then maybe, MAYBE, we should be better than that!"
            show Suzuki bb speaking p1 with dissolve
            Suzuki "Man, you have no idea what you're talking about, do you?"
            Suzuki "I bet you think you'd do an even better job if you were captain instead."
            show Kaori u frustrated p2 with dissolve
            Kaori "Not gonna lie, after that sorry performance I flirted with the thought."
            Suzuki frown "Ohhhh, that's cold."
            Suzuki confident "Well if you really feel that way, I might as well check out your pitching."
            Kaori u shout p1 "That was a joke, you dunce."
            "They had a weird way of talking to each other. Like some perverse ritual of one-upping each other."
            jump arriveToEat

label arriveToEat:
    scene cafe outside with dissolve
    "Our group wandered the streets, arriving in a commercial district. Vendors, eateries, and retail outlets flanked the street on both sides."
    "Suzuki and Kaori were focused on a particular restaurant. It looked like a family eatery, with that vintage look to it that you see in generational operations."
    "A little beat-up and plain-looking, compared to the franchised brands that peppered this stretch of road, but charming in its distinct imperfections."

    scene cafe inside with dissolve
    #sfx: door opening bell
    "We enter through the front, our entrance signalled by the jingle of a bell."
    #revise the crap out of this desc based on the BG
    "The interior looked even more dated than the storefront. Some of the wooden tables looked like they'd been there for decades, and had the marks to show it."
    "Real oak, too. Nice."
    "A young lady was manning the front. She'd been leaning idly, playing with her hair, but she stood up straight when she saw our enormous group."
    "I had a tinge of regret. I felt for these poor wait staff, I really did. It looks like the place wasn't serving that many people."
    "And now it was gonna get real busy in a hurry, with a throng of excitable student athletes."
    "You should always call ahead and get a reservation with a group this large."
    show Suzuki bb tough p1 with easeinleft:
        align (0.4, 1.0)
    Suzuki "Well, I'll just check us in real quick."
    Hiroya "Hey Suzuki, you think if we cut into any of these tables, you could guess their age based on the rings?"
    Suzuki bb speaking p1 "Haha, laugh it up. Don't try it, though, seriously."
    Suzuki frown "Jeez, who's working today."
    "He stepped up to the check-in counter to hail the young lady working the front."
    #i don't think we have yukiko waitress outfits yet so revise later
    show Yukiko c curious with dissolve:
        align (0.7, 1.0)
    show Suzuki bb vhappy p2
    Suzuki "Hey Yukiko! How long ago'd you get here?"
    Yukiko pout "Aaaahh, I just got in and the rush is already coming in full force! Woe is meee..."
    show Yukiko c curious with dissolve
    "Her eyes widened as her eyes drifted over the few dozen boys we just brought in."
    Yukiko speaking questioning "Who're all your friends?"
    Suzuki "We got the whole Sugawara baseball team here, can you hook us up with some tables?"
    Yukiko smile sweet "Weeeell, we could push a bunch of them together. How's that sound?"
    Yukiko "It'd be a tight squeeze, but I couldn't really turn away the boss's son~"
    Yukiko smile confident "But you'll have to give me a proper tryout for the baseball team, okidoke?"
    Suzuki bb frown p2 "We'll, uh, talk about that later."
    Suzuki bb vhappy p2 "I'll give you a hand moving stuff around. Oh, and put everything on {i}her{/i} bill~"

    scene cafe inside with dissolve
    show Kaori u cool p1
    "Suzuki gestured to Kaori, who didn't seem all that happy with this arrangement."
    Kaori "Nrgh... y-yeah, what he said."
    Kaori shout "If any of you jackoffs order the steak dinner, I will {i}end{/i} you. Is that clear?"
    hide Kaori with dissolve
    "Suzuki and Yukiko worked together to move around several of the tables for the jocks."
    "Kaori, meanwhile, was content in retreating into a nearby booth."
    "Unsure how to get involved with the tables, I slide in across from her."
    show Kaori u cool p1 with dissolve
    Hiroya "Hey, uh, are you really okay with paying for everyone's meals?"
    Kaori speaking "It's not a matter of being {i}okay{/i} with it. It's an obligation, a verbal contract."
    Kaori "It'd be shitty of me to back out now, right?"
    show Kaori u glaring p1 with dissolve
    Hiroya "Well, maybe, but that's still like twenty guys here. That seems, well, excessive?"
    Kaori u speaking p1 "Don't worry about it. My family's pretty well-off, so it's not like we'll starve at home."
    Hiroya "Really? How loaded do you have to be?"
    Kaori u speaking p2 "You know you can't just up and ask a girl these sorts of things, right?"
    Kaori u glaring p1"Or, well, anyone for that matter."
    Hiroya "I didn't mean it like that! It just came as a surprise."
    "She gave me this dull look of utter disdain. Like I had just uttered something incomprehensibly stupid."
    Kaori u frustrated p2 "{i}Siiiigh...{/i}"
    show Kaori u frustrated p1 with dissolve
    "She leaned back into her seat."
    Hiroya "What? Did I say something weird?"
    Kaori u cool p1 "No, no. well, kinda, but not really. Not your fault, anyway."
    "Well that sure is a mixed response."
    Kaori speaking "The Chiba Clan's influence spread pretty far, so I was just surprised someone like you hadn't realized."
    Kaori u speaking p1 "I don't wanna brag or anything, but insofar as political matters extend, we're a preeetty big deal."
    show Kaori u cool p1 with dissolve
    Hiroya "Huh. Interesting. What're they involved in?"
    Kaori "Eh, mostly construction and development deals. You need real estate to drive the economic sectors."
    Kaori "Plus the Dynasty Bridge, the spitting icon of this city."
    Kaori u happy p2 "It's no exaggeration to say that, without the Chiba Clan, our fair city wouldn't exist. Not like it does now, at least."
    "Kaori puffed out her chest, swelling with pride."
    Hiroya "Huh, wow. I never heard of them."
    show Kaori u cool p1 with dissolve
    "And then she deflated in short order."
    Kaori "Of course not. There {i}is{/i} such a thing as being too honest, Hiroya."
    Hiroya "N-no, don't get me wrong, this is interesting stuff, I think?"
    Kaori u frustrated p2 "Well, only an excellent family could produce an excellent student council president such as myself. You should be grateful, honestly."
    Hiroya "G-grateful for what? You guys basically abducted me!"
    Kaori u wink p1 "It's a privilege to be an assistant for me. You could put it on your resume~"
    show Kaori u wink p2 with dissolve
    Hiroya "I'll think about it?"
    "It was definitely odd to hold a conversation like this. I really don't have a read on Kaori."
    show Yukiko c smile eyesclosed onlayer master:
        subpixel True xpos 0.15 ypos 1.0 xanchor 0.2 yanchor 1.0 rotate None
        parallel:
            xpos 1.15
            easein_quart 1.0 xpos 0.15
    "Before we could continue further, the girl from the front approached our table with a wholly food-serviceable smile."
    Yukiko c smile vhappy "Hey guys, welcome to Drifter's Grill! I'm Yukiko, and I'll be your server today~"
    Yukiko "How're you guys finding things? Did you figure out what you'd like?"
    show Yukiko c smile eyesclosed with dissolve
    "Wasn't she whinier when she was talking to Suzuki? It was odd to see this change in behaviour, but I don't think much of it."
    Kaori "I'll just get the grilled chicken salad, with a ginger ale on the side."
    Kaori u speaking p2 "And I think Hiroya's ready to order too. We don't wanna waste your time."
    "Kaori glanced to me with a knowing expression."
    "I hadn't even looked at the menu! What'd I do to deserve this!?"
    jump ordering

label ordering:
    "Gotta think quick..."
    menu:
        "Order what she's having.":
            $ lunch = "salad"
            Hiroya "I'll have what she's having. It sounds good."
            show Yukiko c vhappy with dissolve
            Yukiko "Alright, two chicken salads! You guys sit tight, okay?"
            jump ordered
        "Get some payback, go big.":
            $ lunch = "steak"
            "This is ridiculous. If she thinks she can tease me like this, she has another thing coming."
            "I remember she's the one footing the bill for everyone here."
            Hiroya "Do you guys serve lobster at all?"
            show Kaori u shout p1 with dissolve
            "Kaori instantly shot me a look of pure, utter hatred. I could feel her aura."
            "If a butterfly flew between us, it'd probably get evaporated. But I perservered!"
            Yukiko smile attitude "W-well, nothing that fancy."
            Hiroya "Ah, well. I'll just get the AAA sirloin."
            Yukiko c smile vhappy "Excellent! One chicken salad and one steak coming up!"
            jump ordered
        "Pick something at random.":
            $ lunch = "liver"
            "I open the menu feverishly to a random page and point at something."
            "Squinting, I point at something."
            Hiroya "I'll have the, uh... chopped liver, and potatos."
            show Yukiko c curious with dissolve
            show Kaori u wink p2 with dissolve
            "They both look at me like I had stripped down to my underpants."
            Yukiko "That's, um, the senior's menu."
            "I understood implicitly that this is one of Kaori's tests, so I continued my bluff."
            Hiroya "Y-yeah, it's good eating. Rich in vitamins."
            Kaori u happy p2 "Well, he {i}is{/i} a big, growing boy."
            Yukiko c smile vhappy "...Okay! A chicken salad and... liver. I'll get your drinks!"
            jump ordered
        "Ask for more time.":
            "Are you kidding? It's {i}free food{/i}! I can't afford to be picky right now!"
            "They're staring at me expectantly. I can't disappoint them! I gotta be a man!"
            jump ordering

label ordered:
    hide Yukiko with easeoutright
    "Yukiko hurried away with our orders."
    Kaori u wink p2 "Good reaction time. At least you can think on your feet."
    if lunch == "steak":
        Kaori u wink p2 "I'll overlook your insubordination. This time."
    if lunch == "liver":
        Kaori u happy p1 "The liver, though? Really?"
    if lunch == "salad":
        Kaori "Bit of a boring choice, though..."
    Hiroya "What was I supposed to do? You just put me on the spot like that!"
    Kaori u speaking p1 "Well, I wasn't planning on wasting a lot of time here anyway."
    Kaori "We need to figure out our next move against Princess Shizuka."
    show Kaori u cool p1 with dissolve
    Hiroya "What? Why?"
    Kaori shout "Why? Should we just buckle at the first sign of adversity!?"
    Hiroya "Well, no, but-"
    Kaori "Of course not! We should tighten our belts and throw ourselves back in!"
    Hiroya "'Tighten our...' n-no, I mean, that's not what I meant-"
    if Shizuka >= 1:
        Hiroya "She didn't seem that bad to me. She was actually kind of... friendly?"
        Kaori u concerned p2 "Don't tell me she managed to seduce you too. You two weren't even together that long!"
        Hiroya "She didn't seduce me! It was just a small chat."
        Kaori u glaring p1 "Weren't you supposed to get intel anyway? I mean, I'm sure Suzuki didn't give Shizuka enough credit, but..."
        Hiroya "I can make friends with other people."
        Kaori u shout p1 "The fate of the school is in our hands! You should take your responsibilities a bit more seriously!"
        Hiroya "Oh, yes, an exhibition baseball game is {i}very{/i} serious. My mistake, I'll redouble my efforts."
        Kaori u frustrated p1 "That's the spirit."
        "I answer back with scathing sarcasm, but it didn't seem to register with Kaori."
    else:
        Hiroya "They beat the team pretty handily at baseball. You know what they say about trying the same thing and respecting different results?"
        Kaori u speaking p1 "Oh, that's a cliché and you know it. Due diligence can move continents."
        Hiroya "I... okay."
        "Taking a deep breath, I allow Kaori to speak her mind. She seemed determined, if nothing else."
    Kaori u wink p2 "We need a new strategy. I figure you'd be a better tactician than Suzuki."
    Hiroya "Since when was I a tactician in all this!? All I wanted was a roast meat sandwich!"
    Kaori u speaking p1 "The pact is sealed, young Hiroya. A sandwich is a binding contract."
    Hiroya "No it isn't!"
    #sfx door jingle
    scene black with dissolve
    show Kaori u cool p1 with dissolve
    "As our ridiculous conversation hit a crescendo, the front door of the restaurant jingled forebodingly."
    "The jovial atmosphere of the restaurant quieted to a hush. It was eerie."
    "Everyone turned their heads to see the mysterious newcomer."
    "Greatly confused myself, I turn around to get a better look."
    show Kaori u shout p1 with dissolve
    "Oh shit, I recognize her. And she's coming right over to our table!"

    scene cafe inside with dissolve
    show Kaori u shout p2 with easeinleft:
        align (0.1, 1.0)
    Shizuka "Hello, Kaori?"
    Kaori u shout p1 "{b}Ack!{/b} What the-!?"
    Kaori speaking "What are you doing here! You can't just invade Sugawara's war room!"
    Shizuka questioning "I might have misheard you, this is a 'war room'?"
    Hiroya "Kaori's thinking of the next way Sugawara can succeed over your school."
    Shizuka u mad  "Oh, I see. She can be pretty resourceful."
    Kaori "What's that face you're making? This is serious!"
    Shizuka speaking "I didn't want to distract you or anything."
    Shizuka "I only wanted to come by and give my regards. It was a good game."
    Shizuka happy "A good exercise between our two schools."
    Kaori u shout p2 "'A good exercise!?' Maybe for stroking your inflated ego, maybe!"
    show Shizuka u mad 1 with dissolve
    "Shizuka visibly grimaced at Kaori's objection. It was only for a second, but she looked hurt."
    Shizuka neutral "Still, she recovered quickly. Remarkably so."
    Show Shizuka speaking "I see you guys are busy, so that's all I had to say."
    Shizuka u happy "It was nice to see you again too, Hiroya."
    Hiroya "I uh, yeah, definitely."
    hide Shizuka with easeoutleft
    "With a polite bow, she excused herself. Kaori glared at me in response."
    Kaori "What are you doing, fraternizing with the {i}enemy{/i}?"
    Hiroya "It's like I said! She was only trying to be polite."
    "I turn around in my seat to see Shizuka exiting through the front door again. She disapears out of sight."
    "Turning back to Kaori, I heave a sigh. Kaori's being a real piece of work."
    Hiroya "I don't know why you have to be a jerk to her."
    Kaori u frustrated p1 "..."
    "Kaori's hard expression had softened after Shizuka departed. She looked to be in deep thought."
    Hiroya "She was asking about you at the ball game too. Did you guys-"
    Kaori "Go bug Suzuki for a while."
    Hiroya "Huh? But what about our war council?"
    Kaori "I need to think on my own. Go. {i}Now{/i}."
    Hiroya "..."
    jump ch3Suzuki

label ch3Suzuki:

    scene cafe inside with dissolve
    "Heaving a sigh, I raise myself from the table to give Kaori time to herself."
    "Trudging over, I head over to the busiest table. The jocks seemed to be having an impromptu arm-wrestling tournament."
    "I can't quite make out what it's about between their hollering. I assume it's some form of peacocking."
    "Some of them shoot me a challenging glance, but I shrink back. I didn't wanna get involved in that."
    "Oddly, I didn't see Suzuki over there."
    Hiroya "Maybe he's somewhere else?"
    "I glance around the crowded diner looking for him."
    show Suzuki bb tough p1 with dissolve
    "He's found a table in the far corner, left to his own devices."
    "He was alone. That was odd."
    "I pull up a seat across from him."
    Hiroya "Hey Suzuki."
    Suzuki speaking "Oh, hey."
    Hiroya "You okay, man? You kinda look like a brooding loner sort over here."
    Suzuki bb tough p1 "Huh? No, just..."
    Suzuki bb vhappy p2 "Just chilling out by myself. Moving the tables by myself took a lot outta me, y'know?"
    Hiroya "Wasn't Yukiko helping you with that?"
    Suzuki bb speaking p1 "Rearranging heavy objects is the domain of the man. I had it covered on my own."
    "He wasn't a very convincing liar. I casually glance behind me."
    Hiroya "I'd just assume you'd be hanging with the boys."
    Suzuki speaking "They aren't going anywhere. I just needed a bit to reflect."
    Hiroya "'Reflect'? Now {i}that{/i} doesn't sound at all like you."
    Suzuki bb shouting p1 "What!? Am I just some kinda meathead to you, Hiroya!?"
    Hiroya "No! Well, maybe. There {i}is{/i} a ton of meat in your sandwiches."
    Suzuki bb vhappy p1 "Guilty as charged!"
    Suzuki happy "Nah, I'm not actually depressed or anything. Don't get the wrong idea."
    Suzuki speaking "Well, no, I'm annoyed we lost, but hey, you win some, you lose some. It's not like we lost the pennant or something."
    Hiroya "You got pretty steamed at those guys from Endo, though."
    Suzuki bb tough p1 "They stepped to me and my boys, okay? They can't just assume they're hot shit after one game goes their way."
    "He had a point. I lean back in my chair with an understanding nod."
    "Silence falls between us as Suzuki goes back to his contemplatie state."
    "I should ask him about something."
    menu:
        "What's with Kaori?":
            Hiroya "Kaori seems pretty upset about the whole thing."
            Suzuki bb speaking p1 "Get used to it. She made Endo her own personal crusade. It ain't pretty."
            Suzuki happy "Kaori's tough, though. She'll take a lickin' and keep on tickin'!"
            Suzuki bb tough p1 "I hope she didn't send you to lecture me."
            Hiroya "N-no, nothing like that. She just needed time to think."
            Suzuki speaking "Hm. I guess that means we're all going back to war tomorrow."
            Hiroya "War? I can't be conscripted over a meat sandwich!"
            Suzuki bb speaking p1 "You'd be surprised. Maybe I can teach you how to swing a bat."
            Suzuki "Don't worry about her for now. She'll be fine. Probably."
            Hiroya "I guess."
        "What's on your mind?":
            Hiroya "If you aren't bummed about the game, then why {i}are{/i} you here alone?"
            Suzuki bb speaking p1 "Oh, it's nothing. Was just replaying the game in my head, is all. Easier to do with less distractions."
            Suzuki "When I should've swung or not, whether I could've gone for a steal."
            Suzuki confident "You learn the most from the games you lose, right?"
            Hiroya "I mean, true, but..."
            Hiroya "You actually looked pretty good out there."
            Hiroya "And everyone else looked pretty clueless."
            Suzuki bb shouting p1 "H-hey, keep it down, man! They're not even a table away!"
            Hiroya "S-shoot, sorry."
            Suzuki bb tough p1 "'Sides. We win as a team, we lose as a team. There's always something I know I coulda done different."
            Suzuki confident "I'll save the team-wide talk for practice."
            "He beamed with a clever grin. One of my eyebrows perked up in response."
            Hiroya "You're gonna ream them out then, aren't you?"
            Suzuki bb vhappy p2 "Yup~"
            "Of course..."
        "Ask about Yukiko":
            Hiroya "Who's the waitress, Yukiko?"
            Suzuki bb speaking p1 "I don't really know much about her myself. She's still pretty new."
            Suzuki "She says she's trying to save money for after high school."
            Hiroya "She's young though, right? Is she even in high school?"
            Suzuki happy "Think she'll be transferring to Sugawara soon, actually. Maybe we'll see more of her."
            Suzuki bb vhappy p2 "What, you think she's cute?"
            Hiroya "That isn't it at all! I thought she might've been, like, your sister!"
            Suzuki confident "I bet you got a crush on her because she was nice to you~"
            Hiroya "I-it's not like that! She's a waitress, that's her {i}job{/i}!"
            "I could feel my face filling with heat! Suzuki was super annoying."
    Suzuki bb speaking p1 "I bet they're about to send out the food. You should pro'ly head back to your seat."
    Hiroya "Yeah, I guess so. Good chat, Suzuki."
    Suzuki happy "Same. I'll probably sit down with the rest of the guys soon enough."
    Suzuki bb vhappy p1 "Then the party's {i}really{/i} gonna start~"
    Hiroya "Well, I don't wanna get in your way."
    hide Suzuki with dissolve
    "I opted to stand clear of what will surely become a disaster zone, excusing myself from Suzuki's table."
    show Kaori u frustrated p1 with dissolve
    "Walking back to Kaori's table, I took my seat again across from her."
    "She still looked deep in thought, and I determine this wasn't the best time to bug her. Silence is golden, after all."
    Yukiko c smile vhappy "FOOOOOOD'S READY~"
    show Yukiko c smile eyesclosed very happy onlayer master:
        subpixel True xpos 0.15 ypos 1.0 xanchor 0.2 yanchor 1.0 rotate None
        parallel:
            xpos 1.15
            easein_quart 1.0 xpos 0.15
    "Like a bat out of Hell, Yukiko swung by our table with an exuberant grin."
    show Kaori u wink p2 with dissolve
    Yukiko "So I got the salad here for Miss Kaori, aaaand..."
    if lunch == "steak":
        Yukiko c smile eyesclosed "The steak dinner for our resident gourmet~"
        "Looking down at the plate, I could tell it was expertly grilled. Premium sirloin on a bed of local vegetables and mashed potatos."
        "This would've been a more pleasant sight to look at, if Kaori wasn't looking across the table at me, with intent to kill."
    if lunch == "liver":
        Yukiko c smile eyesclosed "The, ah, ahem, senior's dinner, with liver and fried onion."
        "I gazed at the plate. The liver and onions came together in a browned, saucy lump that wasn't the most aesthetically pleasing to the eye."
        "It didn't {i}smell{/i} particularly terrible, though? Maybe this stuff had a lot of good vitamins."
        "I was desperately trying to convince myself that this was a good decision."
    if lunch == "salad":
        Yukiko c smile eyesclosed "Ah, right, you ordered a salad too! No confusion!"
        Yukiko "Guys don't usually order salads though. Ah well~"
        "My plate looks almost identical to Kaori's in presentation."
        "Slices of grilled chicken were arranged in a neat circle on a bed of iceberg lettuce, sliced tomato, carrots and cabbage."
    Yukiko c smile eyesclosed "Enjoy! Call me if there's anything more I can do to help!"
    Kaori u speaking p1 "Thank you. This looks delightful."
    hide Yukiko with easeoutleft
    "Yukiko hurried off once more. She always looked to be in such a rush."
    "Kaori gave me a knowing glance, and we quietly dug into our meals."
    scene black with dissolve
    Hiroya "Damn, this {i}is{/i} good..."
    Kaori "Enjoy. I'm not always this generous."
    "We shared a quiet meal together, while the faint rumble of a raucous baseball team filled the air on the other side of the restaurant."
    "..."
    jump ch3Night

#pretty sure this is where ch3night should start
label ch3Night:
    #i honestly have no idea if there's a night variant for the streets
    scene bridge sidewalk night with dissolve
    "After a night of partying, the lot of us trickled out, slowly but surely."
    show Kaori u cool p1 with dissolve
    "Kaori paid everyone's tab well ahead of time, but that didn't stop the boys from loitering way too long. Kaori looked drained."
    show Suzuki bb vhappy p2 with easeinright:
        align (0.05, 1.0)
    Suzuki "Woo! Hell of a night, hey guys!?"
    Kaori u cool p1 "..."
    "Kaori merely huffed a sigh in response. She looked miffed, but at the same time, much too tired to actually act on it."
    Hiroya "I don't know why you're so happy about this, Suzuki. Don't you have to help clean up?"
    Suzuki bb shouting p1 "..."
    show Kaori u wink p2 2 with dissolve
    hide Suzuki with easeoutright
    Suzuki "GOTTAGOSEEYOUGUYSTOMORROW!"
    "He hollered, sprinting back into the restaurant."
    Kaori u frustrated p2 "That boy..."
    Kaori u wink p2 "Well, I should be going home too. I'll catch up with you again tomorrow at school."
    Hiroya "R-right. See you tomorrow."
    show Kaori u cool p1 with dissolve
    "She gave me a look of confusion, before shrugging it off. She took a sharp turn and strolled off."
    hide Kaori with easeoutleft
    "Of course I would forget that miserable fact. I didn't have a home to return to anymore."
    "Heaving a sigh, I dig my hands into my pocket. At least Kaori and Suzuki didn't catch anything."
    "I weighed my options. I could try and drift about the establishments that were still open, but I didn't have much money to my name."
    "And some of these places could get pretty dicey at night."
    "Maybe I should just stake out my claim under the bridge ASAP. There're probably a few other drifters eager to find some kind of shelter for the night."
    "Not that it exactly qualified as 'shelter', but in a pinch, it'd have to do. Between all the shenanigans with Kaori and Suzuki, I didn't have any time to explore alternatives."
    "Turning around with my back to the restaurant, I strolled towards the Dynasty Bridge. At the very least, I had enough food in my stomach to last the night."

    scene bridge below night with dissolve
    "Surprisingly, the bridge was clear."
    "There wasn't much I could bring with me when I walked out. I kept a sleeping bag on me, but..."
    "My main concern was the weather. The temperature was dropping terribly quickly."
    "I doubt I'd get hypothermia or frostbite, but a cold would suck. Well, more than things suck already."
    "There're some barrels off to the side. I wondered if others before me had similar ideas, and brought one for just such an occasion."
    Hiroya "Well, it's better than freezing."
    "Shrugging my shoulders, I head over to drag the barrel over, closer to the interior of the concrete and away from the bushes."
    "It occurs to me that I didn't bring a lighter. Or materials for a fire."
    "I sigh, rising from my feet. There should be some stuff nearby."
    scene black with dissolve
    "Wading through the shrubbery by the road, I gather dried grass, some twigs, and a few rocks. I have to do it quickly, because it's certainly not getting any warmer."
    "I never had to start a fire without matches or a lighter. I guess I have to go primitive and bang some rocks together."
    #sfx: rocks scraping/banging
    "{b}KLINK! KLINK!{/b}"
    Hiroya "TV made this look a hundred times easier."
    "I keep at it, getting increasingly irritated, until..."
    #sfx: fire
    "...Sparks catch the dry grass, and light it up. I make sure the fire catches."
    Hiroya "Fire. Fire good."

    scene bridge sidewalk night with dissolve
    "Huddling over the fire, I rub my hands together as if to catch the warmth in my palms."
    "This whole set-up could work for a while. I could mooch food during the day, then come back here for almost-warmth and almost-shelter."
    #sfx: throwing rock into water
    "{i}Plop.{/i}"
    "I don't have any brilliant ideas for sanitation. I guess I could keep using the school showers, but laundry costs money."
    "I could perform on the streets. But I don't know any instruments."
    #sfx: throwing rock into water
    "{i}Plop.{/i}"
    "And when winter hits, it's gonna be rough. I'd have to layer up."
    "I could check out the thrift store, see what's available. Or commit to petty larceny."
    #sfx: big splash
    "{b}KASPLOOSH!{/b}"
    Hiroya "What the-!?"

    #focus on writing, sprite past this point later
    "I flinched reflexively, my eyes darting over to the nearby river. What on Earth was that?"
    "There was a weird sound I was trying to ignore for a while. I decided to listen for the sound some more."
    "As if on cue, I watched a small rock plummet from the bridge above me."
    #sfx: throwing rock into water
    "It sinks into the river below, making a pathetic {i}plop{/i} as it did."
    "One of my eyebrows perked up. Was someone throwing rocks up there? What kind of person does that?"
    #sfx: big splash
    Hiroya "!"
    "Another big splash. This was getting tiresome."
    Hiroya "Think I'll just go up there and give them a piece of my mind."
    "My eyes drifted around my camp. I spotted a ladder nearby."
    "It was primarily used by maintenance workers, but it'd be the quickest way up."
    "I stroll over and get a feel for them. They were still dry, but chilly to the touch. Taking a deep breath, I ready myself for the climb."
    scene black with dissolve
    "Getting into a rhythm, I pull myself up higher and higher. My upper body strength's in a better place than I remember."
    "Maybe it's just puberty. I barely exert myself, but I make a point of not looking down."
    #q lines voiced by Kaori
    "???" "..."
    "I can almost make out someone's muttering at the top of the bridge. I continue my ascent, but I try to stay quiet to make out their voice."
    "???" "...can't stand it..."
    "I paused. It was a girl's voice. The voice sounded familiar."
    "She sounded frustrated. I continued up the ladder to listen in."
    "???" "...coming over like that, like everything's fine... it's not, and it never will be!"
    "Oh gosh. I recognized that voice!"
    "I scramble up the remaining rungs to peek over the side."

    scene bridge sidewalk night with dissolve
    "The moon cast a foreboding light over the metal frame of the Dynasty Bridge. It was terribly lonely up here."
    "The silence was broken up by the enraged ravings of one distraught girl."
    show Kaori u frustrated p1 with dissolve
    "Kaori Chiba...?"
    Kaori "Such an insufferable egotist! That knowing sneer! Grgh!"
    #sfx throw
    "She through a rock over the railing at lightning speed."
    Kaori "Why does she have to stick her nose into everything! Hasn't she sabotaged us enough!?"
    "And then she flung another. She knelt down to pick up a particularly heavy rock."
    Kaori "{i}Huff{/i}... must be easy being Daddy's little princess. She never worked a {i}day in her life-{/i}"
    Hiroya "You, uh, need a hand with that rock?"
    Kaori shout "KYAH!?"
    #sfx rock hitting pavement
    "She cried out in utter shock, her head swiftly turning to meet my eyes head on. Her mouth robotically opened and closed, trying to get some kind of explanation out."

    Kaori "H-H-Hiroya!? What are you {i}doing{/i} out here!? At this hour?"
    Hiroya "Shouldn't I be asking you that? You're the one throwing rockets off the bridge and making a racket."
    Kaori u sad1 p2 "I..."
    "She paused, taken aback. She knew I had a point, but she didn't look ready to admit it."
    Kaori u shoutblush p1 "It's not becoming of a gentleman to sneak up on a woman! You nearly gave me a heart attack!"
    Kaori "Go on! Apologize!"
    Hiroya "H-hey, don't blame me for anything! You're the crazy one throwing rocks."
    Kaori u sad1 p2 "I-"
    "Kaori grimaced when I pointed that out. She truly thought she was alone up here. Maybe she was."
    "She had been so vocal up to this point, but now she was stunned into silence."
    "What could I even say?"
    #if we wanna add a point system later here's a good spot to add some
    menu:
        "Lecture her.":
            Hiroya "You shouldn't be out here alone like this. It's dangerous."
            Kaori "I know that. Everyone does. That's why no one comes out here."
            Kaori "You think I don't realize that?"
            "My mouth flattened. Kaori didn't respond well to being talked down to."
            Hiroya "Don't snap at me like that. I don't want you to get into trouble, is all."
            Kaori u embarrassed p1 "You don't {i}need{/i} to look out for me, okay? I can take care of myself."
            Hiroya "Tch."
            "This wasn't going anywhere. Sighing, I begin to lower myself."
            Kaori u shout p1 "W-wait, wait, no. I'm sorry, I-I'm just stressed out."
            Kaori "I didn't mean to yell at you, it's just been a hard week for me."
            Hiroya "You want me to hang around for a bit?"
            Kaori u embarrassed p1 "...Sure."
            "With a nod, I haul myself over the railing to hang with her. It was quiet, and the air was heavier than it was before, but at least Kaori seemed calmer now."
            "She nodded slightly. I wasn't sure, but she was trying to be friendlier at least."
        "Joke with her.":
            Hiroya "You're not trying to hit anyone with those rocks, right?"
            Kaori u shoutblush p1 "What? Why would I?"
            Hiroya "You don't think Shizuka would really be wandering down on the banks, right?"
            Kaori u embarrassed p2 "Nah, I just... need to work off some steam."
            Kaori "And I wouldn't, like, want Shizuka to get {i}hurt{/i} or anything."
            Hiroya "Funny that you'd show concern for her and not for me."
            Kaori u frustrated p1 "Why would I be concerned about you?"
            Hiroya "You could've banged up my beautiful face, y'know. Cause some lasting damage."
            Kaori "I doubt I could disfigure it any more than it already is."
            Hiroya "Haha, ouch, Kaori. Harsh."
            Kaori "You could've just hollered or something..."
            Hiroya "But then I'd strain my tender vocal chords."
            Kaori "Jeez, you {i}are{/i} delicate. You're not getting scouted for the baseball team."
            "We share a few light laughs, but the air still feels heavy."
        "Join her.":
            "My eyes drift to the collection of large and small rocks and pebbles by her feet. Pulling myself over the railing to meet with her, I walk past her."
            "I reach down for one, and Kaori gives me a look of mild confusion."
            Kaori concerned "Huh? What are you doing?"
            Hiroya "When you're throwing, it's all in the wrist, you see."
            "I demonstrate by chucking one off the side. It goes surprisingly far."
            # If there is a wide-eyed amazed pose for Kayori added replace the neutral pls.
            show Kaori u cool p2 with dissolve
            "Kaori's eyes widen with curiosity."
            Kaori u wink p2 "Huh. You don't throw like a girl after all."
            Hiroya "I guess hanging with the baseball team helped me pick up on a few things."
            "Kaori flashed me a knowing smile, and quietly came up to my side."
            "For some time we simply spent time throwing rocks into the river. Between the two of us, Kaori's supply was exhausted quickly enough, but..."
            "Kaori was so quiet and {i}into it{/i}. She got into this kind of zen."
            "Maybe we bonded a little without having to say a single word. It was hard to say."
    "I relaxed on the railing next to Kaori, looking out onto the horizon."
    "I glance aside to Kaori. She always had this intense, inscrutable look on her face, as if she was willing up the strength to stand down a tidal wave."
    "And knowing her, she'd probably insist that it bow before her first."
    Kaori u cool p1 "I came out here to unwind, and vent. That's all, really."
    Hiroya "You come out here often?"
    Kaori u embarrassed p1 "Not too often?"
    "Her response was a little cagey and uncertain. I took it as a 'yes', but opted not to press her any further."
    "We continued to stare at the moonlit sky. It was oddly serene, like we were in a world all of our own."
    "Isolated and peaceful. The ambient sounds of traffic and cicadas filled the silences between us."
    Kaori u shout p1 "...Hey, Hiroya."
    "Kaori spoke up to break the silence between us. She glanced over to me with a somber look."
    Hiroya "Yeah?"
    Kaori "Did I ever tell you {i}why{/i} I became the student council president?"
    Hiroya "Not really. Nothing outside of your acceptance speeches."
    "Truthfully, I wasn't paying the fullest attention back then, but I kept that to myself. Kaori wanted to say something."
    "Kaori looked ahead, across the water."
    Kaori "I guess I didn't tell you that much about my family."
    Hiroya "You did mention a few things at dinner, like how they were involved in construction."
    Kaori "Well, we kind of... fell on some hard times."
    Hiroya "Hard times? Wait, you {i}just{/i} paid for everyone's dinners, right?"
    Kaori u speaking p1 "Heheh. It's good to keep up appearances, Hiroya."
    Hiroya "Th, that's not the point. Could you afford it?"
    Kaori concerned "Yeah, I could. It's just dicier than usual."
    Kaori "Mom and Dad, they also had a hand in building Sugawara, and Sugawara's always been, well, a fantastic place. Lot of memories."
    Kaori "I always wanted to go there, to learn everything I could, and join my family in politics. To make a real, positive difference."
    Kaori "But now, with Shizuka and Endo kicking at our tires, the school's in a rough way. Fewer enrollments, fewer sponsorships..."
    Kaori "We can't attract the best faculty anymore. We might have to close shop within a few years."
    Kaori "I... I ended up pushing to become president, so I could... I could make a stand."
    Kaori "For my family to have someone to rally around, and for the school to bounce back."
    Kaori u shout p1 "I don't wanna be remembered as the last student council president who sat around and did nothing."
    "She flashed a sad smile, her eyes lowering to the moonlit river."
    "Kaori seemed so nostalgic in this moment."
    Hiroya "I didn't realize..."
    Kaori u embarrassed p1 "I'm not exactly vocal about this sort of stuff. I didn't mean to burden you, I just..."
    Kaori "You seem reliable."
    Hiroya "Reliable's good."
    Kaori u frustrated p2 "Don't get an inflated ego or anything."
    Hiroya "Still, if there's anything I can do, you can ask me for help, you know?"
    Kaori u shout p1 "Yeah, I know, it's just - I'm not sure what there is that could be done."
    "She sighed, lamenting her tragic fate."
    Hiroya "We'll think of something."
    Kaori u embarrassed p1 "Yeah. I always do."
    "She rubbed her shoulder, a little anxiously. She bit her lip, before glancing over to me."
    Kaori speaking "But, hey, enough about me. What're you doing out here?"
    Kaori u happyblush p2 "Don't tell me you were following me the whole time."
    Hiroya "What? No. I-"
    "This was weird. She was so honest with me a second ago. It's not like I could lie in her face at this time."
    "I take a deep breath. The truth was a bitter pill to swallow, but Kaori deserved nothing less."
    Hiroya "I, uh... live here."
    Kaori speaking "No you don't."
    "She regarded me with considerable skepticism. Why didn't she believe me?"
    Hiroya "No, seriously, I, ah, got in a fight with my old man. And I ran out. And now I'm taking up shelter underneath the bridge."
    Kaori u shout p1 "You serious, Hiroya?"
    Hiroya "..."
    "I nodded, rather thoroughly ashamed to admit it. Still, it felt like a weight was being lifted from my chest."
    Kaori "Huh. That explains why you looked like shit this morning."
    "And now the weight was placed squarely back where it was. Brutal."
    # show kayori wide eyed worried(or whatever it's named) with dissolve
    "Her eyes widened."
    Kaori "Waitwait, you can't just - a Sugawara student living out on the streets is a horrible thing to bear!"
    Hiroya "It's, well, not the greatest, but I can probably-"
    Kaori "This would be a black-eye on our school's reputation! I can't possibly overlook this!"
    Kaori u frustrated p1 "Thank you for bringing this to my attention! I have an idea!"
    Hiroya "You really don't have to - wait, what?"
    "She was positively beaming now. She really thought of something that quickly?"
    "Normally, when she had that look in her eyes, it spelled trouble. But this time, I saw her in a new light. A flagbearer for hope, I suppose."
    Hiroya "What are you thinking about, Kaori?"
    Kaori shout "Get your things, quickly! It's late and we can't be out here long!"
    hide Kaori with easeoutright
    Hiroya "H-hey, wait! Ouch, jeez, okay!"
    "She clutched my arm and dragged me away from the railing, speeding down the concrete walkways and back to solid land."

    scene bridge below night with dissolve
    show Kaori u cool p1 with dissolve
    "I hastily gather my things under Kaori's piercing gaze. Her eyes drifted around my camp with a look of contempt."
    Kaori "Boy, Hiroya, if you came out here to camp, you could've come a lot more prepared than this."
    Hiroya "I was in a rush! And I'm poor!"
    Kaori u wink p1 "Well, you won't have to survive out here another night."
    Hiroya "Wait, what?"
    Kaori "Trust me. I have {i}connections{/i}."
    "She slyly stated with a wink."
    "As soon as I was done, she clutched my arm again and was already sprinting off."
    hide Kaori with easeoutright
    Kaori "C'mon, c'mon! I thought you were supposed to be some kind of badass!"
    Hiroya "I-I can run by myself, thank you!"

    scene bridge sidewalk night with dissolve
    "Ten minutes later, we slowed to a stop back in the commercial district."
    #should add a closed eyes smiling contently pose?
    show Kaori u speaking p1 with dissolve
    Kaori "Alright! We've arrived!"
    Hiroya "Isn't this... Suzuki's place?"
    Kaori "Of course! His family lives here, so I'll set you up with him. He owes me."
    #sfx: door banging
    "She banged on the door with great fervour and ferocity. The clattering of the door was piercing at this quiet hour - I half-suspected the door would topple over at any minute."
    Kaori shout "Suzuuuukiiiiii!"
    #sfx door jingle
    "Suzuki groggily wandered out with a dull expression on his face."
    #tired suzuki pose? Also pajamas maybe?
    show Suzuki bb speaking p2 onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos -0.2
            ease 2.0 xpos 0.2
    Suzuki "Kaori? Hiroya? We're closed, guys, come on..."
    Kaori u speaking p1 "I need you to take care of Hiroya. He'll be lodging with you for the foreseeable future."
    Suzuki bb shouting p1 "What!?"
    Hiroya "Yeah, what?"
    Kaori "Well, what would be more appropriate? Boys sleeping together, or a boy sharing a room with a girl?"
    Kaori "I have an image to maintain, and Suzuki owes me many favours. Now I'm cashing them."
    Suzuki "Hey, hey, hold up, don't I get a say in this!?"
    Kaori "Suzuki, Hiroya's sleeping on the streets. He needs a roof over his head. You understand, right?"
    Suzuki bb speaking p1 "Seriously!? Hey, dude, is that really true?"
    Hiroya "T-technically. K-Kaori, I was doing fine-"
    Kaori shout "No! I will not tolerate your homeless situation! You will bunk with Suzuki and you will like it!"
    "She barked with the ferocity of a drill instructor."
    "Honestly, there was little room to argue. A warm bed would be nice, and Suzuki's leftovers would be fantastic."
    show Suzuki bb frown p2 with dissolve
    "Suzuki seemed conflicted on the point. It was spelled out on his face."
    "Eventually, she sighed."
    Suzuki speaking "{i}Fiiiiine...{/i} I guess he can stay for a little while."
    Kaori u speaking p1 "I knew I made an excellent choice in partnering with you, Suzuki."
    Suzuki "This deal's getting worse all of the time."
    Kaori "Pray I don't change it any further. Now, I'm off, I'll leave it to you two to get sorted out."
    hide Kaori with easeoutleft
    show Suzuki bb speaking p1 onlayer master:
        subpixel True xpos 0.2 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.2
            ease 1.0 xpos 0.5
    Kaori "Toodles~"
    "She sprinted off so quickly. She was brave, trying to stick me with Suzuki so brazenly like this."
    Suzuki "...'S'it true, man? You sleeping out on the streets?"
    Hiroya "Y-yeah. Don't tell too many people, alright?"
    Suzuki frown "Naw man, I get it. I'll keep quiet. Just don't make a mess of things."
    Suzuki "C'mon in. Think I got a spare futon somewhere."

    scene cafe inside night with dissolve
    show Suzuki bb speaking p1 with dissolve
    "Suzuki pulled me inside, relocking the door behind me. It was already dark inside, as if everyone else had gone to bed."
    Hiroya "Does everyone in your house go to bed so early? It's only 11."
    Suzuki "We start opening at 6 in the morning. We were all asleep."
    Hiroya "Shit. Sorry for waking you up on my account."
    Suzuki "Naw, it's fine. Kaori woke me up, not you. Not your fault."
    Hiroya "W-well, I mean, it kinda is. I walked out on my family, but-"
    Suzuki "You ain't going back?"
    Hiroya "No way in hell. Not to that selfish pig father of mine."
    Suzuki "Sounds like there's some beef between you guys. It's a little late for me to ask about it, so..."
    Suzuki "I'll look for the futon. We'll catch up in the morning."
    show Suzuki bb speaking p1 onlayer master:
        subpixel True xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 1.0 rotate None
        parallel:
            xpos 0.5
            ease 2.0 xpos 1.5
    "He staggered off to begin his search. Thinking he'd need a second pair of eyes, I followed."
    "Tiredly, we searched and gathered the things we need. After some work, we had an arrangement worked out."
    #revisit this based on the contents of the BG we want
    show Suzuki bb speaking p2 with dissolve:
        align (0.5, 1.0)
    Suzuki "A'ight, you'll be sleeping here."
    Hiroya "Isn't this a pantry?"
    Suzuki "What? It's big enough, right? You can stretch your legs, easy."
    Hiroya "The spices are really strong."
    Suzuki "Breathe through your mouth, you'll be fine. Good night."
    hide suzuki with dissolve
    "Without another word, he slammed the door behind me, and stomped off."
    "I look around to get a feel for my new surroundings."
    Hiroya "Well, it beats sleeping under the bridge."
    "Wearily, I slipped underneath the sheets, feeling my weary body relax, almost in agreement to the plushy cushions."
    "Definitely beats sleeping on hard concrete too."
    scene black with dissolve
    "I didn't have any energy to continue questioning what had happened, and allowed myself to pass out."
    return
