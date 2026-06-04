import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

engine.say('''Hello everyone, today I am going to present a small Python project based on the `pyttsx3` module.
This module is used for text-to-speech conversion. It helps the computer speak the text written inside the program.

First, we import the `pyttsx3` library in Python.
Then we initialize the speech engine using the `init()` method.
After that, we write the text which we want the computer to speak.

In this project, the computer greets the user by saying:
“Hello Ankita, welcome to Python programming.”

We can also control the speed and volume of the voice.
One important advantage of `pyttsx3` is that it works offline, so internet connection is not required.

This project is simple, beginner-friendly, and useful for learning Python modules and automation concepts.
It can also be used in voice assistants, announcement systems, and accessibility applications.

Thank you.
''')
engine.runAndWait()

print("Voice executed")