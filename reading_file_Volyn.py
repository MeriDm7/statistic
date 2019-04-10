from reading_file_Ternopil import causes


def open_file(path):
    f = open(path, encoding='utf-8', errors='ignore')
    data = f.readlines()
    lst_with_data = []
    for i in data:
        i = i.replace('"', ' ').replace("\t", ' ').replace("\n", " ").replace("'", ' ').split(' ')
        lst_with_data.append(i)
    lst_with_data = lst_with_data[17:]
    for i in range(len(lst_with_data)):
        lst_with_data[i] = int(lst_with_data[i][0])
    new_lst = []
    for i in range(13):
        new_lst.append(lst_with_data[i * 8:i * 8 + 8])   
    dict_by_years = {}
    for i in new_lst:
        dict_by_years[int(i[0])] = causes(i)
    return dict_by_years  


print(open_file("Volyn_obl.csv"))