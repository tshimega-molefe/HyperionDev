# Function to print dictionary values given the keys
def print_values_of(
    dictionary, *keys
):  # Fixed Error 1: Changed 'keys' to '*keys' to accept multiple arguments
    for key in keys:
        print(
            dictionary.get(key)
        )  # Fixed Error 2: Corrected variable name and used .get() for safer access


# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {
    "lisa": "BAAAAAART!",
    "bart": "Eat My Shorts!",
    "marge": "Mmm~mmmmm",
    "homer": "d'oh!",  # Fixed Error 3: Fixed string quotation formatting
    "maggie": "(Pacifier Suck)",
}

print_values_of(simpson_catch_phrases, "lisa", "bart", "homer")

"""
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

"""
