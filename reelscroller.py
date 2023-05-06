import pyautogui
import time
import keyboard

# Define the duration of the swipe gesture in seconds
swipe_duration = 1

# Define the start and end points of the swipe gesture
start_x, start_y = pyautogui.size()[0] / 2, pyautogui.size()[1] * 0.9
end_x, end_y = pyautogui.size()[0] / 2, pyautogui.size()[1] * 0.1

# Define a variable to keep track of whether the script is running or paused
running = False

def start():
    global running
    running = True
    print("Script started")

def stop():
    global running
    running = False
    print("Script paused")

# Register the start() and stop() functions to be called when the spacebar is pressed
keyboard.add_hotkey("space", start)
keyboard.add_hotkey("space", stop, suppress=True)

while True:
    if running:
        # Perform the swipe gesture from the bottom to the top of the screen
        pyautogui.moveTo(start_x, start_y)
        pyautogui.mouseDown()
        pyautogui.moveTo(end_x, end_y, duration=swipe_duration)
        pyautogui.mouseUp()

        # Pause the loop for 30 seconds
        time.sleep(30)
    else:
        # If the script is paused, sleep for 0.1 seconds to reduce CPU usage
        time.sleep(0.1)
