from random import randint

from colorama import Fore


def encrypt_text(text, auto_justify=True, encrypt_spaces=True):
    """
    :param text: text to be encrypted
    :param auto_justify: Boolean, decides if unnecessary spaces will be removed and special character conventions are implemented
    :param encrypt_spaces: Boolean, decides if spaces are encrypted
    :return: encrypted text
    """

    special_chars = [",", ".", "!", "?", "-", "(", ")"]
    special_chars_no_spacing = ["(", "-"]
    specials_lib = {
        "heute": ["n", "r", "e", "t", "s", "O"],
        "Bahnhof": ["4", "0", "2", "U"],
        "alle": ["h", "c", "i"],
        ",": "@",
        ".": "#",
    }
    space_replacements = ["?", "%", "&"]

    word_list = []
    specials_positioning = []

    word_was_found = False
    for i in range(len(text)):
        char = text[i]
        if char.isalnum() and not word_was_found:   # checks if char is number or letter and if there was no word found previously to not iterate again over same word
            word_was_found = True   # signals a word was found
            word = [char]
            for j in range(i + 1, len(text)):   # iterates through rest of text from current index + 1
                char_from_i = text[j]
                if char_from_i.isalnum():
                    word.append(char_from_i)    # appends chars to word
                if not char_from_i.isalnum() or j == len(text) - 1:
                    word_list.append(word)  # appends word to list once no number or letter is found
                    break

        if not char.isalnum():  # iterates until a special char comes, indicating a word has ended
            word_was_found = False
            if not auto_justify and char == " ":    # if auto-justifying is not activated spaces will be saved
                specials_positioning.append((len(word_list), space_replacements[randint(0, 2)] if encrypt_spaces else " "))
            if char in special_chars:   # special chars are saved one index further than the word preceding it
                if char in specials_lib.keys():
                    char = specials_lib[char]
                specials_positioning.append((len(word_list), char))
            if i == len(text) - 1:  # need to add empty word at end of list if text ends with special char
                word_list.append([""])

    skip_word_reverse_indexes = []  # saves indexes of special words to not be reversed

    for m in range(len(word_list)):
        word_to_check = "".join(c for c in word_list[m])
        if word_to_check in specials_lib.keys():
            word_list[m] = specials_lib[word_to_check]
            skip_word_reverse_indexes.append(m)

    encrypted_text = ""

    for k in range(len(word_list)):
        reversed_word = []
        specials_at_position = False
        for specials_pair in specials_positioning:  # special chars following the previous word are attached to the front of the current one
            if specials_pair[0] == k + 1:
                specials_at_position = True    # checks if there are special chars following this word
            if specials_pair[0] == k:
                n = specials_pair[1]
                if auto_justify and n not in special_chars_no_spacing:
                    n += space_replacements[randint(0, 2)] if encrypt_spaces else " "
                reversed_word.append(n)

        if (k + 1) % 5 != 0 and k not in skip_word_reverse_indexes:     # does not reverse word if its count is dividable by 5 or if it is a special word
            for c in reversed(word_list[k]):
                reversed_word.append(c)
        else:
            for h in word_list[k]:
                reversed_word.append(h)

        if not specials_at_position:    # if another word follows adds spacing
            reversed_word.append(space_replacements[randint(0, 2)] if encrypt_spaces else " ")
        encrypted_text += "".join(c for c in reversed_word)

    return encrypted_text


def print_test_cases():
    test_case_special_chars = ".heute Bahnhof,alle!( 234234)abcd-abc"
    test_case_fifth_word = "eno owt eerht ruof Jedes a b c d Fünfte ,.,.,,.  , , ,, . . . ..          , .,a b c d Wort a b c d wird a b c d nicht a b c d umgekehrt"
    test_case_normal_text = "Lorem ipsum dolor sit-amet  , consectetur adipiscing .Sed do eiusmod tempor (  lorem ipsum dolor)."
    test_case_adjustable = "Random Word test"
    print(f"Original Text: {test_case_special_chars} \nAuto-Justify and Space-Encryption: {Fore.GREEN}On{Fore.RESET} \nEncrypted Text: {encrypt_text(test_case_special_chars, True, True)}")
    print(f"Auto-Justify: {Fore.RED}Off{Fore.RESET} \nEncrypted Text: {encrypt_text(test_case_special_chars, False, False)}")
    print()
    print(f"Original Text: {test_case_fifth_word} \nAuto-Justify: {Fore.GREEN}On{Fore.RESET} \nEncrypted Text: {encrypt_text(test_case_fifth_word, True, False)}")
    print(f"Auto-Justify: {Fore.RED}Off{Fore.RESET} \nEncrypted Text: {encrypt_text(test_case_fifth_word, False, False)}")
    print()
    print(f"Original Text: {test_case_normal_text} \nAuto-Justify: {Fore.GREEN}On{Fore.RESET} \nEncrypted Text: {encrypt_text(test_case_normal_text, True, False)}")
    print(f"Auto-Justify: {Fore.RED}Off{Fore.RESET} \nEncrypted Text: {encrypt_text(test_case_normal_text, False, False)}")
    print()
    print(f"Original Text: {test_case_adjustable} \nEncrypted Text: {encrypt_text(test_case_adjustable)}")

print_test_cases()
