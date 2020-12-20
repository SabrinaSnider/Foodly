import pandas as pd
from functools import cmp_to_key


def groupByLocationAndSort(data, locationKey):
  grouped = groupByLocation(data, locationKey)
  return sorted(grouped.items(), key=cmp_to_key(compareLocation))

def groupByLocation(data, locationKey):
  if not data:
    return None
  dataframe = pd.DataFrame(data)
  return dataframe.groupby(locationKey).apply(lambda x: x.to_dict(orient='records'))

def compareLocation(A, B):
  locationA = A[0]
  locationB = B[0]
  if 'Aisle' not in locationA: # if A is not an 'aisle,' put A first
    return -1
  if 'Aisle' not in locationB: #if A is an 'aisle' but B is not, put B first
    return 1
  aisleA = int(locationA.split("Aisle ",1)[1])
  aisleB = int(locationB.split("Aisle ",1)[1])
  return aisleA - aisleB
