import os
from gtts import gTTS
import PyPDF2

def convert():
    try:
        pdf = input('Path of PDF File: ')
        start_page = int(input('Start Page: '))
        end_page = int(input('End Page: '))

        filename = os.path.splitext(os.path.basename(pdf))[0]
        file = open(pdf, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdf)

        text = ''
        for num in range(start_page -1 , end_page):
            page = pdfReader.getPage(num)
            text += page.extractText()

        print('Converting to MP3...')

        mp3_file = gTTS(text=text, lang='en', slow=False)

        mp3_file.save(f'{filename}.mp3')

        print('File has been converted')

    except FileNotFoundError:
        print('File was not found')

    except ValueError:
        print('Conversion failed because the page numbers must be integers')

    except Exception as e:
        print(f'Conversion failed: {e}')

if __name__=='__main__':
    convert()