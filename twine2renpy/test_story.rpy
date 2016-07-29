
init:
    define e = Character("Eileen")

init python:
    pass

label start:
    e "This is a test story for twine2rpy."
    e "The purpose of this script is to allow developers to use Twine for storyboarding and basic prototyping, taking advantage of the visual node links between internalLinks and choice macros, and then easily transfer to a .rpy file."
    e "To get the source code for your .tws file, go to File > Export Source Code... to create a source .txt file."
    e "Here's an internalLink."
    jump test_link

label test_link:
    e "Here's a choice menu. You will need to indent your menus with tabs as usual."
    menu:
        "Option 1":
            jump option_1
        "Option 2":
            jump option_2
        "Option 3":
            jump option_3

label option_2:
    $ option = 2
    e "So you picked option 2!  That's fine."
    call last_passage
    return

label option_3:
    $ option = 3
    e "So you picked option 3.  All right."
    call last_passage
    return

label option_1:
    $ option = 1
    e "So you picked option 1.  Okay then."
    call last_passage
    return

label last_passage:
    e "Here's an example of an if block. Place if, else, and endif statements on separate lines, just as you would in Python."
    e "Twine does not have an elif statement, but you can use nested if statements, which will be properly converted into an if/elif/else block in the .rpy."
        
    if option == 1:
        e "You picked Option 1, didn't you?"
    elif option == 2:
        e "You picked option 2, didn't you?"
    else:
        e "I guess you picked 3!"
        
    e "I can also interpolate your choice: option [option]."
        
    e "However, multiple assignment and multiple conditions separated by ';' or ternary operators is not converted."
        
    e "And that's the end of the demo."
    return
