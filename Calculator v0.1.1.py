import customtkinter as ctk
import threading
import time
from typing import Optional, Union

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

global state
state: str = "off"
global thread
thread: Optional[threading.Thread] = None
global colorTheme
colorTheme: str = "dark-blue"

class Root(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Calculator")
        self.geometry("350x450")
        self.resizable(False, False)
        self.mainFrame: Optional[MainFrame] = None
        self.settingsFrame: Optional[SettingsFrame] = None
        self.initUi()

    def initUi(self) -> None:
        self.mainFrame = MainFrame(parent=self)
        self.mainFrame.pack(expand=True, fill="both", padx=5, pady=5)

    def changeWindow(self, window: str) -> None:
        if window == "Settings":
            if self.mainFrame:
                self.mainFrame.pack_forget()
            self.settingsFrame = SettingsFrame(parent=self)
            self.settingsFrame.pack(expand=True, fill="both", padx=5, pady=5)
        elif window == "Main":
            if self.settingsFrame:
                self.settingsFrame.pack_forget()
            self.mainFrame = MainFrame(parent=self)
            self.mainFrame.pack(expand=True, fill="both", padx=5, pady=5)

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent: Root) -> None:
        super().__init__(parent)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.inputOutputEntry: ctk.CTkEntry = ctk.CTkEntry(
            self, font=("Arial", 20), placeholder_text="0", state="disabled"
        )
        self.inputOutputEntry.grid(
            row=0, column=0, columnspan=4, sticky="nsew", padx=3, pady=3
        )

        self.createButtons()

    def createButtons(self) -> None:
        buttons = [
            ("Settings", self.settingButtonEventHandler, 1, 0),
            ("/", self.divisionButtonEventHandler, 1, 1),
            ("*", self.multiplicationButtonEventHandler, 1, 2),
            ("Clear", self.clearButtonEventHandler, 1, 3),
            ("7", self.sevenButtonEventHandler, 2, 0),
            ("8", self.eightButtonEventHandler, 2, 1),
            ("9", self.nineButtonEventHandler, 2, 2),
            ("+", self.additionButtonEventHandler, 2, 3),
            ("4", self.fourButtonEventHandler, 3, 0),
            ("5", self.fiveButtonEventHandler, 3, 1),
            ("6", self.sixButtonEventHandler, 3, 2),
            ("-", self.subtractionButtonEventHandler, 3, 3),
            ("1", self.oneButtonEventHandler, 4, 0),
            ("2", self.twoButtonEventHandler, 4, 1),
            ("3", self.threeButtonEventHandler, 4, 2),
            ("=", self.equalButtonEventHandler, 4, 3, 2),
            ("0", self.zeroButtonEventHandler, 5, 0, 1, 2),
            (".", self.dotButtonEventHandler, 5, 2),
        ]

        for button in buttons:
            text, command, row, col = button[:4]
            rowspan = button[4] if len(button) > 4 else 1
            colspan = button[5] if len(button) > 5 else 1
            ctk.CTkButton(self, text=text, command=command).grid(
                row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew", padx=3, pady=3
            )

    def insertChar(self, char: str) -> None:
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", char)
        self.inputOutputEntry.configure(state="disabled")

    def divisionButtonEventHandler(self) -> None:
        self.insertChar("/")

    def multiplicationButtonEventHandler(self) -> None:
        self.insertChar("*")

    def sevenButtonEventHandler(self) -> None:
        self.insertChar("7")

    def eightButtonEventHandler(self) -> None:
        self.insertChar("8")

    def nineButtonEventHandler(self) -> None:
        self.insertChar("9")

    def additionButtonEventHandler(self) -> None:
        self.insertChar("+")

    def fourButtonEventHandler(self) -> None:
        self.insertChar("4")

    def fiveButtonEventHandler(self) -> None:
        self.insertChar("5")

    def sixButtonEventHandler(self) -> None:
        self.insertChar("6")

    def subtractionButtonEventHandler(self) -> None:
        self.insertChar("-")

    def oneButtonEventHandler(self) -> None:
        self.insertChar("1")

    def twoButtonEventHandler(self) -> None:
        self.insertChar("2")

    def threeButtonEventHandler(self) -> None:
        self.insertChar("3")

    def zeroButtonEventHandler(self) -> None:
        self.insertChar("0")

    def dotButtonEventHandler(self) -> None:
        self.insertChar(".")

    def settingButtonEventHandler(self) -> None:
        self.master.changeWindow("Settings")  # type: ignore

    def clearButtonEventHandler(self) -> None:
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.delete(0, "end")
        self.inputOutputEntry.configure(state="disabled")

    def equalButtonEventHandler(self) -> None:
        op = self.inputOutputEntry.get()
        try:
            ans = eval(op)
            self.inputOutputEntry.configure(state="normal")
            self.inputOutputEntry.delete(0, "end")
            self.inputOutputEntry.insert("end", str(ans))
            self.inputOutputEntry.configure(state="disabled")
        except:
            self.inputOutputEntry.configure(state="normal")
            self.inputOutputEntry.delete(0, "end")
            self.inputOutputEntry.insert("end", "Error")
            self.inputOutputEntry.configure(state="disabled")

