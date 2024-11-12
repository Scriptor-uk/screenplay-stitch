from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
import os
import tempfile
from PIL import Image

def clear_console():
    # Clear console for both Windows and Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')

def extract_and_convert_pages(pdf_path):
    try:
        # Strip any leading and trailing quotes
        pdf_path = pdf_path.strip("'\"")

        # Open the PDF file
        pdf = PdfReader(pdf_path)
        total_pages = len(pdf.pages)

        # Get user input for page range
        print(f"PDF has {total_pages} pages.")
        page_range = input("Enter page range (e.g., '8-10' or '1,3,5'): ").strip()

        # Clear console after input
        clear_console()

        pages_to_extract = set()  # Using set to avoid duplicates
        for part in page_range.split(','):
            if '-' in part:
                start, end = map(int, part.split('-'))
                pages_to_extract.update(range(start-1, end))
            else:
                pages_to_extract.add(int(part)-1)

        # Convert to sorted list for ordered extraction
        pages_to_extract = sorted(pages_to_extract)

        # Validate page numbers
        if any(p < 0 or p >= total_pages for p in pages_to_extract):
            raise ValueError("Invalid page numbers")

        # Use a context manager for temporary file
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as temp_pdf_file:
            # Create a temporary PDF with selected pages
            output_pdf = PdfWriter()
            for page_num in pages_to_extract:
                output_pdf.add_page(pdf.pages[page_num])
            output_pdf.write(temp_pdf_file)
            temp_pdf_path = temp_pdf_file.name

        try:
            images = convert_from_path(
                temp_pdf_path,
                dpi=200,
                thread_count=os.cpu_count()
            )

            # Calculate dimensions once
            heights = [img.height for img in images]
            total_height = sum(heights)
            max_width = max(img.width for img in images)

            # Create the combined image
            combined_image = Image.new('RGB', (max_width, total_height), 'white')

            # Paste all images
            current_height = 0
            for img in images:
                combined_image.paste(img, (0, current_height))
                current_height += img.height

            # Save the combined image
            output_filename = "combined_pages.png"
            combined_image.save(
                output_filename,
                "PNG",
                optimize=True,
                quality=80
            )

            print(f"Successfully created {output_filename}")
            return output_filename

        finally:
            # Clean up temporary file in all cases
            try:
                os.unlink(temp_pdf_path)
            except Exception as e:
                print(f"Warning: Could not delete temporary file: {e}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    finally:
        # Force garbage collection
        if 'combined_image' in locals():
            del combined_image
        if 'images' in locals():
            del images

if __name__ == "__main__":
    pdf_path = input("Enter the path to your PDF file: ").strip()
    clear_console()
    extract_and_convert_pages(pdf_path)
