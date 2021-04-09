# Markpanso
A Python script to turn a Espanso package written in the YAML format into a Markdown styled table

## Installation

Simply cloning or downloading this repository to get the `markpanso.py` Python script will do.

For convenience rename this file to `markpanso` and place it in your `$PATH`, which for a standard UNIX system should be at `~/.local/bin`. Then, from a terminal, type `markpanso` to use this script.

## Usage

Tell `markpanso` where your Espanso package is at:
```
markpanso /path/to/package/package.yml
```

And the Markdown styled table will be printed to your terminal.

If you want to store that table in a file, then use the `-o` or `--output` flag to point it to an arbitrary placed file (supports relative paths):
```
markpanso /path/to/package/package.yml -o /path/to/store/table.txt
```

And the contents that would be printed to stdout will be placed in `/path/to/store/table.txt`

## References
- [Compart/Unicode](https://www.compart.com/en/unicode/): Massive agregator for all Unicode symbols organized into categories that also allows you to search a symbol knowing it's name and vice-versa. This is the best place to look for specific symbols by name or by category giving you a full organized overview of the Unicode standard.

- [unicodedata documentation](https://docs.python.org/3/library/unicodedata.html): Docs for the Python package `unicodedata`.

- [PyYAML documentation](https://pyyaml.org/wiki/PyYAMLDocumentation): Documentation for the Python package `yaml`.

- [python-tabulate](https://github.com/astanin/python-tabulate): Repository for the Python package`python-tabulate`, includes documentation.

## License
This package is licensed under the MIT license.

For further information refer to the file `LICENSE` available on this repository.
