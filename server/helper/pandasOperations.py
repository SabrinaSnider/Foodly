import pandas as pd

def groupByLocation(data, key):
  dataframe = pd.DataFrame(data)
  return dataframe.groupby(key).apply(lambda x: x.to_dict(orient='records'))
