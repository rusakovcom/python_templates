def percentage_changed(sum1, sum2):
  if sum1 == 0:
    return 'sum1 cannot be 0'
  direction = "decrease" if sum2 < sum1 else "increase"
  percent = round(100 * abs(sum2 - sum1) / sum1, 2)
  return f"{percent}% {direction}"



sum1 = float(input('sum1: '))
sum2 = float(input('sum2: '))
print(percentage_changed(sum1, sum2))

# test cases:
# print(percentage_changed(1000, 840))  #  "16% decrease"
# print(percentage_changed(100, 950))  #  "850% increase"
# print(percentage_changed(500, 250))  #  "50% decrease"
# print(percentage_changed(1200, 1800))  #  "50% increase"
# print(percentage_changed(600, 600))  #  "0% no change"
# print(percentage_changed(800, 200))  #  "75% decrease"
# print(percentage_changed(400, 2000))  #  "400% increase"