from bs4 import BeautifulSoup
import requests
import os


def img_downloader(url, folder):
    try:
        dir = os.path.join(os.getcwd(), folder)

        if not os.path.exists(dir):
            os.mkdir(dir)

        os.chdir(dir)

        link = requests.get(url)
        soup = BeautifulSoup(link.text, 'html.parser')

        imgs = soup.find_all('img')

        for img in imgs:
            alt = img['alt']
            img_link = img['src']

            with open(f"{alt.replace('/', '').replace('|', '')}.jpg", 'wb') as f:
                pics = requests.get(img_link)
                f.write(pics.content)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    url = '____________________'  # input url of a website with images here
    folder = '___________________'  # input folder name here - folder will hold all the downloaded images
    img_downloader(url, folder)
