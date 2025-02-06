import argparse
from bs4 import BeautifulSoup
from tqdm import tqdm
import pdfkit
from pathlib import Path

def convert_one_html_to_pdf(html_file, pdf_file, overwrite=False, skip_existing=False):
    # if both overwrite and skip_existing are True, overwrite takes precedence
    # sanity check
    assert html_file.exists(), f"Source file {html_file} does not exist"

    if pdf_file.exists() and overwrite:
        assert pdf_file.is_file(), f"Destination path must be a file, not a folder"
    elif not pdf_file.exists():
        assert pdf_file.suffix == ".pdf", f"Destination file must have a .pdf extension"
    elif pdf_file.exists() and not overwrite:
        if skip_existing: return
        print(f"Destination file {pdf_file} already exists, use --overwrite to overwrite")
        raise FileExistsError(f"Destination file {pdf_file} already exists")
    else:
        print(f"Invalid destination path")

    with open(html_file, "r", encoding="utf-8") as file:
        html = file.read()

    # Read the header
    with open("header.html", "r", encoding="utf-8") as file:
        header = file.read()

    header = BeautifulSoup(header, "html.parser")

    # Insert HTML into header body
    header.body.insert(0, BeautifulSoup(html, "html.parser"))
    html = header.prettify()

    # Convert HTML to PDF
    pdfkit.from_string(html, pdf_file, verbose=True, options={"enable-local-file-access": True})

def convert_html_to_pdf(src_folder, dst_folder, overwrite=False, skip_existing=False):
    src_path = Path(src_folder)
    dst_path = Path(dst_folder) 

    if src_path.is_file():
        convert_one_html_to_pdf(src_path, dst_path, overwrite, skip_existing)
        print(f"Converted {src_path} to {dst_path}")
        return
    
        
    assert src_path.exists(), f"Source folder {src_path} does not exist"
    dst_path.mkdir(parents=True, exist_ok=True)
    
    html_files = list(src_path.rglob("*.html"))
    for html_file in tqdm(html_files):
        pdf_file = dst_path / html_file.with_suffix(".pdf").name
        convert_one_html_to_pdf(html_file, pdf_file, overwrite, skip_existing)
        print(f"Converted {html_file} to {pdf_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert HTML files to PDF.")
    parser.add_argument("src", help="Source folder containing HTML files or a single HTML file")
    parser.add_argument("dst", default=".",  help="Destination folder for PDF files or a single PDF file")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing PDF file")
    parser.add_argument("--skip-existing", action="store_true", help="Skip existing PDF file")
    args = parser.parse_args()
    convert_html_to_pdf(args.src, args.dst, args.overwrite, args.skip_existing)