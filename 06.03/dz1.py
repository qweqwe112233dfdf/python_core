def nsd(a, b):
    if b == 0:
        return a
    return nsd(b, a % b)

print(nsd(48, 18))