init:
    #Text outlines
    $ style.say_default.outlines = [(1, "000000", 0, 0), (1, "#202020", 1, 1)]
    $ style.say_thought.outlines = [(1, "000000", 0, 0), (1, "#202020", 1, 1)]
    $ style.say_dialogue.outlines = [(1, "000000", 0, 0), (1, "#202020", 1, 1)]
    $ style.pref_label_text.outlines = [(1, "000000", 0, 0), (1, "#202020", 1, 1)]


    $ leftoffset = Position(xpos = .35)
    $ leftoffset2 = Position(xpos = .15)
    $ rightoffset = Position(xpos = .65)
    $ rightoffset2 = Position(xpos = .85)
    $ chaptertitlespot = Position(xanchor = 0.0, yanchor = 0.5, xpos = 0.6, yalign = 0.45)

    # Character Initialization: These lines represent all the possible sprites you can call up.
    # When adding new sprites, this is where you define them. If you rename the files, they have to be renamed here too.
    # The "Color" value lets you choose a six hexadecimal color code for each character's name.

    #Main Character Definitions:
    define Akari = Character("Akari Miyazaki", image = "Akari",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Kaori = Character("Kaori Chiba", image = "Kaori",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Suzuki = Character("Kisaragi Suzuki", image = "Suzuki",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Shizuka = Character("Shizuka Endo", image = "Shizuka",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Miyu = Character("Miyu Nanako", image = "Miyu",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Yukiko = Character("Yukiko Mizuno", image = "Yukiko",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Izumi = Character("Izumi Mizuno", image = "Izumi",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Hiroya = Character("Hiroya Tachibana", image = "Hiroya",who_color="#ffffff",what_prefix = '"', what_suffix = '"')

    ##These are side characters who don't have images. They don't technically need to be defined but it'll auto add quotes this way.
    define Dad = Character("Dad",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Hojo = Character("Hojo-sensei",who_color ="ffffff", what_prefix = '"' , what_suffix = '"')
    define Hirayama = Character("Hirayama-sensei",who_color ="ffffff", what_prefix = '"' , what_suffix = '"')
    define Miyazaki = Character("Miyazaki",who_color ="ffffff", what_prefix = '"' , what_suffix = '"')
    define BaseballGuy = Character("Baseball Guy",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Aoi = Character("Aoi",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Touma = Character("Touma",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Juichi = Character("Juichi",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Tall = Character("The tall one",who_color="#ffffff",what_prefix = '"', what_suffix = '"')
    define Round = Character("The round one",who_color="#ffffff",what_prefix = '"', what_suffix = '"')



    #Example of a night time character tint:
    image characternight = im.MatrixColor("sprites/Kaori/Uniform/pose 1/Kaori u shocked p1.png",
                                im.matrix.saturation(0.7)*im.matrix.tint(.9,.9,1)*im.matrix.brightness(-0.05))
    #Akari Sprites:
    #Uniform:
    #First pose
    image Akari u confident p1 = "sprites/Akari/Uniform/pose 1/Akari u confident p1.png"
    image Akari u frown p1 = "sprites/Akari/Uniform/pose 1/Akari u frown p1.png"
    image Akari u happy p1 = "sprites/Akari/Uniform/pose 1/Akari u happy p1.png"
    image Akari u nervous p1 = "sprites/Akari/Uniform/pose 1/Akari u nervous p1.png"
    image Akari u questioning p1 = "sprites/Akari/Uniform/pose 1/Akari u questioning p1.png"
    image Akari u sad p1 = "sprites/Akari/Uniform/pose 1/Akari u sad p1.png"
    image Akari u scheming p1 = "sprites/Akari/Uniform/pose 1/Akari u scheming p1.png"
    image Akari u speaking p1 = "sprites/Akari/Uniform/pose 1/Akari u speaking p1.png"
    image Akari u vhappy p1 = "sprites/Akari/Uniform/pose 1/Akari u vhappy p1.png"
    #Second pose
    image Akari u confident p2 = "sprites/Akari/Uniform/pose 2/Akari u confident p2.png"
    image Akari u frown p2 = "sprites/Akari/Uniform/pose 2/Akari u frown p2.png"
    image Akari u happy p2 = "sprites/Akari/Uniform/pose 2/Akari u happy p2.png"
    image Akari u nervous p2 = "sprites/Akari/Uniform/pose 2/Akari u nervous p2.png"
    image Akari u questioning p2 = "sprites/Akari/Uniform/pose 2/Akari u questioning p2.png"
    image Akari u sad p2 = "sprites/Akari/Uniform/pose 2/Akari u sad p2.png"
    image Akari u scheming p2 = "sprites/Akari/Uniform/pose 2/Akari u scheming p2.png"
    image Akari u speaking p2 = "sprites/Akari/Uniform/pose 2/Akari u speaking p2.png"
    image Akari u vhappy p2 = "sprites/Akari/Uniform/pose 2/Akari u vhappy p2.png"
    #Third Pose
    image Akari u confident p3 = "sprites/Akari/Uniform/pose 3/Akari u confident p3.png"
    image Akari u frown p3 = "sprites/Akari/Uniform/pose 3/Akari u frown p3.png"
    image Akari u happy p3 = "sprites/Akari/Uniform/pose 3/Akari u happy p3.png"
    image Akari u nervous p3 = "sprites/Akari/Uniform/pose 3/Akari u nervous p3.png"
    image Akari u questioning p3 = "sprites/Akari/Uniform/pose 3/Akari u questioning p3.png"
    image Akari u sad p3 = "sprites/Akari/Uniform/pose 3/Akari u sad p3.png"
    image Akari u scheming p3 = "sprites/Akari/Uniform/pose 3/Akari u scheming p3.png"
    image Akari u speaking p3 = "sprites/Akari/Uniform/pose 3/Akari u speaking p3.png"
    image Akari u vhappy p3 = "sprites/Akari/Uniform/pose 3/Akari u vhappy p3.png"
    #Fourth Pose
    image Akari u confident p4 = "sprites/Akari/Uniform/pose 4/Akari u confident p4.png"
    image Akari u frown p4 = "sprites/Akari/Uniform/pose 4/Akari u frown p4.png"
    image Akari u happy p4 = "sprites/Akari/Uniform/pose 4/Akari u happy p4.png"
    image Akari u nervous p4 = "sprites/Akari/Uniform/pose 4/Akari u nervous p4.png"
    image Akari u questioning p4 = "sprites/Akari/Uniform/pose 4/Akari u questioning p4.png"
    image Akari u sad p4 = "sprites/Akari/Uniform/pose 4/Akari u sad p4.png"
    image Akari u scheming p4 = "sprites/Akari/Uniform/pose 4/Akari u scheming p4.png"
    image Akari u speaking p4 = "sprites/Akari/Uniform/pose 4/Akari u speaking p4.png"
    image Akari u vhappy p4 = "sprites/Akari/Uniform/pose 4/Akari u vhappy p4.png"
    #Fifth Pose
    image Akari u angry1 p5 = "sprites/Akari/Uniform/Pose 5/Akari u angry1 p5.png"
    image Akari u angry2 p5 = "sprites/Akari/Uniform/Pose 5/Akari u angry2 p5.png"
    image Akari u angry3 p5 = "sprites/Akari/Uniform/Pose 5/Akari u angry3 p5.png"
    #Sixth Pose
    image Akari u angry1 p6 = "sprites/Akari/Uniform/Pose 6/Akari u angry1 p6.png"
    image Akari u angry2 p6 = "sprites/Akari/Uniform/Pose 6/Akari u angry2 p6.png"
    image Akari u angry3 p6 = "sprites/Akari/Uniform/Pose 6/Akari u angry3 p6.png"
    #Akari Casual
    image Akari c confident = "sprites/Akari/Casual/Akari c confident.png"
    image Akari c frown = "sprites/Akari/Casual/Akari c frown.png"
    image Akari c happy = "sprites/Akari/Casual/Akari c happy.png"
    image Akari c nervous = "sprites/Akari/Casual/Akari c nervous.png"
    image Akari c questioning = "sprites/Akari/Casual/Akari c questioning.png"
    image Akari c sad = "sprites/Akari/Casual/Akari c sad.png"
    image Akari c scheming = "sprites/Akari/Casual/Akari c scheming.png"
    image Akari c speaking = "sprites/Akari/Casual/Akari c speaking.png"
    image Akari c vhappy = "sprites/Akari/Casual/Akari c vhappy.png"
    #Akari Casual Holding Uroko
    #cat expression 1
    image Akari cat1 confident = "sprites/Akari/cat/cat1/Akari cat1 confident.png"
    image Akari cat1 frown = "sprites/Akari/cat/cat1/Akari cat1 frown.png"
    image Akari cat1 happy = "sprites/Akari/cat/cat1/Akari cat1 happy.png"
    image Akari cat1 questioning = "sprites/Akari/cat/cat1/Akari cat1 questioning.png"
    image Akari cat1 speaking = "sprites/Akari/cat/cat1/Akari cat1 speaking.png"
    image Akari cat1 vhappy = "sprites/Akari/cat/cat1/Akari cat1 vhappy.png"
    #cat expression 2
    image Akari cat2 confident = "sprites/Akari/cat/cat2/Akari cat2 confident.png"
    image Akari cat2 frown = "sprites/Akari/cat/cat2/Akari cat2 frown.png"
    image Akari cat2 happy = "sprites/Akari/cat/cat2/Akari cat2 happy.png"
    image Akari cat2 questioning = "sprites/Akari/cat/cat2/Akari cat2 questioning.png"
    image Akari cat2 speaking = "sprites/Akari/cat/cat2/Akari cat2 speaking.png"
    image Akari cat2 vhappy = "sprites/Akari/cat/cat2/Akari cat2 vhappy.png"
    #cat expression 3
    image Akari cat3 confident = "sprites/Akari/cat/cat3/Akari cat3 confident.png"
    image Akari cat3 frown = "sprites/Akari/cat/cat3/Akari cat3 frown.png"
    image Akari cat3 happy = "sprites/Akari/cat/cat3/Akari cat3 happy.png"
    image Akari cat3 questioning = "sprites/Akari/cat/cat3/Akari cat3 questioning.png"
    image Akari cat3 speaking = "sprites/Akari/cat/cat3/Akari cat3 speaking.png"
    image Akari cat3 vhappy = "sprites/Akari/cat/cat3/Akari cat3 vhappy.png"

    #Kaori sprites:
    #First pose confident pose, standing to the side
    image Kaori u caring p1 = "sprites/Kaori/Uniform/pose 1/Kaori u caring p1.png"
    image Kaori u concerned p1 = "sprites/Kaori/Uniform/pose 1/Kaori u concerned p1.png"
    image Kaori u cool p1 = "sprites/Kaori/Uniform/pose 1/Kaori u cool p1.png"
    image Kaori u consoling p1 = "sprites/Kaori/Uniform/pose 1/Kaori u consoling p1.png"
    image Kaori u frustrated p1 = "sprites/Kaori/Uniform/pose 1/Kaori u frustrated p1.png"
    image Kaori u happyblush p1 = "sprites/Kaori/Uniform/pose 1/Kaori u happyblush p1.png"
    image Kaori u glaring p1 = "sprites/Kaori/Uniform/pose 1/Kaori u glaring p1.png"
    image Kaori u shocked p1 = "sprites/Kaori/Uniform/pose 1/Kaori u shocked p1.png"
    image Kaori u happy p1 = "sprites/Kaori/Uniform/pose 1/Kaori u happy p1.png"
    image Kaori u shout p1 = "sprites/Kaori/Uniform/pose 1/Kaori u shout p1.png"
    image Kaori u shoutblush p1 = "sprites/Kaori/Uniform/pose 1/Kaori u shoutblush p1.png"
    image Kaori u embarrassed p1 = "sprites/Kaori/Uniform/pose 1/Kaori u embarrassed p1.png"
    image Kaori u sad1 p1 = "sprites/Kaori/Uniform/pose 1/Kaori u sad1 p1.png"
    image Kaori u sad2 p1 = "sprites/Kaori/Uniform/pose 1/Kaori u sad2 p1.png"
    image Kaori u speaking p1 = "sprites/Kaori/Uniform/pose 1/Kaori u speaking p1.png"
    image Kaori u wink p1 = "sprites/Kaori/Uniform/pose 1/Kaori u wink p1.png"
    image Kaori u confused p1 = "sprites/Kaori/Uniform/pose 1/Kaori u confused p1.png"
    #Second pose leaning forward
    image Kaori u caring p2 = "sprites/Kaori/Uniform/pose 2/Kaori u caring p2.png"
    image Kaori u concerned p2 = "sprites/Kaori/Uniform/pose 2/Kaori u concerned p2.png"
    image Kaori u cool p2 = "sprites/Kaori/Uniform/pose 2/Kaori u cool p2.png"
    image Kaori u consoling p2 = "sprites/Kaori/Uniform/pose 2/Kaori u consoling p2.png"
    image Kaori u frustrated p2 = "sprites/Kaori/Uniform/pose 2/Kaori u frustrated p2.png"
    image Kaori u happyblush p2 = "sprites/Kaori/Uniform/pose 2/Kaori u happyblush p2.png"
    image Kaori u glaring p2 = "sprites/Kaori/Uniform/pose 2/Kaori u glaring p2.png"
    image Kaori u shocked p2 = "sprites/Kaori/Uniform/pose 2/Kaori u shocked p2.png"
    image Kaori u happy p2 = "sprites/Kaori/Uniform/pose 2/Kaori u happy p2.png"
    image Kaori u shout p2 = "sprites/Kaori/Uniform/pose 2/Kaori u shout p2.png"
    image Kaori u shoutblush p2 = "sprites/Kaori/Uniform/pose 2/Kaori u shoutblush p2.png"
    image Kaori u embarrassed p2 = "sprites/Kaori/Uniform/pose 2/Kaori u embarrassed p2.png"
    image Kaori u sad1 p2 = "sprites/Kaori/Uniform/pose 2/Kaori u sad1 p2.png"
    image Kaori u sad2 p2 = "sprites/Kaori/Uniform/pose 2/Kaori u sad2 p2.png"
    image Kaori u speaking p2 = "sprites/Kaori/Uniform/pose 2/Kaori u speaking p2.png"
    image Kaori u wink p2 = "sprites/Kaori/Uniform/pose 2/Kaori u wink p2.png"
    image Kaori u confused p2 = "sprites/Kaori/Uniform/pose 2/Kaori u confused p2.png"
    #Suzuki Sprites:
    #Baseball Outfit:
    #First pose, arms by his sides
    image Suzuki bb confident p1 = "sprites/Suzuki/bb/pose1/suzuki bb confident p1.png"
    image Suzuki bb frown p1 = "sprites/Suzuki/bb/pose1/suzuki bb frown p1.png"
    image Suzuki bb happy p1 = "sprites/Suzuki/bb/pose1/suzuki bb happy p1.png"
    image Suzuki bb questioning p1 = "sprites/Suzuki/bb/pose1/suzuki bb questioning p1.png"
    image Suzuki bb shouting p1 = "sprites/Suzuki/bb/pose1/suzuki bb shouting p1.png"
    image Suzuki bb speaking p1 = "sprites/Suzuki/bb/pose1/suzuki bb speaking p1.png"
    image Suzuki bb tough p1 = "sprites/Suzuki/bb/pose1/suzuki bb tough p1.png"
    image Suzuki bb vhappy p1 = "sprites/Suzuki/bb/pose1/suzuki bb vhappy p1.png"
    #Second pose, arms up by his head
    image Suzuki bb confident p2 = "sprites/Suzuki/bb/pose2/suzuki bb confident p2.png"
    image Suzuki bb frown p2 = "sprites/Suzuki/bb/pose2/suzuki bb frown p2.png"
    image Suzuki bb happy p2 = "sprites/Suzuki/bb/pose2/suzuki bb happy p2.png"
    image Suzuki bb questioning p2 = "sprites/Suzuki/bb/pose2/suzuki bb questioning p2.png"
    image Suzuki bb shouting p2 = "sprites/Suzuki/bb/pose2/suzuki bb shouting p2.png"
    image Suzuki bb speaking p2 = "sprites/Suzuki/bb/pose2/suzuki bb speaking p2.png"
    image Suzuki bb tough p2 = "sprites/Suzuki/bb/pose2/suzuki bb tough p2.png"
    image Suzuki bb vhappy p2 = "sprites/Suzuki/bb/pose2/suzuki bb vhappy p2.png"
    #Suzuki Casual
    image Suzuki c confident = "sprites/Suzuki/casual/suzuki c confident.png"
    image Suzuki c frown = "sprites/Suzuki/casual/suzuki c frown.png"
    image Suzuki c happy = "sprites/Suzuki/casual/suzuki c happy.png"
    image Suzuki c vhappy = "sprites/Suzuki/casual/suzuki c vhappy.png"
    image Suzuki c speaking = "sprites/Suzuki/casual/suzuki c speaking.png"
    image Suzuki c tough = "sprites/Suzuki/casual/suzuki c tough.png"
    image Suzuki c questioning = "sprites/Suzuki/casual/suzuki c questioning.png"
    image Suzuki c shouting = "sprites/Suzuki/casual/suzuki c shouting.png"
    #Suzuki Uniform
    #Pose 1 crossed arms
    image Suzuki u happy p1 = "sprites/Suzuki/uniform/pose1/suzuki u happy p1.png"
    image Suzuki u confident p1 = "sprites/Suzuki/uniform/pose1/suzuki u confident p1.png"
    image Suzuki u frown p1 = "sprites/Suzuki/uniform/pose1/suzuki u frown p1.png"
    image Suzuki u questioning p1 = "sprites/Suzuki/uniform/pose1/suzuki u questioning p1.png"
    image Suzuki u shouting p1 = "sprites/Suzuki/uniform/pose1/suzuki u shouting p1.png"
    image Suzuki u speaking p1 = "sprites/Suzuki/uniform/pose1/suzuki u speaking p1.png"
    image Suzuki u tough p1 = "sprites/Suzuki/uniform/pose1/suzuki u tough p1.png"
    image Suzuki u vhappy p1 = "sprites/Suzuki/uniform/pose1/suzuki u vhappy p1.png"
    #pose2 pointing
    image Suzuki u happy p2 = "sprites/Suzuki/uniform/pose2/suzuki u happy p2.png"
    image Suzuki u confident p2 = "sprites/Suzuki/uniform/pose2/suzuki u confident p2.png"
    image Suzuki u frown p2 = "sprites/Suzuki/uniform/pose2/suzuki u frown p2.png"
    image Suzuki u questioning p2 = "sprites/Suzuki/uniform/pose2/suzuki u questioning p2.png"
    image Suzuki u shouting p2 = "sprites/Suzuki/uniform/pose2/suzuki u shouting p2.png"
    image Suzuki u speaking p2 = "sprites/Suzuki/uniform/pose2/suzuki u speaking p2.png"
    image Suzuki u tough p2 = "sprites/Suzuki/uniform/pose2/suzuki u tough p2.png"
    image Suzuki u vhappy p2 = "sprites/Suzuki/uniform/pose2/suzuki u vhappy p2.png"

    #Shizuka Sprites:
    image Shizuka u neutral = "sprites/Shizuka/uniform/Shizuka u neutral.png"
    image Shizuka u happy = "sprites/Shizuka/uniform/Shizuka u happy.png"
    image Shizuka u speaking = "sprites/Shizuka/uniform/Shizuka u speaking.png"
    image Shizuka u mad = "sprites/Shizuka/uniform/Shizuka u mad.png"
    image Shizuka u questioning = "sprites/Shizuka/uniform/Shizuka u questioning.png"
    image Shizuka u confident = "sprites/Shizuka/uniform/Shizuka u confident.png"

    #Miyu Sprites:
    #Uniform
    image Miyu u nervous = "sprites/Miyu/Uniform/Miyu u nervous.png"
    image Miyu u happy = "sprites/Miyu/Uniform/Miyu u happy.png"
    image Miyu u speaking = "sprites/Miyu/Uniform/Miyu u speaking.png"
    image Miyu u upset = "sprites/Miyu/Uniform/Miyu u upset.png"
    image Miyu u concentrating = "sprites/Miyu/Uniform/Miyu u concentrating.png"
    #Casual
    image Miyu u nervous = "sprites/Miyu/Uniform/Miyu u nervous.png"
    image Miyu u happy = "sprites/Miyu/Uniform/Miyu u happy.png"
    image Miyu u speaking = "sprites/Miyu/Uniform/Miyu u speaking.png"
    image Miyu u upset = "sprites/Miyu/Uniform/Miyu u upset.png"
    image Miyu u concentrating = "sprites/Miyu/Uniform/Miyu u concentrating.png"

    #Yukiko Sprites:
    #casual outfit
    image Yukiko c curious = "sprites/Yukiko/casual/Yukiko c curious.png"
    image Yukiko c frown = "sprites/Yukiko/casual/Yukiko c frown.png"
    image Yukiko c poutyblush = "sprites/Yukiko/casual/Yukiko c poutyblush.png"
    image Yukiko c pout = "sprites/Yukiko/casual/Yukiko c pout.png"
    image Yukiko c smile attitude = "sprites/Yukiko/casual/Yukiko c smile attitude.png"
    image Yukiko c smile confident = "sprites/Yukiko/casual/Yukiko c smile confident.png"
    image Yukiko c smile eyesclosed = "sprites/Yukiko/casual/Yukiko c smile eyesclosed.png"
    image Yukiko c smile sweet = "sprites/Yukiko/casual/Yukiko c smile sweet.png"
    image Yukiko c smile vhappy = "sprites/Yukiko/casual/Yukiko c smile vhappy.png"
    image Yukiko c smile normal = "sprites/Yukiko/casual/Yukiko c smile normal.png"
    image Yukiko c smile happy = "sprites/Yukiko/casual/Yukiko c smile happy.png"
    image Yukiko c speaking annoyed = "sprites/Yukiko/casual/Yukiko c speaking annoyed.png"
    image Yukiko c speaking questioning = "sprites/Yukiko/casual/Yukiko c speaking questioning.png"
    image Yukiko c speaking serious = "sprites/Yukiko/casual/Yukiko c speaking serious.png"
    image Yukiko c upset = "sprites/Yukiko/casual/Yukiko c upset.png"
    image Yukiko c speaking surprised = "sprites/Yukiko/casual/Yukiko c speaking surprised.png"
    #Holding cat
    image Yukiko cat1 frown = "sprites/Yukiko/Cat/frown/yukiko cat1 frown.png"
    image Yukiko cat2 frown = "sprites/Yukiko/Cat/frown/yukiko cat2 frown.png"
    image Yukiko cat3 frown = "sprites/Yukiko/Cat/frown/yukiko cat3 frown.png"
    image Yukiko cat1 pout = "sprites/Yukiko/Cat/pout/yukiko cat1 pout.png"
    image Yukiko cat2 pout = "sprites/Yukiko/Cat/pout/yukiko cat2 pout.png"
    image Yukiko cat3 pout = "sprites/Yukiko/Cat/pout/yukiko cat3 pout.png"
    image Yukiko cat1 poutyblush = "sprites/Yukiko/Cat/poutyblush/yukiko cat1 poutyblush.png"
    image Yukiko cat2 poutyblush = "sprites/Yukiko/Cat/poutyblush/yukiko cat2 poutyblush.png"
    image Yukiko cat3 poutyblush = "sprites/Yukiko/Cat/poutyblush/yukiko cat3 poutyblush.png"
    image Yukiko cat1 smile attitude = "sprites/Yukiko/Cat/smile attitude/yukiko cat1 smile attitude.png"
    image Yukiko cat2 smile attitude = "sprites/Yukiko/Cat/smile attitude/yukiko cat2 smile attitude.png"
    image Yukiko cat3 smile attitude = "sprites/Yukiko/Cat/smile attitude/yukiko cat3 smile attitude.png"
    image Yukiko cat1 smile confident = "sprites/Yukiko/Cat/smile confident/yukiko cat1 smile confident.png"
    image Yukiko cat2 smile confident = "sprites/Yukiko/Cat/smile confident/yukiko cat2 smile confident.png"
    image Yukiko cat3 smile confident = "sprites/Yukiko/Cat/smile confident/yukiko cat3 smile confident.png"
    image Yukiko cat1 smile eyesclosed = "sprites/Yukiko/Cat/smile eyesclosed/yukiko cat1 smile eyesclosed.png"
    # missing image Yukiko cat2 smile eyesclosed = "sprites/Yukiko/Cat/smile eyesclosed/yukiko cat2 smile eyesclosed.png"
    image Yukiko cat3 smile eyesclosed = "sprites/Yukiko/Cat/smile eyesclosed/yukiko cat3 smile eyesclosed.png"
    image Yukiko cat1 smile happy = "sprites/Yukiko/Cat/smile happy/yukiko cat1 smile happy.png"
    image Yukiko cat2 smile happy = "sprites/Yukiko/Cat/smile happy/yukiko cat2 smile happy.png"
    image Yukiko cat3 smile happy = "sprites/Yukiko/Cat/smile happy/yukiko cat3 smile happy.png"
    image Yukiko cat1 smile normal = "sprites/Yukiko/Cat/smile normal/yukiko cat1 smile normal.png"
    image Yukiko cat2 smile normal = "sprites/Yukiko/Cat/smile normal/yukiko cat2 smile normal.png"
    image Yukiko cat3 smile normal = "sprites/Yukiko/Cat/smile normal/yukiko cat3 smile normal.png"
    image Yukiko cat1 smile sweet = "sprites/Yukiko/Cat/smile sweet/yukiko cat1 smile sweet.png"
    image Yukiko cat2 smile sweet = "sprites/Yukiko/Cat/smile sweet/yukiko cat2 smile sweet.png"
    image Yukiko cat3 smile sweet = "sprites/Yukiko/Cat/smile sweet/yukiko cat3 smile sweet.png"
    image Yukiko cat1 smile embarrassed = "sprites/Yukiko/Cat/smile embarrassed/yukiko cat1 smile embarrassed.png"
    image Yukiko cat2 smile embarrassed = "sprites/Yukiko/Cat/smile embarrassed/yukiko cat2 smile embarrassed.png"
    image Yukiko cat3 smile embarrassed = "sprites/Yukiko/Cat/smile embarrassed/yukiko cat3 smile embarrassed.png"
    image Yukiko cat1 smile vhappy = "sprites/Yukiko/Cat/smile vhappy/yukiko cat1 smile vhappy.png"
    image Yukiko cat2 smile vhappy = "sprites/Yukiko/Cat/smile vhappy/yukiko cat2 smile vhappy.png"
    image Yukiko cat3 smile vhappy = "sprites/Yukiko/Cat/smile vhappy/yukiko cat3 smile vhappy.png"
    image Yukiko cat1 speaking annoyed = "sprites/Yukiko/Cat/speaking annoyed/yukiko cat1 speaking annoyed.png"
    image Yukiko cat2 speaking annoyed = "sprites/Yukiko/Cat/speaking annoyed/yukiko cat2 speaking annoyed.png"
    image Yukiko cat3 speaking annoyed = "sprites/Yukiko/Cat/speaking annoyed/yukiko cat3 speaking annoyed.png"
    image Yukiko cat1 speaking questioning = "sprites/Yukiko/Cat/speaking questioning/yukiko cat1 speaking questioning.png"
    image Yukiko cat2 speaking questioning = "sprites/Yukiko/Cat/speaking questioning/yukiko cat2 speaking questioning.png"
    image Yukiko cat3 speaking questioning = "sprites/Yukiko/Cat/speaking questioning/yukiko cat3 speaking questioning.png"
    image Yukiko cat1 speaking serious = "sprites/Yukiko/Cat/speaking serious/yukiko cat1 speaking serious.png"
    image Yukiko cat2 speaking serious = "sprites/Yukiko/Cat/speaking serious/yukiko cat2 speaking serious.png"
    image Yukiko cat3 speaking serious = "sprites/Yukiko/Cat/speaking serious/yukiko cat3 speaking serious.png"
    image Yukiko cat1 speaking surprised = "sprites/Yukiko/Cat/speaking surprised/yukiko cat1 speaking surprised.png"
    image Yukiko cat2 speaking surprised = "sprites/Yukiko/Cat/speaking surprised/yukiko cat2 speaking surprised.png"
    image Yukiko cat3 speaking surprised = "sprites/Yukiko/Cat/speaking surprised/yukiko cat3 speaking surprised.png"
    image Yukiko cat1 upset = "sprites/Yukiko/Cat/upset/yukiko cat1 upset.png"
    image Yukiko cat2 upset = "sprites/Yukiko/Cat/upset/yukiko cat2 upset.png"
    image Yukiko cat3 upset = "sprites/Yukiko/Cat/upset/yukiko cat3 upset.png"
    #Uniform
    #pose1
    image Yukiko u poutyblush p1= "sprites/Yukiko/uniform/pose1/Yukiko u poutyblush p1.png"
    image Yukiko u pout p1= "sprites/Yukiko/uniform/pose1/Yukiko u pout p1.png"
    image Yukiko u smile confident p1 = "sprites/Yukiko/uniform/pose1/Yukiko u smile confident p1.png"
    image Yukiko u smile sweet p1= "sprites/Yukiko/uniform/pose1/Yukiko u smile sweet p1.png"
    image Yukiko u smile vhappy p1 = "sprites/Yukiko/uniform/pose1/Yukiko u smile vhappy p1.png"
    image Yukiko u smile happy p1 = "sprites/Yukiko/uniform/pose1/Yukiko u smile happy p1.png"
    image Yukiko u speaking annoyed p1= "sprites/Yukiko/uniform/pose1/Yukiko u speaking annoyed p1.png"
    image Yukiko u speaking questioning p1 = "sprites/Yukiko/uniform/pose1/Yukiko u speaking questioning p1.png"
    image Yukiko u speaking serious p1 = "sprites/Yukiko/uniform/pose1/Yukiko u speaking serious p1.png"
    image Yukiko u upset p1 = "sprites/Yukiko/uniform/pose1/Yukiko u upset p1.png"
    image Yukiko u speaking surprised p1 = "sprites/Yukiko/uniform/pose1/Yukiko u speaking surprised p1.png"
    #pose2
    image Yukiko u angry p2 = "sprites/Yukiko/uniform/pose2/Yukiko u angry p2.png"
    image Yukiko u curious p2 = "sprites/Yukiko/uniform/pose2/Yukiko u curious p2.png"###Need this expression for p1
    image Yukiko u frown p2 = "sprites/Yukiko/uniform/pose2/Yukiko u frown p2.png"
    image Yukiko u pout p2 = "sprites/Yukiko/uniform/pose2/Yukiko u pout p2.png"
    image Yukiko u poutyblush p2 = "sprites/Yukiko/uniform/pose2/Yukiko u poutyblush p2.png"
    image Yukiko u smile attitude p2 = "sprites/Yukiko/uniform/pose2/Yukiko u smile attitude p2.png"#####need this expression for p1
    image Yukiko u smile confident p2 = "sprites/Yukiko/uniform/pose2/Yukiko u smile confident p2.png"
    image Yukiko u smile embarrassed p2 = "sprites/Yukiko/uniform/pose2/Yukiko u smile embarrassed p2.png"
    image Yukiko u smile eyesclosed p2 = "sprites/Yukiko/uniform/pose2/Yukiko u smile eyesclosed p2.png"
    image Yukiko u smile happy p2 = "sprites/Yukiko/uniform/pose2/Yukiko u smile happy p2.png"
    image Yukiko u smile normal p2 = "sprites/Yukiko/uniform/pose2/Yukiko u smile normal p2.png"
    image Yukiko u smile vhappy p2 = "sprites/Yukiko/uniform/pose2/Yukiko u smile vhappy p2.png"
    image Yukiko u speaking annoyed p2 = "sprites/Yukiko/uniform/pose2/Yukiko u speaking annoyed p2.png"
    image Yukiko u speaking questioning p2 = "sprites/Yukiko/uniform/pose2/Yukiko u speaking questioning p2.png"
    image Yukiko u speaking serious p2 = "sprites/Yukiko/uniform/pose2/Yukiko u speaking serious p2.png"
    image Yukiko u speaking surprised p2 = "sprites/Yukiko/uniform/pose2/Yukiko u speaking surprised p2.png"
    image Yukiko u suspicious p2 = "sprites/Yukiko/uniform/pose2/Yukiko u suspicious p2.png"
    image Yukiko u upset p2 = "sprites/Yukiko/uniform/pose2/Yukiko u upset p2.png"
    #Izumi Sprites:
    image Izumi u confident = "sprites/Izumi/uniform/Izumi u confident.png"
    image Izumi u caring = "sprites/Izumi/uniform/Izumi u caring.png"
    image Izumi u frown = "sprites/Izumi/uniform/Izumi u frown.png"
    image Izumi u sad = "sprites/Izumi/uniform/Izumi u sad.png"
    image Izumi u speaking = "sprites/Izumi/uniform/Izumi u speaking.png"
    image Izumi u suspicious = "sprites/Izumi/uniform/Izumi u suspicious.png"
    image Izumi u nervous = "sprites/Izumi/uniform/Izumi u nervous.png"
    image Izumi u mad = "sprites/Izumi/uniform/Izumi u mad.png"
    #music initialization:
    define audio.delicate = "music/Delicate.mp3"
    define audio.izumitheme = "music/izumitheme.mp3"
    define audio.frozendream = "music/frozendream.mp3"
    define audio.Kaoritheme = "music/Kaoritheme.mp3"
    define audio.Suzukitheme = "music/baseballguy.mp3"
    define audio.SchoolCasual = "music/School Casual.mp3"
    define audio.Chalkboards = "music/Chalkboards.mp3"
    define audio.SugarMorning = "music/Sugar Morning.mp3"
    define audio.Sugawara = "music/SugawaraKS.mp3"
    define audio.Early = "music/early.mp3"
    define audio.Jazz = "music/Jazz.mp3"
    #Background initialization:
    image white = "backgrounds/white.png"
    image chapter screen_1 = "chapter screens/chapter_screen_1.png"
    image akari house day = "backgrounds/akari house day.png"
    image baseball field = "backgrounds/baseball field.png"
    image bridge below day = "backgrounds/bridge below day.png"
    image bridge below night = "backgrounds/bridge below night.png"
    image bridge sidewalk day = "backgrounds/bridge sidewalk day.png"
    image bridge sidewalk night = "backgrounds/bridge sidewalk night.png"
    image cafe inside = "backgrounds/cafe inside.png"
    image cafe outside = "backgrounds/cafe outside.png"
    image classroom empty = "backgrounds/classroom empty.png"
    image classroom = "backgrounds/classroom.png"
    image courtyard = "backgrounds/courtyard.png"
    image courtyard empty = "backgrounds/courtyard empty.png"
    image student council = "backgrounds/student council.png"
    image hallway 1 = "backgrounds/hallway 1.png"
    image hallway 1 empty = "backgrounds/hallway 1 empty.png"
    image hallway 2 = "backgrounds/hallway 2.png"
    image hallway 2 empty = "backgrounds/hallway 2 empty.png"
    image street day = "backgrounds/street day.png"
    image sky night = "backgrounds/sky night.png"
    image sky = "backgrounds/sky.png"
    image apartment day = "backgrounds/apartment day.png"
    image apartment night = "backgrounds/apartment night.png"

    #Logo Initialization:
    image logo = "logo.png"
    image sarchalenlogo = "sarchalenlogo.png"
    image pilogo = "pilogo.png"
    image wclogo = "wclogo.png"

    #CG Initialization:
    image CG Akari fruit happy = "CGs/CG Akari Fruit Happy.png"
    image CG Akari fruit annoyed = "CGs/CG Akari fruit annoyed.png"
    image CG Akari fruit questioning = "CGs/CG Akari fruit questioning.png"
    image CG Kaori Bridge = "CGs/CG Kaori Bridge.png"
    image CG Shizuka dark = "CGs/CG Shizuka dark.png"
    image CG kaori crash = "CGs/Kaori CG.png"
    image CG Yukiko Door Questioning = "CGs/CG Yukiko Door Questioning.png"
    image CG Yukiko Door Smile = "CGs/CG Yukiko Door Smile.png"
    image CG Izumi White = "CGs/CG Izumi White.png"

    #Some prefedined transforms:
    transform xflip:
     xzoom -1

    transform logodissolve:
        linear 1.0 zoom 1.0 ,
        ypos .6

    transform fromRight:
        subpixel True
        alpha 0.0 xalign 1.0 xanchor 0.0
        parallel:
            easein 1.0 alpha 1.0
        parallel:
            easein 1.0 xalign 0.5
        on hide:
            alpha 1 zoom 1 xanchor 0.5 yanchor 0.5
            block:
                linear 0.1 zoom 1.1
                linear 0.5 zoom 0

    transform bounce:
        yoffset 15
        easein .10 yoffset 0
        easeout .175 yoffset 15
#Changes the default "dissolve" speed from .5 to .2
define dissolve = Dissolve(0.3)


define config.say_attribute_transition = dissolve


label splashscreen:
    $ renpy.music.play(config.main_menu_music)
    scene black
    show text "{size=32}{font=font-classic.ttf}{color=#ffffff}SARCHALEN VISUAL MEDIA{/font}"
    $ renpy.pause(.8, hard = True)
    scene white
    show sky night:
        subpixel True xpos 0.4 ypos 1.0 xanchor 0.5 yanchor 1.0 zoom 1.55 rotate None
        parallel:
            xpos 0.5
            linear 14 xpos 0.7
        parallel:
            alpha 0.0
            linear 2 alpha 1.0
    #$ renpy.pause(2.0, hard = True)
    show sarchalenlogo at center with Dissolve(1.0):
        zoom 0.35
        yanchor .5
        ypos .5
    $ renpy.pause(2, hard=True)
    hide sarchalenlogo with Dissolve(1.0)
    show wclogo at center with dissolve:
        zoom 0.25
        yanchor .5
        ypos .5
    $ renpy.pause(1.5, hard=True)
    hide wclogo with Dissolve (1.0)
    $ renpy.pause(.5, hard=True)
    jump update

label update:
    $ UPDATE_URL = "http://sarchalen.com/sugawarachronicle/update/update.json"
    $ new_version = updater.UpdateVersion(url=UPDATE_URL, simulate=None)
    if new_version != None:
        $ updater.update(url=UPDATE_URL, base=None, force=False, public_key=None, simulate=None, add=[], restart=True)
    else:
        return
