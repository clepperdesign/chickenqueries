from openpyxl import load_workbook
wb = load_workbook('ch-database.xlsx')
ws = wb.active
def testing():
    for row in ws.iter_rows():
        for cell in row:
            if cell.value == "dual":
                print(row[0].value + ' ' + str(row[2].value))
testing()
