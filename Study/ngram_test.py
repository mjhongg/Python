word = input('단어를 입력하세요: ')
print(word)

is_palindrome = True
word_len = len(word)

for i in range(word_len):
    if word[i] != word[-1-i]:
        is_palindrome = False
        break

print(is_palindrome)