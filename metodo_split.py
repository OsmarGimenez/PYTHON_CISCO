def mysplit(strng):
    if not strng:
        return []
    words = []
    current_word = ""
    for char in strng:
        if char == " ":
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    return words

print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("    "))
print(mysplit(" abc "))
print(mysplit(""))