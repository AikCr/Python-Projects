letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

zipped_letters = zip(letters, points)
letter_to_points = {key:value for key, value in zipped_letters}
letter_to_points[" "] = 0

#takes in a word and returns how many points it is worth
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total   

# dictionary that maps players to a list of words they played
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"], 
  "wordNerd": ["EARTH", "EYES", "MACHINE"], 
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"], 
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

#iterates through items in player_to_words
for player, words in player_to_words.items():
  player_points = 0
#nested loop that goes through each word in words and adds value of score_word
  for word in words:
    player_points += score_word(word)
#sets current player value to be key of player_to_points with value of player+points
  player_to_points[player] = player_points 

print(player_to_points)
