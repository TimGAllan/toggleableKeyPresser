import keyboard 
import time
import ctypes

# Function to Return True is Caps Lock is enabled.
def CAPSLOCK_STATE():
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)

# Function to Return True is Caps Lock is enabled.
def SCROLLLOCK_STATE():
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_SCROLL = 0x91
    return hllDll.GetKeyState(VK_SCROLL)

# Function to Return True is Caps Lock is enabled.
def NUMLOCK_STATE():
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_NUMLOCK = 0x90
    return hllDll.GetKeyState(VK_NUMLOCK)

def main():
    
    # Wait 3 seconds before starting
    time.sleep(3)
    timeLastPress = round(time.time() * 1000)
    print('Pressing Started')

    while True:
        
        # Calc how long ago the key was pressed
        timeSinceLastPress = round(time.time() * 1000) - timeLastPress

        # If Caplocks is enable and it's been at least 200 ms since last key press, press key.
        if CAPSLOCK_STATE() and timeSinceLastPress>200:
            keyboard.press_and_release('2')
            timeLastPress = round(time.time() * 1000)
            print(timeLastPress)

main()