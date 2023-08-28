from io import BytesIO
from pickle import Unpickler


blocked = [
    '__import__',
    'breakpoint',
    'callable',
    'compile',
    'delattr',
    'eval',
    'exec',
    'exit',
    'help',
    'locals',
    'print',
    'quit',
    'setattr',
    "vars",
    "globals",
]


class Data:
    class Book:
        read = None


class SafeUnpickler(Unpickler):
    def find_class(self, module: str, name: str):
        for block in blocked:
            if block in name:
                print(f"Blocked word found! ({block})")
                return
        if module == "data":
            if name == "self":
                return Data
            if name == "book":
                return Data.Book
            if name == "read":
                return Data.Book.read
        return getattr(__builtins__, name)


if __name__ == '__main__':
    up = SafeUnpickler(BytesIO(bytes.fromhex(input(">> "))))
    print(up.load())
