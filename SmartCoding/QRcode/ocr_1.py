from PTL import Image
import pytesseract

image_path = r'OCR\newpaper.png'

pytesseract.pytesseract.tesseract_cmd \
    =r'C:\Program Files\Tesseract-OCR\tesseract.exe'

text = pytesseract.image_to_string(Image.open(image_path), lang="kor")

print(text)