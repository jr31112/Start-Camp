import random
numbers = range(1,46)
# print(sorted(random.sample(numbers,6)))
lotto = random.sample(numbers,6)
# print(sorted(lotto))
lotto.sort()
print(lotto)