# 1) https://pypi.org/project/streamlit/

# 2) Terminal: cd PYTHON/XmlToPdf > pip install streamlit pandas fpdf
#                                   > streamlit run app.py

# 3) Welcome to Streamlit! / You can now view your Streamlit app in your browser.
        # Local URL: http://localhost:8501
        # Network URL: http://100.126.10.200:8501

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
from fpdf import FPDF
import io

def process_xml(xml_file):
    # --------------------------------
    # Read and parse the XML file
    # --------------------------------
    tree = ET.parse(xml_file)
    root = tree.getroot()
    # -----------------------------------------------------------------------------
    # Extract relevant data from the XML (this will depend on the structure of your XML)
    # -----------------------------------------------------------------------------
    data = []
    for child in root:
        row = {}
        for subchild in child:
            row[subchild.tag] = subchild.text
        data.append(row)

    return pd.DataFrame(data)

def create_xml_output(selected_data):
    # ----------------------------------------
    # Create a new XML root element
    # ----------------------------------------
    root = ET.Element('data')
    # ----------------------------------------
    # Add the selected data to the XML
    # ----------------------------------------
    for row in selected_data:
        item = ET.SubElement(root, 'item')
        for key, value in row.items():
            ET.SubElement(item, key).text = str(value)

    # ---------------------------------------------
    # Create an XML tree and return it as a string
    # ---------------------------------------------
    tree = ET.ElementTree(root)
    output = io.BytesIO()
    tree.write(output, encoding='utf-8', xml_declaration=True)
    output.seek(0)
    return output

# ---------------------------------------------
# Add the selected data to the PDF
# ---------------------------------------------
def create_pdf_output(selected_data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    # ---------------------------------------------
    # Get all unique keys (column names)
    # ---------------------------------------------
    all_keys = set()
    for row in selected_data:
        all_keys.update(row.keys())
    # ---------------------------------------------
    # Sort the keys alphabetically
    # ---------------------------------------------
    sorted_keys = sorted(all_keys)
    # ---------------------------------------------
    # Calculate the width of each column (assuming a maximum page width of 210 mm)
    # ---------------------------------------------
    num_columns = len(sorted_keys)
    column_width = 210 / num_columns
    # ---------------------------------------------
    # Print column headers
    # ---------------------------------------------
    for key in sorted_keys:
        pdf.cell(column_width, 10, txt=key, border=1, align='C')  # Center the text in the header
    pdf.ln()
    # ---------------------------------------------
    # Print data in columns
    # ---------------------------------------------
    for row in selected_data:
        for key in sorted_keys:
            value = row.get(key, "")  # Get the value or an empty string if the key doesn't exist
            pdf.cell(column_width, 10, txt=str(value), border=1)
        pdf.ln()

    # ----------------------------
    # Return the PDF as bytes
    # ----------------------------
    output = io.BytesIO()
    pdf.output(dest='S').encode('latin-1')
    output.write(pdf.output(dest='S').encode('latin-1'))
    output.seek(0)
    return output

def main():
    # ---------------------------------------------------------
    # ---------------------------------------------------------
    # Page configuration / Title / icon / subtitle
    # ---------------------------------------------------------
    # ---------------------------------------------------------
    st.set_page_config(
        page_title="Tool to process XML data",
        page_icon="images/EC-IT-LOGO-1.png",
        layout="centered"
    )
    st.subheader("Tool to process XML data.")

    xml_file = st.file_uploader("Upload file", type="xml")

    if xml_file:
        df = process_xml(xml_file)
        st.subheader("Loaded data")
        st.dataframe(df)

        # ---------------------------------------------------------
        # Multiple row selection (without repetition)
        # ---------------------------------------------------------
        selected_rows = st.multiselect("Select rows for the report", options=range(len(df)), key="selected_rows")

        if st.button("Download XML"):
            if selected_rows:  # Check if rows have been selected
                selected_data = df.iloc[selected_rows].to_dict('records')
                output = create_xml_output(selected_data)
                st.download_button("Download XML", output, "selected_data.xml", "text/xml")
            else:
                st.warning("Please select at least one row before downloading.")

        if st.button("Download PDF"):
            if selected_rows:  # Check if rows have been selected
                selected_data = df.iloc[selected_rows].to_dict('records')
                output = create_pdf_output(selected_data)
                st.download_button("Download PDF", output, "selected_data.pdf", "application/pdf")
            else:
                st.warning("Please select at least one row before downloading.")

main()