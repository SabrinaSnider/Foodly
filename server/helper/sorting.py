import pandas as pd
from functools import cmp_to_key


def organize_list(data, location_key):
  grouped = group_by_location(data, location_key)
  return grouped if grouped is None else sorted(grouped.items(), key=cmp_to_key(compare_location))

def group_by_location(data, location_key):
  if not data: return None
  dataframe = pd.DataFrame(data)
  return dataframe.groupby(location_key).apply(lambda x: x.to_dict(orient='records'))

def compare_location(A, B):
  location_A = A[0]
  location_B = B[0]
  if 'Aisle' not in location_A: return -1 # if A is not in an aisle, put it first
  if 'Aisle' not in location_B: return 1 # if B is not in an aisle, put it first

  aisle_A = int(location_A.split("Aisle ", 1)[1])
  aisle_B = int(location_B.split("Aisle ", 1)[1])
  return aisle_A - aisle_B
