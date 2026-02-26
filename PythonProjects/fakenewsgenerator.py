import random

subjects = [
    "Siddharth Kapur",
    "Anushka Sharma",
    "Bhupendra Patel",
    "A Bharuch Kharising",
    "A Group of Donkeys",
    "Prime Minister Narendra Modi",
    "Auto Rickshaw Driver From Ankleshwar"
]

actions = [
    "has been caught stealing",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of samosa",
    "at a wedding",
    "during a cricket match",
    "in the USA"
    
]

# Generate random news headline
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"{subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo You Want Another Headline? (yes/no): ").strip().lower()

    if user_input == "no":
        print("Thank you for using the Fake News Generator!")
        break