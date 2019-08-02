#!usr/bin/python
msg = """

Hello My name is ahmed ^_^

this is script admin panel *_-

[ python2 admin_panel.py (url) ]

or

[ bash install.sh ]

ok?

about me:

https://m.facebook.com/fox.benghazi
"""
def logo():
  print("""

                    _..-'(                       )`-.._
                   ./'. '||\\.       (\_/)       .//||` .`\.
                ./'.|'.'||||\\|..    )- -(    ..|//||||`.`|.`\.
             ./'..|'.|| |||||\`````` '`"'` ''''''/||||| ||.`|..`\.
           ./'.||'.|||| ||||||||||||.     .|||||||||||| |||||.`||.`\.
          /'|||'.|||||| ||||||||||||{     }|||||||||||| ||||||.`|||`\
         '.|||'.||||||| ||||||||||||{     }|||||||||||| |||||||.`|||.`
        '.||| ||||||||| |/'   ``\||``     ''||/''   `\| ||||||||| |||.`
        |/' \./'     `\./         \!|\   /|!/         \./'     `\./ `\|
        V    V         V          }' `\ /' `{          V         V    V
        `    `         `               V               '         '    '


##########################################################################

                    BY : Fox Benghazi ^_^
""")
#colors
blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'
try:
#library's
 from urllib2 import urlopen,URLError,HTTPError
 from sys import argv
 from os import system
except ModuleNotFoundError:
 print """
\033[33;1m
[ python2 admin_panel.py ]
\033[36;1m
or
\033[33;1m
[ bash install.sh ]

"""
try:
 url = argv[1]
except IndexError:
 print cyan
 print("""
 use:
  python2 admin_panel.py [url]
 ex:
  python2 admin_panel.py www.exploit.com
""")
 print red
line = open("wordlist.txt","r").readlines()
for file in line:
 file=file.strip()
 admin = url+"/"+str(file)
 try:
  urlopen(admin) # urllib2
  print green
  print admin
 except HTTPError,URLError:
  print red
  print admin