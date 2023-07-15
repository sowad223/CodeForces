
# n,k=(map(int, input().split()))
# arr = list(map(int, input().split()))
# count=0
# for i in range(n):
#     if arr[i] >= arr[k - 1] and arr[i] > 0:
#         count += 1
# print(count)
# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# count = 0
# d = {}
# for i in arr:
#     if i > 0:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#
# for key in d:
#     if key >= arr[k-1]:
#         count += d[key]
#
# print(count)
n, k = map(int, input().split())
scores = list(map(int, input().split()))

count = len([score for score in scores if score >= scores[k-1] and score > 0])

print(count)


