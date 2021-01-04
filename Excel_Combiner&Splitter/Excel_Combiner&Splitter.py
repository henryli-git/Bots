from functools import reduce
import pandas as pd


def merge(file):
    try:
        sheetnames = pd.ExcelFile(file).sheet_names
        df_list = []
        for sheet in sheetnames:
            df = pd.read_excel(file, sheet_name=sheet)
            df_list.append(df)

        df_merged = reduce(lambda left, right: pd.merge(left, right, left_index=True, right_index=True, how='outer'),
                           df_list)
        df_merged = df_merged.dropna(axis=1, how='all').fillna('')

        writer = pd.ExcelWriter('Combined.xlsx', engine='xlsxwriter')
        df_merged.to_excel(writer, sheet_name='Combined', index=False)
        worksheet = writer.sheets['Combined']
        worksheet.set_zoom(150)
        writer.save()

        print('Spreadsheets were combined into one spreadsheet')

    except Exception as e:
        print(e)


def split(file):
    try:
        sheetnames = pd.ExcelFile(file).sheet_names
        for sheet in sheetnames:
            df = pd.read_excel(file, sheet_name=sheet)
            df = df.dropna(axis=1, how='all')
            writer = pd.ExcelWriter(f'{sheet}.xlsx', engine='xlsxwriter')
            df.to_excel(writer, sheet_name=sheet, index=False)
            worksheet = writer.sheets[sheet]
            worksheet.set_zoom(150)
            writer.save()

        print('Spreadsheets were separated into different files')

    except Exception as e:
        print(e)


if __name__ == '__main__':
    file = input('Input file path: ')
    while True:
        question = input('Merge (M) or split (S) the spreadsheets or cancel (C): ').lower()
        if question == 'c':
            print('Process was cancelled')
            break
        elif question == 'm':
            merge(file)
            break
        elif question == 's':
            split(file)
            break
        else:
            continue
