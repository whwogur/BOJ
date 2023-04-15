# 1644 소수의 연속합
n = int(input())
a = [False, False] + [True for _ in range(n)]
primes = []

for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

answer, start, end = 0, 0, 0
while end <= len(primes):
    temp = sum(primes[start:end])
    if temp == n:
        answer += 1
        end += 1
    elif temp < n:
        end += 1
    else:
        start += 1

print(answer)

'''
def prime_list(a: int, b: int = -1) -> list[int]:
    """Returns a list of prime numbers in the given range, [1, a] or [a, b]."""

    beg, end = (1, a + 1) if b < 0 else (min(a, b), max(a, b) + 1)
    if end < 5:
        return [i for i in range(beg, end) if i in (2, 3)]
    n = end + 6 - end % 6
    sieve = [False] + [True] * (n // 3 - 1)
    for i in range(math.isqrt(n) // 3 + 1):
        if sieve[i]:
            d, s, j = (k := 1 | 3 * i + 1) * 2, k * k, k * (k + 4 - 2 * (i & 1))
            sieve[s // 3::d] = [False] * ((n // 6 - s // 6 - 1) // k + 1)
            sieve[j // 3::d] = [False] * ((n // 6 - j // 6 - 1) // k + 1)
    b, e = (beg | 1) // 3, n // 3 - 2 + (end % 6 > 1)
    return ([p for p in (2, 3) if p >= beg] +
            [1 | 3 * i + 1 for i in range(b, e) if sieve[i]])

def main():
    N = int(input())

    primes = prime_list(N)
    left_iter, right_iter = iter(primes), iter(primes)
    prime_sum = answer = 0
    while True:
        try:
            if prime_sum == N:
                answer += 1
            if prime_sum <= N:
                prime_sum += next(right_iter)
            else:
                prime_sum -= next(left_iter)
        except StopIteration:
            break

    print(answer)


if __name__ == '__main__':
    main()
'''