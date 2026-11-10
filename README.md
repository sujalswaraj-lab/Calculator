# Simple Calculator

A beginner-friendly command-line calculator written in Python.

## Features

- Addition, subtraction, multiplication and division
- Handles division by zero without crashing
- Rejects invalid input (like letters) and asks again
- Keeps running until you quit

## Requirements

- Python 3.6 or newer
- No extra libraries needed

## How to Run

```bash
python calculator.py
```

On some systems you may need to use `python3` instead of `python`.

## Usage

Enter a number, an operation (`+`, `-`, `*` or `/`), and a second number. Type `q` at any prompt to quit.

```
=== Simple Calculator ===
Operations: +  -  *  /
Type 'q' at any prompt to quit.

Enter first number: 7
Enter operation (+, -, *, /): *
Enter second number: 6
Result: 42.0

Enter first number: q
Goodbye!
```

## How It Works

Each operation has its own small function (`add`, `subtract`, `multiply`, `divide`). The `calculator()` function loops forever, reads your input, converts the numbers with `float()`, and calls the matching function using `if`/`elif`.

## Ideas for Improvement

- Add power (`**`) and remainder (`%`) operations
- Remember the last result so you can keep calculating with it
- Let the user type a full expression like `3 + 4`
- Print whole numbers without the `.0` (show `42` instead of `42.0`)
