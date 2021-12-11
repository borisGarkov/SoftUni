months = int(input())
water_bill = 20
internet_bill = 15
other_bill = 0
electricity_bill_total = 0

for i in range(months):
    electricity_bill = float(input())

    electricity_bill_total += electricity_bill
    other_bill += (water_bill + internet_bill + electricity_bill) * 1.20

total_bill = other_bill + electricity_bill_total + \
             (water_bill * months) + (internet_bill * months)

print(f"Electricity: {electricity_bill_total:.2f} lv")
print(f"Water: {water_bill * months:.2f} lv")
print(f"Internet: {internet_bill * months:.2f} lv")
print(f"Other: {other_bill:.2f} lv")
print(f"Average: {total_bill / months:.2f} lv")
