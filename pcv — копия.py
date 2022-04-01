# Personas kodu validacijas programmina
# Versija 0.0.2
# (c) 2006 Alvils Berzins
# http://alvils.latvietis.com/
# Programma licenceta ar GNU GPL; detalas - http://www.gnu.org/
#
# Programmas darbinasanai nepieciesams Python - http://www.python.org/
#
# Versiju vesture:
# 0.0.2 - 21.08.2006. raw_input() izsaukums programmas beigas.
# 0.0.1 - 16.08.2006. Pirma versija.
#
import re
#
def ValidatePerscode(Perscode):
    if len(Perscode)<11 and len(Perscode)<12:
        return False
    if len(Perscode)==12:
        Perscode = Perscode[0:6] + Perscode[7:12]
    if re.search("([^0-9])", Perscode):
        return False
    ValidationData = [1,6,3,7,9,10,5,8,4,2]
    Checksum = 0
    for C in xrange(0,10):
        Checksum += int(Perscode[C]) * int(ValidationData[C])
    Checksum = (1101 - Checksum) % 11
    if Checksum != int(Perscode[10]):
        return False
    return True
#
# Tests
print ("Ievadiet personas kodu:")
Testcode = input()
Res = ValidatePerscode(Testcode)
if Res:
    print ("Kods ir derigs.")
else:
    print ("Kods NAV derigs.")
print ("Nospiediet Enter, lai beigtu darbu ar programmu.")
#input()
