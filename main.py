import fitz  # PyMuPDF
import os

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
    # Example usage:
    # Change the pdf_path to the path of your PDF file
    pdf_file = "pdfs/RAG.pdf"
    
    if os.path.exists(pdf_file):
        print(f"Processing: {pdf_file}")
        extract_images_from_pdf(pdf_file)
    else:
        print(f"PDF file not found: {pdf_file}")
        print("Please provide a valid path to a PDF file.")
