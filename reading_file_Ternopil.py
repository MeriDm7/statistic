def causes(lst):
    causes_dict = {}
    causes_dict["Total"] = int(lst[1])
    causes_dict["Cancer"] = int(lst[3])
    causes_dict["Heart disease"] = int(lst[2])
    return causes_dict


def open_file(path):
    f = open(path, encoding='utf-8', errors='ignore')
    data = f.readlines()
    lst_with_data = []
    for i in data:
        i = i.replace('"', ' ').replace("\t", ' ').replace("\n", " ").replace("'", ' ').split(' ')
        lst_with_data.append(i)
    dict_by_years = {}
    for i in lst_with_data[7:]:
        dict_by_years[int(i[0])] = causes(i)
    return dict_by_years  


print(open_file("Ternopil_obl.csv"))