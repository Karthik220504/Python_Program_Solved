def even_odd_permutations(low, high, k, sum=0):
    MOD = 10**9 + 7

    if k == 0:
        return 1 if sum % 2 == 0 else 0

    count = 0
    for num in range(low, high + 1):
        count += even_odd_permutations(low, high, k - 1, sum + num)
        #count %= MOD

    return count

# Example usage
low, high = map(int, input().split())
k = int(input())
print(even_odd_permutations(low, high, k))
