def skaitlis(sk):
    a={"1":"viens","2":"divi"}
    return a.get(sk,"Nepareizi!")
x = input()
print(skaitlis(x))