from pynput.mouse import Controller, Button
from pynput.keyboard import Key, Controller as KeyboardController
import time

# Initialize mouse and keyboard controllers
mouse = Controller()
keyboard = KeyboardController()
delay = 0.18

#_______________________________________________________________________________________________________________________________________

def show_desktop():
    """
    Minimizes all applications by pressing the Windows key + 'D'.
    This simulates the "Show Desktop" functionality.
    """
    time.sleep(1.8)
    with keyboard.pressed(Key.cmd):  # Using 'with' for better resource management
        time.sleep(delay)
        keyboard.press('d')
        keyboard.release('d')

#_______________________________________________________________________________________________________________________________________

def sleep(duration):
    """
    Pauses the execution for the specified duration.

    Args:
        duration (float): Time in seconds to pause the execution.
    """
    time.sleep(duration)

#_______________________________________________________________________________________________________________________________________

def open_browser(browser_name="Microsoft Edge"):
    """
    Opens the specified browser using the Windows search functionality.

    Args:
        browser_name (str): Name of the browser to open (default is "Microsoft Edge").
    """
    with keyboard.pressed(Key.cmd):
        pass  # Simulates pressing and releasing the Windows key
    sleep(delay)
    keyboard.type(browser_name)
    sleep(delay)
    with keyboard.pressed(Key.enter):
        pass  # Simulates pressing and releasing the Enter key
    sleep(delay + 2.7)

#_______________________________________________________________________________________________________________________________________

def open_new_tab():
    """
    Opens a new tab in the browser by simulating the Ctrl + 'T' key combination.
    """
    with keyboard.pressed(Key.ctrl):
        keyboard.press('t')
        keyboard.release('t')

#_______________________________________________________________________________________________________________________________________

def maximize_window():
    """
    Maximizes the current window using the Windows key + Up Arrow key combination.
    """
    with keyboard.pressed(Key.cmd):
        keyboard.press(Key.up)
        keyboard.release(Key.up)

#_______________________________________________________________________________________________________________________________________


def navigate_to_website(url="https://popcat.click/"):
    """
    Navigates to the specified website by typing the URL and pressing Enter.

    Args:
        url (str): URL of the website to navigate to (default is "https://popcat.click/").
    """
    keyboard.type(url)
    sleep(delay)
    with keyboard.pressed(Key.enter):
        pass  # Simulates pressing and releasing the Enter key
    sleep(delay + 1.8)

#_______________________________________________________________________________________________________________________________________

def click_until_termination():
    """
    Continuously clicks the mouse at the current position until the mouse is moved to the top-left corner (0, 0).

    To terminate the program, move the mouse pointer to the top-left corner of the screen (coordinate 0, 0).
    """
    mouse.position = (855, 428)  # Coordinates to center of the screen (adjust for your screen resolution)
    while mouse.position != (0, 0):
        time.sleep(delay - 0.1)
        mouse.press(Button.left)
        mouse.release(Button.left)
#_______________________________________________________________________________________________________________________________________

def main():
    # Main execution block
    try:
        sleep(delay)
        show_desktop()
        sleep(delay + 1.8)

        # Step 1: Open the browser
        open_browser()

        # Step 2: Open a new tab
        open_new_tab()

        # Step 3: Maximize the browser window
        maximize_window()

        # Step 4: Navigate to the website
        navigate_to_website()

        # Step 5: Perform continuous clicks until termination
        click_until_termination()

    except Exception as e:
        print(f"An error occurred: {e}")
        exit()
#_______________________________________________________________________________________________________________________________________

# Run the program
if __name__ == "__main__":
    main()