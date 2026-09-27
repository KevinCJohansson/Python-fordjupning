# Automatiserad rapportgenerator

Litet Python-projekt som omvandlar rå försäljningsdata till en PDF-rapport — byggt som en individuell Python-fördjupning i en Data Science-kurs, med fokus på templating med Jinja2 och PDF-generering med WeasyPrint.

## Vad projektet gör

1. Läser in försäljningsdata från CSV (pandas)
2. Beräknar nyckeltal: total försäljning, antal ordrar, genomsnittligt ordervärde, topprodukter, försäljning per kategori/region
3. Genererar grafer för veckovis försäljningstrend, försäljning per kategori och försäljning per region (matplotlib)
4. Renderar en HTML-rapport från en Jinja2-mall (`report_template.html`), som importerar återanvändbara komponenter från `macros.html`, utifrån nyckeltalen och graferna
5. Konverterar HTML-rapporten till PDF (WeasyPrint)

## Teknikstack

- **pandas** – inläsning och aggregering av data
- **matplotlib** – grafgenerering
- **Jinja2** – HTML-templating
- **WeasyPrint** – rendering från HTML till PDF

## Projektstruktur

```Python_fordjupning/

├── utils/
│ ├── __init__.py
│ ├── data_loader.py # läser in och tolkar rådata från CSV
│ ├── metrics.py # beräknar nyckeltal och aggregeringar
│ ├── visualizations.py # genererar grafbilder
│ └── report_generator.py # renderar Jinja2-mallen och bygger PDF:en
├── data/
│ ├── sales_2018_Q1.csv
│ ├── sales_2018_Q2.csv
│ ├── sales_2018_Q3.csv
│ └── sales_2018_Q4.csv
├── main.py
├── report_template.html
├── macros.html # återanvändbara Jinja2-macro
├── requirements.txt
├── report_assets/ # genererade grafbilder (skapas automatiskt)
└── report.pdf är den slutliga genererade pdf-rapporten
```

## Installation

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

På Windows krävs även Pango för WeasyPrint. Se [installationsguiden](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows)

## Användning
Välj dataset i main sedan kör i terminalen

```powershell
python main.py
```

Detta genererar `report.pdf` i projektets rotmapp.