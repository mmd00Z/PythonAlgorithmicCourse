numbers = [15, 14, 17, 16, 12.5, 20, 20, 20]

i = 0
sum_value = 0
while i < len(numbers):
  sum_value += numbers[i]
  i += 1

print(sum_value / len(numbers))