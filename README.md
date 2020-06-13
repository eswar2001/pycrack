# pycrack
Salt cracker in python  :smile:
![...](https://github.com/eswar2001/pycrack/blob/master/Capture.JPG)
### Note:
    It works in unix/linux systems only
### Requirements:
    python
    Dictonary File
### How to run?
    clone and open 
    run "python decrypt.py"
    enter the path for dictonary file and username_password file 
 
[Try to run in Repl](https://repl.it/repls/MammothFrivolousAdvance)



### GPU advantage
add "from numba import jit, cuda" near imports
add "@jit(target ="cuda")" above targetpass function
