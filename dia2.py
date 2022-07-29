#Si la cuenta fue de $150.00, dividir entre 5 personas, con 12% de propina.
#Cada persona debe pagar (150.00 / 5) * 1.12 = 33.6
#Formatea el resultado a 2 decimales = 33.60
#Consejo: Hay 2 formas de redondear un número. Es posible que tengas que buscar en Google para resolver esto.💪

print("Welcom to the tip calculator\n")
total = input("How much was the total bill?\n")
tip = input("How much percentage tip do you want to give?\n")
people = input("How many people split the account\n")

porcentage = float(tip) / 100
tip_money = float(total) * porcentage
total_bill = float(total) + float(tip_money)

final_amount = total_bill / int(people)
final_amount = "{:.2f}".format(final_amount)
print(f"Each person must pay: ${final_amount} ")