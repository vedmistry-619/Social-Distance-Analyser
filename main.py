
import tkinter as tk
import tkinter.ttk as ttk
import threading

import lib.main_menu as main_menu


class FrameSwitcher(tk.Tk):
    def __init__(self):
        
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(main_menu.MainMenuWindow, None)  # Direct Main menu for debugging purpose
        # Setting Login Window to load first

    def switch_frame(self, frame_class, bg_frame):
        """Destroys current frame and replaces it with a new one."""    
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
            bg_frame.destroy()
            # Useful in Logout scenario
            # Enabling Login window resize and resizing master window to login window size then disabling resizing
        
                
        self._frame = new_frame
        self._frame.pack()


if __name__ == "__main__":
    app = FrameSwitcher()
    app.mainloop()