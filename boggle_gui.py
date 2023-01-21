import tkinter as tki
import typing

BUTTON_HOVER_COLOR = 'gray'
REGULAR_COLOR = 'lightgray'
BUTTON_ACTIVE_COLOR = 'slateblue'
BUTTON_STYLE = {"font": ("Courier", 30),
                "borderwidth" : 1,
                "relief": tki.RAISED,
                "bg": REGULAR_COLOR,
                "activebackground": BUTTON_ACTIVE_COLOR}
class BoggleGUI:
    __buttons : dict[str: tki.Button] = {}

    def __init__(self) -> None:
        root = tki.Tk()
        root.title("Boggle")
        root.resizable(False, False)
        self.__main_window = root

        self.__outer_frame = tki.Frame(root, bg=REGULAR_COLOR,
                                       highlightbackground=REGULAR_COLOR,
                                       highlightthickness=5)
        self.__outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self.__display_label = tki.Label(self.__outer_frame, font=("Courier", 30),
                                        bg=REGULAR_COLOR, width=23, relief="ridge")
        self.__display_label.pack(side=tki.TOP, fill=tki.BOTH)

        self.__lower_frame = tki.Frame(self.__outer_frame)
        self.__lower_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self.__create_buttons_in_lower_frame()
        self.__main_window.bind("<Key>", self.__key_pressed)
    

    def run(self):
        self.__main_window.mainloop()
    
    def set_display(self, display_text: str) -> None:
        self.__display_label["text"] = display_text
    
    def set_button_command(self, button_name: str, cmd) -> None:
        self.__buttons[button_name].configure(command=cmd)
    
    def get_button_chars(self) -> list[str]:
        return list(self.__buttons.keys())


    def __create_buttons_in_lower_frame(self) -> None:
        for i in range(5):
            tki.Grid.columnconfigure(self.__lower_frame, i, weight=1)
        
        for i in range(5):
            tki.Grid.rowconfigure(self.__lower_frame, i, weight=1)
        
        self.__make_button("A", 0, 0)

    def __make_button(self, button_char: str, row: int, col: int,
                     rowspan: int = 1, columnspan: int = 1, should_be_released: bool = True) -> tki.Button:
        button = tki.Button(self.__lower_frame, text=button_char, **BUTTON_STYLE)
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=columnspan, sticky=tki.NSEW)
        self.__buttons[button_char] = button
    

        def __on_enter(event) -> None:
            button['background'] = BUTTON_HOVER_COLOR
        
        def __on_leave(event) ->None:
            button['background'] = REGULAR_COLOR

        button.bind("<Enter>", __on_enter)
        button.bind("<Leave>", __on_leave)
    
    def __key_pressed(self, event) -> None:
        if(event.char in self.__buttons):
            self.__simulate_button_press(event.char)
        elif event.keysym == "Return":
            self.__simulate_button_press("=")
    
    def __simulate_button_press(self, button_char: str) -> None:
        """make buttons light up when pressed, then return to normal """
        button = self.__buttons[button_char]
        button["bg"] = BUTTON_ACTIVE_COLOR
        button["bg"] = BUTTON_ACTIVE_COLOR

        def return_button_to_normal() -> None:
            x,y = self.__main_window.winfo_pointerxy()
            # is the widget under the mouse
            widget_under_mouse = self.__main_window.winfo_containing(x, y)

            if widget_under_mouse is button:
                button["bg"] = BUTTON_HOVER_COLOR
            else:
                button["bg"] = REGULAR_COLOR

        button.invoke()
        button.after(100, func=return_button_to_normal)

if __name__ == "__main__":
    bg = BoggleGUI()
    bg.set_display("TEST_MODE")
    bg.run()
    
