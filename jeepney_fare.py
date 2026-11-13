distance = int(input("Enter distance in km: "))
discount = input("Do you get a discount? (Y/N): ").upper()

if distance <= 4:
    fare = 13.00
else:
    fare = 13.00 + (distance - 4) * 1.80

if discount == "Y":
    fare = fare * 0.80

print(f"Fare: PHP {fare:.2f}")
