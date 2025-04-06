import fitz
import io
from PIL import Image
import os
import logging

def pdf_extract_image(FILE, PATH):
    newpath = FILE[:-4]
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    print("Extracting Images...")
    pdf_file = fitz.open(FILE)
    for page_index in range(len(pdf_file)):
        page = pdf_file.load_page(page_index)
        image_list = page.get_images(full=True)
        if image_list:
            print(f"[+] Found a total of {len(image_list)} images on page {page_index}")
        else:
            print("[!] No images found on page", page_index)

        print(image_list)
        for image_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_name = f"image{page_index+1}_{image_index}.{image_ext}"
            save_path = f"/{newpath}/{image_name}"
            with open(save_path, "wb") as image_file:
                image_file.write(image_bytes)
                print(f"[+] Image saved as {image_name}")
                logging.info("Image Saved!")
        print("Images have been Extracted!")

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
# logger.setLevel(logging.DEBUG)

try:
    directory_in_str = "/Users/ajvj56/MyCSJournalAJVJ/VolumeX_FreeLancer/Python/PDFParse"
    directory = os.fsencode(directory_in_str)
    for FILE in os.listdir(directory):
        filename = os.fsdecode(FILE)
        if filename.endswith(".pdf"): 
            FILE = os.path.join(directory_in_str, filename)
            print(f"File currently: {filename} \n\n")
            pdf_extract_image(FILE, directory_in_str)
            continue
        else:
            continue
except Exception as err:
        print("An Error as occured, check the log!")
        logging.error(f"Unexpected {err=}, {type(err)=}")