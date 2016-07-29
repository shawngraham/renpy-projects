''' twine2rpy is for storyboarding/testing Ren'py scripts in Twine and converting the Twine source file to .rpy. 
Converts PassageTitle to label, internalLinks to jump, <<display>> to call, <<choice>> to jump, <<set>>, <<print>>, and if blocks. 
Doesn't convert multiple variable assignment or multiple conditions (using ;) or ternary operators.
From the command line: twine2rpy.py source.txt '''
        
import sys 
twine_operators = {	"eq":"==", "neq":"!=", "gt":">", "gte":">=", "lt":"<", "lte":"<=", "true":"True", "false":"False" } 
 
def set_call(line, spacing):
    start_title = line.find('"')
    end_title = line.rfind('"')
    return ("    " * spacing) + "call " + line[start_title+1:end_title].replace(" ", "_").lower() + "\n"
 
def set_label(line):
    line = line[2:].lower().rstrip().lstrip()
    if line == "init" or line == "init python" or "screen" in line:
        return "\n" + line + ":\n"
    else:
        return "\nlabel " + line.replace(" ", "_") + ":\n" 
    
def set_jump(line, spacing):
    title_end = line.find("]]")
    if "|" in line:
        title_start = line.find("|")        
        title = line[title_start+1:title_end]
    else:
        title_start = line.find("[[")
        title = line[title_start+2:title_end]
    return ("    " * spacing) + "jump " + title.replace(" ", "_").lower() + "\n"
    
def choice_macro(line, spacing):
    label_start = line.find('"')
    label_end = line.rfind('"')
    return ("    " * spacing) + "jump " + line[label_start+1:label_end].replace(" ", "_").lower() + "\n"

def set_variable(line, spacing):
    line_start = line.find("$")
    line_end = line.find(">")
    return ("    " * spacing) + "$ " + line[line_start+1:line_end] + "\n"
    
def interpolate(line, spacing):
    line = line.rstrip().lstrip()
    var_start = line.find("$")
    var_end = line.find(">")
    start_bracket = line.find("<")
    line_start = line[:start_bracket-1]
    return ("    " * spacing) + line_start + " [" + line[var_start+1:var_end] + "]" + line[var_end+2:] + "\n" 

def if_block(line, spacing):
    global in_if_block
    if "<<if" in line:   
        in_if_block = True
        if_start = line.find("$")
        if_end = line.rfind(">")
        for k, v in twine_operators.iteritems():
            if k in line:
                line = line.replace(k, v)       
        if "else" in line: # nested if (elif)
            return ("    " * (spacing-1)) + "elif " + line[if_start+1:if_end-1] + ":" + "\n"             
        else:               
            return ("    " * spacing) + "if " + line[if_start+1:if_end -1] + ":" + "\n"    
    elif "<<endif" in line:
        in_if_block = False
        return ""     
    else: 
        return ("    " * (spacing-1)) + "else:" + "\n"
    
def check_spacing(line):
    spaces = (len(line) - len(line.lstrip()))+1
    return spaces

def convert(txt_file):
    global rpy_file
    for item in txt_file.split("\n"):
        if item:
            spacing = check_spacing(item)
            if in_if_block:
                spacing+=1
            if "::" in item:
                new_line = set_label(item)
            elif "[[" in item:
                new_line = set_jump(item, spacing)
            elif "<<display" in item:
                new_line = set_call(item, spacing)
            elif "<<choice" in item:
                new_line = choice_macro(item, spacing)
            elif "<<set" in item:
                new_line = set_variable(item, spacing)
            elif "<<if" in item or "<<else" in item or "<<endif" in item:
                new_line = if_block(item, spacing)  
            elif "<<print" in item:
                new_line = interpolate(item, spacing)
            else:
                item = item.lstrip().rstrip()
                new_line = ("    " * spacing) + item + "\n"
            rpy_file.write(new_line)
    return
    
# for if block tracking
in_if_block = False    
    
# Open Twine source file  
file_name = sys.argv[1]
open_file = open(file_name)
txt_file = open_file.read() 

# Create .rpy file with same name
renpy_file = file_name[:file_name.find(".")].rstrip() + ".rpy"
rpy_file = open(renpy_file, "w")
convert(txt_file)   
open_file.close()
rpy_file.close()