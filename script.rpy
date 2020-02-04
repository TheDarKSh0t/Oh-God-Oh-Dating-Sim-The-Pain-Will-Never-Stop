define S = Character("Shinobu")
define Thot1 = Character("Girl")
define Thot2 = Character("Girl2")
define A = Character("Authur")
label start:
    scene pic1
    pause
    Thot1 " Hey there hot stuff what's your name"
    $ Ss = renpy.input("My Name is")
    if Ss == "":
        "Thats not right"
    Thot1 "Hello there [Ss]"
    Thot2 "Well here we’ll call you daddy"
    Ss "well if you want to I won’t-"
    A "Rise and shine you sexually repressed fuck"
    Ss "What"
    A"You have work don’t you?"
    Ss"Right but was that really needed"
    A"Ya, you should get dressed I’ve cooked breakfast already"
return
