def a(mala_a, mala_b=12, mala_c=12):
    if mala_a + mala_b > mala_c and mala_a + mala_c > mala_b and mala_b + mala_c > mala_a:
        return "Trijstūris ir derīgs"
    else:
        return "Trijstūris nav derīgs"

x = int(input("Ievadiet pirmās malas garumu: "))
y = int(input("Ievadiet otras malas garumu: "))
# z = int(input("Ievadiet trešās malas garumu: "))

print(a(x, y))