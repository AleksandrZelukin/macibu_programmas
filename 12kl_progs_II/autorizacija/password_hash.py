from werkzeug.security import check_password_hash, generate_password_hash


a = input("Parole>> ")
pwd = generate_password_hash(a)
print(pwd)

print(check_password_hash(pwd,a))
