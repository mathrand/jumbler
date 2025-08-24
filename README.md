# Character Substitution Permutation Generator

This Python script generates every possible permutation of a given word by applying character substitutions and variations. The substitutions are based on a predefined dictionary that maps characters to similar-looking replacements (e.g., 'a' becomes '@' or '4').

## Features

Substitutes characters in a word with common alternatives (e.g., 'a' becomes '@', 's' becomes '$').

Creates permutations of the input word with all possible character substitutions.

Prints the output permutations along with the timestamp of when the process starts and ends.

## Prerequisites

Python 3.x

No external dependencies required (standard Python libraries used).

## How It Works

The script uses a substitution list where each character in the list is mapped to similar-looking characters.

For each character in the input word, the script substitutes it with available options (lowercase, uppercase, and predefined special characters).

The result is printed as all possible combinations of these substitutions.

## Usage

Clone this repository or download the script file.

Open a terminal or command prompt.

Run the script by passing a word as an argument:

python jmbl.py <your_word>


For example:

python jmbl.py hello


The script will output all permutations of the word "hello" with the possible character substitutions.

Example Output
Started 2021-05-24 14:30:00
h3ll0
h3l10
h3ll0
h3ll0
...

Arguments

<your_word>: The word you want to generate permutations for.


