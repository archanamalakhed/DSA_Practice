def sort_descending_pure(numbers):
    result = sorted(numbers,reverse=True)
    return result
original = [15, 2, 45, 12, 9]
result = sort_descending_pure(original)
print("Original:", original) # Should still be [15, 2, 45, 12, 9] using sorted
print("Result:", result)     # Should be [45, 15, 12, 9, 2]

def get_leaderboard(player_data):
    player_data.sort(key=lambda player: player[1], reverse=True)
    return player_data
players = [("Alice", 450), ("Bob", 1200), ("Charlie", 850)]
print(get_leaderboard(players)) # Expected Output: [('Bob', 1200), ('Charlie', 850), ('Alice', 450)]

def is_anagram(str1, str2):
    # sorted() breaks the strings into lists of characters and sorts them alphabetically
    return sorted(str1) == sorted(str2)
print(is_anagram("listen", "silent")) # Output: True
print(is_anagram("hello", "world"))   # Output: False
