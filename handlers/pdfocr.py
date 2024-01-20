from PIL import Image

import pytesseract
import pdf2image

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
# /Users/codingpan/Workspace/PythonProjects/python-docker/python-docker-demo/.venv/lib/python3.9/site-packages
TEST_IMAGE_NAME = '/Users/codingpan/Documents/Finance/eStmt_2023-12-11.pdf'
# Simple image to string
# print(pytesseract.image_to_string(Image.open('test.png')))

# Convert PDF to image
images = pdf2image.convert_from_path(TEST_IMAGE_NAME)

# Extract text from image
for image in images:
    text = pytesseract.image_to_string(image)
    print(text)

# In order to bypass the image conversions of pytesseract, just use relative or absolute image path
# NOTE: In this case you should provide tesseract supported images or tesseract will return error
# print(pytesseract.image_to_string('test.png'))

# List of available languages
# print(pytesseract.get_languages(config=''))

# French text image to string
# print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

# Batch processing with a single file containing the list of multiple image file paths
# print(pytesseract.image_to_string('images.txt'))

# Timeout/terminate the tesseract job after a period of time
# try:
#     print(pytesseract.image_to_string(TEST_IMAGE_NAME, timeout=2)) # Timeout after 2 seconds
# except RuntimeError as timeout_error:
#     # Tesseract processing is terminated
#     pass

# Get bounding box estimates
# print(pytesseract.image_to_boxes(Image.open(TEST_IMAGE_NAME)))

# Get verbose data including boxes, confidences, line and page numbers
# print(pytesseract.image_to_data(Image.open(TEST_IMAGE_NAME)))

# Get information about orientation and script detection
# print(pytesseract.image_to_osd(Image.open(TEST_IMAGE_NAME)))

# Get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr(TEST_IMAGE_NAME, extension='pdf')
# with open(TEST_IMAGE_NAME, 'w+b') as f:
#     f.write(pdf) # pdf type is bytes by default

# Get HOCR output
# hocr = pytesseract.image_to_pdf_or_hocr(TEST_IMAGE_NAME, extension='hocr')

# Get ALTO XML output
# xml = pytesseract.image_to_alto_xml(TEST_IMAGE_NAME)

# getting multiple types of output with one call to save compute time
# currently supports mix and match of the following: txt, pdf, hocr, box, tsv
# text, boxes = pytesseract.run_and_get_multiple_output(TEST_IMAGE_NAME, extensions=['txt', 'box'])