languages = ["Python","Javascript","Ruby"]

length = { language: len(language) for language in languages if "t" in language} 
print(length)

word = "supercalifragilisticexpialidocious"

letter_count = { letter:word.count(letter) for letter in word if letter > "j"}
print(letter_count)

