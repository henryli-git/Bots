import os

to_pay_dir = ""
to_enter_dir = ""
paid_dir = ""
duplicates = ""


def duplicate_checker():

    if not os.path.exists(duplicates):
        os.makedirs(duplicates)

    to_enter_invoices = os.listdir(to_enter_dir)
    to_pay_invoices = []
    paid_invoices = []

    for root, dirs, files in os.walk(to_pay_dir):
        for file in files:
            to_pay_invoices.append(file)

    for root, dirs, files in os.walk(paid_dir):
        for file in files:
            paid_invoices.append(file)

    to_pay_invoices_set = set(os.path.basename(k)[:28] for k in to_pay_invoices if not k.endswith(".ini"))
    paid_invoices_set = set(os.path.basename(k)[:28] for k in paid_invoices if not k.endswith(".ini"))

    for x in to_enter_invoices:
        if x[:28] in to_pay_invoices_set:
            os.rename(to_enter_dir + os.sep + x, duplicates + os.sep + x)

        if x[:28] in paid_invoices_set:
            os.rename(to_enter_dir + os.sep + x, duplicates + os.sep + x)


if __name__ == "__main__":
    duplicate_checker()
