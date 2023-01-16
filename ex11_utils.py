from typing import List, Tuple, Iterable, Optional
import itertools

Board = List[List[str]]
Path = List[Tuple[int, int]]
BOARD_SIZE = 4


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

    list_of_locations = [[(i,j) for i in range(4)] for j in range(4)]
    path_permutations_of_length_n = list(itertools.permutations(list_of_locations, n)) # all the permutations of n locations
    legal_permutations = list()
    for path in path_permutations_of_length_n:
        if(is_valid_path(board, path, words)):
            legal_permutations.append(path)
    return legal_permutations


def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """
    this function returns all the paths for words of length n"""
    pass

def get_all_words_with_length_n(n: int, words: Iterable[str]) -> List[str]:
    ...


def max_score_paths(board: Board, words: Iterable[str]) -> List[Path]:
    pass
