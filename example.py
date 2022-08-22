# BOJ 2018 문제
from collections import Counter

N = int(input())

S = [int(input() for _ in range(N))] # list comprehension
# for i in range(N):
#     S.append(int(input()))

S.sort()

# print(sum(S)//N)
# print(S[len(2)//2])
# print(Counter(S).most_common())
# print(max(S)-min(S))

print(sum(S)//N)
print(S[N(2)//2])
print(Counter(S).most_common())
print(max(S)-min(S))