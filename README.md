<div align="center">
    <h2>
        <b>
            File I/O
        </b>
    </h2>
        My Computer Science Class, Programing in Python<br>Meeting 9: Assignment
</div>

---

### Base Theory
<div align="justify">
    In programming, files permanently store data for future use, and Python handles this through the open() function using modes like "r" (read), "w" (write), or "a" (append) alongside methods such as read(), readlines(), and write(). Additionally, Python includes a dedicated csv module to easily process CSV files, a common format for tabular data. Mastering these file operations is essential because it allows programs to efficiently manage large datasets and organize processed results structurally.
</div>

#### Assignment
<div align="justify">
    Write a program that creating CSV file and adding the additional dummy data, and then processing the data throught the CSV
    and displaying it on CLI, and then subtract the total-data and the total of all to summarize it, in the end adding the summarize output into the CSV. 
</div>

### Implementation
My first implementation here will be using:
| File I/O Lib | Explanation |
| :-- | :-- |
| ``mode="r"`` | for reading the file. |
| ``mode="w"`` | for writing or making the file. |
| ``mode="a"`` | for adding new additional data into the file. |
| ``newline=""`` | for making new line in the file. |
---

### File Structure
```
Slicing-Method/
├── File-IO.py      # Fist implementation code
└── README.md       # Please Read For Better General Understanding
```

### How to run
- First, making virtual environtment for yourself and activate it.
    - On Windows (for me using git bash):
    ```bash
    py -m venv .venv && source .venv/Scripts/activate
    ```
    - On linux based OS (bash / zsh):
    ```bash
    python3 -m venv .venv && source .venv/bin/activate
    ```
- Second, run the code file.
    - On windows (for me using git bash):
    ```bash
    py File-IO.py
    ```
    - On linux based OS (bash / zsh):
    ```zsh
    python3 File-IO.py
    ```

---

<div align="center">
    <b>
        Made By Me. 😊
    </b>
</div>