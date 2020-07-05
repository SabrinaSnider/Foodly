import requests

def getPublixProductInfo(itemName):
  url = "https://services.publix.com/api/v3/product/Search?storeNumber=537&keyword=" + itemName
  api_response = requests.get(url).json()
  
  if(len(api_response["Products"]) == 0):
    return None

  data = api_response["Products"][0]
  location = extractLocation(data['rsslocation'])

  if 'section' in location:
    return {
      "productId": data["Productid"],
      "aisle": location['aisle'],
      "section": location['section']
    }
  else:
    return {
      "productId": data["Productid"],
      "aisle": location['aisle'],
    }

def extractLocation(location) :
  split = location.split(' - ')
  if len(split) > 1:
    return {
      "aisle": split[0],
      "section": split[1],
    }
  else:
    return {
      "aisle": split[0]
    }
