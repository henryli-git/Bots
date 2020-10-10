from PIL import Image
from glob import glob
from os import path


def add_watermark(*args):
    try:
        input_images = glob(f'{source_folder_path}/*.*')

        for input_image in input_images:
            output_filename = path.basename(input_image)

            img = Image.open(input_image)
            img_width, img_height = img.size

            watermark = Image.open(watermark_path)
            watermark_width, watermark_height = watermark.size

            position = (int(img_width / 2 - watermark_width / 2), int(img_height / 2 - watermark_height / 2))

            transparent_img = Image.new('RGB', (img_width, img_height))
            transparent_img.paste(img, (0, 0))
            transparent_img.paste(watermark, position, mask=watermark)
            transparent_img.show()
            transparent_img.save(f'{destination_folder_path}/watermarked_{output_filename}')

        print('\nWatermark has been successfully applied')

    except Exception as e:
        print(f'\nThere was an error: {e}')


if __name__ == '__main__':
    source_folder_path = input('Enter source folder path: ')
    destination_folder_path = input('Enter destination folder path: ')
    watermark_path = input('Enter path of watermark: ')

    add_watermark(source_folder_path, destination_folder_path, watermark_path)
