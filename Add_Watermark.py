from PyPDF2 import PdfFileReader, PdfFileWriter
import os

input_pdf = input('Path of pdf that is to be watermarked: ')
input_pdf_name = os.path.splitext(input_pdf)[0]
watermark = input('Path of watermark in pdf format: ')
output_pdf = f"{input_pdf_name}_watermarked.pdf"


def add_watermark(watermark, input_pdf, output_pdf):
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    reader = PdfFileReader(input_pdf)
    writer = PdfFileWriter()

    for page in range(reader.getNumPages()):
        page = reader.getPage(page)
        page.mergePage(watermark_page)
        writer.addPage(page)

    with open(output_pdf, 'wb') as file:
        writer.write(file)


add_watermark(watermark, input_pdf, output_pdf)

print('\nYour watermarked file is in the same directory as your original file.')
print('Thanks for using this program!')
