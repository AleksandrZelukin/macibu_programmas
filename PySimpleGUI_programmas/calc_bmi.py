def calc_bmi(h,w):
    try:
        h, w = float(h), float(w)
        bmi = round(w / h **2, 1)
        if bmi < 18.5:
            standard = "Extra vājš"
        elif 18.5 <= bmi <= 23.9:
            standard = "Normāls"
        elif 24.0 <= bmi <= 27.9:
            standard = "lieks svars"
        else:
            standard = "trekns"
    except (ValueError, ZeroDivisionError):
        return None
    else:
        return (f'BMI: {bmi}, {standard}')

a=calc_bmi(170,90)
print(a)