import os
import threading
import subprocess
import sys
import time
from tkinter import messagebox
from pystray import Icon, MenuItem, Menu
from PIL import Image
from plyer import notification
import keyboard


notification.notify(
    title='EmRec Notification',
    message='EmRec is working in the Background!',
    app_name='EmRec',
    timeout=5
)


def run_camera_record():
    subprocess.Popen([sys.executable, 'camera-record.py'])


def run_screen_record():
    subprocess.Popen([sys.executable, 'screen-record.py'])


def show_selection_popup():
  result = messagebox.askquestion("EmRec Selection", "Please select your option:\nClick 'Yes' for Camera, 'No' for Screen.")
  if result == "yes":
      threading.Thread(target=run_camera_record(), daemon=True).start()
      
  else:
      threading.Thread(target=run_screen_record(), daemon=True).start()
  



def on_double_click(icon, item):
    subprocess.Popen([sys.executable, 'models/gui.py'])


def create_tray_icon():
    image = Image.open("icon.png")
    menu = Menu(
        MenuItem('Open', on_double_click),
        MenuItem('Quit', lambda icon, item: os._exit(0))
    )
    icon = Icon("EmRec", image, "EmRec - Emergency Recorder", menu)
    icon.run()


if __name__ == "__main__":
    icon_tray = threading.Thread(target=create_tray_icon, daemon=True)
    icon_tray.start()

    while True:
        if keyboard.is_pressed("F9"):
            show_selection_popup()
            time.sleep(1)  
        time.sleep(0.1)
