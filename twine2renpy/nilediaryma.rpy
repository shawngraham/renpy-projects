
label �::_init:
    define tl = Character('The Lady', color="#c8ffc8")
    define sg = Character('Shawn', color="#c8c8ff")

init python:
    pass

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
    jump first_choice

label first_choice:
    menu:
                                    "Is it a game?":
                                                    jump game
                                    "Are you telling a story?":
                                                    jump story

label story:
    show shawn full at center with dissolve
                        sg "more or less, a story of interleaved discovery."
                        call game

label game:
    sg "It uses game mechanics to weave two interrelated stories."
                        menu:
                                    "Hmmm, you say doubtfully.":
                                                    jump notmuchgame
                                    "Ok. I want to read more of the diary.":
                                                    jump diary_part_two

label diary_part_two:
                        scene sunset with fade
                        tl "On Sunday night a woman in the steerage died of heart defects"
                        tl "The following night she was buried at sea, the Capt. and Dr. being present."
                        show shawn full at left with dissolve
                        sg "This was when the diary had fully gripped me."
                        sg "Already, by the first page, we'd had a rogue wave,"
                        sg "a dead whale,"
                        sg "and a burial at sea."
                        show shawn eyesfront mouthopen at left
                        sg "I've just finished transcribing her adventures in Italy;"
                        sg "Soon we'll be getting to Egypt."

label notmuchgame:
                        scene black
                        with dissolve
                        sg "hang on, ok?"
                        sg "this is just me still working through how this platform works."
                        show shawn full at right with dissolve
                        sg "the idea is that you'll get the story of the Nile Diary"
                        sg "but also get 4th-wall breaks that explain what I'm trying to achieve."
                        
    call the_end

label the_end:
                        scene transkribus blur
                        with dissolve
                        
                        sg "I will show you how my research on the diary is done,"
                        sg "the choices I made, the tech I've used, and pointers to further info, etc"
                        
                        scene splash
                        sg "so stay tuned..."
                        return
