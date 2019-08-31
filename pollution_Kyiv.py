from convert_to_float import convert


def file_with_pollution(path):
    """
    Open file with pollution and create a dict with number of pollution each year
    """
    f = open(path, encoding='utf-8', errors='ignore')
    data = f.readlines()
    lst_with_data = []
    for i in data:
        i = i.replace('"', ' ').replace("\t", ' ').replace("\n", " ").replace("'", ' ').split(' ')
        lst_with_data.append(i)
    lst_with_data = lst_with_data[237:][::2][:-7]
    res_lst = []
    for i in range(13):
        res_lst.append(lst_with_data[i * 7: i * 7 + 2])
    dict_with_years = {}
    for i in res_lst:
            dict_with_years[int(i[0][0])] = convert(i[1][0])
    return dict_with_years
    

def result():
    """
    Return the dict.
    """
    res = file_with_pollution("Pollution_Kyiv.csv")
    dict_Kyiv = {}
    dict_Kyiv["Kyiv"] = res
    return dict_Kyiv