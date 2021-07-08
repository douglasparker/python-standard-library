import sys
from enum import Enum

def getOS():
    if(sys.platform == "aix"): return "AIX"
    elif(sys.platform == "linux"): return "Linux"
    elif(sys.platform == "win32"): return "Windows"
    elif(sys.platform == "cygwin"): return "Windows/Cygwin"
    elif(sys.platform == "darwin"): return "macOS"

class Prompt(Enum):
    Alert   = 1
    Confirm = 2
    List    = 3 # TO-DO
    Integer = 4
    Float   = 5

def prompt(output, prompt=Prompt.Alert):
    if(prompt == Prompt.Alert):
        output += " Press [Enter] to continue: "
        response = input(output)
        return True

    elif(prompt == Prompt.Confirm):
        output += " [Y/N]: "
        while(True):
            response = input(output)
            if(response in (None, "y", "n")):
                if(response == "y"):
                    return True
                elif(response == "n"):
                    return False
                break
            else:
                print("'" + response + "'" + " is not a valid response.")

    elif(prompt == Prompt.Integer):
        output += " [Integer]: "
        while(True):
            response = input(output)
            try:
                response = int(response)
                return response
            except:
                print("'" + response + "'" + " is not a valid response.")
    
    elif(prompt == Prompt.Float):
        output += " [Float]: "
        while(True):
            response = input(output)
            try:
                response = float(response)
                return response
            except:
                print("'" + response + "'" + " is not a valid response.")

