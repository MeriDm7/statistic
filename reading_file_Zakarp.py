from reading_file_Ternopil import causes


def open_file(path):
    f = open(path, encoding='utf-8', errors='ignore')
    data = f.readlines()
    lst_with_data = []
    for i in data:
        i = i.replace('"', ' ').replace("\t", ' ').replace("\n", " ").replace("'", ' ').split(' ')
        lst_with_data.append(i)
    lst_with_data = lst_with_data[25:]
    dict_by_years = {}
    for i in lst_with_data:
        dict_by_years[int(i[0])] = causes(i)
    return dict_by_years


print(open_file("Zakarp_obl.csv"))