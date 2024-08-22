# Created list of destinations and a test traveler
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]
#test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

# defined function to find index of specific location in the destinations list
def get_destination_index(destination):
  index = destinations.index(destination)
  return index

# tested out function by printing index of Paris, France (0)
#print(get_destination_index("Paris, France"))

# defined function to retrieve index of the travel destination of test traveler
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

# tested out function by printing index of Erin Wilkes destination 
#test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)

# makes empty list of attractions same size as destinations list
attractions = [[] for destination in destinations]
#print (attractions)

# locates index of destination in list and adds attraction to the corresponding index in the attractions list
def add_attraction(destination, attraction):
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return

# added more attractions for each of the 5 destinations
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
#print (attractions)
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
#destination_index saves destinations index
  destination_index = get_destination_index(destination)
#attractions_in_city looks up destinations attractions in attractions list
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
#for loop that saves each item from attractions_in_city into a variable called possible_attraction
  for attraction in attractions_in_city:
    possible_attraction = attraction
#for each attraction, tagged info about it (from index 1 of the attraction in attractions list) is saved into variable attraction_tags
    attraction_tags = attraction[1]
#for loop goes through provided interests and checks if they are in the attraction_tags
    for interest in interests:
      if interest in attraction_tags:
# if the given interest is in tags, the matching attraction is added to attractions with interest
        attractions_with_interest.append(possible_attraction[0])
  return attractions_with_interest

def get_attractions_for_traveler(traveler):
# saves destination and interest into variables
  traveler_destination = traveler[1]
  traveler_interests = traveler[2]
# finds attractions using destination and interests
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler[1] + ": "
# loops through traveler_attractions and adds attraction interests_string
  for tra_attr in traveler_attractions:
    interests_string += tra_attr
    return interests_string

la_arts = find_attractions("Los Angeles, USA", ['art'])

smills_france = get_attractions_for_traveler(['Dereck Smill', 'Paris, France', ['monument']])
print(smills_france)
