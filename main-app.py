import os
import json
import eyed3
import logging
from tqdm import tqdm

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

eyed3_logger = logging.getLogger("eyed3")
eyed3_logger.setLevel(logging.ERROR)

def find_mp3_files(folder_path):
    mp3_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp3"):
                mp3_files.append(os.path.join(root, file))
    return mp3_files

def extract_artist_names(mp3_files):
    artist_counts = {}
    for mp3_file in tqdm(mp3_files, desc="Processing MP3 files", unit="file"):
        try:
            audio_file = eyed3.load(mp3_file)
            if audio_file.tag:
                artist = audio_file.tag.artist
                if artist:
                    if artist in artist_counts:
                        artist_counts[artist] += 1
                    else:
                        artist_counts[artist] = 1
            else:
                logger.warning(f"Skipping file '{mp3_file}' due to missing or improperly formatted metadata")
        except Exception as e:
            logger.error(f"Error processing file '{mp3_file}': {e}")
    return artist_counts

def save_artist_counts_to_json(artist_counts, output_file):
    with open(output_file, "w") as f:
        json.dump(artist_counts, f, indent=4)

def main():
    folder_path = "d:\my music"
    output_file = "artist_counts.json"

    mp3_files = find_mp3_files(folder_path)
    logger.info(f"Found {len(mp3_files)} MP3 files in the folder '{folder_path}'")

    artist_counts = extract_artist_names(mp3_files)
    logger.info(f"Found {len(artist_counts)} unique artist names")

    save_artist_counts_to_json(artist_counts, output_file)
    logger.info(f"Saved artist counts to '{output_file}'")

if __name__ == "__main__":
    main()
