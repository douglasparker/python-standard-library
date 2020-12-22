import sys

def getOS():
    if(sys.platform == "aix"): return "AIX"
    elif(sys.platform == "linux"): return "Linux"
    elif(sys.platform == "win32"): return "Windows"
    elif(sys.platform == "cygwin"): return "Windows/Cygwin"
    elif(sys.platform == "darwin"): return "macOS"