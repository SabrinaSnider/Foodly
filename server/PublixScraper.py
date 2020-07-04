import requests
from bs4 import BeautifulSoup

STORE_COOKIE = "%7B%22StoreName%22%3A%22Butler%20Plaza%20West%22%2C%22StoreNumber%22%3A1312%2C%22Option%22%3A%22ACDFJNORU%22%2C%22ShortStoreName%22%3A%22Butler%20Plaza%20West%22%7D"

def getPublixProductID(itemName):
  url = "https://services.publix.com/api/v3/product/Search?storeNumber=537&keyword=" + itemName
  api_response = requests.get(url).json()
  
  if(len(api_response["Products"]) == 0):
    return None
  
  return api_response["Products"][0]["Productid"]

def getItemLocation(itemName):
  # Get product ID from Publix
  productID = getPublixProductID(itemName)
  if productID is None:
    return "unknown"

  url = "http://publix.com/pd/" + productID
  
  # Set location by sending a cookie through a session.
  session = requests.Session()
  session.post(url, cookies = {'Store': STORE_COOKIE})
  
  # Make get request for product page information.
  request = session.get(url)
  page = BeautifulSoup(request.content, 'html.parser')
  
  # Extract location from page.
  locationTags = page.findAll("li", {"class" : "location"})
  
  if len(locationTags) == 0: 
    return "unknown"
    
  return locationTags[0].find("span").get_text()
