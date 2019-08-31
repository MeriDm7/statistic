from convert_to_float import  convert


def file_with_pollution(path):
    """
    Open file with pollution and create dicts with number of pollution each year.
    """
    f = open(path, encoding='utf-8', errors='ignore')
    data = f.readlines()
    lst_with_data = []
    for i in data:
        i = i.replace('"', ' ').replace("\t", ' ').replace("\n", " ").replace("'", ' ').split(' ')
        lst_with_data.append(i)
    lst_with_data = lst_with_data[239:][::2][:-7]
    res_lst = []
    for i in range(13):
        res_lst.append(lst_with_data[i * 7: i * 7 + 2])
    dict_with_years = {}
    for i in res_lst:
            dict_with_years[int(i[0][0])] = convert(i[1][0])
    return dict_with_years
    

def result():
    """
    Return list with dicts.
    """
    res_1 = file_with_pollution("Pollution_Zhytomyr.csv")
    res_2 = file_with_pollution("Pollution_Rivne.csv")  
    dict_Zh = {}
    dict_Rivn = {}
    dict_Zh["Zhytomyr"] = res_1
    dict_Rivn["Rivne"] = res_2
    lst = [dict_Rivn, dict_Zh]
    return lst