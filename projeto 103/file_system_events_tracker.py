import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/apple/Documents/Tracker"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Criado: {event.src_path}")

    def on_modified(self, event):
        print(f"Modificado: {event.src_path}")

    def on_moved(self, event):
        print(f"Movido: {event.src_path}")

    def on_deleted(self, event):
        print(f"Excluido: {event.src_path}")


observer = Observer()
observer.schedule(FileEventHandler(), from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
