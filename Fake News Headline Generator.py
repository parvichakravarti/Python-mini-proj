#import the random module
import random

#Create Subjects
subjects = [
    "Shahrukh Khan",
    "Virat Kolhi",
    "Nirmala Sitaraman",
    "A Mumbai Cat",
    "A Group of Monkey",
    "Prime Minister Modi",
    "Auto Rikshaw Driver from Delhi"
]

actions = [
    "launches rocket",
    "cancels ticket",
    "dance with boxer",
    "eats fish",
    "declares war on apple",
    "orders cake",
    "celebrates birthday"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

#start the headine generator loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = f" Breaking News: {subject} {action} {places_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip()
    if user_input == "no":
        break

#print goodbye message
print("\nThanks for using the Fake News Headline Generator. Have a fun day")