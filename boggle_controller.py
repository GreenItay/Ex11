from boggle_gui import BoggleGUI
from boggle_model import Model
from boggle_board_randomizer import *
class Controller:
    def __init__(self) -> None:
        self.__board = randomize_board()
        self.__words = self.load_words("boggle_dict.txt")
        self.__model = Model(self.__board, self.__words)
        self.__gui = BoggleGUI(self.__board, self.submit,self.cancel,self.letter_press)
        
        self.__gui.run()
        


    def letter_press(self, loc):
        self.__model.add_to_path(loc)
        self.__gui.set_current_word_display(self.__model.get_current_word())
    
    def submit(self):
        is_valid = self.__model.submit_word()
        if(is_valid):
            self.__gui.add_word_sumbitted_words(is_valid)
        self.__model.cancel()
        self.__gui.set_score_display(self.__model.get_score())
        self.__gui.set_current_word_display(self.__model.get_current_word())

    def cancel(self):
        self.__model.cancel()
        self.__gui.set_current_word_display(self.__model.get_current_word())
    
    def load_words(self, path) -> dict:
        words = dict()
        with open(path) as f:
            for line in f:
                words[line.strip()] = True
        return words

if __name__ == "__main__":
    c = Controller()