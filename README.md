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
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line, passing the path to your PDF file as an argument:

```bash
python main.py path/to/your/document.pdf
```

**Optional Arguments:**
- `-o` or `--output`: Specify a custom output base directory (default is `output`).
  
```bash
python main.py path/to/your/document.pdf -o custom_output_dir
```

Find your extracted images in the `output/` directory!

## Example
If you run the script on a file named `RAG.pdf`, the images will be exported to:
`output/RAG/page_1_img_1.jpeg`, `output/RAG/page_4_img_1.png`, etc.
