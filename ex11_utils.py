from typing import List, Tuple, Iterable, Optional
import itertools

Board = List[List[str]]
Path = List[Tuple[int, int]]
BOARD_SIZE = 4
seen_words = set()
new_set = dict()

def partial_is_valid_path(board, path, words):
    word = ""
    for loc in path:
        word += board[loc[0]][loc[1]]
    return any(key.startswith(word) for key in words)

def get_word_from_path(board, path):
    word = ""
    for i in range(len(path)):
        block = path[i]
        if(block in path[:i]): # you can't repeat blocks
            return None
        if(not (is_neighboring(block, i-1, path) and is_cube_in_board_range(block, BOARD_SIZE))): # if the current cube is a neighbor of the the previous one, and is not equal
            return None
        word += board[block[0]][block[1]]
    return word

def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """
    :param: board: a 2d list of strings which are the values of the cubes
    :param: path: a list of 2d tuples which are the path on the board
    :param: words: a set containing all the possible words
    :return: True if the path is legal and the word in in the set, False otherwise
    """

    word = get_word_from_path(board, path)
    if(word in words):
        return word
    return None


def is_cube_in_board_range(block, board_size):
    """
    this function returns True if the block is within range of the board, False otherwise"""
    if 0 <= block[0] < board_size and 0 <= block[1] < board_size:
        return True
    return False

def is_neighboring(block1, index_of_other_block, path):
    """
    this function returns true if either on of the blocks is at distance of 1 from the other,
    False otherwise
    """

    if(index_of_other_block == -1):
        return True
    block2 = path[index_of_other_block]
    for i in range(3):
        for j in range(3):
            if(block1 == (block2[0] - 1 + i, block2[1] - 1 + j)):
                return True
    return False

def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    new_set = create_all_substrings(words)
    if(n > len(board) ** 2): return [] # too big for this board
    legal_paths = list()
    for i in range(len(board)):
        for j in range(len(board)):
            
            find_length_n_words_helper(n, board, [(i,j)], words, (i,j), legal_paths,is_length_n_words=False)
                
    return legal_paths


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    new_set = create_all_substrings(words)
    if(n > len(board) ** 2): return [] # too big for this board
    legal_paths = list()
    for i in range(len(board)):
        for j in range(len(board)):
            find_length_n_words_helper(n, board, [(i,j)], words, (i,j), legal_paths)
    return legal_paths
    ...
def find_length_n_words_helper(n, board, visited_locations, words, current_location, legal_paths, is_length_n_words = True, should_use_same_word_twice = True):
    if(n == 0):
        return
    if(n == 1):
        word = is_valid_path(board, visited_locations, words)
        if(word):
            if(should_use_same_word_twice):
                legal_paths.append(visited_locations)
            elif(not should_use_same_word_twice and word not in seen_words):
                seen_words.add(word)
                legal_paths.append(visited_locations)
    
    elif(get_word_from_path(board, visited_locations) in new_set):
        for i in range(-1, 2):
            for j in range(-1, 2):
                potential_location = (i + current_location[0], j + current_location[1])
                if(potential_location not in visited_locations and is_in_range(potential_location, 4)):
                    new_visited = visited_locations[:]
                    new_visited.append(potential_location)
                    block_str = board[potential_location[0]][potential_location[1]]
                    if(is_length_n_words):
                        find_length_n_words_helper(n - len(block_str), board, new_visited, words,\
                                              potential_location, legal_paths, is_length_n_words, should_use_same_word_twice)
                    else:
                        find_length_n_words_helper(n - 1, board, new_visited, words,\
                                              potential_location, legal_paths, is_length_n_words, should_use_same_word_twice)                
        

def is_in_range(loc, board_size):
    return 0<=loc[0]<board_size and 0<=loc[1]<board_size



    ...
def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    new_set = create_all_substrings(words)
    best_score_paths = []
    for k in range(10, 0, -1):
        legal_paths = list()
        for i in range(len(board)):
            for j in range(len(board)):
                find_length_n_words_helper(k, board, [(i,j)], words, (i,j), legal_paths, is_length_n_words= False, should_use_same_word_twice=False)
        best_score_paths.extend(legal_paths)
    return best_score_paths


def create_all_substrings(words: Iterable[str]):
    for word in words:
        temp = ""
        for i in range(len(word)):
            temp += word[i]
            new_set[temp] = 0
