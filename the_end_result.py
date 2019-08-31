# In this file, I import a list of dictionaries that contain mortality information.
#I calculate the percentage of deaths in total and for various reasons (Heart Disease and Cancer)
#  relative to the total population each year in a particular area and record that percentage
#  instead of the previous one. And I calculate the average mortality rate in each area and add 
# it to the dictionaries

from RESULT import lst_with_res
from convert_to_float import convert


lst_with_keys = []
for i in lst_with_res:
    for j in i.keys():
        lst_with_keys.append(j)


for i in range(len(lst_with_res)):
    dict_by_year = lst_with_res[i][lst_with_keys[i]]
    lst_with_years = []
    for j in dict_by_year.keys():
        lst_with_years.append(j)
    dict_2005 = dict_by_year[lst_with_years[0]]
    lst_with_num = []
    for l in dict_2005.keys():
        lst_with_num.append(l)


for i in range(len(lst_with_res)):
        my_dict = lst_with_res[i][lst_with_keys[i]]
        all_percent_of_dead = []
        all_cancer = []
        all_heart = []
        for j in lst_with_years:
                dead = my_dict[j][lst_with_num[0]]
                cancer = my_dict[j][lst_with_num[1]]
                heart = my_dict[j][lst_with_num[2]]
                total = convert(my_dict[j][lst_with_num[3]]) * 1000
                percent_dead = (dead * 100) / total
                percent_cancer = (cancer * 100) / total
                percent_heart = (heart * 100) / total
                lst_with_res[i][lst_with_keys[i]][j][lst_with_num[0]] = round(percent_dead, 2)
                lst_with_res[i][lst_with_keys[i]][j][lst_with_num[1]] = round(percent_cancer, 2)
                lst_with_res[i][lst_with_keys[i]][j][lst_with_num[2]] = round(percent_heart, 2)
                lst_with_res[i][lst_with_keys[i]][j][lst_with_num[3]] = total
                all_percent_of_dead.append(round(percent_dead, 2))
                all_cancer.append(round(percent_cancer, 2))
                all_heart.append(round(percent_heart, 2))
        mid_dead = round(sum(all_percent_of_dead) / len(all_percent_of_dead), 2)
        mid_cancer = round(sum(all_cancer) / len(all_cancer), 2) 
        mid_heart = round(sum(all_heart) / len(all_heart), 2)  
        mid_dict = {}
        mid_dict["Dead"] = mid_dead
        mid_dict["Cancer"] = mid_cancer
        mid_dict["Heart"] = mid_heart     
        lst_with_res[i][lst_with_keys[i]]["All"] = mid_dict   
