import pymupdf
import os

class PDFReader:
    def convert_pdf_to_images(self, pdf_path):
        doc = pymupdf.open(pdf_path)

        # suppose we have "a.pdf" from it get the file name from the base name.
        # remove .pdf tp empty --> so final answer is "a"
        # now create the folder with that file name here it is a and then save all the images of the pdf and save it in this folder itself.

        folder_name = os.path.basename(pdf_path).replace(".pdf", "")

        # now i want to create image folder inside the storage\pdfs.

        output_dir = os.path.join("storage", "pdfs", folder_name)

        # we dont have output directory in folder, so we create logic if not then create it.

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # return all the image path into list (but we dont have to)
        image_paths = []

        for i in range(len(doc)):
            page = doc.load_page(i)
            matrix = pymupdf.Matrix(2,2) # (1,1) --> low resolution and (2,2) --> high resolution but there are many more...
            pix = page.get_pixmap(matrix=matrix)

            # create path to save image
            img_path = os.path.join(output_dir, f"page_{i}.png")
            pix.save(img_path)

            image_paths.append(img_path)


        doc.close()

        return image_paths
