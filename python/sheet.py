import pandas as pd

def get_all_sheet_name():
    # 读取Excel文件
    file_path = '校招生大作业.xlsx'  # 替换为实际文件路径
    xls = pd.ExcelFile(file_path)

    # 获取所有表的名称
    sheet_names = xls.sheet_names
    res = {}
    res['code'] = 200
    res['data'] = sheet_names
    return res

def get_sheet_content(index):
    index = int(index)
    file_path = '校招生大作业.xlsx'  # 替换为实际文件路径
    # 读取第一个工作表的内容，跳过第一行作为表头
    df = pd.read_excel(file_path, sheet_name=index, header=0)
    
    # 处理合并单元格
    df.iloc[:, 0] = df.iloc[:, 0].ffill()  # 使用前一个非空单元格的值填充空值
    df = df.fillna('')
    # 将DataFrame转换为字典列表
    data_list = df.to_dict(orient='records')

    # for data in data_list:
    #     print(data)
    grouped_data = {}

    for data in data_list:
        category = data['类别']
        del data['类别']   
        if category in grouped_data:
            
            grouped_data[category].append(data)
        else:
            grouped_data[category] = [data]
    res = {}
    res['code'] = 200
    res['data'] = grouped_data
    return res

