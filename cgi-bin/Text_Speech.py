#!/usr/bin/env python3

import cgi
from gtts import gTTS
import os

print("Content-Type: text/html\n")

form = cgi.FieldStorage()
mytext = form.getvalue('text')

if mytext:
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("/var/www/html/welcome.mp3")
    print("MP3 file generated successfully.")
else:
    print("No text provided.")
