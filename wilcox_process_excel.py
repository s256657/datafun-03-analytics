"""
Process an Excel file to count occurrences of a price decreases year to year in a column.

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib

# Import from external packages
import openpyxl

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

def count_number_in_column(file_path: pathlib.Path, column_letter: str) -> int:
    """Count the occurrences of a negative number in a given column of an Excel file."""
    try:
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        count = 0
        for cell in sheet[column_letter]:
            if cell.value and isinstance(cell.value, (int, float)) and cell.value < 0:
                count += 1
        return count
    except Exception as e:
        logger.error(f"Error reading Excel file: {e}")
        return 0

def process_excel_file():
    """Read an Excel file, count occurrences of negative numbers in a specific column, and save the result."""
    input_file = pathlib.Path(fetched_folder_name, "changesinprice.xlsx")
    output_file = pathlib.Path(processed_folder_name, "price_decrease_count.txt")
    column_to_check = "C"  # Replace with the appropriate column letter
    number_count = count_number_in_column(input_file, column_to_check)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with output_file.open('w') as file:
        file.write(f"Occurrences of negative numbers in column'{column_to_check}': {number_count}\n")
    logger.info(f"Processed Excel file: {input_file}, Negative count svaed to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting Excel processing...")
    process_excel_file()
    logger.info("Excel processing complete.")