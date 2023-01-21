from typing import List, Tuple, Iterable, Optional
import itertools

Board = List[List[str]]
Path = List[Tuple[int, int]]
BOARD_SIZE = 4

def partial_is_valid_path(board, path, words):
    word = ""
    for loc in word:
        word += word[loc[0]][loc[1]]
    return any(key.startswith(word) for key in words)

def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """
    :param: board: a 2d list of strings which are the values of the cubes
    :param: path: a list of 2d tuples which are the path on the board
    :param: words: a set containing all the possible words
    :return: True if the path is legal and the word in in the set, False otherwise
    """

    word = ""
    for i in range(len(path)):
        block = path[i]
        if(block in path[:i]): # you can't repeat blocks
            return None
        if(not (is_neighboring(block, i-1, path) and is_cube_in_board_range(block, BOARD_SIZE))): # if the current cube is a neighbor of the the previous one, and is not equal
            return None
        word += board[block[0]][block[1]]
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
    """
    this function looks at all path permutations on the board, of length n, and then keeps only the valid ones,
    then returns them
    :param: n:  the desired length of the path
    :param: board: :param: path: a list of 2d tuples which are the path on the board
    :param: words: a set containing all the possible words
    :return: List[Tuple(int,int)] of legal paths of length n
    """

    list_of_locations = [(i,j) for i in range(4) for j in range(4)]
    path_permutations_of_length_n = itertools.permutations(list_of_locations, n) # all the permutations of n locations
    legal_permutations = list()
    for path in path_permutations_of_length_n:
        valid = is_valid_path(board, path, words)
        if(valid):
            words[valid] = False # this word has been seen
            legal_permutations.append(list(path))
    return legal_permutations


def find_length_n_words_2(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    this function returns all the paths for words of length n"""
    legal_permutations = list()
    list_of_locations = [(i,j) for i in range(4) for j in range(4)]
    list_of_possible_permutations = list()
    double_letterts = count_double_letters_on_board(board)
    list_of_possible_permutations = itertools.permutations(list_of_locations, n)
    for i in range(max(n//2,  n - double_letterts), n+1):
        for path in list_of_possible_permutations:
            valid = is_valid_path(board, path, words)
            if(valid is None): continue
            elif(len(valid) == n):
                words[valid] = False # this word has been seen
                legal_permutations.append(list(path))
    return legal_permutations

def count_double_letters_on_board(board) -> int:
    ...
    # use the count("qu") to find the range of n's to scan: [n - count("qu"), n]
    count = 0
    for row in board:
        for col in board:
            if(len(col) == 2):
                count += 1
    return count

def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    legal_paths = list()
    for i in range(len(board)):
        for j in range(len(board)):
            
            find_length_n_words_helper(n, board, [(i,j)], words, (i,j), legal_paths)
                
    return legal_paths
    ...
def find_length_n_words_helper(n, board, visited_locations, words, current_location, legal_paths):
    if(n == 0):
        #legal_paths.append([])
        return
    if(n == 1):
        word = is_valid_path(board, visited_locations, words)
        if(word):
            legal_paths.append(visited_locations)
    elif(partial_is_valid_path(board, visited_locations, words)):
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                potential_location = (i + current_location[0], j + current_location[1])
                if(potential_location not in visited_locations and is_in_range(potential_location, 4)):
                    new_visited = visited_locations[:]
                    new_visited.append(potential_location)
                    block_str = board[potential_location[0]][potential_location[1]]
                    find_length_n_words_helper(n - len(block_str), board, new_visited, words,\
                     potential_location, legal_paths)
        

def is_in_range(loc, board_size):
    return 0<=loc[0]<board_size and 0<=loc[1]<board_size


    ...
def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    ...


