from io import BytesIO
from pickle import Unpickler

if __name__ == '__main__':
    up = Unpickler(BytesIO(bytes.fromhex(input(">> "))))
    up.load()
