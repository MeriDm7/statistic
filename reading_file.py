def causes(lst):
    causes_dict = {}
    causes_dict["Total"] = int(lst[1])
    causes_dict["Cancer"] = int(lst[3])
    causes_dict["Heart disease"] = int(lst[10])
    return causes_dict


def open_file(path):
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
    for i in data_by_years:
        dict_by_years[int(i[0])] = causes(i)
    return dict_by_years  


print(open_file("Lviv_oblast'.csv"))    