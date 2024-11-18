import requests
import random

# Function to fetch random words
def get_random_words(count):
    try:
        # Using an online API to get random words
        response = requests.get(f"https://random-word-api.herokuapp.com/word?number={count}")
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch random words. Using fallback list.")
    except Exception as e:
        print(f"Error: {e}. Using fallback list.")
    # Fallback list of terms if API fails
    return [
        "technology", "education", "travel", "programming", "fitness",
        "space", "artificial intelligence", "finance", "recipes", "sports"
    ]

# Number of random terms to generate
num_searches = 30

# Fetch random words
search_terms = get_random_words(num_searches)

# Display the terms
print("Copy and paste the following terms into Bing:")
for term in search_terms:
    print(term)

