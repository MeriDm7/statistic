from reading_file_Ternopil import causes
from reading_file_Kyiv import open_file


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
    people = people[110:]
    for i in range(len(people)):
        people[i] = people[i][0] 
    dict_with_total = {}
    for i in range(13):
        dict_with_total[people[i * 10]] = people[i * 10 + 1]  
    return dict_with_total


def result():
    """
    Return the dict.
    """
    new_lst = open_file("Chernivetska_obl.csv")
    dict_by_years = {}
    dict_with_total = file_with_total_inform("Total_Chernivtsi.csv")
    for i in new_lst:
        dict_by_years[int(i[0])] = causes(i)
        dict_by_years[int(i[0])].update({"Total": dict_with_total[i[0]]})
    res_dict = {}
    res_dict["Chernivtsi"] = dict_by_years    
    return res_dict
