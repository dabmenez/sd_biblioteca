import re

def convert_to_float(value_str):
    """
    Converts a string representing a monetary value to a float.
    
    Parameters:
    value_str (str): The string to convert.
    
    Returns:
    float: The converted float value or 0.0 if conversion fails.
    """
    value_str = value_str.replace('.', '').replace(',', '.')
    try:
        return float(value_str)
    except ValueError:
        return 0.0

def extract_sections(text, regex_pattern):
    """
    Extracts sections from a given text based on a regex pattern.
    
    Parameters:
    text (str): The text to search within.
    regex_pattern (str): The regex pattern to use for extraction.
    
    Returns:
    list: A list of matched sections.
    """
    return re.findall(regex_pattern, text, re.IGNORECASE | re.DOTALL)

def debug_print(debug_info):
    """
    Prints debug information for troubleshooting purposes.
    
    Parameters:
    debug_info (dict): The debug information to print.
    """
    for key, value in debug_info.items():
        print(f"{key}: {value}")
