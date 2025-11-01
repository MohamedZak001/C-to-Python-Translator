# Programming Translator

A Python-to-C code translator that converts Python syntax into equivalent C code. This educational project uses NLTK for parsing Python input and generates corresponding C language constructs.

## What this project does

- Reads `input.txt` containing Python code snippets
- Tokenizes and parses the Python input using NLTK
- Produces `output.txt` containing the equivalent C code translation
- Visualizes parse trees of the input code structure (requires GUI support)

## Setup

1. Create a virtual environment:
```bash
python3 -m venv env
source env/bin/activate  # On Linux/Mac
# or
.\env\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. For GUI tree visualization (optional), install tkinter:
```bash
sudo apt-get update
sudo apt-get install python3-tk  # On Ubuntu/Debian
```

The script will:

- Print the raw input (from `input.txt`).
- Print the token list produced by the tokenizer.
- Write a translated result to `output.txt`.
- If the grammar matches, it will try to display parse tree GUI windows (requires tkinter/display). If no GUI is available or the grammar does not match, no window will open.

## Usage

1. Create an `input.txt` file with your Python code. Example:
```python
for i in range(9):
    if a > b:
        c = c + 1
```

2. Run the translator:
```bash
python main.py
```

3. Check `output.txt` for the C code translation:
```c
for(i = 1; i < 9; i++){
    if(a > b){
        c = c + 1;
    }
}
```

The script will also:
- Print the input code
- Show tokenization details
- Attempt to display parse trees (if GUI available)


## Supported Constructs

Currently supports translation of:
- Basic for loops with range
- Simple if statements
- Basic arithmetic operations
- Variable assignments

Note: This is a teaching tool with limited language support, not a full Python-to-C compiler.
