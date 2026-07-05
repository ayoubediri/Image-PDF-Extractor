# Image PDF Extractor

A simple and efficient Python tool to extract all embedded images from a PDF file. The images are extracted without loss of quality and saved in their original format.

## Features

- Extracts all images from any given PDF document.
- Preserves the original format and quality of the embedded images (e.g., PNG, JPEG).
- Automatically organizes extracted images into an output directory structured as `output/[name_of_pdf]/`.

## Prerequisites

- Python 3.6 or higher
- [PyMuPDF](https://pymupdf.readthedocs.io/) (`fitz`)

## Installation

1. **Clone this repository** (or download the files):
   ```bash
   git clone <your-repository-url>
   cd image_pdf_extrctur
   ```

2. **Create a virtual environment (Recommended)**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Linux/Mac
   # .venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install PyMuPDF
   ```

## Usage

1. Open `main.py` and modify the `pdf_file` variable at the bottom of the script to point to your target PDF.
   ```python
   if __name__ == "__main__":
       pdf_file = "path/to/your/document.pdf"
       ...
   ```

2. Run the script:
   ```bash
   python main.py
   ```

3. Find your extracted images in the `output/` directory!

## Example
If you run the script on a file named `RAG.pdf`, the images will be exported to:
`output/RAG/page_1_img_1.jpeg`, `output/RAG/page_4_img_1.png`, etc.
