from typing import Tuple

import pdfplumber
import re


# Regex to capture a number (that may have decimals or commmas) and the 
# following characters that may represent the units that the number is
NUMBER_REGEX = "([-+]?\\d*\\.?\\d+(?:,\\d+)?)\\s*([a-zA-Z]+)?"


def get_unit_factor(text: str) -> int:
    """
    Determine the number's units (i.e. thousands, millions, etc.)

    Args:
        text (str): Text we want to check

    Returns:
        int: The unit factor that we found
    """
    
    if not text:
        return 1
    
    text = text.lower()
    if "million" in text or "$(M)" in text:
        return 1000000
    elif "billion" in text:
        return 1000000000
    elif "thousand" in text:
        return 1000
    return 1


def extract_info_from_pdf(pdf_path: str) -> Tuple[list, list]:
    """
    Extract the content from the PDF on a per page basis.

    Args:
        pdf_path (str): Path to PDF file

    Returns:
        list: List of text extracted from the PDF per page
        list: List of tables extracted forom the PDF per page
    """
    
    pdf_pages = []
    with pdfplumber.open(pdf_path) as pdf:
        pdf_pages = [page.extract_text() for page in pdf.pages]
        pdf_tables = [page.extract_tables() for page in pdf.pages]
    
    return pdf_pages, pdf_tables


def find_numbers_with_units_in_text(pdf_pages: list) -> list:
    """
    Find the numbers, conidering units in the PDF
    
    Args:
        pdf_pages (list): List of PDF pages
    
    Returns:
        numbers (list): List of the numbers found
    """ 
    
    numbers = []
    for text in pdf_pages:
        if not text:
            continue
        
        matches = re.findall(NUMBER_REGEX, text)
        for num, unit in matches:
            if num:
                num = float(num.replace(",", ""))
                try:
                    numbers.append(num * get_unit_factor(unit))
                except ValueError:
                    pass
    return numbers


def find_numbers_with_units_in_tables(pdf_pages: list, pdf_tables: list) -> list:
    """
    Find the numbers from tables that we extract from a PDF while considering units

    Args:
        pdf_pages (list): List of PDF pages
        pdf_tables (list): List of tables found in the PDF

    Returns:
        list: List of the numbers found
    """

    numbers = []
    units = [get_unit_factor(text) for text in pdf_pages]
            
    for i, tables in enumerate(pdf_tables):
        unit = units[i]
        for table in tables:
            # For row in table, if there is a row append the cell if there is a cell in the row
            cells = [cell for row in table if row for cell in row if cell]
            
            for cell in cells:
                matches = re.findall(NUMBER_REGEX, cell)
                for num, _ in matches:
                    if num:
                        num = float(num.replace(",", ""))
                        try:
                            numbers.append(num * unit)
                        except ValueError:
                            pass
    return numbers