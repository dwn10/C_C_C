# 1) https://pypi.org/project/streamlit/      pip install streamlit

# 2) Terminal: cd Streamlit/E-Rechnung > pip install -r requirements.txt
#                                      > streamlit run app.py

# 3) Willkommen bei Streamlit! / Sie können Ihre Streamlit-App jetzt im Browser anzeigen.
        # Lokale URL: http://localhost:8501
        # Netzwerk-URL: http://100.126.10.200:8501

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

import streamlit as st
import pandas as pd
import lxml.etree as ET
from datetime import datetime
import uuid
import os
import json
import requests
from pathlib import Path

# Seitenkonfiguration
st.set_page_config(
    page_title="E-Rechnung Generator",
    page_icon="📑",
    layout="wide"
)

# Benutzerdefinierte CSS-Stile
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .stAlert {
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .invoice-form {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .xml-viewer {
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        white-space: pre-wrap;
        background-color: #1e1e1e;
        color: #d4d4d4;
        padding: 1.5rem;
        border-radius: 0.5rem;
        font-size: 0.9rem;
        line-height: 1.5;
        overflow-x: auto;
        border: 1px solid #333;
    }
    .xml-viewer .tag {
        color: #569cd6;
    }
    .xml-viewer .attribute {
        color: #9cdcfe;
    }
    .xml-viewer .value {
        color: #ce9178;
    }
    .xml-preview {
        background-color: #1e1e1e;
        color: #d4d4d4;
        padding: 1rem;
        border-radius: 0.5rem;
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        font-size: 0.9rem;
        border: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# Verzeichnis für Rechnungen erstellen, falls es nicht existiert
INVOICE_DIR = Path("rechnungen")
INVOICE_DIR.mkdir(exist_ok=True)

def rechnungs_id_erzeugen():
    """Erzeugt eine eindeutige Rechnungs-ID."""
    return str(uuid.uuid4())

def leitweg_id_prüfen(leitweg_id):
    """Überprüft das Format der Leitweg-ID."""
    import re
    pattern = r'^\d{2}[0-9A-Z]-\d{3,12}-\d{2}$'
    return bool(re.match(pattern, leitweg_id))

def xml_rechnung_erstellen(daten):
    """Erstellt ein XML-Dokument im XRechnung-Format."""
    root = ET.Element("ubl:Invoice", {
        "xmlns:ubl": "urn:oasis:names:specification:ubl:schema:xsd:Invoice-2",
        "xmlns:cac": "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2",
        "xmlns:cbc": "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"
    })
    
    # Grundlegende Rechnungsinformationen
    ET.SubElement(root, "cbc:CustomizationID").text = "urn:cen.eu:en16931:2017#compliant#urn:xoev-de:kosit:standard:xrechnung_2.0"
    ET.SubElement(root, "cbc:ID").text = daten["rechnungs_id"]
    ET.SubElement(root, "cbc:IssueDate").text = daten["rechnungsdatum"]
    ET.SubElement(root, "cbc:DueDate").text = daten["fälligkeitsdatum"]
    ET.SubElement(root, "cbc:InvoiceTypeCode").text = "380"
    
    # Lieferantinformationen
    supplier_party = ET.SubElement(root, "cac:AccountingSupplierParty")
    supplier = ET.SubElement(supplier_party, "cac:Party")
    supplier_name = ET.SubElement(supplier, "cac:PartyName")
    ET.SubElement(supplier_name, "cbc:Name").text = daten["lieferant_name"]
    
    # Käuferinformationen
    customer_party = ET.SubElement(root, "cac:AccountingCustomerParty")
    customer = ET.SubElement(customer_party, "cac:Party")
    customer_name = ET.SubElement(customer, "cac:PartyName")
    ET.SubElement(customer_name, "cbc:Name").text = daten["kunde_name"]
    
    # Leitweg-ID
    buyer_reference = ET.SubElement(root, "cbc:BuyerReference")
    buyer_reference.text = daten["leitweg_id"]
    
    # Summen
    legal_monetary_total = ET.SubElement(root, "cac:LegalMonetaryTotal")
    ET.SubElement(legal_monetary_total, "cbc:TaxExclusiveAmount", currencyID="EUR").text = str(daten["netto_betrag"])
    ET.SubElement(legal_monetary_total, "cbc:TaxInclusiveAmount", currencyID="EUR").text = str(daten["brutto_betrag"])
    ET.SubElement(legal_monetary_total, "cbc:PayableAmount", currencyID="EUR").text = str(daten["brutto_betrag"])
    
    return ET.ElementTree(root)

def rechnung_speichern(daten):
    """Speichert die Rechnung im XML- und JSON-Format."""
    # XML erstellen
    xml_tree = xml_rechnung_erstellen(daten)
    xml_dateiname = INVOICE_DIR / f"rechnung_{daten['rechnungs_id']}.xml"
    xml_tree.write(xml_dateiname, encoding="UTF-8", xml_declaration=True)
    
    # Daten im JSON-Format speichern
    json_dateiname = INVOICE_DIR / f"rechnung_{daten['rechnungs_id']}.json"
    with open(json_dateiname, 'w', encoding='utf-8') as f:
        json.dump(daten, f, ensure_ascii=False, indent=4)
    
    return xml_dateiname, json_dateiname

def format_xml(xml_string):
    """XML formatieren für bessere Lesbarkeit."""
    try:
        # Parse XML string
        parser = ET.XMLParser(remove_blank_text=True)
        root = ET.fromstring(xml_string.encode('utf-8'), parser)
        # Als formatierten String darstellen und Farben zuweisen
        formatted_xml = ET.tostring(root, encoding='unicode', pretty_print=True)
        # XML-Elemente markieren
        formatted_xml = (formatted_xml
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;'))
        return formatted_xml
    except Exception as e:
        return f"Fehler beim Formatieren des XML: {str(e)}"

def extract_invoice_details(root):
    """Wichtige Informationen aus der XML-Rechnung extrahieren."""
    ns = {
        'ubl': 'urn:oasis:names:specification:ubl:schema:xsd:Invoice-2',
        'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
        'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
    }
    
    try:
        details = {}
        # Hilfsfunktion zum Finden von Elementen
        def find_element(xpath, default="Nicht gefunden"):
            element = root.find(xpath, ns)
            return element.text if element is not None else default
        
        details = {
            "Rechnungsnummer": find_element('.//cbc:ID'),
            "Ausstellungsdatum": find_element('.//cbc:IssueDate'),
            "Fälligkeitsdatum": find_element('.//cbc:DueDate'),
            "Währung": find_element('.//cbc:DocumentCurrencyCode', "EUR"),
            "Leitweg-ID": find_element('.//cbc:BuyerReference'),
            "Lieferant": find_element('.//cac:AccountingSupplierParty//cbc:RegistrationName'),
            "Kunde": find_element('.//cac:AccountingCustomerParty//cbc:RegistrationName'),
            "Nettobetrag": find_element('.//cbc:TaxExclusiveAmount', "0.00"),
            "Mehrwertsteuer": find_element('.//cbc:TaxAmount', "0.00"),
            "Gesamtbetrag": find_element('.//cbc:PayableAmount', "0.00")
        }
        return details
    except Exception as e:
        st.error(f"Fehler beim Extrahieren der Rechnungsdetails: {str(e)}")
        return None

def main():
    st.title("📑 E-Rechnung Generator")
    st.markdown("### Test Version D.Paz")
    st.markdown("---")

    tabs = st.tabs(["Rechnung Erstellen", "Rechnungen Anzeigen", "Rechnung Prüfen"])
    
    with tabs[0]:
        st.header("Neue Rechnung Erstellen")
        
        with st.form("rechnung_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            
            with col1:
                lieferant_name = st.text_input(
                    "Name des Lieferanten",
                    help="Name des Unternehmens, das die Rechnung ausstellt"
                )
                lieferant_anschrift = st.text_input("Anschrift des Lieferanten")
                lieferant_steuernummer = st.text_input("Steuernummer des Lieferanten")
                
            with col2:
                kunde_name = st.text_input(
                    "Name des Kunden",
                    help="Name der Organisation, die die Rechnung erhält"
                )
                kunde_anschrift = st.text_input("Anschrift des Kunden")
                leitweg_id = st.text_input(
                    "Leitweg-ID",
                    help="Format: XX-XXXXXXX-XX"
                )
            
            st.markdown("### Rechnungsdetails")
            col3, col4 = st.columns(2)
            
            with col3:
                rechnungsdatum = st.date_input("Rechnungsdatum")
                fälligkeitsdatum = st.date_input("Fälligkeitsdatum")
                
            with col4:
                netto_betrag = st.number_input("Nettobetrag (€)", min_value=0.0, step=0.01)
                mwst = st.selectbox("Mehrwertsteuer (%)", [0, 4, 10, 21])
                
            beschreibung = st.text_area("Beschreibung", height=100)
            
            submitted = st.form_submit_button("Rechnung Erstellen")
            
            if submitted:
                if not leitweg_id_prüfen(leitweg_id):
                    st.error("Das Format der Leitweg-ID ist ungültig")
                else:
                    # Summen berechnen
                    mwst_betrag = netto_betrag * (mwst/100)
                    brutto_betrag = netto_betrag + mwst_betrag
                    
                    # Daten vorbereiten
                    rechnungs_daten = {
                        "rechnungs_id": rechnungs_id_erzeugen(),
                        "rechnungsdatum": rechnungsdatum.strftime("%Y-%m-%d"),
                        "fälligkeitsdatum": fälligkeitsdatum.strftime("%Y-%m-%d"),
                        "lieferant_name": lieferant_name,
                        "lieferant_anschrift": lieferant_anschrift,
                        "lieferant_steuernummer": lieferant_steuernummer,
                        "kunde_name": kunde_name,
                        "kunde_anschrift": kunde_anschrift,
                        "leitweg_id": leitweg_id,
                        "netto_betrag": netto_betrag,
                        "mwst": mwst,
                        "mwst_betrag": mwst_betrag,
                        "brutto_betrag": brutto_betrag,
                        "beschreibung": beschreibung
                    }
                    
                    # Rechnung speichern
                    xml_datei, json_datei = rechnung_speichern(rechnungs_daten)
                    
                    st.success(f"""
                    ✅ Rechnung erfolgreich erstellt
                    - ID: {rechnungs_daten['rechnungs_id']}
                    - XML: {xml_datei.name}
                    - JSON: {json_datei.name}
                    """)
    
    with tabs[1]:
        st.header("Vorhandene Rechnungen")
        if list(INVOICE_DIR.glob("*.json")):
            rechnungen = []
            for json_datei in INVOICE_DIR.glob("*.json"):
                with open(json_datei, 'r', encoding='utf-8') as f:
                    daten = json.load(f)
                    rechnungen.append({
                        "ID": daten["rechnungs_id"],
                        "Datum": daten["rechnungsdatum"],
                        "Lieferant": daten["lieferant_name"],
                        "Kunde": daten["kunde_name"],
                        "Gesamtbetrag": f"{daten['brutto_betrag']}€"
                    })
            
            df = pd.DataFrame(rechnungen)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Keine Rechnungen vorhanden")
    
    with tabs[2]:
        st.header("Rechnung Prüfen")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            uploaded_file = st.file_uploader("XML-Rechnung hochladen", type=['xml'])
            
            if uploaded_file:
                try:
                    # Den Inhalt der Datei lesen und sicherstellen, dass er nicht leer ist
                    xml_bytes = uploaded_file.read()
                    if not xml_bytes:
                        st.error("❌ Die hochgeladene Datei ist leer")
                        st.stop()
                    
                    # Den Inhalt dekodieren
                    try:
                        xml_content = xml_bytes.decode('utf-8')
                    except UnicodeDecodeError:
                        try:
                            xml_content = xml_bytes.decode('iso-8859-1')
                        except UnicodeDecodeError:
                            st.error("❌ Fehler bei der Dekodierung der XML-Datei")
                            st.info("Die Datei muss in UTF-8 oder ISO-8859-1 kodiert sein")
                            st.stop()
                    
                    # Überprüfen, ob der Inhalt mit <?xml o <ubl:Invoice anfängt
                    if not (xml_content.strip().startswith('<?xml') or xml_content.strip().startswith('<ubl:Invoice')):
                        st.error("❌ Die Datei scheint keine gültige XML-Datei zu sein")
                        st.info("Die Datei muss mit <?xml oder <ubl:Invoice beginnen")
                        st.stop()
                    
                    # Debug: Die ersten Zeichen der XML-Datei anzeigen
                    st.text("XML Vorschau (erste 100 Zeichen):")
                    st.markdown(f'<div class="xml-preview">{xml_content[:100]}</div>', unsafe_allow_html=True)
                    
                    # XML mit lxml parsen
                    parser = ET.XMLParser(remove_blank_text=True)
                    try:
                        tree = ET.fromstring(xml_content.encode('utf-8'), parser)
                    except ET.ParseError as pe:
                        st.error(f"❌ XML-Parsing Fehler: {str(pe)}")
                        st.info("Bitte überprüfen Sie das Format der XML-Datei")
                        # XML-Inhalt zum Debuggen anzeigen
                        with st.expander("XML Inhalt anzeigen"):
                            st.code(xml_content, language="xml")
                        st.stop()
                    
                    # Basisstruktur prüfen
                    if "Invoice" in tree.tag:
                        st.success("✅ XML-Struktur ist gültig")
                        
                        # Details extrahieren und anzeigen
                        details = extract_invoice_details(tree)
                        if details:
                            st.markdown("### Rechnungsdetails")
                            for key, value in details.items():
                                st.write(f"**{key}:** {value}")
                                
                        # Formatiertes XML in der rechten Spalte anzeigen
                        with col2:
                            st.markdown("### XML Ansicht")
                            formatted_xml = format_xml(xml_content)
                            st.markdown(f'<div class="xml-viewer">{formatted_xml}</div>', unsafe_allow_html=True)
                    else:
                        st.error("❌ Die Datei scheint keine gültige Rechnung zu sein")
                        st.info("Die XML-Datei muss ein XRechnung-Dokument sein")
                
                except Exception as e:
                    st.error(f"❌ Unerwarteter Fehler: {str(e)}")
                    st.info("Bitte kontaktieren Sie den Support, wenn der Fehler weiterhin besteht")
                    # Debugging-Informationen anzeigen
                    with st.expander("Debug Information"):
                        st.code(str(e), language="python")

if __name__ == "__main__":
    main()