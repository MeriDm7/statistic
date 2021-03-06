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
    people = people[25:]   
    dict_with_total = {}
    for i in range(13):
        dict_with_total[people[i][0]] = people[i][1]  
    return dict_with_total


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
    dict_with_total = file_with_total_inform("Total_Mykolaiv.csv")
    lst_with_data = lst_with_data[12:]  
    dict_by_years = {}
    for i in lst_with_data:
        dict_by_years[int(i[0])] = causes(i)
        dict_by_years[int(i[0])].update({"Total": dict_with_total[i[0]]})
    res_dict = {}
    res_dict["Mykolaiv"] = dict_by_years    
    return res_dict


def result():
    """
    Return the dict.
    """
    res = open_file("Mykolaiv.csv")
    return res