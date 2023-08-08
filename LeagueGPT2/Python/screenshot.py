import time
from PIL import ImageGrab

def take_screenshot(file_name):
    height = 300
    width = 550
    x1 = 50
    y1 = ImageGrab.grab().height - height - 200

    x2 = x1 + width
    y2 = ImageGrab.grab().height - 200
    # Capture the screen region you want. Modify the coordinates as needed.
    # The coordinates (left, top, right, bottom) define a rectangular region.
    screen_region = (x1, y1, x2, y2)
    screenshot = ImageGrab.grab(bbox=screen_region)

    # Save the screenshot to a file with the provided name and format (e.g., PNG).
    screenshot.save(file_name)

# Set the time interval between each screenshot (in seconds).
time_interval = 1

# The number of screenshots you want to capture. Change it to the desired value.
num_screenshots = 3

for i in range(num_screenshots):
    # Generate a unique filename for each screenshot, e.g., screenshot_1.png, screenshot_2.png, etc.
    file_name = f"screenshot_{i + 1}.png"
    take_screenshot(file_name)
    time.sleep(time_interval)