class SettingsFrame(ctk.CTkFrame):
    def __init__(self, parent: Root) -> None:
        super().__init__(parent)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.initUi()

    def initUi(self) -> None:
        ctk.CTkLabel(self, text="Settings", font=("Arial", 20), anchor="center").grid(
            row=0, column=0, columnspan=2, sticky="nw", padx=15, pady=15
        )

        ctk.CTkLabel(self, text="Appearance Mode:", font=("Arial", 15), anchor="center").grid(
            row=1, column=0, columnspan=3, sticky="sw", padx=15, pady=15
        )

        ctk.CTkLabel(self, text="Dark Mode").grid(
            row=2, column=0, columnspan=1, sticky="new", padx=15, pady=15
        )

        self.switchValue = ctk.StringVar(value=ctk.get_appearance_mode().lower())
        self.darkLightModeSwitch = ctk.CTkSwitch(
            self,
            text="",
            variable=self.switchValue,
            offvalue="dark",
            onvalue="light",
            command=self.darkLightModeSwitchEventHandler,
        )
        self.darkLightModeSwitch.grid(
            row=2, column=1, columnspan=1, sticky="new", padx=15, pady=15
        )

        ctk.CTkLabel(self, text="Light Mode").grid(
            row=2, column=2, columnspan=1, sticky="new", padx=15, pady=15
        )

        ctk.CTkLabel(self, text="Color Theme:", font=("Arial", 15), anchor="center").grid(
            row=3, column=0, columnspan=3, sticky="sw", padx=15, pady=15
        )

        self.colorTheme = ctk.StringVar(value=colorTheme)

        themes = [("Dark Blue", "dark-blue"), ("Blue", "blue"), ("Green", "green")]
        for i, (text, value) in enumerate(themes):
            ctk.CTkRadioButton(
                self,
                text=text,
                value=value,
                variable=self.colorTheme,
                command=self.colorThemeRadioButtonsEventHandler,
            ).grid(row=4, column=i, columnspan=1, sticky="new", padx=15, pady=15)

        ctk.CTkButton(self, text="Back", command=self.backButtonEventHandler).grid(
            row=5, column=0, columnspan=3, sticky="sew", padx=15, pady=15
        )

    def darkLightModeSwitchEventHandler(self) -> None:
        value = self.switchValue.get()
        global state
        state = "on" if value == "light" else "off"
        ctk.set_appearance_mode(value)

    def colorThemeRadioButtonsEventHandler(self) -> None:
        theme = self.colorTheme.get()
        global colorTheme
        colorTheme = theme
        ctk.set_default_color_theme(theme)
        self.master.destroy()  # type: ignore
        root = Root()
        root.mainloop()

    def backButtonEventHandler(self) -> None:
        self.master.changeWindow("Main")  # type: ignore

def checkThread(thread: Optional[threading.Thread]) -> bool:
    return thread is None or not thread.is_alive()

def switchThread() -> None:
    while True:
        time.sleep(1.0)
        if state == "on":
            root.settingsFrame.darkLightModeSwitch.select()  # type: ignore
        elif state == "off":
            root.settingsFrame.darkLightModeSwitch.deselect()  # type: ignore

if __name__ == "__main__":
    root = Root()
    root.mainloop()
