!pip install pygeocodio
#Basic usage
#Import the API client and ensure you have a valid API key:

from geocodio import GeocodioClient
client = GeocodioClient(YOUR_API_KEY)

#Geocoding
#Geocoding an individual address:

geocoded_location = client.geocode("42370 Bob Hope Drive, Rancho Mirage CA")
geocoded_location.coords
(33.738987255507, -116.40833849559)

#Batch geocoding
#You can also geocode a list of addresses:

geocoded_addresses = client.geocode([
        '2 15th St NW, Washington, DC 20024',
        '3101 Patterson Ave, Richmond, VA, 23221'
    ])

#Return a list of just the coordinates for the resultant geocoded addresses:

>>> geocoded_addresses.coords
[(38.890083, -76.983822), (37.560446, -77.476008)]
>>> geocoded_addresses[0].coords
(38.890083, -76.983822), (37.560446, -77.476008)

#Lookup an address by queried address:

geocoded_addresses.get('2 15th St NW, Washington, DC 20024').coords
(38.879138, -76.981879))

# Address parsing
# And if you just want to parse an individual address into its components:

client.parse('1600 Pennsylvania Ave, Washington DC')
  {
      "address_components": {
          "number": "1600",
          "street": "Pennsylvania",
          "suffix": "Ave",
          "city": "Washington",
          "state": "DC"
      },
      "formatted_address": "1600 Pennsylvania Ave, Washington DC"
  }

