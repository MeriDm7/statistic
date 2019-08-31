from convert_to_float import convert


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
    lst_with_data = lst_with_data[241:][::2][:-7]
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
    res_1 = file_with_pollution("Pollution_Ivano_Frankivsk.csv")
    res_2 = file_with_pollution("Pollution_Sumy.csv")
    dict_Iv = {}
    dict_Sum = {}
    dict_Iv["Ivano_Frankivsk"] = res_1
    dict_Sum["Sumy"] = res_2
    lst = [dict_Iv, dict_Sum]
    return lst