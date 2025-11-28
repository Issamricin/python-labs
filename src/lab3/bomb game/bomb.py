"""
A library to animate a bomb in the terminal

ASCII art from ASCII Art Archive:

    https://www.asciiart.eu/weapons/explosives

ANSI escape to blur the animation from:

    https://gist.github.com/pfreixes/a911dd6e17aca6bcc6a2
"""

import time
import sys

def detonate():
    """This function detonates the bomb"""
    oignited()
    time.sleep(0.5)
    erase()

    ignited()
    time.sleep(0.5)

    for n in range(7):
        erase()
        explode(n)

    sys.exit(1)

def erase():
    """Erase 11 lines"""
    for n in range(11):
        print("\033[K", end="")
        print("\033[1A", end="")

def oignited():
    """Prints an unlit dynamite"""
    print("""



      )
     (
    .-`-.
    :   :
    :TNT:
    :___:
          """)

def ignited():
    """Prints an ignited dynamite"""
    print("""



    \|/
   - o -
    /-`-.
    :   :
    :TNT:
    :___:
          """)

def explode(n):
    """Prints step n in the explosion sequence, 0 <= n <= 5."""
    if n == 0:
        print("""





    .---.
    : | :
    :-o-:
    :_|_:
""")
        time.sleep(0.1)
    elif n == 1:
        print("""





    .---.
    (\|/)
    --0--
    (/|\)
""")
        time.sleep(0.1)
    elif n == 2:
        print("""




   '.\|/.'
   (\   /)
   - -O- -
   (/   \)
   ,'/|\'.
""")
        time.sleep(0.1)
    elif n == 3:
        print("""





'.  \ | /  ,'
  `. `.' ,'
 ( .`.|,' .)
 - ~ -0- ~ -
""")
        time.sleep(0.1)
    elif n == 4:
        print("""


','|'.` )
  .' .'. '.
,'  / | \  '.
    \ '  "  
 ` . `.' ,'
 . `` ,'. "
   ~ (   ~ -
""")
        time.sleep(0.1)
    elif n == 5:
        print("""
. ','|` ` .
  .'  "  '
,   ' , '  `

   (  ) (
    ) ( )
    (  )
     ) /
    ,---.
""")
        time.sleep(0.5)
    elif n == 6:
        print("""








   ,--.
""")
