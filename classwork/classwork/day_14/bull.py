from itertools import product

syllable_types = [
    "V", "CV", "NV", "PV",
    "FV", "OV", "AV", "RV"
]


def is_valid(sequence):
    # Every syllable type already ends in V,
    # but keep this check for clarity.
    if any(not syllable.endswith("V") for syllable in sequence):
        return False

    # No two vowels may be adjacent.
    # Since every syllable ends in V, the next syllable
    # cannot begin with V.
    for i in range(len(sequence) - 1):
        if sequence[i + 1].startswith("V"):
            return False

    # Join the syllables into the actual word,
    # then reject AVAV anywhere in it.
    word = "".join(sequence)

    if "AVAV" in word:
        return False

    return True


patterns = []

for syllable_count in range(1, 4):
    for sequence in product(syllable_types, repeat=syllable_count):
        if is_valid(sequence):
            # Concatenate syllables into one word.
            patterns.append("".join(sequence).lower())


# Output one slash-separated list with no spaces
print("/".join(patterns))

# Count
print(f"\nTotal patterns: {len(patterns)}")
