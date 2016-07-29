# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
init:
    image bg steamer = "bg_steamer.jpg"
    image bg whale ="bg_whale.jpg"
    image bg sinking ="bg_sinking.jpg"
    
    image transkribus blur="transkribus-blur.png"
    image clipping ="clipping.png"
    image diaryone ="diary-pg-1.png"
    image sunset ="sunset.jpg"
    image notebook ="notebook.png"

    image shawn full ="shawn.png"
    image shawn eyesright ="shawn_eyes_right.png"
    image shawn eyesfront mouthopen ="shawn_eyes_front_mouth_open.png"
    image shawn laugh = "shawn_laugh.png"

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

    play sound "23722__milo__ship2-bergen.ogg"

    scene bg steamer at Pan((100, 100), (1000, 1000), 20.0)
    with fade
    
    tl " Left New York in Cunard steamer Algeria."

    stop music

    scene bg whale with fade 
    play sound "seagulls_and_preacher.ogg"
    tl "Capt. read service on Sunday morning - in afternoon dead body of whale, white and shiny quite near us upon the water and hundreds of little birds upon it"
    
    scene bg sinking with fade
    tl "The second sunday morning suddenly a great wave rose ten feet above the deck "    
    tl "and came down upon it knocking down every one before it"
    tl  "and came down the gangway."

    show shawn full at left with dissolve

    sg "Oh, hey, hi. 'Scuse me."
    sg "You need to know what you're reading here."
    
    show shawn eyesright at left with dissolve
    
    sg "And what this is all about."

    menu:

        "Is it a game?":

            jump game

        "Are you telling a story?":

            jump story

label game:
     sg "It uses game mechanics to weave two interrelated stories."

     menu:

        "Hmmm.":

            jump notmuchgame

        "Ok. I want to read more of the diary.":

            jump diary_part_two


label story:
     show shawn full at center with dissolve
     sg "more or less"
     jump game
     
label diary_part_two:

     scene sunset with fade
     play sound "seagulls.ogg"
     tl "On Sunday night a woman in the steerage died of heart defects"
     tl "The following night she was buried at sea, the Capt. and Dr. being present."

     show shawn full at left with dissolve
     sg "This was when the diary had fully gripped me."
     sg "Already, by the first page, we'd had a rogue wave,"
     sg "a dead whale,"
     sg "and a burial at sea."

     show shawn eyesfront mouthopen at left 
     sg "I've just finished transcribing her adventures in Italy;"
     sg "Soon we'll be getting to Egypt!"
     
     menu:
          "Ok, I've had enough.":
               jump theend
          "Let me see how much you've transcribed.":
               jump notebook

label notebook:
     scene notebook with dissolve
     show shawn eyesright at left with dissolve
     sg "This is my open notebook."
     show shawn laugh at left with dissolve
     sg "People think I'm ...odd for having one."
     
     sg "But you can see where I'm at if you go there."
     sg "smgprojects.github.io"

     jump theend

label notmuchgame:
     scene black
     with dissolve

     sg "This is just me still working through how this platform works."
     show shawn full at right with dissolve 
     sg "the idea is that you'll get the story of the Nile Diary"
     sg "but also get 4th-wall breaks that explain what I'm trying to achieve."
    
     jump theend 
    

label theend:     
     scene transkribus blur
     with dissolve
     play sound "331375__xanco123__mysterious-event-music-01.ogg"
     sg "I will show you how my research on the diary is done,"
     sg "the choices I made, the tech I've used, and pointers to further info, etc"
     
     scene splash
     sg "so stay tuned..."

return
