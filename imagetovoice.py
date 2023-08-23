from PIL import Image
from gtts import gTTS
import pytesseract
from pytesseract import image_to_string

'''step 1 :-  if you don,t have library like pillow,gtts and pytesseract then open the ternminal and copy and paste following code : _----
pip install pillow
pip install gtts
pip install pytesseract
'''
"""Step 2:- download the exe file of tesseract.exe for window 
Run the file and note down the path where you are going to save it
you can download it from link below :--
https://github.com/UB-Mannheim/tesseract/wiki
"""
#In place of 'C:\Program Files\Tesseract-OCR\tesseract.exe' you have to write the path of tesseract while installing

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_sound(path_to_image):
    """
    Function for converting an  image to sound
    """
    try:
        loaded_image = Image.open(path_to_image)
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        print(cleaned_text)
        sound = gTTS(cleaned_text, lang="en")
        sound.save(r"C:\Users\rahul\OneDrive\Desktop\sound.mp3")
        return True
    except Exception as bug:
        print("The bug thrown while excuting the code\n", bug)
        return


if __name__ == "__main__":
    image_to_sound(r"C:\Users\rahul\OneDrive\Desktop\img.png")