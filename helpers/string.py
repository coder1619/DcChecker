import random
from config import TOKENS, USER_FILE

class String:
    def __init__(self):
        pass

    def get_token(self) -> str:
        return random.choice(TOKENS)
    
    def get_user_list(self):
        with open(USER_FILE) as f:
            return [line.strip() for line in f if line.strip()]
        
    def gen_username(self, type: str, length: str) -> str:
        if type == "letters":
            letters = "abcdefghijklmnopqrstuvwxyz"
            return ''.join(random.choices(letters, k=int(length)))
        elif type == "numbers":
            numbers = "0123456789"
            return ''.join(random.choices(numbers, k=int(length)))
        elif type == "random":
            chars = "abcdefghijklmnopqrstuvwxyz0123456789_."
            return ''.join(random.choices(chars, k=int(length)))