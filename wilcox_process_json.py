"""
Process a JSON file to count number of found meteorite landings and save the result.

JSON file is in the format where meteorite data is a list of dictionaries with key "found".

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import json

# Import from local project modules
from util_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "wilcox_data"
processed_folder_name: str = "wilcox_data_processed"

#####################################
# Define Functions
#####################################

def count_found_meteorites(file_path: pathlib.Path, word: str) -> int:
    """Count the number of meteorites found from a JSON file."""
    word_count = 0

    try:
        with file_path.open('r') as file:
            # Use the json module load() function 
            # to read data file into a Python dictionary
            meteorite_dictionary = json.load(file)  
            # initialize an empty dictionary to store the counts
            def search_for_word(data):
                nonlocal word_count
                if isinstance(data, str):
                    word_count += data.lower().count(word.lower())  
                elif isinstance(data, list):
                    for item in data:
                        search_for_word(item)
                elif isinstance(data, dict):
                    for key, value in data.items():
                        search_for_word(value)
            search_for_word(meteorite_dictionary)
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")

    return {word_count}

def process_json_file():
    """Read a JSON file, count found meteorites, and save the result."""
    input_file: pathlib.Path = pathlib.Path (fetched_folder_name, "meteoritelandings.json")
    output_file: pathlib.Path = pathlib.Path(processed_folder_name, "found_meteorite_landings.txt")
    
    meteorites_found = count_found_meteorites(input_file, "found")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write(f"Meteorites found: {meteorites_found}\n")
    
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")