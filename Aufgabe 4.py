#BMI

yourName = input("wie heisst du? Ich heisse Ezekiel...")
yourWeight = int(input("Wie schwer bist du in KG?"))
yourHeight = int(input("Wie Gross bist du in CM?")) / 100

yourBMI = yourWeight / (yourHeight ** 2)

print(yourName + ", dein BMI ist " + str(yourBMI))
