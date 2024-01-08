import PyPDF2
import pyperclip
import fitz
import os
import pygame
import transformers
import tensorflow
from transformers import pipeline
from pdf2docx import Converter
from gtts import gTTS
from pygame import mixer
mixer.init()

# #class Human:
#     #def __init__(self,y,z):
#         #elf.name = y;
#         #self.age = z;
#     def sayName():
#         prin

# h1 = Human("Jai",16);
# print(h1.name);
# print(h1.age);


class Pdf_Tools:
    def __init__(self):
        pass

    def cut_pdf(self,input_pdf_path, init_page, end_page, output_pdf_path):
        with open(input_pdf_path, 'rb') as input_pdf:
            init_page -= 1
            pdf_reader = PyPDF2.PdfReader(input_pdf)
            pdf_length = len(pdf_reader.pages)

            with open(output_pdf_path, "wb") as output_pdf:
                pdf_writer = PyPDF2.PdfWriter()
                for page_num in range(init_page, end_page):
                    pdf_writer.add_page(pdf_reader.pages[page_num])
                pdf_writer.write(output_pdf)


    def merge_pdf(self,pdf1_path, pdf2_path, output_pdf_path):
        pdf_writer = PyPDF2.PdfWriter()

        with open(pdf1_path, "rb") as pdf_1:
            pdf_reader1 = PyPDF2.PdfReader(pdf_1)
            for page_num in range(len(pdf_reader1.pages)):
                page = pdf_reader1.pages[page_num]
                pdf_writer.add_page(page)

        with open(pdf2_path, "rb") as pdf_2:
            pdf_reader2 = PyPDF2.PdfReader(pdf_2)
            for page_num in range(len(pdf_reader2.pages)):
                page = pdf_reader2.pages[page_num]
                pdf_writer.add_page(page)

        with open(output_pdf_path, "wb") as output_pdf:
            pdf_writer.write(output_pdf)


    def extract_text(self,input_pdf_filepath):
        text = ""
        input_pdf = fitz.open(input_pdf_filepath)
        for page_num in range(input_pdf.page_count):
            page = input_pdf.load_page(page_num)
            text += page.get_text()
        tools.copy_text_to_clipboard(text)
        return text


    def chunk_text(self,input_text):
        length = len(input_text)
        max_length = 5096

        chunked_text = []

        if length < max_length:
            chunked_text.append(input_text)
        else:
            start = 0
            while start < length:
                chunked_text.append(input_text[start:start+max_length])
                start += max_length
        return chunked_text


    def text_to_speech(self,text):
        language = "en"
        speech = gTTS(text=text, lang=language, slow=False)
        speech.save("textToSpeech.mp3")

        mixer.music.load("textToSpeech.mp3")
        mixer.music.set_volume(0.7)
        mixer.music.play()

        paused = False

        clock = pygame.time.Clock()
        while pygame.mixer.music.get_busy():
            clock.tick(30)

    def protect_pdf(self,input_pdf_filepath, password):
        with open(input_pdf_filepath, "rb") as input_pdf:
            pdf_reader = PyPDF2.PdfReader(input_pdf_filepath);
            pdf_writer = PyPDF2.PdfWriter();

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

            pdf_writer.encrypt(password)

            with open(input_pdf_filepath, "wb") as output_pdf:
                pdf_writer.write(output_pdf)


    def compress(self,input_pdf_filepath):
        pdf_reader = PyPDF2.PdfReader(input_pdf_filepath)
        pdf_writer = PyPDF2.PdfWriter()

        for page in pdf_reader.pages:
            page.compress_content_streams()
            pdf_writer.add_page(page)

        with open(f"{input_pdf_filepath}-compressed.pdf", "wb") as output_pdf:
            pdf_writer.write(output_pdf)

    def pdf_to_png(self,input_pdf_filepath):
        pdf_document = fitz.open(input_pdf_filepath)

        # Iterate through each page
        for page_number in range(pdf_document.page_count):
            # Get each page
            page = pdf_document.load_page(page_number)

            # Convert the page to a pixmap
            pixmap = page.get_pixmap()

            # Save the pixmap as a PNG file
            pixmap.save(f"page_{page_number + 1}.png")

        # Close the PDF document
        pdf_document.close()


    def pdf_to_docx(self,input_pdf_filepath, output_pdf_filepath):
        cv = Converter(input_pdf_filepath)

        if os.path.exists(output_pdf_filepath) == False:
            with open(output_pdf_filepath, "a") as file:
                pass

        # Convert PDF to Word
        cv.convert(output_pdf_filepath, start=0, end=None)

        # Close the converter
        cv.close()


    def copy_text_to_clipboard(self,text):
        pyperclip.copy(text)


    def summarize_text(self, input_text):
        summarizer = pipeline("summarization", model="t5-small")

        # Running the summarization on the input text
        summarized_text = ""

        for each in input_text:
            summarized = summarizer(input_text, max_length=100, min_length=100, do_sample=False)
            summary_text = summarized[0]['summary_text']
            summarized_text += summary_text

        return summarized_text


if __name__ == "__main__":

    tools = Pdf_Tools()

    decision = input("""Please select what you would like to do from the options below: 
                     
    (1) Cut PDF
    (2) Merge PDF
    (3) Extract Text
    (4) Chunk Text from PDF
    (5) Text-To-Speech
    (6) Password Protect PDF
    (7) Compress PDF
    (8) Convert PDF to PNG Images
    (9) Convert PDF to DOCX
    (10) Copy PDF text to clipboard
    (11) Summarize Text
    (12) STOP
                     """)
    
    while decision != "12":

        if decision == "1":
            tools.cut_pdf("files/RDPD.pdf", 15, 23, "files/output4.pdf")
            # tools.cut_pdf("files/RDPD.pdf", 16, 17, "files/output5.pdf")

        if decision == "2":
            tools.merge_pdf("files/output4.pdf", "files/RDPD.pdf", "files/output_merge.pdf")

        if decision == "3":
            print(tools.extract_text("files/output4.pdf"))
        if decision == "4":
            chunk_text_input = tools.extract_text("files/output4.pdf")
            chunk = tools.chunk_text(chunk_text_input)
            for each in chunk:
                print(each)
                print("\n\n\n\n\n\n\n\n")

        if decision == "5":
            give = tools.extract_text("files/output5.pdf")
            tools.text_to_speech(text=give)

        #SHOWCASE COMPRESS BEFORE PROTECTION
        if decision == "6":
            tools.protect_pdf("files/RDPD.pdf", "test")

        #SHOWCASE COMPRESS BEFORE PROTECTION
        if decision == "7":
            tools.compress("files/RDPD.pdf")
        if decision == "8":
            tools.pdf_to_png("files/output5.pdf")
        if decision == "9":
            tools.pdf_to_docx("files/output5.pdf", "files/output5.docx")
        if decision == "10":
            tools.copy_text_to_clipboard("I love CS!!!!!!!!!!!!!!!!!!")
        if decision == "11":
            input_text = tools.extract_text("files/output5.pdf")
            chunked_input = tools.chunk_text(input_text)
            print(tools.summarize_text(chunked_input))

        decision = input("""Please select what you would like to do from the options below: 
                     
    (1) Cut PDF
    (2) Merge PDF
    (3) Extract Text
    (4) Chunk Text from PDF
    (5) Text-To-Speech
    (6) Password Protect PDF
    (7) Compress PDF
    (8) Convert PDF to PNG Images
    (9) Convert PDF to DOCX
    (10) Copy PDF text to clipboard
    (11) Summarize Text
    (12) STOP
                     """)