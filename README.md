
# Antibody Sequence Similarity Checker

This project provides a simple tool to compare antibody sequences and find similarities between them.

## Requirements

- Python 3
- Biopython library (`pip install biopython`)

## Files

- `antibody_similarity_checker.py`: The main Python script for loading antibody sequences from a FASTA file and finding similar sequences.
- `README.md`: Instructions for running the project.

## Usage

1. Place your antibody sequences in a FASTA file named `antibodies.fasta`.
2. Run the script:
   ```
   python antibody_similarity_checker.py
   ```
3. The script will print sequences with a similarity ratio above the given threshold (default is 0.85).

## Example

To run the script:

```sh
python antibody_similarity_checker.py
```

Ensure you have your `antibodies.fasta` file in the same directory.
