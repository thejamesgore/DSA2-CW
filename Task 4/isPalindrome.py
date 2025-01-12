def isPalindrome(word):
    if len(word) <= 1:
        return True # Base case for our recursion call

    # Extract the first and last characters of the word
    first_char = word[0]
    last_char = word[-1]

    # Check if the first and last characters are the same
    if first_char != last_char:
        return False  # If they are not the same, it is not a palindrome
    rest_of_word = word[1:len(word)-1]

    return isPalindrome(rest_of_word)
