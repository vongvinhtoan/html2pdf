# HTML to PDF Converter

This script converts HTML math problems into PDF files.

## Usage

To convert HTML files to PDF, use the following command:

```sh
python html2pdf.py <src> <dst> [--overwrite] [--skip-existing]
```

- `<src>`: Source folder containing HTML files or a single HTML file.
- `<dst>`: Destination folder for PDF files or a single PDF file. Defaults to the current directory.
- `--overwrite`: Overwrite existing PDF files.
- `--skip-existing`: Skip existing PDF files.

Example:

```sh
python html2pdf.py ./html_files ./pdf_files --overwrite
```

## Installation

To install the necessary dependencies, run the following commands:

### For macOS

```sh
# https://github.com/frappe/frappe/issues/29064#issuecomment-2574683304
curl -L https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-2/wkhtmltox-0.12.6-2.macos-cocoa.pkg -O
installer -pkg wkhtmltox-0.12.6-2.macos-cocoa.pkg -target ~ 
pip install pdfkit
```

### For Linux

```sh
# https://wkhtmltopdf.org/downloads.html
sudo apt-get install wkhtmltopdf
pip install pdfkit
```
