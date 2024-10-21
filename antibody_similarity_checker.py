
import difflib
from Bio import SeqIO

def load_sequences(file_path):
    """
    Load antibody sequences from a given file.
    Args:
        file_path (str): Path to the FASTA file containing antibody sequences.
    Returns:
        dict: Dictionary with sequence IDs as keys and sequences as values.
    """
    sequences = {}
    with open(file_path, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequences[record.id] = str(record.seq)
    return sequences

def calculate_similarity(seq1, seq2):
    """
    Calculate the similarity between two sequences.
    Args:
        seq1 (str): First sequence.
        seq2 (str): Second sequence.
    Returns:
        float: Similarity ratio between 0 and 1.
    """
    return difflib.SequenceMatcher(None, seq1, seq2).ratio()

def find_similar_sequences(sequences, threshold=0.8):
    """
    Find and print sequences with similarity above a given threshold.
    Args:
        sequences (dict): Dictionary of sequences.
        threshold (float): Minimum similarity ratio to consider.
    """
    ids = list(sequences.keys())
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            seq1 = sequences[ids[i]]
            seq2 = sequences[ids[j]]
            similarity = calculate_similarity(seq1, seq2)
            if similarity >= threshold:
                print(f"{ids[i]} and {ids[j]} have similarity of {similarity:.2f}")

if __name__ == "__main__":
    # Provide the path to your FASTA file with antibody sequences
    file_path = "antibodies.fasta"
    sequences = load_sequences(file_path)
    find_similar_sequences(sequences, threshold=0.85)
