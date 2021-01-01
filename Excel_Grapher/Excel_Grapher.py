from io import BytesIO
import os
import pandas as pd
import matplotlib.pyplot as plt


def excel_grapher():
    try:
        file_input = input('File Path: ')
        file_path = os.path.dirname(file_input)
        sheetnames = pd.ExcelFile(file_input).sheet_names

        for sheet in sheetnames:
            file = pd.read_excel(file_input, sheet_name=sheet)
            df = pd.DataFrame(file)
            df = df.dropna(axis=1, how='all')
            df_stats = df.describe()

            plt.style.use('ggplot')
            img = df.boxplot().figure
            imgdata = BytesIO()
            plt.savefig(imgdata)
            plt.close(img)

            writer = pd.ExcelWriter(f'{file_path}/{sheet}.xlsx', engine='xlsxwriter')
            df_stats.to_excel(writer, sheet_name=sheet)
            worksheet = writer.sheets[f'{sheet}']
            worksheet.insert_image('B11', '', {'image_data': imgdata})
            worksheet.set_zoom(150)
            writer.save()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    excel_grapher()
