import os
import pymupdf

THUMBNAIL_DIR = os.path.join("storage", "thumbnails")

class ThumbnailGenerator:
    def generate_thumbnail(self, pdf_path):
        doc = pymupdf.open(pdf_path)
        page = doc.load_page(0) # first page of the pdf
        pix = page.get_pixmap() # convert that first page into low resolution image

        base_name = os.path.basename(pdf_path).replace(".pdf", ".png") # basename = keepthe file name as it is for .png file anf replace extantion of ".pdf to ".png" 
        thumb_path = os.path.join(THUMBNAIL_DIR, base_name)

        pix.save(thumb_path)

        doc.close()

        return thumb_path
    
    def get_total_pages(self, pdf_path):
        doc = pymupdf.open(pdf_path)
        total = len(doc)
        doc.close()
        return total

