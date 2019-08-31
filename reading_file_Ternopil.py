def causes(lst):
    """
    Function for creating dict with certain keys.
    """
    causes_dict = {}
    causes_dict["Dead"] = int(lst[1])
    causes_dict["Cancer"] = int(lst[3])
    causes_dict["Heart disease"] = int(lst[2])
    return causes_dict


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
    people = people[::2]   
    people = people[120:]
    for i in range(len(people)):
        people[i] = people[i][0] 
    dict_with_total = {}
    for i in range(13):
        dict_with_total[people[i * 10]] = people[i * 10 + 1]  
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
    dict_by_years = {}
    dict_with_total = file_with_total_inform("Total_Ternopil.csv")
    for i in lst_with_data[7:]:
        dict_by_years[int(i[0])] = causes(i) 
        dict_by_years[int(i[0])].update({"Total": dict_with_total[i[0]]})
    res_dict = {}
    res_dict["Ternopil"] = dict_by_years    
    return res_dict


def result():
    """
    Return the dict.
    """
    res = open_file("Ternopil_obl.csv")
    return res