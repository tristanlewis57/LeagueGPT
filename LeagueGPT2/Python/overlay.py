import sys
import os
import atexit
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

def read_message_text(file_path):
    with open(file_path, "r") as file:
        message_text = file.read().strip()
    return message_text

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, overlay):
        super().__init__()
        self.overlay = overlay

    def on_modified(self, event):
        if event.src_path.endswith("response.txt"):
            message_text = read_message_text("response.txt")
            self.overlay.central_widget.setText(message_text)
            self.overlay.adjustSize()

def remove_lock_file(lock_file_path):
    if os.path.exists(lock_file_path):
        os.remove(lock_file_path)

def main():
    # Check if the lock file exists
    lock_file_path = "overlay.lock"
    if os.path.exists(lock_file_path):
        print("An instance of the script is already running.")
        return

    # Create the lock file
    with open(lock_file_path, "w") as lock_file:
        lock_file.write("locked")

    # Register the function to remove the lock file when the script exits
    atexit.register(remove_lock_file, lock_file_path)

    app = QApplication(sys.argv)

    # Create a transparent overlay window
    overlay = QMainWindow()
    overlay.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
    overlay.setAttribute(Qt.WA_TranslucentBackground)
    overlay.setStyleSheet("background-color: transparent; color: white; font-size: 18px;")

    # Read the initial message text from response.txt
    message_text = read_message_text("response.txt")

    # Create a central widget for the overlay window
    central_widget = QLabel(message_text, overlay)
    central_widget.setAlignment(Qt.AlignTop | Qt.AlignLeft)
    overlay.setCentralWidget(central_widget)
    overlay.central_widget = central_widget

    # Move the overlay to the top-left corner of the screen
    overlay.move(20, 20)

    # Show the overlay window
    overlay.show()

    # Start the file change handler to monitor response.txt changes
    event_handler = FileChangeHandler(overlay)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()

    try:
        # Start the event loop
        sys.exit(app.exec_())

    finally:
        # Stop the file change observer and remove the lock file when the script finishes or encounters an error
        observer.stop()
        observer.join()

        if os.path.exists(lock_file_path):
            os.remove(lock_file_path)

if __name__ == "__main__":
    main()
