'''
MODULES
file containing code written by somebody else
PIP 
package manager of python used to install modules on system 
command 
python -m pip install (package/library)
python tells windows to start python engine , -m stands for module
'''
#pip install pyttsx3 pyjokes  this must be done in terminal 
import pyttsx3
import pyjokes as  tanish
print('pritning jokesl')
joke =tanish.get_joke()
print (joke) 
engine= pyttsx3.init()
engine.say("mikasa i have always hated you")
engine.runAndWait()


 