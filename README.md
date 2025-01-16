# Captions-Merger

This Python script merges multiple text files (.txt) from the current folder into a single file, keeping the original filename as a prefix for each line.

## Description

The script performs the following operations:
1. Searches for all .txt files in the execution folder
2. Creates a new file named `caption_list.txt` (or `caption_list_N.txt` if the file already exists)
3. For each text file found:
   - Reads the content
   - Removes line breaks
   - Adds a new line in the unified file with the format: `[filename] [content]`

## Requirements

- Python 3.x
- The modules used (`os` and `glob`) are part of Python's standard library, so no additional installations are needed.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Tranchillo/Captions-Merger.git
```

2. Navigate to the project directory:
```bash
cd Captions-Merger
```

## Usage

1. Place the script in the folder containing the .txt files you want to merge
2. Run the script:
```bash
python Captions-Merger.py
```

The program will create a new file `caption_list.txt` (or `caption_list_N.txt` if the file already exists) containing all unified texts.

## Output

- The output file will be named `caption_list.txt`
- If a file with this name already exists, a file with progressive numbering will be created (e.g., `caption_list_1.txt`)
- Each line in the output file will have the format: `[filename] [content]`

## Error Handling

The script includes error handling for:
- Folder without .txt files
- Individual file reading errors
- General execution errors

## Contributing

Feel free to open issues or submit pull requests to improve this project.

## License

MIT License
