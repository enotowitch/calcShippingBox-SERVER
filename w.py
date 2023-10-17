# watcher.py
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".py"):
            print(f"Changes detected in {event.src_path}. Restarting...")
            subprocess.run(["python", "main.py"])

observer = Observer()
observer.schedule(MyHandler(), path=".", recursive=True)
observer.start()

try:
    observer.join()
except KeyboardInterrupt:
    observer.stop()
observer.join()
