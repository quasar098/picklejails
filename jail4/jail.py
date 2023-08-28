from io import BytesIO
from pickle import Unpickler


blocked = [
    '__build_class__',
    '__debug__',
    '__doc__',
    '__import__',
    '__loader__',
    '__name__',
    '__package__',
    '__spec__',
    'breakpoint',
    'callable',
    'compile',
    'copyright',
    'credits',
    'delattr',
    'eval',
    'exec',
    'exit',
    'hasattr',
    'help',
    'hex',
    'id',
    'input',
    'int',
    'isinstance',
    'issubclass',
    'iter',
    'len',
    'license',
    'list',
    'locals',
    'map',
    'max',
    'memoryview',
    'min',
    'next',
    'object',
    'oct',
    'open',
    'ord',
    'pow',
    'print',
    'property',
    'quit',
    'range',
    'repr',
    'reversed',
    'round',
    'set',
    'setattr',
    'slice',
    'sorted',
    "vars",
    'staticmethod',
    'str',
    'sum',
    'super',
    'tuple',
    'type',
    'zip'
]


class SafeUnpickler(Unpickler):
    def find_class(self, _: str, name: str):
        for block in blocked:
            if block in name:
                print(f"Blocked word found! ({block})")
                break
        else:
            return getattr(__builtins__, name)


if __name__ == '__main__':
    up = SafeUnpickler(BytesIO(bytes.fromhex(input(">> "))))
    up.load()
