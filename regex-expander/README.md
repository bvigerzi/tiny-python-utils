# Regex Expander

A small CLI that will expand a specified regular expression into all possible values.

## Getting Started

1. (Optional) Setup [virtual Python environment](https://docs.python.org/3/tutorial/venv.html)
2. Install dependencies
    - `$ pip install -r requirements.txt`
3. Ready to start! Refer to usage for more info

## Usage

```bash
$ python3 expander.py --pattern "test(1|2)[A-Z]" --file-name "custom-name.txt" --delimiter "\t"
```

The pattern and delimiter arguments should be wrapped in quotations to ensure they are parsed correctly. The `file-name` defaults to `expanded.txt`, while the delimiter defaults to the newline character (`\n`).

## Special Cases and Error Conditions

### -bash: !: event not found

This error condition is caused by not escaping the `!` in your regular expression. `!` is treated as a special character in bash and must be escaped (with the `\` prefix). This will result in a valid regular expression that expands correctly.

#### Example

```bash
$ python3 expander.py --pattern "test(1|2|\!)"
```

Gives the following (expected) output:

```
test1
test2
test!
```

## Word of Caution

This utility makes no attempt to handle user error. If an infinite-state regular expression is entered (e.g. `a*`) then the program will not fail safely. It will continue to (attempt to) expand the expression to infinity until terminated (by user action or otherwise).
