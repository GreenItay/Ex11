from ex11_utils import *
class Model:
    def __init__(self, board, words):
        self.__seen_words = set()
        self.__score  = 0
        self.__current_path = []
        self.__board = board
        self.__words = words
        self.__current_word = ""
    
    def cancel(self):
        self.__current_path = []
        self.__current_word = ""

    def add_to_path(self, loc) -> None:
        if(is_neighboring(loc, -1, self.__current_path) and loc not in self.__current_path):
            self.__current_path.append(loc)
        self.__current_word += self.__board[loc[0]][loc[1]]
        ...
    
    def submit_word(self):
        word = is_valid_path(self.__board, self.__current_path, self.__words)
        if(word and self.__words[word]):
            self.__add_to_score(len(self.__current_path))
            self.__words[word] = False # this word has been submitted and cannot be submitted again
            self.__current_path = []
            return word
        self.__current_path = []
        return None
        

    def get_score(self):
        return self.__score

    def get_current_word(self):
        return self.__current_word

    def __add_to_score(self, path_length : int) -> None:
        self.__score += path_length ** 2

    def set_score_to_zero(self):
        self.__score = 0
