from io import BytesIO
from pickle import Unpickler


class SafeUnpickler(Unpickler):
    def find_class(self, _: str, name: str):
        for blocked in ["eval", "exec", "exit", "open", "os", "subprocess", "setattr", "__import__"]:
            if blocked in name:
                print(f"Blocked word found! ({blocked})")
                break
        else:
            return getattr(__builtins__, name)


if __name__ == '__main__':
    up = SafeUnpickler(BytesIO(bytes.fromhex(input(">> "))))
    up.load()
