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

    def __init__(self, board : list[list[str]], *button_commands) -> None:
        root = tki.Tk()
        root.geometry("900x600")
        root.title("Boggle")
        root.resizable(False, False)
        self.__main_window = root

        self.__outer_frame = tki.Frame(root, bg=REGULAR_COLOR,
                                       highlightbackground=REGULAR_COLOR,
                                       highlightthickness=5)
        self.__outer_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self.__score_label = tki.Label(self.__outer_frame, font=("Courier", 30),
                                        bg=REGULAR_COLOR, width=12, relief="ridge")
        self.__score_label.pack(side=tki.TOP, fill=tki.BOTH)

        self.__current_word_label = tki.Label(self.__outer_frame, font=("Courier", 30),
                                        bg=REGULAR_COLOR, width=12, relief="ridge")
        self.__current_word_label.pack(side=tki.TOP, fill=tki.BOTH)

        self.__lower_frame = tki.Frame(self.__outer_frame)
        self.__lower_frame.pack(side=tki.TOP, fill=tki.BOTH, expand=True)

        self.__side_frame = tki.Frame(self.__outer_frame)
        self.__side_frame.pack(side=tki.RIGHT, fill=tki.BOTH, expand=True)

        self.__button_commands = button_commands


        
        # initializing the scroll bar
        h1 = tki.Scrollbar(self.__side_frame, orient = 'horizontal')
        h1.pack(side = tki.BOTTOM, fill=tki.X)
        v1 = tki.Scrollbar(self.__side_frame)
        v1.pack(side = tki.RIGHT, fill=tki.Y)
        #this object will show all the words we've submitted already
        
        self.__seen_words_text = tki.Text(self.__side_frame, width = 200, height = 80, wrap = tki.NONE,
		        xscrollcommand = h1.set,
		        yscrollcommand = v1.set, font=("Courier", 30))
        self.__seen_words_text.pack(side=tki.BOTTOM, fill=tki.X)
        h1.config(command=self.__seen_words_text.xview)
        v1.config(command=self.__seen_words_text.yview)
        
        # adding the buttons (the blocks + submit + cancel)
        self.__create_buttons_in_lower_frame(board)
        self.set_current_word_display()
        self.set_score_display()
        self.__main_window.bind("<Key>", self.__key_pressed)

    def run(self):
        
        self.__main_window.mainloop()
    
    def set_score_display(self, display_text: int = 0) -> None:
        self.__score_label["text"] = str(display_text)
    
    def set_current_word_display(self, word: str = "") -> None:
        self.__current_word_label["text"] = word

    def add_word_sumbitted_words(self, word :str) -> None:
        self.__seen_words_text.insert(tki.END, word + "\n")

    def set_button_command(self, button_name: str, button_commands: tuple, *args) -> None:
        if(button_name == 'SUBMIT'):
            self.__buttons[button_name].configure(command=button_commands[0])
        elif (button_name == 'CANCEL'):
            self.__buttons[button_name].configure(command=button_commands[1])
        else:
            self.__buttons[button_name].configure(command=lambda: button_commands[-1](*args))
    
    def get_button_chars(self) -> list[str]:
        return list(self.__buttons.keys())


    def __create_buttons_in_lower_frame(self, board) -> None:
        for i in range(6):
            tki.Grid.columnconfigure(self.__lower_frame, i, weight=1)
        
        for i in range(5):
            tki.Grid.rowconfigure(self.__lower_frame, i, weight=1)
        
        for i in range(4):
            for j in range(4):
                self.__make_button(board[i][j], i, j)
        self.__make_button("SUBMIT", 0, 4, rowspan=2)
        self.__make_button("CANCEL", 2, 4, rowspan=2)
        

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
        self.set_button_command(button_char, self.__button_commands, (row, col))
    
    def __key_pressed(self, event) -> None:
        if(event.char in self.__buttons):
            self.__simulate_button_press(event.char)
        elif event.keysym == "Return":
            #self.__simulate_button_press("=")
            ...
    
    def __simulate_button_press(self, button_char: str) -> None:
        """make buttons light up when pressed, then return to normal """
        button = self.__buttons[button_char]
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
        button.after(1, func=return_button_to_normal)

if __name__ == "__main__":
    print("please run boggle_controller")
    
