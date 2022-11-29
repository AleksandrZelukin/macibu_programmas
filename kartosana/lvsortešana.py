lv={'ā':'a','č':'c','ē':'e','ģ':'g','ī':'i','ķ':'k','ļ':'l','ņ':'n','š':'s','ū':'u','ž':'z'}
def lvkey(text):
    key1 = ""
    key2 = ""
    for c in text:
        k= 0
        if c.isupper():
            k+= 1
            c = c.lower()

        if c in lv:
            k += 2
            c = lv[c]

        key1 += c
        key2 += str(k)

    return key1, key2

a = ['sākums', 'sala', 'auglis']

for i in sorted(a, key=lvkey):
    print(i)

            
