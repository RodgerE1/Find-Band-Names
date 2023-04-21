 # Find Band Names 🎸🎵

Find Band Names is a Python script that scans a folder containing MP3 files and extracts the unique artist names from the files' metadata. The artist names are saved to a JSON file for further processing or analysis.

## 📦 Dependencies

- Python 3.6 or higher
- eyed3
- tqdm

## 🛠 Installation

1. Clone the repository or download the `main-app.py` script.
2. Install the dependencies using `pip`:

## 🚀 Usage

1. Open the `main-app.py` script in your favorite text editor.
2. Replace `path/to/mp3/folder` with the path to the folder containing your MP3 files.
3. (Optional) Change the output JSON file name if desired (default is `artist_names.json`).
4. Save the script.
5. Open a terminal/command prompt and navigate to the directory containing the script.
6. Run the script using:


7. The script will scan the specified folder for MP3 files, extract the unique artist names, and save them to the output JSON file. Progress information and log messages will be displayed in the terminal/command prompt.

## 📝 Notes

- The script only supports MP3 files with ID3 tags. Files with missing or incorrect metadata may result in incomplete or inaccurate extraction of artist names.
- If you encounter any issues or need to modify the script for your specific use case, please refer to the [eyed3 documentation](https://eyed3.readthedocs.io/) and [tqdm documentation](https://tqdm.github.io/) for more information.

## 📜 License

This project is released under the [MIT License](https://opensource.org/licenses/MIT).


