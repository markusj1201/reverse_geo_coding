#Reverse geocoding
#Reverse geocode a point to find a matching address:

location = client.reverse((33.738987, -116.4083))
location.formatted_address
"42370 Bob Hope Dr, Rancho Mirage CA, 92270"

# Batch reverse geocoding
# And multiple points at a time:

locations = client.reverse([
    (33.738987, -116.4083),
    (33.738987, -116.4083),
    (38.890083, -76.983822)
 ])
 
# Return the list of formatted addresses:

locations.formatted_addresses
["42370 Bob Hope Dr, Rancho Mirage CA, 92270",  "42370 Bob Hope Dr, Rancho Mirage CA, 92270", "2 15th St NW, Washington, DC 20024"]

# Access a specific address by queried point tuple:

locations.get("38.890083,-76.983822").formatted_address
"2 15th St NW, Washington, DC 20024"

# Or by the more natural key of the queried point tuple:

locations.get((38.890083, -76.983822)).formatted_address
"2 15th St NW, Washington, DC 20024"
