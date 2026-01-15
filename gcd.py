
from functools import reduce
from typing import Iterable, Tuple, List
import math
import re
import random

def _parse_ints(s: str) -> List[int]:
    parts = [p for p in re.split(r'[\s,]+', s.strip()) if p != '']
    return [int(p) for p in parts]

def validate_input(s: str, expected):
    """
    Validate and parse input string `s` according to `expected`:
      - 'int' -> returns int(s)
      - 'positive_int' -> returns int(s) if >= 0
      - 'ints' -> returns list[int] parsed from s (any count)
      - n (int) -> expects exactly n integers and returns list[int]
    Raises ValueError on invalid input.
    """
    s = s.strip()
    if expected == 'int':
        return int(s)
    if expected == 'positive_int':
        v = int(s)
        if v < 0:
            raise ValueError("Expected non-negative integer")
        return v
    if expected == 'ints':
        vals = _parse_ints(s)
        if not vals:
            raise ValueError("No integers found")
        return vals
    if isinstance(expected, int):
        vals = _parse_ints(s)
        if len(vals) != expected:
            raise ValueError(f"Expected exactly {expected} integers, got {len(vals)}")
        return vals
    raise ValueError("Unknown expected type")

def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

def gcd_list(nums: Iterable[int]) -> int:
    nums = list(nums)
    if not nums:
        return 0
    return reduce(gcd, nums)

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean algorithm.
    Returns (g, x, y) such that g = gcd(a, b) and a*x + b*y = g.
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t

def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)

def modinv(a: int, m: int) -> int:
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse for {a} mod {m} (gcd={g})")
    return x % m

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

def miller_rabin(n: int, k: int = 5) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

if __name__ == "__main__":
    while True:
        print("\nOptions: (g)cd  (e)xtended-gcd  (p)rime-check  (m)iller-rabin  (q)uit")
        choice = input("Choose: ").strip().lower()
        if choice == 'q':
            break
        if choice == 'g':
            s = input("Enter integers separated by space or comma (e.g. 48 18 12): ")
            try:
                nums = validate_input(s, 'ints')
            except ValueError as e:
                print("Invalid numbers:", e)
                continue
            result = gcd_list(nums) if len(nums) > 1 else abs(nums[0])
            print("GCD ->", result)
        elif choice == 'e':
            s = input("Enter two integers (a b) to compute extended gcd: ")
            try:
                a, b = validate_input(s, 2)
            except ValueError as e:
                print("Invalid input:", e)
                continue
            g, x, y = extended_gcd(a, b)
            print(f"gcd({a}, {b}) = {g}; coefficients x = {x}, y = {y}  (a*x + b*y = g)")
        elif choice == 'p':
            s = input("Enter integer to check for prime: ")
            try:
                n = validate_input(s, 'int')
            except ValueError as e:
                print("Invalid integer:", e)
                continue
            print(f"{n} is prime ->", is_prime(n))
        elif choice == 'm':
            s = input("Enter integer to test (Miller-Rabin): ")
            try:
                n = validate_input(s, 'int')
            except ValueError as e:
                print("Invalid integer:", e)
                continue
            k_s = input("Rounds (k, default 5): ").strip()
            try:
                k = int(k_s) if k_s != '' else 5
            except ValueError:
                print("Invalid rounds; using default 5.")
                k = 5
            print(f"{n} is probably prime ->", miller_rabin(n, k))
        else:
            print("Unknown option.")
