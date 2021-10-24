# Zadanie 7 + 8 

import requests 
import argparse

class Brewery:
  
  def __init__(self, id, name, brewery_type, street, 
   address_2, address_3, city,state, county_province,postal_code, country,
   longitude,latitude, phone, website_url, updated_at, created_at):
    self.id = id
    self.name = name
    self.brewery_type = brewery_type
    self.street = street
    self.address_2 = address_2
    self.address_3 = address_3
    self.city = city 
    self.state = state
    self.county_province = county_province
    self.postal_code = postal_code
    self.country = country
    self.longitude = longitude
    self.latitude = latitude
    self.phone = phone
    self.website_url = website_url
    self.updated_at = updated_at
    self.created_at = created_at
   
  def __str__(self):
        return f'Brewery id: {self.id}, name: {self.name} is located in {self.city}, {self.country}. Phone number: {self.phone}, website: {self.website_url}'

def get_data():
    api_url = 'https://api.openbrewerydb.org/breweries'
    x = input('Do you want to define number of objects? yes/no?')
    if x=='yes':
      number = input('how many?')
      api_url += f'?per_page={number}'
    r = requests.get(api_url)
    data = r.json()
    
    return data
  
def add_to_list(data):
    list_b = []
    for i in data:
        id = i['id']
        name = i['name']
        brewery_type = i['brewery_type']
        street = i['street']
        address_2 = i['address_2']
        address_3 = i['address_3']
        city = i['city']
        state = i['state']
        county_province = i['county_province']
        postal_code = i['postal_code']
        country = i['country']
        longitude = i['longitude']
        latitude = i['latitude']
        phone = i['phone']
        website_url =i['website_url']
        updated_at = i['updated_at']
        created_at = i['created_at']
        obj = Brewery(id,name,brewery_type,street,address_2,address_3,city,state,county_province,postal_code,country,
        longitude,latitude,phone,website_url,updated_at,created_at)
        list_b.append(obj)
    return list_b

def show_objects(list_b):
      for i in list_b:
          print(i)

if __name__== '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--city')
  result = parser.parse_args()
  if result.city:
    data = (requests.get(f'https://api.openbrewerydb.org/breweries?by_city={result.city}')).json()
  else:
    data = get_data()


list_b = add_to_list(data)
show_objects(list_b)


