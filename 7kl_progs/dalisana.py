a = int(input("Pirmais skaitlis:"))
b = int(input("Otrais skaitlis: "))

c = a%b
d = a//b

if c == 0:
    print(f"Skaitlis {a} dalits uz {b} bez atlikuma")
else:
    print(f"Skaitlis {a} nav dalits uz {b} bez atlikuma")

