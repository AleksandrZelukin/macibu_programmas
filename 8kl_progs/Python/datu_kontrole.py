import datetime

d = '29.02.2024'
if len(d.split('.')) == 3:
    try:
        datetime.datetime.strptime(d, '%d.%m.%Y')
        print('Ok')
            
    except Exception:
        print('неверный формат')
else:
    try:
        datetime.datetime.strptime(d, '%d.%m')
        print('Ok')
            
    except Exception:
        print('неверный формат')