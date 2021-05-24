def prime_check(number):
    flag = 0
    for c in range(2, number // 2 + 1):
        if number % c == 0:
            flag = 1
            break
    if flag == 1:
        return True
    else:
        return False


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def primRoots(modulo):
    roots = []
    required_set = set(num for num in range(1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range(1, modulo))
        if required_set == actual_set:
            roots.append(g)
    return roots


if __name__ == "__main__":
    p = int(input("Enter any prime number:"))
    while prime_check(p):
        p = int(input("Re-Enter any prime number:"))
    primitive_roots = primRoots(p)
    print(primitive_roots)

p1 = int(input("select any primitive number:"))

xa = int(input("Enter the private key value for user A:"))
ya = (p1 ** xa) % p
print("\nPublic key value for user A is:", ya)

xb = int(input("Enter the private key value for user B:"))
yb = (p1 ** xb) % p
print("\nPublic key value for user B is:", yb)

print("\n")
print("privately calculated shared secret:")
user_a = (yb ** xa) % p
print("User A shared secret key value is:", user_a)

user_b = (ya ** xb) % p
print("User B shared secret key value is:", user_b)
