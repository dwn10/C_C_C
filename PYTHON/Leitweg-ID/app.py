# 1) https://pypi.org/project/streamlit/      pip install streamlit

# 2) Terminal: cd Streamlit/Leitweg-ID > pip install -r requirements.txt
#                                      > streamlit run app.py

# 3) Willkommen bei Streamlit! / Sie können Ihre Streamlit-App jetzt im Browser anzeigen.
        # Lokale URL: http://localhost:8501
        # Netzwerk-URL: http://100.126.10.200:8501

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

import streamlit as st
import requests
import re
from functools import lru_cache

# Seitenkonfiguration
st.set_page_config(
    page_title="Leitweg-ID Generator",
    page_icon="🔢",
    layout="centered"
)

# Benutzerdefinierte CSS-Stile
st.markdown("""
    <style>
    .stAlert {
        padding: 1rem;
        border-radius: 0.5rem;
    }
    .stButton>button {
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

@lru_cache(maxsize=128)
def calcular_prüfziffer(leitweg_id):
    """Berechnet die Prüfziffer für eine Leitweg-ID mit effizientem Caching."""
    leitweg_id = "".join(
        [str(ord(c) - 55) if c.isalpha() else c for c in leitweg_id]
    )
    leitweg_id += "00"
    resto = int(leitweg_id) % 97
    prüfziffer = 98 - resto
    return f"{prüfziffer:02d}"

def validar_bundesland(code):
    """Überprüft den Bundeslandcode."""
    valid_codes = {
        "01": "Schleswig-Holstein", "02": "Hamburg", "03": "Niedersachsen",
        "04": "Bremen", "05": "Nordrhein-Westfalen", "06": "Hessen",
        "07": "Rheinland-Pfalz", "08": "Baden-Württemberg", "09": "Bayern",
        "10": "Saarland", "11": "Berlin", "12": "Brandenburg",
        "13": "Mecklenburg-Vorpommern", "14": "Sachsen", "15": "Sachsen-Anhalt",
        "16": "Thüringen"
    }
    return code in valid_codes, valid_codes.get(code, "Ungültiger Code")

@st.cache_data(ttl=3600)  # Cache für 1 Stunde
def verificar_codigo_postal(plz):
    """Überprüft die deutsche Postleitzahl über eine externe API."""
    try:
        response = requests.get(f"https://api.zippopotam.us/DE/{plz}")
        if response.status_code == 200:
            return True, response.json()
        return False, "Postleitzahl nicht gefunden"
    except Exception as e:
        return False, f"Fehler bei der Überprüfung der Postleitzahl: {str(e)}"

def main():
    st.title("🔢 Leitweg-ID Generator")
    st.markdown("---")

    with st.form("leitweg_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            bundesland = st.text_input(
                "Bundesland-Code (2 Stellen):",
                max_chars=2,
                help="Beispiel: 05 für Nordrhein-Westfalen"
            )

        with col2:
            plz = st.text_input(
                "Postleitzahl (5 Stellen):",
                max_chars=5,
                help="Geben Sie die deutsche Postleitzahl zur Validierung ein"
            )

        regierungsbezirk = st.text_input(
            "Regierungsbezirk (1 Stelle):",
            max_chars=1,
            help="Optional - Beispiel: 1"
        )

        landkreis = st.text_input(
            "Landkreis (2 Stellen):",
            max_chars=2,
            help="Optional - Beispiel: 01"
        )

        gemeinde = st.text_input(
            "Gemeindekennzahl (3, 4 oder 7 Stellen):",
            help="Beispiel: 001"
        )

        feinadressierung = st.text_input(
            "Feinadressierung (max. 30 Zeichen):",
            max_chars=30,
            help="Optional - Nur Buchstaben, Zahlen und Bindestriche erlaubt"
        )

        submitted = st.form_submit_button("Leitweg-ID Generieren")

    if submitted:
        # Validierungen
        is_valid = True
        error_messages = []

        # Bundesland validieren
        if not bundesland.isdigit() or len(bundesland) != 2:
            is_valid = False
            error_messages.append("Der Bundesland-Code muss aus 2 Ziffern bestehen.")
        else:
            valid_bundesland, state_name = validar_bundesland(bundesland)
            if not valid_bundesland:
                is_valid = False
                error_messages.append(f"Ungültiger Bundesland-Code. {state_name}")
            else:
                st.info(f"Bundesland: {state_name}")

        # Postleitzahl validieren
        if plz:
            if not plz.isdigit() or len(plz) != 5:
                is_valid = False
                error_messages.append("Die Postleitzahl muss aus 5 Ziffern bestehen.")
            else:
                valid_plz, plz_info = verificar_codigo_postal(plz)
                if valid_plz:
                    st.success("Postleitzahl erfolgreich überprüft.")
                else:
                    st.warning(plz_info)

        # Gemeindekennzahl-Format validieren
        if not re.match(r'^\d{3,4}$|^\d{7}$', gemeinde):
            is_valid = False
            error_messages.append("Die Gemeindekennzahl muss 3, 4 oder 7 Ziffern haben.")

        # Erlaubte Zeichen in Feinadressierung validieren
        if feinadressierung and not re.match(r'^[a-zA-Z0-9-]*$', feinadressierung):
            is_valid = False
            error_messages.append("Die Feinadressierung darf nur Buchstaben, Zahlen und Bindestriche enthalten.")

        if is_valid:
            # Leitweg-ID erstellen
            grobadressierung = bundesland + regierungsbezirk + landkreis + gemeinde
            leitweg_id = grobadressierung + "-" + feinadressierung if feinadressierung else grobadressierung
            prüfziffer = calcular_prüfziffer(leitweg_id)
            leitweg_id_completa = f"{leitweg_id}-{prüfziffer}"

            st.success("### Generierte Leitweg-ID:")
            st.code(leitweg_id_completa, language="text")
            
            # Kopieren in die Zwischenablage
            st.markdown(f"""
                <textarea id="leitweg_id" style="position: absolute; left: -9999px">{leitweg_id_completa}</textarea>
                <script>
                    function copyToClipboard() {{
                        var copyText = document.getElementById("leitweg_id");
                        copyText.select();
                        document.execCommand("copy");
                    }}
                </script>
                """, unsafe_allow_html=True)
            
            if st.button("📋 In Zwischenablage kopieren"):
                st.write("ID in die Zwischenablage kopiert!")
        else:
            for error in error_messages:
                st.error(error)

if __name__ == "__main__":
    main()