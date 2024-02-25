"""
    Base Tokenizer for Inheritance
    Utility Functions
"""

def get_stat(ids: list[int]) -> dict[tuple[int, int], int]:
    stat = {}
    for pair in zip(ids, ids[1:]):
        stat[pair] = stat.get(pair, 0) + 1
        
    return stat

def get_max_occuring_pair(stat: dict[tuple[int, int], int]) -> tuple[int, int]:
    return max(stat, key=stat.get)


class Tokenizer:
    def __init__(self) -> None:
        pass
    
    def train(self, text: str, vocab_size: int, verbose: bool = False) -> None:
        raise NotImplementedError
    
    def encode(self, text: str) -> list[int]:
        raise NotImplementedError
    
    def decode(self, ids: list[int]) -> str:
        raise NotImplementedError
    
if __name__ == '__main__':
    text = """League of Legends is a multiplayer online battle arena (MOBA) game in which the player controls a character"""
    # preprocess
    encoded = text.encode('utf-8')
    ids = list(map(int, encoded))  
    # get stats
    stats = get_stat(ids)
    max_pair = get_max_occuring_pair(stats)
    print(max_pair)