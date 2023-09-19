import random

# List of jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "I'm reading a book on anti-gravity. It's impossible to put down!",
    "Why did the bicycle fall over? Because it was two-tired!",
    "What did the left eye say to the right eye? Between you and me, something smells.",
    "Why was the math book sad? Because it had too many problems.",
    "How do you organize a space party? You 'planet'!",
    "What do you call a fish with no eyes? Fsh!",
]


# Function to generate a random joke
def generate_random_joke():
    return random.choice(jokes)


# Displaye the random joke
random_joke = generate_random_joke()
print(random_joke)
