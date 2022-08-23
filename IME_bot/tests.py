date = '11/05/2022'
month = '11/05/2022'

date_b = date[0:2]

month_b = month[3:5]
print(month_b)

if month_b[0] == str(0):
    month_b = int(month[4])
    month = int(month_b - 1)
    print(month)
else:
    month_b = int(month[3:5])
    month = int(month_b - 1)
    print(month)
if date_b[0] == str(0):
    date = date[1]
    print(date)
else:
    date = date_b
    print(date)


