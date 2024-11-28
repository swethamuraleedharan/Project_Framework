import xlrd
path = r'C:\Users\user\PycharmProjects\pythonProject\pythonProject\Framework\Excel_Files\registernew_data.xlsx'
reg_workbook = xlrd.open_workbook(path)
reg_sheet_name = reg_workbook.sheet_by_name('register')
reg_rows = reg_sheet_name.get_rows()
header = next(reg_rows)

def register_locators():
    reg_dict = {}
    for ele in reg_rows:
        reg_dict[ele[0].value] = (ele[1].value , ele[2].value)
    return reg_dict


