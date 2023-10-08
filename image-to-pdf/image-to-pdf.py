from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import re
from dotenv import load_dotenv

load_dotenv()

# ==================================================
# ENV
subject_name = os.environ["SUBJECT_NAME"]
class_no = int(os.environ["CLASS_NO"])
filename_is_number = int(os.environ["FILENAME_IS_NUMBER"])
# ==================================================

class_no = str(class_no)

def natural_sort_key(s):
    # return filename as number by extract
    return [int(text) if text.isdigit() else text.lower() for text in re.split('(\d+)', s)]

def images_to_pdf(input_folder, output_pdf_path):
    image_files = [f for f in os.listdir(input_folder) if f.endswith(".jpg")]
    
    if filename_is_number:
        image_files.sort(key=natural_sort_key)  # sort files by number
    else:
        image_files.sort()                      # sort files by name

    c = canvas.Canvas(output_pdf_path, pagesize=letter)
    width, height = letter

    for image_file in image_files:
        img = Image.open(os.path.join(input_folder, image_file))
        img_width, img_height = img.size
        img_aspect = img_height / float(img_width)

        # set pdf size
        c.setPageSize((width, width * img_aspect))

        # add images to pdf file
        c.drawImage(os.path.join(input_folder, image_file), 0, 0, width, width * img_aspect)
        c.showPage()

    c.save()

if __name__ == "__main__":
    if subject_name is None:
        print("Please set subject name")
        exit()

    input_folder = "input/" + subject_name + "/" + class_no     # input folder path
    output_pdf_path = subject_name + "_" + class_no + ".pdf"    # output file name
    images_to_pdf(input_folder, output_pdf_path)

    print("Done")