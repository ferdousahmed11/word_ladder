from collections import deque

# Function to check if two words differ by exactly one character
def is_adjacent(word1, word2):
    diff_count = sum(c1 != c2 for c1, c2 in zip(word1, word2))
    return diff_count == 1

# Function to find the word ladder using breadth-first search
def find_word_ladder(begin_word, end_word, word_list):
    if end_word not in word_list:
        return []

    word_list = set(word_list)
    queue = deque([(begin_word, [begin_word])])

    while queue:
        word, ladder = queue.popleft()
        if word == end_word:
            return ladder
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in word_list and is_adjacent(word, new_word):
                    queue.append((new_word, ladder + [new_word]))
                    word_list.remove(new_word)

    return []

# Function to display the word ladder
def display_word_ladder(ladder):
    if ladder:
        print("Word ladder found:")
        for word in ladder:
            print(word)
    else:
        print("No word ladder found.")

# Game setup
begin_word = input("Enter the start word: ")
end_word = input("Enter the end word: ")
word_list = input("Enter the word list, separated by spaces: ").split()

# Find and display the word ladder
ladder = find_word_ladder(begin_word, end_word, word_list)
display_word_ladder(ladder)
