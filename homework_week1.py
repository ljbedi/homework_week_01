# COMMIT TEST 

users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

print(users["Jonathan"]["twitter"])


# 2. Get Erik's hometown

print(users["Erik"]["home_town"])

# 3. Get the list of Erik's lottery numbers

print(users["Erik"]["lottery_numbers"])

# 4. Get the species of Avril's pet Monty

print(users["Avril"]["pets"][0]["species"])
# print(users["Erik"]["pets"][3]['species']) < EXPECTING THIS TO BE PARROT 

# 5. Get the smallest of Erik's lottery numbers

erik_lowest_lottery = min(users["Erik"]["lottery_numbers"])
print(erik_lowest_lottery)
      
# TO FIND THE MINIMUM - MIN

# 6. Return an list of Avril's lottery numbers that are even

avril_lottery_numbers = users["Avril"]["lottery_numbers"]
avril_even_numbers = []

for number in avril_lottery_numbers:
    if number % 2 == 0:
        avril_even_numbers.append(number)

print(avril_even_numbers)

# What are we doing? We are wanting even lottery numbers, where do we get the numbers from? Path to the source
# avril_lottery_numbers FROM users > Avril > Lottery numbers.
# Now we have told where we want the loop to look, we need to say we want the even numbers from it. 
# DEFINE THAT > avil_even_numbers (needs a value to add to) - () or []?? 
# We have to give it a value out of the loop = 0? THIS WILL THEN BE FILLED WITH VALUES AS THE LOOP RUNS?? 
# LOOP - for every even number in the list, add it to our list of even numbers (avril_even_numbers = []? append?
# So we need the loop to check for even? number % 2 == 0. if they are even then add to our list of even numbers, list 
# them together and then print them off 



# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers


# 8. Change Erik's hometown to Edinburgh


# 9. Add a pet dog to Erik called "fluffy"


# 10. Add another person to the users dictionary