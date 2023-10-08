from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from dotenv import load_dotenv

load_dotenv()

# ==================================================
# CHANGE BELOW
subject_name = os.environ["SUBJECT_NAME"]

class_no_start = 2
class_no_end = 4
# whether your image file name is number or not
filename_is_number = False
# ==================================================

class_no_arr = list(range(class_no_start, class_no_end + 1))
class_no_arr = [str(i) for i in class_no_arr]

def natural_sort_key(s):
    # return filename as number by extract
    return [int(text) if text.isdigit() else text.lower() for text in re.split('(\d+)', s)]

def images_to_pdf(input_folder, output_pdf_path):
    image_files = [f for f in os.listdir(input_folder) if f.endswith(".jpg")]
    image_files.sort()  # sort files by name

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

    for class_no in class_no_arr:
        input_folder = "input/" + subject_name + "/" + class_no     # input folder path
        output_pdf_path = subject_name + "_" + class_no + ".pdf"    # output file name
        images_to_pdf(input_folder, output_pdf_path)
        print("Done " + class_no)

    print("Done")