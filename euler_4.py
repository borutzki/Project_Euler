# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

max = 0
for i in range(999,99,-1):
    for n in range(999,99,-1):
        res = i*n
        if str(res)[::-1] == str(res):
            if res > max:
                max = res
            break
print(max)
    