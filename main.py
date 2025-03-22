import streamlit as st

from utils import (
    extract_info_from_pdf,
    find_numbers_with_units_in_tables, 
    find_numbers_with_units_in_text
)


st.header("Find Largest Number In Document")

uploaded_file = st.file_uploader("Upload File (.pdf format)")
find_largest_num = st.button("Find the Number!")
if uploaded_file and find_largest_num:
    with st.spinner("Finding largest number...", show_time=True):
        pages, tables = extract_info_from_pdf(uploaded_file)
        numbers_in_text = find_numbers_with_units_in_text(pages)
        numbers_in_tables = find_numbers_with_units_in_tables(pages, tables)
        
    st.write(f"Largest Number Found: {max(max(numbers_in_text), max(numbers_in_tables))}")
    
elif not uploaded_file and find_largest_num:
    st.error("Please upload a file first!")