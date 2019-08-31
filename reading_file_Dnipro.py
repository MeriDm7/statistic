from reading_file_Ternopil import causes
from reading_file_Lviv import file_with_total_inform

def open_file(path_1):
    """
    Open file and create a dict with information about death each year.
    """
    f_1 = open(path_1, encoding='utf-8', errors='ignore')
    data_1 = f_1.readlines()
    lst_with_data = []
    for i in data_1:
        i = i.replace('"', ' ').replace("\t", ' ').replace("\n", " ").replace("'", ' ').split(' ')
        lst_with_data.append(i)
    dict_with_total = file_with_total_inform("Total_Dnipro.csv")
    lst_with_data = lst_with_data[21:] 
    dict_by_years = {}
    for i in lst_with_data:
        dict_by_years[int(i[0])] = causes(i)
        dict_by_years[int(i[0])].update({"Total": dict_with_total[i[0]]})
    res_dict = {}
    res_dict["Dnipro"] = dict_by_years    
    return res_dict


def result():
    """
    Return the dict.
    """
    res = open_file("Dnipro.csv")
    return res