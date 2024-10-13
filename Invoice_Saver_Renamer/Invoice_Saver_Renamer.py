from pathlib import Path
import os
import win32com.client
import re
import PyPDF2

output_dir = ""
desktop = ""


def save_rename():
    output_dir.mkdir(parents=True, exist_ok=True)

    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

    inbox = outlook.GetDefaultFolder(6)
    donebox = outlook.GetDefaultFolder(6).Folders("Done")

    messages = inbox.Items

    for msg in messages:
        subject = msg.Subject
        date = msg.SentOn.strftime("%Y%m%d")
        body = msg.body
        attachments = msg.Attachments

        if "Vendor_1_Invoice" in subject:
            msg.Categories = "Blue category"
            msg.Save()
            for attachment in attachments:
                attachment.SaveAsFile(output_dir / str(attachment))

        if "Vendor_2_Invoice" in subject:
            msg.Categories = "Blue category"
            msg.Save()
            for attachment in attachments:
                if ".pdf" in attachment.FileName:
                    pdf_name = str(desktop) + str(subject[4:33]) + " - " + str(date) + ".pdf"
                    attachment.SaveAsFile(pdf_name)

        if "Vendor_3_Invoice" in subject:
            msg.Categories = "Blue category"
            msg.Save()
            for attachment in attachments:
                attachment.SaveAsFile(output_dir / (str(attachment)[:28] + " " + str(date) + ".pdf"))

        if "Vendor_4_Invoice" in subject:
            msg.Categories = "Blue category"
            msg.Save()
            for attachment in attachments:
                if ".pdf" in attachment.FileName:
                    attachment.SaveAsFile(output_dir / str(attachment))

    for msg in reversed(messages):
        if msg.Categories == "Blue category":
            msg.Move(donebox)

    filer()


def filer():
    os.chdir(output_dir)
    for file in os.listdir():
        if "emailsignaturesmlogo" in file:
            os.remove(file)
            continue

        name, ext = os.path.splitext(file)

        if "Vendor_1" in name:
            invoice_amount = re.findall("\(?\d+,?\d+\.\d+\)?", pdf_extractor(file))
            if invoice_amount == []:
                os.remove(file)
            else:
                os.rename(file, f"{name} ${invoice_amount[-1]}.pdf")
                continue

        if "Vendor_2" in name:
            invoice_amount = re.findall("\(?\d+,?\d+\.\d+\)?", pdf_extractor(file))
            if invoice_amount == []:
                os.remove(file)
            else:
                os.rename(file, f"{name} ${invoice_amount[-1]}.pdf")
                continue

        if "Vendor_3" or "Vendor_4" in name:
            invoice_amount = re.findall("\(?\$\d+,?\d+\.\d+\)?", pdf_extractor(file))

            if invoice_amount == []:
                os.remove(file)

            else:
                invoice_anixter = re.findall("[7]\d{8}", pdf_extractor(file))
                invoice_tried = re.findall("[7]\d\D\d{6}", pdf_extractor(file))

                if invoice_anixter:
                    os.rename(file, f"Anixter {invoice_anixter[0]} {invoice_amount[-1]}.pdf")
                elif invoice_tried:
                    os.rename(file, f"Tri-ed {invoice_tried[0]} {invoice_amount[-1]}.pdf")


def pdf_extractor(file):
    output = ""
    with open(file, 'rb') as pdfFileObject:
        reader = PyPDF2.PdfReader(pdfFileObject)
        count = len(reader.pages)
        for i in range(count):
            page = reader.pages[i]
            output += page.extract_text()

    return output


if __name__ == "__main__":
    save_rename()
