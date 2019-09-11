import xlrd
'''不管这个excel有多少个sheet表格，每个表格有多少条用例，依次去自动执行,而且自动判断用例的结果，只差一步用的执行了吧'''
def case_data(file):
    excel = xlrd.open_workbook(file)
    sheet_count = len(excel.sheets())  # 获取excel表总共有多少个sheet表格
    result_list = []  # 定义一个空list
    for n in range(0, sheet_count):
        sheet = excel.sheet_by_index(n)  # 表示去读第几个sheet表格
        rows, cols = sheet.nrows, sheet.ncols
        # print(rows,cols)                  #这个excel的行，列，4,4
        first_row_value = sheet.row_values(0)  # 先获取第一行所有的值，字典的key
        # print(first_row_value)               #[编号，接口用例名称，Host，接口url]
        for i in range(1, rows):
            # 每一行组装成一个字典,定义一个空字典
            info = {}
            for j in range(0, cols):
                info[first_row_value[j]] = sheet.row_values(i)[j]
            result_list.append(info)
    return  result_list

res=case_data(r"D:\PythonCode\Demo\intercase.xlsx")
print(res)

'''判断第一条用例是否正确'''
import json
def is_json_contain(actual,expect):
    '''预期结果是否在实际结果中，而且值正确'''
    if not isinstance(actual,dict) or not isinstance(expect,dict):
        actual=json.loads(actual)
        expect=json.loads(expect)
        # actual=eval(actual)
        # expect=eval(expect)
        print(type(actual),type(expect))
    for key ,value in expect.items():
        if key in actual:
            print("{}在实际结果里面".format(key))
            if value!=actual[key]:
                print("结果错误：预期结果是:{0},但是实际结果是：{1}".format(value,actual[key]))
            else:
                print("结果正确，pass")
        else:
            print("{}根本就不在实际结果里面".format(key))
res=case_data(r"D:\PythonCode\Demo\intercase.xlsx")
actual=res[0]['实际结果']
expect=res[0]['预期结果']
print(actual)
print(expect)
is_json_contain(actual,expect)