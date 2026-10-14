# C_C_C - Multi-Language Development & Project Repository

<p align="center">
  <strong>Language:</strong>
  <a href="README.md">Español</a> |
  <a href="README.en.md">English</a> |
  <a href="README.de.md">Deutsch</a>
</p>

Welcome to the **C_C_C** repository. This project brings together a diverse suite of applications, learning modules, enterprise utilities, and structured technical documentation across multiple programming languages and technological environments (**C**, **CONZEPT 16**, **Java**, **Python**, **React/Supabase**, and **YEET**).

---

## 📑 Table of Contents

- [Project Structure](#-project-structure)
- [Module Overview](#-module-overview)
  - [1. C (C Language)](#1-c-c-language)
  - [2. CONZEPT 16](#2-conzept-16)
  - [3. JAVA](#3-java)
  - [4. PROJEKT (Inventory System)](#4-projekt-inventory-system)
  - [5. PYTHON](#5-python)
  - [6. YEET (Vectorsoft)](#6-yeet-vectorsoft)
- [Technologies Used](#-technologies-used)
- [Installation and Usage Guide](#-installation-and-usage-guide)
- [Author](#-author)

---

## 📁 Project Structure

```text
C_C_C/
├── C/                     # Calculators and arithmetic algorithms in C and Python
├── CONZEPT_16/            # Modules and GUI developed in CONZEPT 16 enterprise platform
│   ├── Konvertierung/     # Data type conversions (Alpha, Int, Float, Date, Time, etc.)
│   ├── StringKonverter/   # Advanced string processing and character encoding (OEM, UTF-8, etc.)
│   └── Taschenrechner/    # Graphical calculator with history list and state tracking
├── JAVA/                  # Desktop applications in Java (Swing & Maven)
│   ├── CRUD/              # Product management system (Flat files / Local database)
│   └── Calculator/        # Interactive calculator with Swing GUI
├── PROJEKT/               # Documentation and architectural design for Enterprise Inventory System
│   └── Documentation/     # Technical specs (Dev, User, Lastenheft, UML, ERD, PDF presentation)
├── PYTHON/                # Microservices and interactive utilities built with Streamlit
│   ├── E-Rechnung/        # German electronic invoice generator and validator (XRechnung)
│   ├── Leitweg-ID/        # Official Leitweg-ID generator & validator for public authorities
│   ├── Taschenrechner/    # Python calculator module
│   └── XmlToPdf/          # Dynamic XML data viewer with export to filtered XML and PDF
├── YEET/                  # Low-Code platform documentation and prototypes (Vectorsoft YEET)
│   ├── Documentation/     # Official web reference manual in PDF format
│   └── README.md          # Barcode & QR code scanner integration guides
├── README.md              # Main repository documentation (Spanish)
├── README.en.md           # English documentation
└── README.de.md           # German documentation
```

---

## 🔍 Module Overview

### 1. C (C Language)
* **Purpose:** Procedural programming fundamentals, binary arithmetic, and console I/O handling.
* **Key Files:**
  * `calculadora.c`, `calculator.c`, `taschenrechner.c`: Calculator implementations with core arithmetic operations (+, -, *, /, %), backspace digit deletion, and sign toggle.
  * `cal_simple.c`, `tasch_simple.c`: Streamlined versions for quick console execution.
  * `calculadora.py`, `taschenrechner.py`: Equivalent Python scripts for comparative analysis between compiled and interpreted paradigms.
  * Pre-compiled `.exe` binaries ready for execution on Windows.

### 2. CONZEPT 16
* **Purpose:** Graphical enterprise interfaces (GUI) and event-driven programming on the **CONZEPT 16** relational platform (Vectorsoft).
* **Sub-projects:**
  * **`Konvertierung/`:** Interactive tool demonstrating type conversions (`Alpha`, `Int`, `BigInt`, `Float`, `Decimal`, `Time`, `Date`, and boolean checkboxes).
  * **`StringKonverter/`:** Text manipulation and character encoding converter (`OEM`, `ANSI`, `HTML`, `URI`, `UTF-8`, `Base64`), case modifications, name reordering, and German umlaut processing.
  * **`Taschenrechner/`:** GUI calculator equipped with display, function buttons, and persistent calculation history list (`LastLineDataList`).

### 3. JAVA
* **Purpose:** Object-oriented software with Java Swing UI components and Maven dependency management.
* **Sub-projects:**
  * **`CRUD/` (`pryArchivos`):** Product inventory management application featuring GUI forms (`FrmGestionProductos`, `FrmProductos`) with flat-file persistence and database integration.
  * **`Calculator/`:** Desktop graphical calculator built with `JFrame`, `JPanel`, and event listeners via `ActionListener`.

### 4. PROJEKT (Inventory System)
* **Purpose:** Comprehensive technical documentation and software architecture for a full-scale **Inventory Management System (Inventarsystem)** built with **React** (Frontend) and **Supabase / PostgreSQL** (Backend).
* **Documentation Assets:**
  * **`Markdown/`:**
    * `README.md`: Project roadmap, milestones, and methodology overview.
    * `Dev.md`: Developer manual, VS Code setup, database schemas, and API integration.
    * `User.md`: End-user manual detailing daily inventory operations.
    * `Lastenheft.md`: Business requirements specification and scope definition.
    * `DB-Inventar.md`: PostgreSQL schema, table definitions, indexes, and constraints in Supabase.
    * `UML-Diagramme.md` & `DiagrammeIMG.md`: Use case diagrams, process chains (EPK), and system architecture.
    * `Links.md`: Reference links and project resources.
  * **`PDF/`:** Executive slide deck presentation (`Präsentation_D-Paz.pdf`).

### 5. PYTHON
* **Purpose:** Web applications and automation utilities built on top of the **Streamlit** framework.
* **Sub-projects:**
  * **`E-Rechnung/`:** German e-invoicing management tool implementing the **XRechnung** standard (XML/JSON), with automated VAT calculation and `Leitweg-ID` validation.
  * **`Leitweg-ID/`:** Validation and generator tool for German public procurement routing codes (`Leitweg-ID`), verifying federal state codes, postal codes, and check digits.
  * **`XmlToPdf/`:** Dynamic XML data processor displaying tabular data in DataFrames with selective export to formatted PDF documents and customized XML.
  * **`Taschenrechner/`:** Python calculator module.

### 6. YEET (Vectorsoft)
* **Purpose:** Technical guides and integration workflows for Vectorsoft's Low-Code platform **YEET**.
* **Highlights:**
  * JavaScript client logic (`UI Logic`) connecting camera hardware for barcode and QR code reading.
  * Real-time synchronization between visual tables (`yTable`) and OData data entities (`apiObject.odata.odataEntityRead`).
  * Comprehensive official guide provided in `Yeet-Doku-Web.pdf`.

---

## 🛠 Technologies Used

| Category | Technologies / Languages |
| :--- | :--- |
| **Languages** | C, Java (JDK 8+), Python 3.8+, JavaScript, SQL, CONZEPT 16 |
| **Frameworks & Libraries** | Streamlit, Pandas, Java Swing, Maven, React, TanStack Query |
| **Databases & Backend** | Supabase, PostgreSQL, OData |
| **Standards & Formats** | XRechnung, XML, JSON, PDF |
| **Tooling & IDEs** | VS Code, NetBeans, Git |

---

## 🚀 Installation and Usage Guide

### 🐍 Python Applications (Streamlit)
To run any of the applications inside `PYTHON/` (e.g., `E-Rechnung`, `Leitweg-ID`, or `XmlToPdf`):

```bash
# 1. Navigate to the desired directory
cd PYTHON/E-Rechnung   # or PYTHON/Leitweg-ID or PYTHON/XmlToPdf

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the application
streamlit run app.py
```

### ☕ Java Applications
* Open the directory (`JAVA/CRUD` or `JAVA/Calculator`) in any Java-compatible IDE (NetBeans, IntelliJ IDEA, Eclipse).
* For `JAVA/CRUD`, build with Maven:
  ```bash
  mvn clean install
  ```

### ⚡ C Programs
* On Windows, pre-compiled `.exe` binaries located in `C/` can be launched directly.
* To compile from source using GCC:
  ```bash
  gcc calculadora.c -o calculadora.exe
  ./calculadora.exe
  ```

---

## 👤 Author

* **D. Paz** ([@dwn10](https://github.com/dwn10))
* Repository: [https://github.com/dwn10/C_C_C](https://github.com/dwn10/C_C_C)
