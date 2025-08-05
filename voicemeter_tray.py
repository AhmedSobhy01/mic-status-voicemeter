import time
import threading
from pystray import Icon, MenuItem
from PIL import Image
import voicemeeter
import os
import sys

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class B2Tray:
    def __init__(self):
        self.ico_unmuted  = Image.open(resource_path("unmuted.png"))
        self.ico_muted    = Image.open(resource_path("muted.png"))
        self.ico_notfound = Image.open(resource_path("notfound.png"))

        self.icon = Icon(
            "VM B2",
            self.ico_notfound,
            "Voicemeeter not found",
            menu=(MenuItem("Exit", self.stop),)
        )

        self._last_muted = None
        self._vmr        = None
        self._running    = True

    def _ensure_connected(self):
        if self._vmr is None:
            try:
                # voicemeeter.launch("banana")
        
                # hwnd = win32gui.FindWindow(None, "Voicemeeter Banana")
                # if hwnd:
                #     win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

                self._vmr = voicemeeter.remote("banana")
                self._vmr.login()
            except Exception:
                return False
        return True

    def _update_loop(self):
        while self._running:
            if not self._ensure_connected():
                time.sleep(1)
                continue

            try:
                muted = self._vmr.outputs[4].mute
            except Exception:
                if self.icon.icon is not self.ico_notfound:
                    self.icon.icon  = self.ico_notfound
                    self.icon.title = "Voicemeeter not found"
                self._vmr = None
                self._last_muted = None
                continue

            if muted != self._last_muted:
                self.icon.icon  = self.ico_muted   if muted else self.ico_unmuted
                self.icon.title = f"Voicemeeter B2 is {'MUTED' if muted else 'UNMUTED'}"
                self._last_muted = muted

            time.sleep(0.1)

    def run(self):
        threading.Thread(target=self._update_loop, daemon=True).start()
        self.icon.run()

    def stop(self, icon, item):
        self._running = False
        self.icon.stop()
        if self._vmr:
            try:   self._vmr.logout()
            except: pass

if __name__ == "__main__":
    B2Tray().run()
