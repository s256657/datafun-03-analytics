"""
Process a text file to count occurrences of the word "Romeo" and save the result.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib

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

def count_word_occurrences(file_path: pathlib.Path, word: str) -> int:
    """Count the occurrences of a specific word in a text file (case-insensitive)."""
    try:
        with file_path.open('r') as file:
            content: str = file.read()
            return content.lower().count(word.lower())
    except Exception as e:
        logger.error(f"Error reading text file: {e}")
        return 0

def process_text_file():
    """Read a text file, count occurrences of 'Romeo', and save the result."""
    input_file = pathlib.Path(fetched_folder_name, "solar_flares.txt")
    output_file = pathlib.Path(processed_folder_name, "month_flare_count.txt")
    words_to_count: str = "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    word_counts = {}
    for word in words_to_count:
        word_counts [word] = count_word_occurrences (input_file, word)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open('w') as file:
        file.write(f"Occurrences of '{word}': {word_counts}\n")
    logger.info(f"Processed text file: {input_file}, Word count saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting text processing...")
    process_text_file()
    logger.info("Text processing complete.")