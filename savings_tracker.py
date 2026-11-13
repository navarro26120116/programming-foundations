
total_saved = 0
days = 0

while True:
    savings = float(input("Savings today (0 to stop): "))

    if savings == 0:
        break

    total_saved += savings
    days += 1

print(f"Total saved in {days} days: PHP {total_saved:,.2f}")
