import customtkinter as ctk
import threading
import time


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


global STATE
STATE = "off"
global THREAD
THREAD = None
global COLOR_THEME
COLOR_THEME = "dark-blue"


class Root(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("350x450")
        self.resizable(False, False)

        self.InitUi()

    def InitUi(self):
        self.mainFrame = MainFrame(parent=self)
        self.mainFrame.pack(expand=True, fill="both", padx=5, pady=5)

    def ChangeWindow(self, window):
        if window == "Settings":
            self.mainFrame.pack_forget()
            self.settingsFrame = SettingsFrame(parent=self)
            self.settingsFrame.pack(expand=True, fill="both", padx=5, pady=5)
        elif window == "Main":
            self.settingsFrame.pack_forget()
            self.mainFrame = MainFrame(parent=self)
            self.mainFrame.pack(expand=True, fill="both", padx=5, pady=5)


class MainFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.inputOutputEntry = ctk.CTkEntry(
            self, font=("Arial", 20), placeholder_text="0", state="disabled"
        )
        self.inputOutputEntry.grid(
            row=0, column=0, columnspan=4, sticky="nsew", padx=3, pady=3
        )

        self.settingsButton = ctk.CTkButton(
            self, text="Settings", command=self.SettingButtonEventHandler
        )
        self.settingsButton.grid(row=1, column=0, sticky="nsew", padx=3, pady=3)

        self.divisionButton = ctk.CTkButton(
            self, text="/", command=self.DivisionButtonEventHandler
        )
        self.divisionButton.grid(row=1, column=1, sticky="nsew", padx=3, pady=3)

        self.multiplicationButton = ctk.CTkButton(
            self, text="*", command=self.MultiplicationButtonEventHandler
        )
        self.multiplicationButton.grid(row=1, column=2, sticky="nsew", padx=3, pady=3)

        self.clearButton = ctk.CTkButton(
            self, text="Clear", command=self.ClearButtonEventHandler
        )
        self.clearButton.grid(row=1, column=3, sticky="nsew", padx=3, pady=3)

        self.sevenButton = ctk.CTkButton(
            self, text="7", command=self.SevenButtonEventHandler
        )
        self.sevenButton.grid(row=2, column=0, sticky="nsew", padx=3, pady=3)

        self.eightButton = ctk.CTkButton(
            self, text="8", command=self.EightButtonEventHandler
        )
        self.eightButton.grid(row=2, column=1, sticky="nsew", padx=3, pady=3)

        self.nineButton = ctk.CTkButton(
            self, text="9", command=self.NineButtonEventHandler
        )
        self.nineButton.grid(row=2, column=2, sticky="nsew", padx=3, pady=3)

        self.additionButton = ctk.CTkButton(
            self, text="+", command=self.AdditionButtonEventHandler
        )
        self.additionButton.grid(row=2, column=3, sticky="nsew", padx=3, pady=3)

        self.fourButton = ctk.CTkButton(
            self, text="4", command=self.FourButtonEventHandler
        )
        self.fourButton.grid(row=3, column=0, sticky="nsew", padx=3, pady=3)

        self.fiveButton = ctk.CTkButton(
            self, text="5", command=self.FiveButtonEventHandler
        )
        self.fiveButton.grid(row=3, column=1, sticky="nsew", padx=3, pady=3)

        self.sixButton = ctk.CTkButton(
            self, text="6", command=self.SixButtonEventHandler
        )
        self.sixButton.grid(row=3, column=2, sticky="nsew", padx=3, pady=3)

        self.subtractionButton = ctk.CTkButton(
            self, text="-", command=self.SubtractionButtonEventHandler
        )
        self.subtractionButton.grid(row=3, column=3, sticky="nsew", padx=3, pady=3)

        self.oneButton = ctk.CTkButton(
            self, text="1", command=self.OneButtonEventHandler
        )
        self.oneButton.grid(row=4, column=0, sticky="nsew", padx=3, pady=3)

        self.twoButton = ctk.CTkButton(
            self, text="2", command=self.TwoButtonEventHandler
        )
        self.twoButton.grid(row=4, column=1, sticky="nsew", padx=3, pady=3)

        self.threeButton = ctk.CTkButton(
            self, text="3", command=self.ThreeButtonEventHandler
        )
        self.threeButton.grid(row=4, column=2, sticky="nsew", padx=3, pady=3)

        self.equalButton = ctk.CTkButton(
            self, text="=", command=self.EqualButtonEventHandler
        )
        self.equalButton.grid(row=4, column=3, rowspan=2, sticky="nsew", padx=3, pady=3)

        self.zeroButton = ctk.CTkButton(
            self, text="0", command=self.ZeroButtonEventHandler
        )
        self.zeroButton.grid(
            row=5, column=0, columnspan=2, sticky="nsew", padx=3, pady=3
        )

        self.dotButton = ctk.CTkButton(
            self, text=".", command=self.DotButtonEventHandler
        )
        self.dotButton.grid(row=5, column=2, sticky="nsew", padx=3, pady=3)

    def DivisionButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", "/")
        self.inputOutputEntry.configure(state="disabled")

    def MultiplicationButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", "*")
        self.inputOutputEntry.configure(state="disabled")

    def SevenButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", "7")
        self.inputOutputEntry.configure(state="disabled")

    def EightButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", "8")
        self.inputOutputEntry.configure(state="disabled")

    def NineButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", "9")
        self.inputOutputEntry.configure(state="disabled")

    def AdditionButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", "+")
        self.inputOutputEntry.configure(state="disabled")

    def FourButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", "4")
        self.inputOutputEntry.configure(state="disabled")

    def FiveButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", "5")
        self.inputOutputEntry.configure(state="disabled")

    def SixButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", "6")
        self.inputOutputEntry.configure(state="disabled")

    def SubtractionButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", "-")
        self.inputOutputEntry.configure(state="disabled")

    def OneButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", "1")
        self.inputOutputEntry.configure(state="disabled")

    def TwoButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", "2")
        self.inputOutputEntry.configure(state="disabled")

    def ThreeButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", "3")
        self.inputOutputEntry.configure(state="disabled")

    def ZeroButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", "0")
        self.inputOutputEntry.configure(state="disabled")

    def DotButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.insert("end", ".")
        self.inputOutputEntry.configure(state="disabled")

    def SettingButtonEventHandler(self):
        self.master.ChangeWindow("Settings")

    def ClearButtonEventHandler(self):
        self.inputOutputEntry.configure(state="normal")
        self.inputOutputEntry.delete(0, "end")
        self.inputOutputEntry.configure(state="disabled")

    def EqualButtonEventHandler(self):
        op = self.inputOutputEntry.get()
        try:
            ans = eval(op)
            self.inputOutputEntry.configure(state="normal")
            self.inputOutputEntry.delete(0, "end")
            self.inputOutputEntry.insert("end", ans)
            self.inputOutputEntry.configure(state="disabled")
        except:
            self.inputOutputEntry.configure(state="normal")
            self.inputOutputEntry.delete(0, "end")
            self.inputOutputEntry.insert("end", "Error")
            self.inputOutputEntry.configure(state="disabled")


class SettingsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        self.InitUi()

    def InitUi(self):
        self.label = ctk.CTkLabel(
            self, text="Settings", font=("Arial", 20), anchor="center"
        )
        self.label.grid(row=0, column=0, columnspan=2, sticky="nw", padx=15, pady=15)

        self.appearanceLabel = ctk.CTkLabel(
            self, text="Appearance Mode:", font=("Arial", 15), anchor="center"
        )
        self.appearanceLabel.grid(
            row=1, column=0, columnspan=3, sticky="sw", padx=15, pady=15
        )

        self.darkModeLabel = ctk.CTkLabel(self, text="Dark Model")
        self.darkModeLabel.grid(
            row=2, column=0, columnspan=1, sticky="new", padx=15, pady=15
        )

        self.SWITCH_VALUE = ctk.StringVar(value="dark")
        self.darkLightModeSwitch = ctk.CTkSwitch(
            self,
            text="",
            variable=self.SWITCH_VALUE,
            offvalue="dark",
            onvalue="light",
            command=self.DarkLightModelSwitchEventHandler,
        )
        self.darkLightModeSwitch.grid(
            row=2, column=1, columnspan=1, sticky="new", padx=15, pady=15
        )

        self.thread = THREAD
        if CheckThread(self.thread):
            self.thread = threading.Thread(target=SwitchThread)
            self.thread.start()

        self.lightModeLabel = ctk.CTkLabel(self, text="Light Model")
        self.lightModeLabel.grid(
            row=2, column=2, columnspan=1, sticky="new", padx=15, pady=15
        )

        self.colorThemeLabel = ctk.CTkLabel(
            self, text="Color Theme:", font=("Arial", 15), anchor="center"
        )
        self.colorThemeLabel.grid(
            row=3, column=0, columnspan=3, sticky="sw", padx=15, pady=15
        )

        self.colorTheme = ctk.StringVar(value=COLOR_THEME)

        self.colorThemeRadioButtonOne = ctk.CTkRadioButton(
            self,
            text="Dark Blue",
            value="dark-blue",
            variable=self.colorTheme,
            command=self.ColorThemeRadioButtonsEventHandler,
        )
        self.colorThemeRadioButtonOne.grid(
            row=4, column=0, columnspan=1, sticky="new", padx=15, pady=15
        )

        self.colorThemeRadioButtonTwo = ctk.CTkRadioButton(
            self,
            text="Blue",
            value="blue",
            variable=self.colorTheme,
            command=self.ColorThemeRadioButtonsEventHandler,
        )
        self.colorThemeRadioButtonTwo.grid(
            row=4, column=1, columnspan=1, sticky="new", padx=15, pady=15
        )

        self.colorThemeRadioButtonThree = ctk.CTkRadioButton(
            self,
            text="Green",
            value="green",
            variable=self.colorTheme,
            command=self.ColorThemeRadioButtonsEventHandler,
        )
        self.colorThemeRadioButtonThree.grid(
            row=4, column=2, columnspan=1, sticky="new", padx=15, pady=15
        )

        self.backButton = ctk.CTkButton(
            self, text="Back", command=self.BackButtonEventHandler
        )
        self.backButton.grid(
            row=5, column=0, columnspan=3, sticky="sew", padx=15, pady=15
        )

    def DarkLightModelSwitchEventHandler(self):
        self.value = self.SWITCH_VALUE.get()
        global STATE
        STATE = "on" if self.value == "light" else "off"
        ctk.set_appearance_mode(self.value)

    def ColorThemeRadioButtonsEventHandler(self):
        self.theme = self.colorTheme.get()
        self.colorTheme.set(self.theme)
        global COLOR_THEME
        COLOR_THEME = self.theme
        ctk.set_default_color_theme(self.theme)
        self.master.destroy()
        root = Root()
        root.mainloop()
        self.thread = THREAD
        if CheckThread(self.thread):
            self.thread = threading.Thread(target=SwitchThread)
            THREAD = self.thread
            self.thread.start()
        self.master.ChangeWindow("Settings")

    def BackButtonEventHandler(self):
        self.master.ChangeWindow("Main")


def CheckThread(thread):
    if thread is None or not thread.is_alive():
        return True


def SwitchThread():
    while True:
        time.sleep(1.0)
        if STATE == "on":
            root.settingsFrame.darkLightModeSwitch.select()
        elif STATE == "off":
            root.settingsFrame.darkLightModeSwitch.deselect()


if __name__ == "__main__":
    root = Root()
    root.mainloop()


# TODO:
# FIX: Thread is not stopping when the window is closed
# FIX: Thread is stopping when changing color theme
# FIX: when changing color theme the mainframe is displaying not the settings frame
