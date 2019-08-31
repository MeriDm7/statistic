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
    lst_with_data = lst_with_data[238:][::2][:-7]
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
    res_1 = file_with_pollution("Pollution_Chernigiv.csv")
    dict_Chern = {}
    dict_Chern["Chernigiv"] = res_1
    res_2 = file_with_pollution("Pollution_Odessa.csv")
    dict_Odessa = {}
    dict_Odessa["Odessa"] = res_2
    res_3 = file_with_pollution("Pollution_Ternopil.csv")
    dict_Ternopil = {}
    dict_Ternopil["Ternopil"] = res_3
    lst_with_dict = [dict_Chern, dict_Odessa, dict_Ternopil]
    return lst_with_dict
