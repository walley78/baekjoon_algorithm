import sys

input = sys.stdin.readline

def get_common_prefix_length(word1, word2):
    length = min(len(word1), len(word2))
    for i in range(length):
        if word1[i] != word2[i]:
            return i
    return length

N = int(input())
words = [input().strip() for _ in range(N)]

# Store original indices
word_indices = {word: idx for idx, word in enumerate(words)}

# Sort words alphabetically
sorted_words = sorted(words)

max_prefix_length = -1
best_pair = (None, None)

# Compare each word with the next k words (k=3 should be sufficient)
k = 3  # We can compare each word with the next 3 words
for i in range(N):
    # Compare with next k words, but don't go beyond array bounds
    for j in range(i + 1, min(i + k + 1, N)):
        prefix_length = get_common_prefix_length(sorted_words[i], sorted_words[j])
        
        if prefix_length > max_prefix_length:
            # If we find a longer prefix, determine the order based on original indices
            if word_indices[sorted_words[i]] < word_indices[sorted_words[j]]:
                best_pair = (sorted_words[i], sorted_words[j])
            else:
                best_pair = (sorted_words[j], sorted_words[i])
            max_prefix_length = prefix_length
        elif prefix_length == max_prefix_length:
            # For equal prefix lengths, compare using original indices
            if word_indices[sorted_words[i]] < word_indices[sorted_words[j]]:
                curr_pair = (sorted_words[i], sorted_words[j])
            else:
                curr_pair = (sorted_words[j], sorted_words[i])
                
            curr_indices = (word_indices[curr_pair[0]], word_indices[curr_pair[1]])
            best_indices = (word_indices[best_pair[0]], word_indices[best_pair[1]])
            
            if curr_indices < best_indices:
                best_pair = curr_pair

print(best_pair[0])
print(best_pair[1])