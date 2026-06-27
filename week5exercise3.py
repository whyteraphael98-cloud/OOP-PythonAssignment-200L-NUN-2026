def count_vowels_consonants(text):
    """
    Count the number of vowels and consonants in the given text.
    
    Vowels are 'a', 'e', 'i', 'o', 'u' (case-insensitive).
    Consonants are alphabetic characters that are not vowels.
    Non-alphabetic characters are ignored.
    
    Args:
        text (str): The input string.
    
    Returns:
        dict: A dictionary with keys "vowels" and "consonants".
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowels_count = 0
    consonants_count = 0
    
    for char in text.lower():
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
    
    return {"vowels": vowels_count, "consonants": consonants_count}

