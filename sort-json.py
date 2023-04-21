import json
from collections import Counter

try:
    # Open the input file
    with open("artist_counts.json", encoding="utf-8", errors="ignore") as f:
        try:
            artists = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")
            raise

    # Convert the dictionary to a Counter object
    counter = Counter(artists)

    # Get the top 50 artists with the highest counts
    top_50_artists = counter.most_common(50)

    # Write the top 50 artists to a text file
    with open("top_50_artists.txt", "w", encoding="utf-8") as f:
        for artist, count in top_50_artists:
            f.write("{0}: {1}\n".format(artist, count))

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")
