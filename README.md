# C_C_C - Repositorio Multilenguaje de Desarrollo & Proyectos

<p align="center">
  <strong>Language:</strong>
  <a href="README.md">Español</a> |
  <a href="README.en.md">English</a> |
  <a href="README.de.md">Deutsch</a>
</p>

Bienvenido al repositorio **C_C_C**. Este proyecto recopila una suite diversa de aplicaciones, módulos de aprendizaje, herramientas empresariales y documentación técnica estructurada a través de múltiples lenguajes de programación y entornos tecnológicos (**C**, **CONZEPT 16**, **Java**, **Python**, **React/Supabase** y **YEET**).

---

## 📑 Tabla de Contenidos

- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Descripción de Módulos](#-descripción-de-módulos)
  - [1. C (Lenguaje C)](#1-c-lenguaje-c)
  - [2. CONZEPT 16](#2-conzept-16)
  - [3. JAVA](#3-java)
  - [4. PROJEKT (Sistema de Inventario)](#4-projekt-sistema-de-inventario)
  - [5. PYTHON](#5-python)
  - [6. YEET (Vectorsoft)](#6-yeet-vectorsoft)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Instrucciones de Instalación y Uso](#-instrucciones-de-instalación-y-uso)

---

## 📁 Estructura del Proyecto

```text
C_C_C/
├── C/                     # Calculadoras y algoritmos aritméticos en lenguaje C y Python
├── CONZEPT_16/            # Módulos y GUI desarrollados en el entorno empresarial CONZEPT 16
│   ├── Konvertierung/     # Conversión de tipos de datos (Alpha, Int, Float, Date, Time, etc.)
│   ├── StringKonverter/   # Procesamiento y manipulación avanzada de cadenas (OEM, UTF-8, etc.)
│   └── Taschenrechner/    # Calculadora gráfica con gestión de historial y memoria
├── JAVA/                  # Aplicaciones de escritorio en Java (Swing & Maven)
│   ├── CRUD/              # Sistema de gestión de productos (Archivos planos / Base de datos)
│   └── Calculator/        # Calculadora interactiva con interfaz Swing
├── PROJEKT/               # Documentación y diseño del Sistema de Inventario Empresarial
│   └── Documentation/     # Especificaciones técnicas (Dev, User, Lastenheft, UML, ERD, PDF)
├── PYTHON/                # Microservicios y utilidades interactivas con Streamlit
│   ├── E-Rechnung/        # Generador y validador de facturas electrónicas alemanas (XRechnung)
│   ├── Leitweg-ID/        # Generador y validador oficial de Leitweg-ID para entes públicos
│   ├── Taschenrechner/    # Módulo de cálculo en Python
│   └── XmlToPdf/          # Conversor dinámico de datos XML a tablas interactivas y PDF
├── YEET/                  # Documentación y prototipos para la plataforma Low-Code YEET
│   ├── Documentation/     # Manual oficial de referencia en formato PDF
│   └── README.md          # Guías de integración de escáner de códigos de barras/QR
├── README.md              # Documentación principal del repositorio (Español)
├── README.en.md           # Documentación en Inglés
└── README.de.md           # Documentación en Alemán
```

---

## 🔍 Descripción de Módulos

### 1. C (Lenguaje C)
* **Propósito:** Fundamentos de programación procedural, aritmética binaria y lógica de entrada/salida en consola.
* **Archivos Clave:**
  * `calculadora.c`, `calculator.c`, `taschenrechner.c`: Implementaciones de calculadoras con manejo de operaciones aritméticas (+, -, *, /, %), borrado de último dígito y cambio de signo.
  * `cal_simple.c`, `tasch_simple.c`: Versiones simplificadas para ejecución rápida.
  * `calculadora.py`, `taschenrechner.py`: Scripts equivalentes en Python para contraste pedagógico entre lenguajes compilados e interpretados.
  * Binarios ejecutables `.exe` correspondientes listos para entorno Windows.

### 2. CONZEPT 16
* **Propósito:** Implementación de interfaces gráficas empresariales (GUI) y manejo de lógica basada en eventos en la plataforma de desarrollo relacional **CONZEPT 16** (Vectorsoft).
* **Subproyectos:**
  * **`Konvertierung/`:** Módulo interactivo de conversión dinámica de tipos de datos (`Alpha`, `Int`, `BigInt`, `Float`, `Decimal`, `Time`, `Date` y booleanos).
  * **`StringKonverter/`:** Utilidad para transformación de cadenas y codificaciones (`OEM`, `ANSI`, `HTML`, `URI`, `UTF-8`, `Base64`), reordenamiento de nombres y manipulación de mayúsculas/minúsculas y umlaute.
  * **`Taschenrechner/`:** Calculadora gráfica completa que incluye pantalla de resultados, botones de control e historial persistente en lista (`LastLineDataList`).

### 3. JAVA
* **Propósito:** Soluciones orientadas a objetos con arquitectura basada en componentes visuales (Java Swing) y empaquetado Maven.
* **Subproyectos:**
  * **`CRUD/` (`pryArchivos`):** Aplicación de gestión y catálogo de productos con interfaz gráfica (`FrmGestionProductos`, `FrmProductos`). Soporta almacenamiento persistente mediante archivos de texto/planos y base de datos local de productos.
  * **`Calculator/`:** Calculadora de escritorio con interfaz gráfica Swing organizada con `JFrame`, `JPanel` y gestión de eventos mediante `ActionListener`.

### 4. PROJEKT (Sistema de Inventario)
* **Propósito:** Núcleo de documentación y análisis de arquitectura de un **Sistema de Inventario (Inventarsystem)** moderno basado en **React** (Frontend) y **Supabase / PostgreSQL** (Backend).
* **Componentes Documentales:**
  * **`Markdown/`:**
    * `README.md`: Visión global, fases del proyecto y estructura metodológica.
    * `Dev.md`: Manual del desarrollador, configuración en VS Code, esquemas de bases de datos y llamadas a API.
    * `User.md`: Manual de usuario final para operaciones cotidianas de inventario.
    * `Lastenheft.md`: Pliego de requerimientos funcionales y no funcionales del cliente.
    * `DB-Inventar.md`: Modelo relacional y sentencias SQL de tablas, índices y constraints.
    * `UML-Diagramme.md` & `DiagrammeIMG.md`: Diagramas de casos de uso, flujos y arquitectura del sistema.
    * `Links.md`: Enlaces y recursos complementarios del proyecto.
  * **`PDF/`:** Presentación ejecutiva del proyecto (`Präsentation_D-Paz.pdf`).

### 5. PYTHON
* **Propósito:** Aplicaciones web analíticas y de automatización empresarial construidas sobre el framework **Streamlit**.
* **Subproyectos:**
  * **`E-Rechnung/`:** Generación y validación de facturas electrónicas alemanas bajo el estándar **XRechnung** (XML/JSON), incluyendo validación de `Leitweg-ID` y cómputo de impuestos.
  * **`Leitweg-ID/`:** Herramienta para la creación y comprobación del código `Leitweg-ID` (identificador oficial alemán de compras públicas), validando Bundesland, código postal y cálculo automático del dígito verificador.
  * **`XmlToPdf/`:** Extractor dinámico de datos XML que presenta la información en DataFrames interactivos y permite exportar subconjuntos filtrados a documentos PDF y archivos XML limpios.
  * **`Taschenrechner/`:** Módulo complementario de calculadora en Python.

### 6. YEET (Vectorsoft)
* **Propósito:** Guías técnicas e integraciones para la plataforma Low-Code **YEET** de Vectorsoft.
* **Aspectos Destacados:**
  * Lógica en JavaScript (`UI Logic`) para integrar escaneo de códigos de barras y códigos QR mediante cámara.
  * Enlace bidireccional con tablas de interfaz (`yTable`) y entidades de datos OData (`apiObject.odata.odataEntityRead`) para actualización de inventarios en tiempo real.
  * Documentación completa del entorno en `Yeet-Doku-Web.pdf`.

---

## 🛠 Tecnologías Utilizadas

| Categoría | Tecnologías / Lenguajes |
| :--- | :--- |
| **Lenguajes** | C, Java (JDK 8+), Python 3.8+, JavaScript, SQL, CONZEPT 16 |
| **Frameworks & Librerías** | Streamlit, Pandas, Java Swing, Maven, React, TanStack Query |
| **Bases de Datos & Backend** | Supabase, PostgreSQL, OData |
| **Estándares & Formatos** | XRechnung, XML, JSON, PDF |
| **Herramientas de Entorno** | VS Code, NetBeans, Git |

---

## 🚀 Instrucciones de Instalación y Uso

### 🐍 Aplicaciones en Python (Streamlit)
Para ejecutar cualquiera de las aplicaciones en la carpeta `PYTHON/` (por ejemplo, `E-Rechnung`, `Leitweg-ID` o `XmlToPdf`):

```bash
# 1. Navegar a la carpeta correspondiente
cd PYTHON/E-Rechnung   # o PYTHON/Leitweg-ID o PYTHON/XmlToPdf

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Iniciar la aplicación
streamlit run app.py
```

### ☕ Aplicaciones en Java
* Abrir el directorio correspondiente (`JAVA/CRUD` o `JAVA/Calculator`) en un IDE compatible (NetBeans, IntelliJ IDEA o Eclipse).
* Para `JAVA/CRUD`, compilar mediante Maven:
  ```bash
  mvn clean install
  ```

### ⚡ Programas en C
* En entornos Windows, se pueden ejecutar directamente los binarios `.exe` precompilados en la carpeta `C/`.
* Para compilar manualmente con GCC:
  ```bash
  gcc calculadora.c -o calculadora.exe
  ./calculadora.exe
  ```

---

## 👤 Autor

* **D. Paz** ([@dwn10](https://github.com/dwn10))
* Repositorio: [https://github.com/dwn10/C_C_C](https://github.com/dwn10/C_C_C)
