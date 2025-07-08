def word_abbreviation(word: str):
    if len(word) > 10:
        return f"{word[0]}{len(word[1:-1])}{word[-1]}"
    return word

n_words = int(input())

new_words = list()

for i in range(n_words):
    new_words.append(word_abbreviation(str(input())))

for word in new_words:
    print(word)