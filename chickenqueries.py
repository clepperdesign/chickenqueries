from openpyxl import load_workbook
wb = load_workbook('ch-database.xlsx')
ws = wb.active
def testing():
    eggnum = int(input("Enter desired number of eggs per year \n"))
    for row in ws.iter_rows():
        for cell in row:
            if isinstance(cell.value, int) and cell.value >= eggnum:
                print(row[0].value + ': ' + str(row[2].value) + ' eggs per year')
#testing()
def sortby():
    criteria = str.lower(input("Filter results by eggs per year or type(meat/eggs)? \n"))
    if "egg" in criteria:
        eggsort = int(input("Enter desired number of eggs per year \n"))
        for row in ws.iter_rows():
            for cell in row:
                if isinstance(cell.value, int) and cell.value >= eggsort:
                    print(row[0].value + ': ' + str(row[2].value) + ' eggs per year')
    if "type" in criteria:
        typesort = str.lower(input("Enter desired type: Eggs, Meat, or Dual \n"))
        for row in ws.iter_rows():
            for cell in row:
                if 'egg' in typesort:
                    if cell.value == 'eggs' or cell.value == 'dual':
                        print(row[0].value + ': ' + str(row[2].value) + ' eggs per year')
                elif 'meat' in typesort:
                    if cell.value == 'meat' or cell.value == 'dual':
                        print(row[0].value)
                elif 'dual' in typesort:
                    if cell.value == 'dual':
                        print(row[0].value + ': ' + str(row[2].value) + ' eggs per year')
                else:
                    print('cluck')                 
sortby()
