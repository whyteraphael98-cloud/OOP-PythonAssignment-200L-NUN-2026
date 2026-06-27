import string

def count_word_frequency(text):
    """
    Count the frequency of each unique word in the input text.

    Args:
        text (str): The input string.

    Returns:
        dict: A dictionary mapping lowercase words to their counts.
    """
    word_counts = {}
    for word in text.split():
        cleaned_word = word.strip(string.punctuation).lower()
        if cleaned_word:
            if cleaned_word in word_counts:
                word_counts[cleaned_word] += 1
            else:
                word_counts[cleaned_word] = 1
    return word_counts

# Example usage
if __name__ == "__main__":
    sample = "Hello hello, world! This is a test. Hello world."
    print(count_word_frequency(sample))
