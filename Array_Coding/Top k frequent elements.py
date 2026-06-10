from collections import Counter

nums = [1,1,1,2,2,3]
k = 2

def check(nums, k):
    counts =Counter(nums)
    
    top_k_items = counts.most_common(k)
    print(top_k_items)
    lt = []
    for i in top_k_items:
        lt.append(i[0])
    print(lt)
check(nums,k)        