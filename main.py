import fitz  # PyMuPDF
import os
import argparse

def extract_images_from_pdf(pdf_path, output_base_dir="output"):
    # Get the name of the pdf without extension
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Create the output directory: output/[name of pdf]/
    output_dir = os.path.join(output_base_dir, pdf_name)
    os.makedirs(output_dir, exist_ok=True)
    
    # Open the PDF file
    try:
        pdf_document = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening PDF: {e}")
        return

    extracted_count = 0
    
    # Iterate through all pages
    for page_index in range(len(pdf_document)):
        page = pdf_document[page_index]
        image_list = page.get_images(full=True)
        
        # Iterate through all images on the page
        for image_index, img in enumerate(image_list, start=1):
            xref = img[0]
            
            # Extract the image bytes
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            
            # Get the image extension (e.g., png, jpeg)
            image_ext = base_image["ext"]
            
            # Construct the output image filename
            image_filename = f"page_{page_index + 1}_img_{image_index}.{image_ext}"
            image_filepath = os.path.join(output_dir, image_filename)
            
            # Save the image
            with open(image_filepath, "wb") as f:
                f.write(image_bytes)
                
            print(f"Saved: {image_filepath}")
            extracted_count += 1
            
    print(f"\nExtraction complete! Extracted {extracted_count} images to {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract all images from a PDF file or a directory of PDFs.")
    parser.add_argument("input_path", help="Path to the input PDF file or directory containing PDFs.")
    parser.add_argument("-o", "--output", default="output", help="Base directory to save extracted images (default: 'output').")
    
    args = parser.parse_args()
    
    if os.path.isfile(args.input_path):
        if args.input_path.lower().endswith(".pdf"):
            print(f"Processing single file: {args.input_path}")
            extract_images_from_pdf(args.input_path, args.output)
        else:
            print(f"Error: '{args.input_path}' is not a PDF file.")
    elif os.path.isdir(args.input_path):
        print(f"Processing directory: {args.input_path}")
        pdf_files = [f for f in os.listdir(args.input_path) if f.lower().endswith(".pdf")]
        
        if not pdf_files:
            print(f"No PDF files found in directory: {args.input_path}")
        else:
            for pdf_file in pdf_files:
                full_path = os.path.join(args.input_path, pdf_file)
                print(f"\n--- Processing: {full_path} ---")
                extract_images_from_pdf(full_path, args.output)
    else:
        print(f"Error: Path not found at '{args.input_path}'")
