from reading_file_Ternopil import causes


def file_with_total_inform(path_2):
    """
    Open file with information about population and create dict with information about population each year.
    """
    f_2 = open(path_2, encoding='utf-8', errors='ignore')
    data_2 = f_2.readlines()
    people = []
    for i in data_2:
        i = i.replace('"', ' ').replace("\t", ' ').replace("\n", " ").replace("'", ' ').split(' ')
        people.append(i)     
    people = people[32:]
    dict_with_total = {}
    for i in range(13):
        dict_with_total[people[i][0]] = people[i][1]  
    return dict_with_total


def open_file(path):
    """
    Open file and create a dict with information about death each year.
    """
    f = open(path, encoding='utf-8', errors='ignore')
    data = f.readlines()
    lst_with_data = []
    for i in data:
        i = i.replace('"', ' ').replace("\t", ' ').replace("\n", " ").replace("'", ' ').split(' ')
        lst_with_data.append(i)
    lst_with_data = lst_with_data[25:]
    dict_by_years = {}
    dict_with_total = file_with_total_inform("Total_Zakarpattya.csv")
    for i in lst_with_data:
        dict_by_years[int(i[0])] = causes(i)
        dict_by_years[int(i[0])].update({"Total": dict_with_total[i[0]]})
    res_dict = {}
    res_dict["Zakarpattya"] = dict_by_years    
    return res_dict


def result():
    """
    Return the dict.
    """
    res = open_file("Zakarp_obl.csv")
    return res