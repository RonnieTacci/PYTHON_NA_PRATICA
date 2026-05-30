from datetime import date

data = date(2026, 12, 10)

# data.day = 10
# data.day == 25 -> False
# data.month = 12
# data.month == 12 -> True
# False and True -> False
if (data.day == 25) and (data.month == 12):
    print("É natal!")
else:
    print("Não é natal")