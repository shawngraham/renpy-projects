# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
init:
    image bg steamer = "bg_steamer.jpg"
    image bg whale ="bg_whale.jpg"
    image bg sinking ="bg_sinking.jpg"
    
    image transkribus blur="transkribus-blur.png"
    image clipping ="clipping.png"
    image diaryone ="diary-pg-1.png"

    image shawn full ="shawn.png"
    image shawn eyesright = "shawn_eyes_right.png"

# Declare characters used by this game.
define tl = Character('The Lady', color="#c8ffc8")
define sg = Character('Shawn', color="#c8c8ff")


#splash
image splash = "Nile Temple.jpg"

label splashscreen:
    scene black 
    with Pause(1)
    
    play sound "331375__xanco123__mysterious-event-music-01.ogg"

    show splash with dissolve
    with Pause(5)
    
    scene black with dissolve
    with Pause(2)

    show text "Shawn Graham @electricarchaeo"
    with Pause (2)

    return

# The game starts here.
label start:

    scene black
    with dissolve

    "The diary had been scanned and uploaded to the university library website."

    show clipping with fade
    "They'd even scanned a clipping they'd found inside."
    "Didn't look like anyone had bothered much with it."
    
    show diaryone
    "I opened it up, and began reading."

    stop music

    play music "23722__milo__ship2-bergen.ogg"

    scene bg steamer at Pan((100, 100), (1000, 1000), 20.0)
    with fade
    
    tl " Left New York in Cunard steamer Algeria."

    stop music

    scene bg whale with fade 
    tl "Capt. read service on Sunday morning - in afternoon dead body of whale, white and shiny quite near us upon the water and hundreds of little birds upon it"
    
    scene bg sinking with fade
    tl "The second sunday morning suddenly a great wave rose ten feet above the deck "    
    tl "and came down upon it knocking down every one before it"
    tl  "and came down the gangway."

    show shawn full at left with dissolve

    sg "Wait. Wait."
    sg "You need to know what you're reading here."
    
    show shawn eyesright at left with dissolve
    
    sg "And what this is all about."

    menu:

        "Is it a game?":

            jump game

        "Are you telling a story?":

            jump story

label game:
     sg "yep"

     menu:

        "Not much of a game, is it.":

            jump notmuchgame

label story:
     show shawn full at center with dissolve
     sg "more or less"
    
label notmuchgame:
     scene black
     with dissolve

     sg "well, hang on, ok?"
     sg "this is just me still working through how this platform works."
     show shawn full at right with dissolve 
     sg "the idea is that you'll get the story of the Nile Diary"
     sg "but also get 4th-wall breaks that explain what I'm trying to achieve."
     
     scene transkribus blur
     with dissolve
     
     sg "I will show you how my research on the diary is done,"
     sg "the choices I made, the tech I've used, and pointers to further info, etc"
     
     scene splash
     sg "so stay tuned..."

     return
