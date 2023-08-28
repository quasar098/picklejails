from io import BytesIO
from pickle import Unpickler


class SafeUnpickler(Unpickler):
    def find_class(self, _: str, name: str):
        for blocked in ["eval", "exec", "exit", "open", "sys", "os", "subprocess", "dis", "load", "set", "_"]:
            if blocked in name:
                print(f"Blocked word found! ({blocked})")
                break
        else:
            return getattr(__builtins__, name)


if __name__ == '__main__':
    up = Unpickler(BytesIO(bytes.fromhex(input(">> "))))
    up.load()
