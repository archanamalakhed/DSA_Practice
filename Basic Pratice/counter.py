from collections import Counter
def count_num_without_in_built(nums):
    freq = {}
    for i in nums:
        freq[i] = freq.get(i,0) +1
    return freq
nums = [2,2,2,3,5,5,0]
print(count_num_without_in_built(nums))
print("Using counter")

nums1 = [1, 2, 2, 3, 1, 4, 2]
frequency = Counter(nums1)
print(dict(frequency))

sentence = "this is a test this is only a test"
words = sentence.split()
word_count = Counter(words)

print(dict(word_count))

def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

sentence = "Archana Archana Archana ONLY aRCHANA"
print(word_frequency(sentence))
