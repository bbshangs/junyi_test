num = int(input())
three = int(num / 3) # number of 3's multiples
five = int(num / 5)  # number of 5's multiples
fifteen = int(num / 15)  # number of 15's multiples
ans = num - (three + five - fifteen) + fifteen
print(ans)
