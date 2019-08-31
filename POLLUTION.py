from pollution_Chernivtsi import result as res_1
from pollution_Kherson import result as res_2
from pollution_Kirovograd import result as res_3
from pollution_Kyiv import result as res_4
from pollution_part_1 import result as res_5
from pollution_part_2 import result as res_6
from pollution_part_3 import result as res_7
from pollution_part_4 import result as res_8
from pollution_Poltava import result as res_9
from pollution_Vinnytsya import result as res_10
from pollution_Volyn import result as res_11
from pollution_Zaporizhzha import result as res_12

# In this file I import all dicts with pollution and create one sorted list with these dicts and add number of total pollution in each dict.
lst_with_dicts = []
lst_with_dicts.append(res_1())
lst_with_dicts.append(res_2())
lst_with_dicts.append(res_3())
lst_with_dicts.append(res_4())
lst_with_dicts = lst_with_dicts + res_5()
lst_with_dicts += res_6()
lst_with_dicts += res_7()
lst_with_dicts += res_8()
lst_with_dicts.append(res_9())
lst_with_dicts.append(res_10())
lst_with_dicts.append(res_11())
lst_with_dicts.append(res_12())
regions = []
for i in lst_with_dicts:
        regions += list(i.keys())

new_lst = []  

regions = list(sorted(regions))   

for i in regions:
    for j in lst_with_dicts:
        if list(j.keys()) == [i]:
            new_lst.append(j)   

new_lst[11]["Mykolaiv"][2016] = new_lst[11]["Mykolaiv"].pop(20162)
new_lst[11]["Mykolaiv"] = dict(sorted(new_lst[11]["Mykolaiv"].items()))
new_lst[4]["Ivano_Frankivsk"][2016] = new_lst[4]["Ivano_Frankivsk"].pop(20162)
new_lst[4]["Ivano_Frankivsk"] = dict(sorted(new_lst[4]["Ivano_Frankivsk"].items()))

lst_with_keys = []
for i in new_lst:
    for j in i.keys():
        lst_with_keys.append(j)
      
lst_with_years = []
example = new_lst[0][lst_with_keys[0]]
for j in example.keys():
    lst_with_years.append(j)

for i in range(len(new_lst)):
        my_dict = new_lst[i][lst_with_keys[i]]
        all_pollution = []
        for j in lst_with_years:
                all_pollution.append(my_dict[j])       
        mid_poll = round(sum(all_pollution) / len(all_pollution), 2)
        new_lst[i][lst_with_keys[i]]["All"] = mid_poll