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
    lst_with_data = lst_with_data[120:][:-7]
    res_lst = []
    for i in range(13):
        res_lst.append(lst_with_data[i * 7: i * 7 + 2])
    dict_with_years = {}
    for i in res_lst:
            dict_with_years[int(i[0][0])] = convert(i[1][0])
    res_dict = {}
    res_dict["Volyn"] = dict_with_years
    return res_dict


def result():
    """
    Return the dict.
    """
    res = file_with_pollution("Pollution_Volyn.csv")
    return res