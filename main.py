import matplotlib.pyplot as plt

from POLLUTION import new_lst
from the_end_result import lst_with_res

def main():
    """
    Get all found information about pollution and death and create graphics from that.
    """
    start = "This program allows you to get a line graph of dependecnce between mortality for various reasons and the release of pollutants into the air in all regions of Ukraine(or in general in Ukraine) from 2005 to 2017.\n"
    print(start)
    choosing = "Do you want to get the information about the whole country(1) or one certain region(2)?\nENTER 1 OR 2. "
    print(choosing)  
    choice = input() 
    pollution = new_lst 
    dead = lst_with_res  
    if choice == "1":
        poll = []
        for i in pollution:
            dict_with_years = list(i.values())[0]
            poll.append(dict_with_years["All"])   
        death = []
        cancer = []
        heart = []
        for i in dead:
            years = list(i.values())[0]
            death.append(years["All"]["Dead"])
            cancer.append(years["All"]["Cancer"])
            heart.append(years["All"]["Heart"])  
    elif choice == "2":
        region = "Please, choose about which region you want to get information(number):\
            \nCherkasy(1)               Chernigiv(2)            Chernivtsi(3)          Dnipro(4)              Ivano_Frankivsk(5)            Kharkiv(6)                  Kherson(7)\
            \nKhmelnytski(8)            Kirovograd(9)           Kyiv(10)               Lviv(11)               Mykolaiv(12)                  Odessa(13)                  Poltava(14)\
            \nRivne(15)                 Sumy(16)                Ternopil(17)           Vinnytsya(18)          Volyn(19)                     Zakarpattya(20)             Zaporizhzha(21)\
            \nZhytomyr(22)"
        print(region)
        chosed_region = input()
        chosed_region = int(chosed_region) - 1
        obl_poll = pollution[chosed_region]
        obl_death = dead[chosed_region]
        poll_by_years = list(obl_poll.values())[0]
        poll = list(poll_by_years.values())[:-1]
        death_by_years = list(list(obl_death.values())[0].values())[:-1]
        death = []
        cancer = []
        heart = []
        for i in death_by_years:
            death.append(i["Dead"])
            cancer.append(i["Cancer"])
            heart.append(i["Heart disease"])
    dict_with_xy = {}
    for i in range(len(poll)):
        dict_with_xy[poll[i]] = [death[i], cancer[i], heart[i]]
    dict_with_xy = dict(sorted(dict_with_xy.items()))    
    x_poll = list(dict_with_xy.keys())
    y1_death = []
    y2_cancer = []
    y3_heart = []
    for i in x_poll:
        y1_death.append(dict_with_xy[i][0])
        y2_cancer.append(dict_with_xy[i][1])
        y3_heart.append(dict_with_xy[i][2])
    plt.plot(x_poll, y1_death, color='black')
    plt.plot(x_poll, y2_cancer, color='orange')
    plt.plot(x_poll, y3_heart, color='red')
    plt.xlabel('Pollution')
    plt.ylabel('Percent of death')
    plt.title('Line')
    plt.show()                             


if __name__ == "__main__":
    main()