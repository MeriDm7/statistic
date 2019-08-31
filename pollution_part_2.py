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
    lst_with_data = lst_with_data[19:][:-1]
    res_lst = []
    for i in lst_with_data:
        res_lst.append(i[:2])  
    return res_lst


def result():
    """
    Return list with dicts.
    """
    res_0 = file_with_pollution("Pollution_Kharkiv.csv")
    res_1 = file_with_pollution("Pollution_Dnipro.csv")
    res_1 = res_1[13:]
    res_2 = file_with_pollution("Pollution_Zakarpattya.csv")
    res_2 = res_2[13:]
    res_3 = file_with_pollution("Pollution_Lviv.csv")
    res_3 = res_3[13:]
    res_4 = file_with_pollution("Pollution_Khmelnytski.csv")
    res_4 = res_4[1:]
    res_5 = file_with_pollution("Pollution_Cherkasy.csv")
    res_5 = res_5[13:]
    res_6 = file_with_pollution("Pollution_Mykolaiv.csv")
    res_6 = res_6[6:]
    lst_with_res = [res_0, res_1, res_2, res_3, res_4, res_5, res_6]
    lst_with_names = ["Kharkiv", "Dnipro", "Zakarpattya", "Lviv", "Khmelnytski", "Cherkasy", "Mykolaiv"]
    lst_with_obl = []
    for i in range(7):
        el = lst_with_res[i]
        dict_with_numbers = {}
        for j in el:
            dict_with_numbers[int(j[0])] = convert(j[1])
        dict_with_names = {}
        dict_with_names[lst_with_names[i]] = dict_with_numbers
        lst_with_obl.append(dict_with_names)    
    return lst_with_obl

