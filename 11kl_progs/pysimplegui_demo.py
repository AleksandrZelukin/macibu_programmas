valsts_pilseta = {
  'Vācija': 'Berlīne',
  'Latvija': 'Rīga',
  'Lietuva': 'Viļņa'
}
while True:
  lietotajs = input('Ievadi valsti: ')
  if lietotajs in valsts_pilseta:
    print(valsts_pilseta[lietotajs])
    break
  else:
    print(valsts_pilseta)
    break