def causes(lst):
    """
    Function for creating dict with certain keys.
    """
    causes_dict = {}
    causes_dict["Dead"] = int(lst[1])
    causes_dict["Cancer"] = int(lst[3])
    causes_dict["Heart disease"] = int(lst[10])
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
    people = people[29:]
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
    res_lst = [] 
    for i in lst_with_data:
        append_lst = []
        for j in i:
            if j.isdigit() or j == "-":
                append_lst.append(j) 
        if len(append_lst) != 0:             
            res_lst.append(append_lst) 
    res_lst = res_lst[1:]
    res = []          
    for i in res_lst:
        if len(i) != len(res_lst[0]):
            i = i[1:]
            res.append(i) 
        else:
            res.append(i)                
    ln = len(res[0])
    data_by_years = []
    for i in range(ln):
        data_y = []
        for j in res:
            data_y.append(j[i])
        data_by_years.append(data_y)    
    dict_by_years = {}
    dict_with_total = file_with_total_inform("Total_Lviv.csv")
    for i in data_by_years:
        dict_by_years[int(i[0])] = causes(i)
        dict_by_years[int(i[0])].update({"Total": dict_with_total[i[0]]})
    res_dict = {}
    res_dict["Lviv"] = dict_by_years    
    return res_dict


def result():
    """
    Return the dict.
    """
    res = open_file("Lviv_oblast'.csv")
    return res