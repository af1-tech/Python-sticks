print("Bete - versiunea Python")
print("Programator: Steciuc Angel Florentin")
print("Regula de baza este: cel care taie ultima piesa a pierdut jocul! \n")
nr_juc=0
nume1=""
nume2=""
rnd=0
bte=0
dificultate=0
loop=10
print("Alege nivelul de dificultate: ")
print("1 - Usor")
print("2 - Normal")
print("3 - Greu")
while (loop!=0):
    try:
        dificultate=int(input("Introdu optiunea aleasa:"))
        if ((dificultate==1) or (dificultate==2) or (dificultate==3)):
            loop=0
        else:
            print("Ai introdus o optiune gresita")
            loop=10
    except ValueError:
        print("Ai introdus o optiune gresita!")


print("Alege numarul de jucatori:")
print("1 - Un jucator contra A.I.")
print("2 - Doi jucatori")
loop=10
while (loop!=0):
    try:
        nr_juc=int(input("Introdu optiunea aleasa:"))
        if (nr_juc==1):
            nume1=input("Introdu numele jucatorului:")
            loop=0
        elif (nr_juc==2):
            nume1=input("Introdu numele primului jucator:")
            nume2=input("Introdu numele celui de al doilea jucator:")
            loop=0;
        else:
            print("Ai introdus o optiune gresita!")
            loop=10;
    except ValueError:
        print("Ai introdus o optiune gresita!")

# creare si afisare initiala a betelor
list1=['|']
list2=['|','|','|']
list3=['|','|','|','|','|']
list4=['|','|','|','|','|','|','|']
if (dificultate==1):
    print("\n","Randul 1   ",end='')
    for i in range (0,len(list1)):
        print(list1[i],end=' ')
    print("\n","Randul 2   ",end='')
    for i in range (0,len(list2)):
        print(list2[i],end=' ')
    print("\n","Randul 3   ",end='')
    for i in range (0,len(list3)):
        print(list3[i],end=' ')
    print("\n")
elif (dificultate==2):
    print("\n", "Randul 1   ", end='')
    for i in range(0, len(list2)):
        print(list2[i], end=' ')
    print("\n", "Randul 2   ", end='')
    for i in range(0, len(list3)):
        print(list3[i], end=' ')
    print("\n", "Randul 3   ", end='')
    for i in range(0, len(list4)):
        print(list4[i], end=' ')
    print("\n")
elif (dificultate==3):
    print("\n", "Randul 1   ", end='')
    for i in range(0, len(list1)):
        print(list1[i], end=' ')
    print("\n", "Randul 2   ", end='')
    for i in range(0, len(list2)):
        print(list2[i], end=' ')
    print("\n", "Randul 3   ", end='')
    for i in range(0, len(list3)):
        print(list3[i], end=' ')
    print("\n", "Randul 4   ", end='')
    for i in range(0, len(list4)):
        print(list4[i], end=' ')
    print("\n")


rand=0
nr_ales=0
jucator=0;

# cuprins joc
if ((nr_juc==1) and (dificultate==1)):
    loop = 10;
    while (loop != 0):
        if (jucator==0):

            # selectare rand
            loop1=10
            while (loop1 != 0):
                print("Muta ",nume1)
                print("Introdu randul pe care il alegi:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 3)):
                        if ((rand == 1) and (len(list1) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 2) and (len(list2) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 3) and (len(list3) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        else:
                            loop1=0
                    else:
                        print("Ai introdus o optiune gresita!")
                        loop1=10
                except ValueError:
                    print("Ai introdus o optiune gresita!")


            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("Cate bete vrei sa tai? ")
                try:
                    nr_ales=int(input())
                    if ((rand == 1) and ((nr_ales==0) or (nr_ales > len(list1)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 2) and ((nr_ales==0) or (nr_ales > len(list2)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 3) and ((nr_ales==0) or (nr_ales > len(list3)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    else:
                        loop1=0
                except ValueError:
                    print("Ai introdus o optiune gresita!")

            print("Ai ales randul",rand, "si ai taiat",nr_ales,"bete.")

            # aplicare alegeri
            if (rand == 1):
                for i in range (0,nr_ales):
                    del list1[-1]
            elif (rand == 2):
                for i in range (0,nr_ales):
                    del list2[-1]
            elif (rand == 3):
                for i in range (0,nr_ales):
                    del list3[-1]

            # afisare noua tabela de joc
            print("Randul 1   ",end=' ')
            for i in range (0,len(list1)):
                print(list1[i],end=' ')
            print("\n")
            print("Randul 2   ",end=' ')
            for i in range (0,len(list2)):
                print(list2[i],end=' ')
            print("\n")
            print("Randul 3   ",end=' ')
            for i in range (0,len(list3)):
                print(list3[i],end=' ')
            print("\n")
            if (len(list1) + len(list2) + len(list3) == 0):
                print("A.I. a castigat!")
                loop=0;
            else:
                jucator=1

        elif (jucator == 1):
            #Rationament A.I.
            print("\n")
            print("Muta A.I.")
            #cazul par par par
            if ((len(list1) % 2 == 0) and (len(list2) % 2 == 0) and (len(list3) % 2 == 0)):
                if ((len(list2) == 2) and (len(list3) > 2)):
                    while (len(list3) != 2):
                        del list3[-1]
                        rnd=3
                        bte=bte+1

                elif ((len(list2) == 2) and (len(list3) == 2)):
                    del list3[-1]
                    rnd = 3
                    bte = bte + 1

                elif ((len(list2) == 0) and (len(list3) >= 2)):
                    while (len(list3.size) != 1):
                        del list3[-1]
                        rnd = 3
                        bte = bte + 1

                elif ((len(list2) == 2) and (len(list3) == 0)):
                    del list2[-1]
                    rnd = 2
                    bte = bte + 1

            #cazul impar impar impar
            elif ((len(list1) % 2 != 0) and (len(list2) % 2 != 0) and (len(list3) % 2 != 0)):
                if ((len(list2) == 1) and (len(list3) == 1)):
                    del list3[-1]
                    rnd = 3
                    bte = bte + 1

                elif ((len(list2) > 1) and (len(list3) > 1)):
                    while (len(list3) != 2):
                        del list3[-1]
                        rnd = 3
                        bte = bte + 1

                elif ((len(list2) > 1) and (len(list3) == 1)):
                    while (len(list2) != 1):
                        del list2[-1]
                        rnd = 2
                        bte = bte + 1
                elif ((len(list2) == 1) and (len(list3) > 1)):
                    while (len(list3) != 1):
                        del list3[-1]
                        rnd = 3
                        bte = bte + 1

            #cazul par par impar
            elif ((len(list1) % 2 == 0) and (len(list2) % 2 == 0) and (len(list3) % 2 != 0)):
                if ((len(list1) == 0) and (len(list2) == 0)):
                    if (len(list3) > 1):
                        while (len(list3) != 1):
                            del list3[-1]
                            rnd = 3
                            bte = bte + 1
                    else:
                        del list3[-1]
                        rnd = 3
                        bte = bte + 1
                elif ((len(list1) == 0) and (len(list2) == 2)):
                    if (len(list3)>1):
                        while (len(list3) != 2):
                            del list3[-1]
                            rnd = 3
                            bte = bte + 1
                    else:
                        while (len(list2) != 0):
                            del list2[-1]
                            rnd = 2
                            bte = bte + 1

            # cazul par impar impar
            elif ((len(list1) % 2 == 0) and (len(list2) % 2 != 0) and (len(list3) % 2 != 0)):
                if (len(list2) == len(list3)):
                    del list3[-1]
                    rnd = 3
                    bte = bte + 1
                elif ((len(list2)==1) and (len(list3)>=1)):
                    while (len(list3)!=0):
                        del list3[-1]
                        rnd = 3
                        bte = bte + 1
                elif (len(list2) > len(list3)):
                    while (len(list2) != len(list3)):
                        del list2[-1]
                        rnd = 2
                        bte = bte + 1
                elif (len(list3) > len(list2)):
                    while (len(list3) != len(list2)):
                        del list3[-1]
                        rnd = 3
                        bte = bte + 1

            # cazul impar par par
            elif ((len(list1) % 2 != 0) and (len(list2) % 2 == 0) and (len(list3) % 2 == 0)):
                if ((len(list2) >= 2) and (len(list3) >= 2)):
                    del list1[-1]
                    rnd = 1
                    bte = bte + 1
                elif ((len(list2) == 0) and (len(list3) >= 2)):
                    while (len(list3) != 0):
                        del list3[-1]
                        rnd = 3
                        bte = bte + 1
                elif ((len(list2) == 2) and (len(list3) == 0)):
                    while (len(list2) != 0):
                        del list2[-1]
                        rnd = 2
                        bte = bte + 1

            #cazul impar impar par
            elif ((len(list1) % 2 != 0) and (len(list2) % 2 != 0) and (len(list3) % 2 == 0)):
                if ((len(list2) >= 1) and (len(list3) == 0)):
                    while (len(list2) != 0):
                        del list2[-1]
                        rnd = 2
                        bte = bte + 1
                elif ((len(list2) == 1) and (len(list3) >= 2)):
                    while (len(list3) != 1):
                        del list3[-1]
                        rnd = 3
                        bte = bte + 1
                elif ((len(list2) == 3) and (len(list3) >= 2)):
                    if (len(list2) > len(list3)):
                        while (len(list2) != len(list3)):
                            del list2[-1]
                            rnd = 2
                            bte = bte + 1
                    elif (len(list3) > len(list2)):
                        while (len(list3) != len(list2)):
                            del list3[-1]
                            rnd = 3
                            bte = bte + 1

            # cazul impar par impar
            elif ((len(list1) % 2 != 0) and (len(list2) % 2 == 0) and (len(list3) % 2 != 0)):
                if ((len(list2) == 0) and (len(list3) >= 1)):
                    while (len(list3) != 0):
                        del list3[-1]
                        rnd = 3
                        bte = bte + 1
                elif ((len(list2) == 2) and (len(list3) == 1)):
                    del list2[-1]
                    rnd = 2
                    bte = bte + 1
                elif ((len(list2) == 2) and (len(list3) >= 3)):
                    while (len(list3) != 2):
                        del list3[-1]
                        rnd = 3
                        bte = bte + 1

            # cazul par impar par
            elif ((len(list1) % 2 == 0) and (len(list2) % 2 != 0) and (len(list3) % 2 == 0)):
                if ((len(list2) == 1) and (len(list3) == 0)):
                    del list2[-1]
                    rnd = 2
                    bte = bte + 1
                elif ((len(list2) == 3) and (len(list3) == 0)):
                    while (len(list2) != 1):
                        del list2[-1]
                        rnd = 2
                        bte = bte + 1
                elif ((len(list2) == 1) and (len(list3) >= 2)):
                    while (len(list3) != 0):
                        del list3[-1]
                        rnd = 3
                        bte = bte + 1
                elif ((len(list2) == 3) and (len(list3) >= 2)):
                    if (len(list2) > len(list3)):
                        del list2[-1]
                        rnd = 2
                        bte = bte + 1
                    elif (len(list3) > len(list2)):
                        del list3[-1]
                        rnd = 3
                        bte = bte + 1

            print("A.I. a ales randul", rnd, "si a taiat", bte, "bete.")
            bte=0

            # afisare noua tabela de joc
            print("Randul 1   ", end=' ')
            for i in range(0, len(list1)):
                print(list1[i], end=' ')
            print("\n")
            print("Randul 2   ", end=' ')
            for i in range(0, len(list2)):
                print(list2[i], end=' ')
            print("\n")
            print("Randul 3   ", end=' ')
            for i in range(0, len(list3)):
                print(list3[i], end=' ')
            print("\n")
            if (len(list1) + len(list2) + len(list3) == 0):
                print(nume1 + " a castigat!")
                loop = 0;
            else:
                jucator = 0

elif ((nr_juc==1) and (dificultate==2)):
    loop = 10;
    while (loop != 0):
        if (jucator==0):

            # selectare rand
            loop1=10
            while (loop1 != 0):
                print("Muta ",nume1)
                print("Introdu randul pe care il alegi:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 3)):
                        if ((rand == 1) and (len(list2) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 2) and (len(list3) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 3) and (len(list4) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        else:
                            loop1=0
                    else:
                        print("Ai introdus o optiune gresita!")
                        loop1=10
                except ValueError:
                    print("Ai introdus o optiune gresita!")

            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("Cate bete vrei sa tai? ")
                try:
                    nr_ales=int(input())
                    if ((rand == 1) and ((nr_ales==0) or (nr_ales > len(list2)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 2) and ((nr_ales==0) or (nr_ales > len(list3)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 3) and ((nr_ales==0) or (nr_ales > len(list4)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    else:
                        loop1=0
                except ValueError:
                    print("Ai introdus o optiune gresita!")

            print("Ai ales randul",rand, "si ai taiat",nr_ales,"bete.")

            # aplicare alegeri
            if (rand == 1):
                for i in range (0,nr_ales):
                    del list2[-1]
            elif (rand == 2):
                for i in range (0,nr_ales):
                    del list3[-1]
            elif (rand == 3):
                for i in range (0,nr_ales):
                    del list4[-1]

            # afisare noua tabela de joc
            print("Randul 1   ",end=' ')
            for i in range (0,len(list2)):
                print(list2[i],end=' ')
            print("\n")
            print("Randul 2   ",end=' ')
            for i in range (0,len(list3)):
                print(list3[i],end=' ')
            print("\n")
            print("Randul 3   ",end=' ')
            for i in range (0,len(list4)):
                print(list4[i],end=' ')
            print("\n")
            if (len(list2) + len(list3) + len(list4) == 0):
                print("A.I. a castigat!")
                loop=0;
            else:
                jucator=1

        elif (jucator == 1):
            #Rationament A.I.
            print("\n")
            print("Muta A.I.")
            # cazul suma para
            if ((len(list2)+len(list3)+len(list4)) % 2 == 0):
                # 0  0  >=2
                if ((len(list2) == 0) and (len(list3) == 0)):
                    while (len(list4) != 1):
                        del list4[-1]
                        rnd = 3
                        bte = bte + 1
                elif ((len(list2) == 0) and (len(list4) == 0)):
                    while (len(list3) != 1):
                        del list3[-1]
                        rnd = 2
                        bte = bte + 1
                elif ((len(list3) == 0) and (len(list4) == 0)):
                    while (len(list2) != 1):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1

                # 1  1  0
                elif ((len(list2) == 1) and (len(list3) == 1) and (len(list4) == 0)):
                    while (len(list2) != 0):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1
                elif ((len(list2) == 1) and (len(list4) == 1) and (len(list3) == 0)):
                    while (len(list2) != 0):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1
                elif ((len(list3) == 1) and (len(list4) == 1) and (len(list2) == 0)):
                    while (len(list3) != 0):
                        del list3[-1]
                        rnd = 2
                        bte = bte + 1

                # 0  3  1
                elif ((len(list2) > 1) and (len(list3) == 1) and (len(list4) == 0)):
                    while (len(list2) != 0):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1
                elif ((len(list2) > 1) and (len(list4) == 1) and (len(list3) == 0)):
                    while (len(list2) != 0):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1
                elif ((len(list2) == 1) and (len(list3) > 1) and (len(list4) == 0)):
                    while (len(list3) != 0):
                        del list3[-1]
                        rnd = 2
                        bte = bte + 1
                elif ((len(list2) == 1) and (len(list4) > 1) and (len(list3) == 0)):
                    while (len(list4) != 0):
                        del list4[-1]
                        rnd = 3
                        bte = bte + 1
                elif ((len(list3) > 1) and (len(list4) == 1) and (len(list2) == 0)):
                    while (len(list3) != 0):
                        del list3[-1]
                        rnd = 2
                        bte = bte + 1
                elif ((len(list3) == 1) and (len(list4) > 1) and (len(list2) == 0)):
                    while (len(list4) != 0):
                        del list4[-1]
                        rnd = 3
                        bte = bte + 1

                # 1  1  2
                elif ((len(list2) == 1) and (len(list3) == 1) and (len(list4) >= 2)):
                    while (len(list4) != 1):
                        del list4[-1]
                        rnd = 3
                        bte = bte + 1
                elif ((len(list2) == 1) and (len(list4) == 1) and (len(list3) >= 2)):
                    while (len(list3) != 1):
                        del list3[-1]
                        rnd = 2
                        bte = bte + 1
                elif ((len(list3) == 1) and (len(list4) == 1) and (len(list2) == 2)):
                    while (len(list2) != 1):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1

                # 2  2  0
                elif ((len(list2) == 2) and (len(list3) == 2) and (len(list4) >= 0)):
                    while (len(list2) != 1):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1
                elif ((len(list2) == 2) and (len(list4) == 2) and (len(list3) >= 0)):
                    while (len(list2) != 1):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1
                elif ((len(list3) == 2) and (len(list4) == 2) and (len(list2) == 0)):
                    while (len(list3) != 1):
                        del list3[-1]
                        rnd = 2
                        bte = bte + 1

                # 2  2  2
                elif ((len(list2) == 2) and (len(list3) == 2) and (len(list4) == 2)):
                    while (len(list2) != 0):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1

                # 0  >2  >2
                elif ((len(list2) == 0) and (len(list3) > 2) and (len(list4) > 2)):
                    if (len(list3) > len(list4)):
                        while (len(list3) != len(list4)):
                            del list3[-1]
                            rnd = 2
                            bte = bte + 1
                    elif (len(list3) < len(list4)):
                        while (len(list4) != len(list3)):
                            del list4[-1]
                            rnd = 3
                            bte = bte + 1
                    elif (len(list3) == len(list4)):
                            del list4[-1]
                            rnd = 3
                            bte = bte + 1
                elif ((len(list2) == 2) and (len(list3) == 0) and (len(list4) > 2)):
                    while (len(list4) != len(list2)):
                        del list4[-1]
                        rnd = 3
                        bte = bte + 1
                elif ((len(list2) == 2) and (len(list3) > 2) and (len(list4) == 0)):
                    while (len(list3) != len(list2)):
                        del list3[-1]
                        rnd = 2
                        bte = bte + 1

                # 2  >2  >2
                elif ((len(list2) == 2) and (len(list3) > 2) and (len(list4) > 2)):
                    if (len(list3) > len(list4)):
                        while (len(list3) != len(list4)):
                            del list3[-1]
                            rnd = 2
                            bte = bte + 1
                    elif (len(list4) > len(list3)):
                        while (len(list4) != len(list3)):
                            del list4[-1]
                            rnd = 3
                            bte = bte + 1
                    elif (len(list3) == len(list4)):
                        del list4[-1]
                        rnd = 3
                        bte = bte + 1

                # 2  2>  2
                elif ((len(list2) == 2) and (len(list3) == 2) and (len(list4) > 2)):
                    while (len(list4) != len(list3)):
                        del list4[-1]
                        rnd = 3
                        bte = bte + 1
                elif ((len(list2) == 2) and (len(list3) > 2) and (len(list4) == 2)):
                    while (len(list3) != len(list3)):
                        del list3[-1]
                        rnd = 2
                        bte = bte + 1
                # 3 >= 3 >= 3
                elif ((len(list2) == 3) and (len(list3) >= 3) and (len(list4) >= 3)):
                    del list2[-1]
                    rnd = 1
                    bte = bte + 1

                # >= 2 >= 3  1
                elif ((len(list2) >= 2) and (len(list3) >= 3) and (len(list4) == 1)):
                    del list4[-1]
                    rnd = 3
                    bte = bte + 1
                elif ((len(list2) >= 2) and (len(list3) == 1) and (len(list4) >= 3)):
                    del list3[-1]
                    rnd = 2
                    bte = bte + 1
                elif ((len(list2) == 1) and (len(list3) >= 2) and (len(list4) >= 3)):
                    del list2[-1]
                    rnd = 1
                    bte = bte + 1




            # cazul suma impara
            elif ((len(list2) + len(list3) + len(list4)) % 2 != 0):
                # 1  1  1
                if ((len(list2) == 1) and (len(list3) == 1) and (len(list4) == 1)):
                    del list4[-1]
                    rnd = 3
                    bte = bte + 1

                # 0  0  1
                elif ((len(list2) == 0) and (len(list3) == 0) and (len(list4) == 1)):
                    while (len(list4) != 0):
                        del list4[-1]
                        rnd = 3
                        bte = bte + 1
                elif ((len(list2) == 0) and (len(list4) == 0) and (len(list3) == 1)):
                    while (len(list3) != 0):
                        del list3[-1]
                        rnd = 2
                        bte = bte + 1
                elif ((len(list3) == 0) and (len(list4) == 0) and (len(list2) == 1)):
                    while (len(list2) != 0):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1

                # 0  0  >=3
                elif ((len(list2) == 0) and (len(list3) == 0) and (len(list4) >= 3)):
                    while (len(list4) != 1):
                        del list4[-1]
                        rnd = 3
                        bte = bte + 1
                elif ((len(list2) == 0) and (len(list4) == 0) and (len(list3) >= 3)):
                    while (len(list3) != 1):
                        del list3[-1]
                        rnd = 2
                        bte = bte + 1
                elif ((len(list3) == 0) and (len(list4) == 0) and (len(list2) == 3)):
                    while (len(list2) != 1):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1

                # 2  1  2
                elif ((len(list2) == 2) and (len(list3) == 1) and (len(list4) == 2)):
                    while (len(list3) != 0):
                        del list3[-1]
                        rnd = 2
                        bte = bte + 1
                elif ((len(list2) == 1) and (len(list4) == 2) and (len(list3) == 2)):
                    while (len(list2) != 0):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1
                elif ((len(list3) == 2) and (len(list4) == 1) and (len(list2) == 2)):
                    while (len(list4) != 0):
                        del list4[-1]
                        rnd = 3
                        bte = bte + 1

                # 2  3  2
                elif ((len(list2) == 2) and (len(list3) >= 3) and (len(list4) == 2)):
                    while (len(list3) != 0):
                        del list3[-1]
                        rnd = 2
                        bte = bte + 1
                elif ((len(list2) == 3) and (len(list4) == 2) and (len(list3) == 2)):
                    while (len(list2) != 0):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1
                elif ((len(list3) == 2) and (len(list4) >= 3) and (len(list2) == 2)):
                    while (len(list4) != 0):
                        del list4[-1]
                        rnd = 3
                        bte = bte + 1

                # 1 >=3  >=3
                elif ((len(list2) == 1) and (len(list3) >= 3) and (len(list4) >= 3)):
                    while (len(list2) != 0):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1
                elif ((len(list2) == 3) and (len(list4) == 1) and (len(list3) >= 3)):
                    while (len(list4) != 0):
                        del list4[-1]
                        rnd = 3
                        bte = bte + 1
                elif ((len(list3) == 1) and (len(list4) >= 3) and (len(list2) == 3)):
                    while (len(list3) != 0):
                        del list3[-1]
                        rnd = 2
                        bte = bte + 1
                # 3 >=3 >=3
                elif ((len(list2) == 3) and (len(list3) >= 3) and (len(list4) >= 3)):
                    del list2[-1]
                    rnd = 1
                    bte = bte + 1

                # 0  1  3
                elif ((len(list2) == 0) and (len(list3) == 1) and (len(list4) >= 2)):
                    while (len(list4) != 0):
                        del list4[-1]
                        rnd = 3
                        bte = bte + 1
                elif ((len(list2) >= 2) and (len(list4) == 1) and (len(list3) == 0)):
                    while (len(list2) != 0):
                        del list2[-1]
                        rnd = 1
                        bte = bte + 1
                elif ((len(list3) >= 2) and (len(list4) == 0) and (len(list2) == 1)):
                    while (len(list3) != 0):
                        del list3[-1]
                        rnd = 2
                        bte = bte + 1

                # 0  2  3
                elif ((len(list2) == 0) and (len(list3) >= 2) and (len(list4) >= 2)):
                    if (len(list3) > len(list4)):
                        while (len(list3) != len(list4)):
                            del list3[-1]
                            rnd = 2
                            bte = bte + 1
                    elif (len(list3) < len(list4)):
                        while (len(list4) != len(list3)):
                            del list4[-1]
                            rnd = 3
                            bte = bte + 1
                elif ((len(list2) >= 2) and (len(list4) == 0) and (len(list3) >= 2)):
                    if (len(list3) > len(list2)):
                        while (len(list3) != len(list2)):
                            del list3[-1]
                            rnd = 2
                            bte = bte + 1
                    elif (len(list3) < len(list2)):
                        while (len(list2) != len(list3)):
                            del list2[-1]
                            rnd = 1
                            bte = bte + 1
                elif ((len(list3) == 0) and (len(list4) >= 2) and (len(list2) >= 2)):
                    if (len(list2) > len(list4)):
                        while (len(list2) != len(list4)):
                            del list2[-1]
                            rnd = 1
                            bte = bte + 1
                    elif (len(list2) < len(list4)):
                        while (len(list4) != len(list2)):
                            del list4[-1]
                            rnd = 3
                            bte = bte + 1

            print("A.I. a ales randul", rnd, "si a taiat", bte, "bete.")
            bte=0

            # afisare noua tabela de joc
            print("Randul 1   ", end=' ')
            for i in range(0, len(list2)):
                print(list2[i], end=' ')
            print("\n")
            print("Randul 2   ", end=' ')
            for i in range(0, len(list3)):
                print(list3[i], end=' ')
            print("\n")
            print("Randul 3   ", end=' ')
            for i in range(0, len(list4)):
                print(list4[i], end=' ')
            print("\n")
            if (len(list2) + len(list3) + len(list4) == 0):
                print(nume1 + " a castigat!")
                loop = 0;
            else:
                jucator = 0

elif ((nr_juc==1) and (dificultate==3)):
    loop = 10;
    while (loop != 0):
        if (jucator==0):

            # selectare rand
            loop1=10
            while (loop1 != 0):
                print("Muta ",nume1)
                print("Introdu randul pe care il alegi:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 4)):
                        if ((rand == 1) and (len(list1) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 2) and (len(list2) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 3) and (len(list3) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 4) and (len(list4) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        else:
                            loop1=0
                    else:
                        print("Ai introdus o optiune gresita!")
                        loop1=10
                except ValueError:
                    print("Ai introdus o optiune gresita!")

            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("Cate bete vrei sa tai? ")
                try:
                    nr_ales=int(input())
                    if ((rand == 1) and ((nr_ales==0) or (nr_ales > len(list1)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 2) and ((nr_ales==0) or (nr_ales > len(list2)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 3) and ((nr_ales==0) or (nr_ales > len(list3)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 4) and ((nr_ales==0) or (nr_ales > len(list4)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    else:
                        loop1=0
                except ValueError:
                    print("Ai introdus o optiune gresita!")

            print("Ai ales randul",rand, "si ai taiat",nr_ales,"bete.")

            # aplicare alegeri
            if (rand == 1):
                for i in range (0,nr_ales):
                    del list1[-1]
            elif (rand == 2):
                for i in range (0,nr_ales):
                    del list2[-1]
            elif (rand == 3):
                for i in range (0,nr_ales):
                    del list3[-1]
            elif (rand == 4):
                for i in range (0,nr_ales):
                    del list4[-1]

            # afisare noua tabela de joc
            print("Randul 1   ",end=' ')
            for i in range (0,len(list1)):
                print(list1[i],end=' ')
            print("\n")
            print("Randul 2   ",end=' ')
            for i in range (0,len(list2)):
                print(list2[i],end=' ')
            print("\n")
            print("Randul 3   ",end=' ')
            for i in range (0,len(list3)):
                print(list3[i],end=' ')
            print("\n")
            print("Randul 4   ", end=' ')
            for i in range(0, len(list4)):
                print(list4[i], end=' ')
            print("\n")
            if (len(list1) + len(list2) + len(list3) + len(list4) == 0):
                print("A.I. a castigat!")
                loop=0;
            else:
                jucator=1

        elif (jucator == 1):
            #Rationament A.I.
            print("\n")
            print("Muta A.I.")
            # cazul suma para
            if ((len(list1) + len(list2) + len(list3) + len(list4)) % 2 == 0):
                if (len(list1) == 0):
                    # cazul suma para
                    if ((len(list2) + len(list3) + len(list4)) % 2 == 0):
                        # 0  0  >=2
                        if ((len(list2) == 0) and (len(list3) == 0)):
                            while (len(list4) != 1):
                                del list4[-1]
                                rnd = 4
                                bte = bte + 1
                        elif ((len(list2) == 0) and (len(list4) == 0)):
                            while (len(list3) != 1):
                                del list3[-1]
                                rnd = 3
                                bte = bte + 1
                        elif ((len(list3) == 0) and (len(list4) == 0)):
                            while (len(list2) != 1):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1

                        # 1  1  0
                        elif ((len(list2) == 1) and (len(list3) == 1) and (len(list4) == 0)):
                            while (len(list2) != 0):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1
                        elif ((len(list2) == 1) and (len(list4) == 1) and (len(list3) == 0)):
                            while (len(list2) != 0):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1
                        elif ((len(list3) == 1) and (len(list4) == 1) and (len(list2) == 0)):
                            while (len(list3) != 0):
                                del list3[-1]
                                rnd = 3
                                bte = bte + 1

                        # 0  3  1
                        elif ((len(list2) > 1) and (len(list3) == 1) and (len(list4) == 0)):
                            while (len(list2) != 0):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1
                        elif ((len(list2) > 1) and (len(list4) == 1) and (len(list3) == 0)):
                            while (len(list2) != 0):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1
                        elif ((len(list2) == 1) and (len(list3) > 1) and (len(list4) == 0)):
                            while (len(list3) != 0):
                                del list3[-1]
                                rnd = 2
                                bte = bte + 1
                        elif ((len(list2) == 1) and (len(list4) > 1) and (len(list3) == 0)):
                            while (len(list4) != 0):
                                del list4[-1]
                                rnd = 4
                                bte = bte + 1
                        elif ((len(list3) > 1) and (len(list4) == 1) and (len(list2) == 0)):
                            while (len(list3) != 0):
                                del list3[-1]
                                rnd = 2
                                bte = bte + 1
                        elif ((len(list3) == 1) and (len(list4) > 1) and (len(list2) == 0)):
                            while (len(list4) != 0):
                                del list4[-1]
                                rnd = 4
                                bte = bte + 1

                        # 1  1  2
                        elif ((len(list2) == 1) and (len(list3) == 1) and (len(list4) >= 2)):
                            while (len(list4) != 1):
                                del list4[-1]
                                rnd = 4
                                bte = bte + 1
                        elif ((len(list2) == 1) and (len(list4) == 1) and (len(list3) >= 2)):
                            while (len(list3) != 1):
                                del list3[-1]
                                rnd = 3
                                bte = bte + 1
                        elif ((len(list3) == 1) and (len(list4) == 1) and (len(list2) == 2)):
                            while (len(list2) != 1):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1

                        # 2  2  0
                        elif ((len(list2) == 2) and (len(list3) == 2) and (len(list4) >= 0)):
                            while (len(list2) != 1):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1
                        elif ((len(list2) == 2) and (len(list4) == 2) and (len(list3) >= 0)):
                            while (len(list2) != 1):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1
                        elif ((len(list3) == 2) and (len(list4) == 2) and (len(list2) == 0)):
                            while (len(list3) != 1):
                                del list3[-1]
                                rnd = 3
                                bte = bte + 1

                        # 2  2  2
                        elif ((len(list2) == 2) and (len(list3) == 2) and (len(list4) == 2)):
                            while (len(list2) != 0):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1

                        # 0  >2  >2
                        elif ((len(list2) == 0) and (len(list3) > 2) and (len(list4) > 2)):
                            if (len(list3) > len(list4)):
                                while (len(list3) != len(list4)):
                                    del list3[-1]
                                    rnd = 3
                                    bte = bte + 1
                            elif (len(list3) < len(list4)):
                                while (len(list4) != len(list3)):
                                    del list4[-1]
                                    rnd = 4
                                    bte = bte + 1
                            elif (len(list3) == len(list4)):
                                del list4[-1]
                                rnd = 4
                                bte = bte + 1
                        elif ((len(list2) == 2) and (len(list3) == 0) and (len(list4) > 2)):
                            while (len(list4) != len(list2)):
                                del list4[-1]
                                rnd = 4
                                bte = bte + 1
                        elif ((len(list2) == 2) and (len(list3) > 2) and (len(list4) == 0)):
                            while (len(list3) != len(list2)):
                                del list3[-1]
                                rnd = 3
                                bte = bte + 1

                        # 2  >2  >2
                        elif ((len(list2) == 2) and (len(list3) > 2) and (len(list4) > 2)):
                            if (len(list3) > len(list4)):
                                while (len(list3) != len(list4)):
                                    del list3[-1]
                                    rnd = 3
                                    bte = bte + 1
                            elif (len(list4) > len(list3)):
                                while (len(list4) != len(list3)):
                                    del list4[-1]
                                    rnd = 4
                                    bte = bte + 1
                            elif (len(list3) == len(list4)):
                                del list4[-1]
                                rnd = 4
                                bte = bte + 1

                        # 2  2>  2
                        elif ((len(list2) == 2) and (len(list3) == 2) and (len(list4) > 2)):
                            while (len(list4) != len(list3)):
                                del list4[-1]
                                rnd = 4
                                bte = bte + 1
                        elif ((len(list2) == 2) and (len(list3) > 2) and (len(list4) == 2)):
                            while (len(list3) != len(list3)):
                                del list3[-1]
                                rnd = 3
                                bte = bte + 1

                        # 3 >= 3 >= 3
                        elif ((len(list2) == 3) and (len(list3) >= 3) and (len(list4) >= 3)):
                            del list2[-1]
                            rnd = 2
                            bte = bte + 1

                        # >= 2 >= 3  1
                        elif ((len(list2) >= 2) and (len(list3) >= 3) and (len(list4) == 1)):
                            del list4[-1]
                            rnd = 4
                            bte = bte + 1
                        elif ((len(list2) >= 2) and (len(list3) == 1) and (len(list4) >= 3)):
                            del list3[-1]
                            rnd = 3
                            bte = bte + 1
                        elif ((len(list2) == 1) and (len(list3) >= 2) and (len(list4) >= 3)):
                            del list2[-1]
                            rnd = 2
                            bte = bte + 1

                # cazul len(list1) != 0
                else:
                    if ((len(list2) >= 1) and (len(list3) >= 1) and (len(list4) >= 1)):
                        del list1[-1]
                        rnd = 1
                        bte = bte + 1
                    elif ((len(list2) == 0) and (len(list3) == 0) and (len(list4) >= 1)):
                        while (len(list4) != 0):
                            del list4[-1]
                            rnd = 4
                            bte = bte + 1
                    elif ((len(list2) >= 1) and (len(list3) == 0) and (len(list4) == 0)):
                        while (len(list2) != 0):
                            del list2[-1]
                            rnd = 2
                            bte = bte + 1
                    elif ((len(list2) == 0) and (len(list3) >= 1) and (len(list4) == 0)):
                        while (len(list3) != 0):
                            del list3[-1]
                            rnd = 3
                            bte = bte + 1
                    elif ((len(list2) == 0) and (len(list3) == 1) and (len(list4) >= 2)):
                        while (len(list4) != 1):
                            del list4[-1]
                            rnd = 4
                            bte = bte + 1
                    elif ((len(list2) == 0) and (len(list3) >= 2) and (len(list4) == 1)):
                        while (len(list3) != 1):
                            del list3[-1]
                            rnd = 3
                            bte = bte + 1
                    elif ((len(list2) == 1) and (len(list3) >= 2) and (len(list4) == 0)):
                        while (len(list3) != 1):
                            del list3[-1]
                            rnd = 3
                            bte = bte + 1
                    elif ((len(list2) == 1) and (len(list3) == 0) and (len(list4) >= 2)):
                        while (len(list4) != 1):
                            del list4[-1]
                            rnd = 4
                            bte = bte + 1
                    elif ((len(list2) >= 2) and (len(list3) == 0) and (len(list4) == 1)):
                        while (len(list2) != 1):
                            del list2[-1]
                            rnd = 2
                            bte = bte + 1
                    elif ((len(list2) >= 2) and (len(list3) == 1) and (len(list4) == 0)):
                        while (len(list2) != 1):
                            del list2[-1]
                            rnd = 2
                            bte = bte + 1
                    elif (((len(list2) >= 2) and (len(list3) >= 2) and (len(list4) == 0)) or (
                                (len(list2) >= 2) and (len(list3) == 0) and (len(list4) >= 2)) or (
                                (len(list2) == 0) and (len(list3) >= 2) and (len(list4) >= 2))):
                        del list1[-1]
                        rnd = 1
                        bte = bte + 1


            # cazul suma impara
            else:
                if (len(list1) == 0):
                    if ((len(list2) + len(list3) + len(list4)) % 2 != 0):
                        # 1  1  1
                        if ((len(list2) == 1) and (len(list3) == 1) and (len(list4) == 1)):
                            del list4[-1]
                            rnd = 4
                            bte = bte + 1

                        # 0  0  1
                        elif ((len(list2) == 0) and (len(list3) == 0) and (len(list4) == 1)):
                            while (len(list4) != 0):
                                del list4[-1]
                                rnd = 4
                                bte = bte + 1
                        elif ((len(list2) == 0) and (len(list4) == 0) and (len(list3) == 1)):
                            while (len(list3) != 0):
                                del list3[-1]
                                rnd = 3
                                bte = bte + 1
                        elif ((len(list3) == 0) and (len(list4) == 0) and (len(list2) == 1)):
                            while (len(list2) != 0):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1

                        # 0  0  >=3
                        elif ((len(list2) == 0) and (len(list3) == 0) and (len(list4) >= 3)):
                            while (len(list4) != 1):
                                del list4[-1]
                                rnd = 4
                                bte = bte + 1
                        elif ((len(list2) == 0) and (len(list4) == 0) and (len(list3) >= 3)):
                            while (len(list3) != 1):
                                del list3[-1]
                                rnd = 3
                                bte = bte + 1
                        elif ((len(list3) == 0) and (len(list4) == 0) and (len(list2) == 3)):
                            while (len(list2) != 1):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1

                        # 2  1  2
                        elif ((len(list2) == 2) and (len(list3) == 1) and (len(list4) == 2)):
                            while (len(list3) != 0):
                                del list3[-1]
                                rnd = 3
                                bte = bte + 1
                        elif ((len(list2) == 1) and (len(list4) == 2) and (len(list3) == 2)):
                            while (len(list2) != 0):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1
                        elif ((len(list3) == 2) and (len(list4) == 1) and (len(list2) == 2)):
                            while (len(list4) != 0):
                                del list4[-1]
                                rnd = 4
                                bte = bte + 1

                        # 2  3  2
                        elif ((len(list2) == 2) and (len(list3) >= 3) and (len(list4) == 2)):
                            while (len(list3) != 0):
                                del list3[-1]
                                rnd = 3
                                bte = bte + 1
                        elif ((len(list2) == 3) and (len(list4) == 2) and (len(list3) == 2)):
                            while (len(list2) != 0):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1
                        elif ((len(list3) == 2) and (len(list4) >= 3) and (len(list2) == 2)):
                            while (len(list4) != 0):
                                del list4[-1]
                                rnd = 4
                                bte = bte + 1

                        # 1 >=3  >=3
                        elif ((len(list2) == 1) and (len(list3) >= 3) and (len(list4) >= 3)):
                            while (len(list2) != 0):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1
                        elif ((len(list2) == 3) and (len(list4) == 1) and (len(list3) >= 3)):
                            while (len(list4) != 0):
                                del list4[-1]
                                rnd = 4
                                bte = bte + 1
                        elif ((len(list3) == 1) and (len(list4) >= 3) and (len(list2) == 3)):
                            while (len(list3) != 0):
                                del list3[-1]
                                rnd = 3
                                bte = bte + 1

                        # 3 >=3 >=3
                        elif ((len(list2) == 3) and (len(list3) >= 3) and (len(list4) >= 3)):
                            del list2[-1]
                            rnd = 2
                            bte = bte + 1

                        # 0  1  3
                        elif ((len(list2) == 0) and (len(list3) == 1) and (len(list4) >= 2)):
                            while (len(list4) != 0):
                                del list4[-1]
                                rnd = 4
                                bte = bte + 1
                        elif ((len(list2) >= 2) and (len(list4) == 1) and (len(list3) == 0)):
                            while (len(list2) != 0):
                                del list2[-1]
                                rnd = 2
                                bte = bte + 1
                        elif ((len(list3) >= 2) and (len(list4) == 0) and (len(list2) == 1)):
                            while (len(list3) != 0):
                                del list3[-1]
                                rnd = 3
                                bte = bte + 1

                        # 0  2  3
                        elif ((len(list2) == 0) and (len(list3) >= 2) and (len(list4) >= 2)):
                            if (len(list3) > len(list4)):
                                while (len(list3) != len(list4)):
                                    del list3[-1]
                                    rnd = 3
                                    bte = bte + 1
                            elif (len(list3) < len(list4)):
                                while (len(list4) != len(list3)):
                                    del list4[-1]
                                    rnd = 4
                                    bte = bte + 1
                        elif ((len(list2) >= 2) and (len(list4) == 0) and (len(list3) >= 2)):
                            if (len(list3) > len(list2)):
                                while (len(list3) != len(list2)):
                                    del list3[-1]
                                    rnd = 3
                                    bte = bte + 1
                            elif (len(list3) < len(list2)):
                                while (len(list2) != len(list3)):
                                    del list2[-1]
                                    rnd = 2
                                    bte = bte + 1
                        elif ((len(list3) == 0) and (len(list4) >= 2) and (len(list2) >= 2)):
                            if (len(list2) > len(list4)):
                                while (len(list2) != len(list4)):
                                    del list2[-1]
                                    rnd = 2
                                    bte = bte + 1
                            elif (len(list2) < len(list4)):
                                while (len(list4) != len(list2)):
                                    del list4[-1]
                                    rnd = 4
                                    bte = bte + 1

                # cazul len(list1) != 0
                else:
                    if ((len(list2) >= 1) and (len(list3) >= 1) and (len(list4) >= 1)):
                        del list1[-1]
                        rnd = 1
                        bte = bte + 1
                    elif ((len(list2) == 0) and (len(list3) == 0) and (len(list4) >= 1)):
                        while (len(list4) != 0):
                            del list4[-1]
                            rnd = 4
                            bte = bte + 1
                    elif ((len(list2) >= 1) and (len(list3) == 0) and (len(list4) == 0)):
                        while (len(list2) != 0):
                            del list2[-1]
                            rnd = 2
                            bte = bte + 1
                    elif ((len(list2) == 0) and (len(list3) >= 1) and (len(list4) == 0)):
                        while (len(list3) != 0):
                            del list3[-1]
                            rnd = 3
                            bte = bte + 1
                    elif ((len(list2) == 0) and (len(list3) == 1) and (len(list4) >= 2)):
                        while (len(list4) != 1):
                            del list4[-1]
                            rnd = 4
                            bte = bte + 1
                    elif ((len(list2) == 0) and (len(list3) >= 2) and (len(list4) == 1)):
                        while (len(list3) != 1):
                            del list3[-1]
                            rnd = 3
                            bte = bte + 1
                    elif ((len(list2) == 1) and (len(list3) >= 2) and (len(list4) == 0)):
                        while (len(list3) != 1):
                            del list3[-1]
                            rnd = 3
                            bte = bte + 1
                    elif ((len(list2) == 1) and (len(list3) == 0) and (len(list4) >= 2)):
                        while (len(list4) != 1):
                            del list4[-1]
                            rnd = 4
                            bte = bte + 1
                    elif ((len(list2) >= 2) and (len(list3) == 0) and (len(list4) == 1)):
                        while (len(list2) != 1):
                            del list2[-1]
                            rnd = 2
                            bte = bte + 1
                    elif ((len(list2) >= 2) and (len(list3) == 1) and (len(list4) == 0)):
                        while (len(list2) != 1):
                            del list2[-1]
                            rnd = 2
                            bte = bte + 1
                    elif (((len(list2) >= 2) and (len(list3) >= 2) and (len(list4) == 0)) or
                        ((len(list2) >= 2) and (len(list3) == 0) and (len(list4) >= 2)) or
                        ((len(list2) == 0) and (len(list3) >= 2) and (len(list4) >= 2))):
                        del list1[-1]
                        rnd = 1
                        bte = bte + 1
                    elif (((len(list2) == 0) and (len(list3) == 1) and (len(list4) == 1)) or
                        ((len(list2) == 1) and (len(list3) == 0) and (len(list4) == 1)) or
                        ((len(list2) == 1) and (len(list3) == 1) and (len(list4) == 0))):
                        del list1[-1]
                        rnd = 1
                        bte = bte + 1


            print("A.I. a ales randul", rnd, "si a taiat", bte, "bete.")
            bte=0

            # afisare noua tabela de joc
            print("Randul 1   ", end=' ')
            for i in range(0, len(list1)):
                print(list1[i], end=' ')
            print("\n")
            print("Randul 2   ", end=' ')
            for i in range(0, len(list2)):
                print(list2[i], end=' ')
            print("\n")
            print("Randul 3   ", end=' ')
            for i in range(0, len(list3)):
                print(list3[i], end=' ')
            print("\n")
            print("Randul 4   ", end=' ')
            for i in range(0, len(list4)):
                print(list4[i], end=' ')
            print("\n")
            if (len(list1) + len(list2) + len(list3) + len(list4) == 0):
                print(nume1 + " a castigat!")
                loop = 0;
            else:
                jucator = 0

elif ((nr_juc==2) and (dificultate==1)):
    loop = 10;
    while (loop != 0):
        if (jucator==0):

            # selectare rand
            loop1=10
            while (loop1 != 0):
                print("Muta ",nume1)
                print("Introdu randul pe care il alegi:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 3)):
                        if ((rand == 1) and (len(list1) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 2) and (len(list2) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 3) and (len(list3) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        else:
                            loop1=0
                    else:
                        print("Ai introdus o optiune gresita!")
                        loop1=10
                except ValueError:
                    print("Ai introdus o optiune gresita!")
            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("Cate bete vrei sa tai? ")
                try:
                    nr_ales=int(input())
                    if ((rand == 1) and ((nr_ales == 0) or (nr_ales > len(list1)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 2) and ((nr_ales == 0) or (nr_ales > len(list2)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 3) and ((nr_ales == 0) or (nr_ales > len(list3)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    else:
                        loop1=0;
                except ValueError:
                    print("Ai introdus o optiune gresita!")

            print(nume1,"a ales randul",rand, "si a taiat",nr_ales,"bete.")

            # aplicare alegeri
            if (rand == 1):
                for i in range (0,nr_ales):
                    del list1[-1]
            elif (rand == 2):
                for i in range (0,nr_ales):
                    del list2[-1]
            elif (rand == 3):
                for i in range (0,nr_ales):
                    del list3[-1]

            # afisare noua tabela de joc
            print("Randul 1   ",end=' ')
            for i in range (0,len(list1)):
                print(list1[i],end=' ')
            print("\n")
            print("Randul 2   ",end=' ')
            for i in range (0,len(list2)):
                print(list2[i],end=' ')
            print("\n")
            print("Randul 3   ",end=' ')
            for i in range (0,len(list3)):
                print(list3[i],end=' ')
            print("\n")
            if (len(list1) + len(list2) + len(list3) == 0):
                print(nume2 + " a castigat!")
                loop=0;
            else:
                jucator=1

        else:
            # selectare rand
            loop1 = 10
            while (loop1 != 0):
                print("Muta ", nume2)
                print("Introdu randul pe care il alegi:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 3)):
                        if ((rand == 1) and (len(list1) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 2) and (len(list2) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 3) and (len(list3) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        else:
                            loop1 = 0
                    else:
                        print("Ai introdus o optiune gresita!")
                        loop1 = 10
                except ValueError:
                    print("Ai introdus o optiune gresita!")
            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("Cate bete vrei sa tai? ")
                try:
                    nr_ales = int(input())
                    if ((rand == 1) and ((nr_ales == 0) or (nr_ales > len(list1)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 2) and ((nr_ales == 0) or (nr_ales > len(list2)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 3) and ((nr_ales == 0) or (nr_ales > len(list3)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    else:
                        loop1 = 0;
                except ValueError:
                    print("Ai introdus o optiune gresita!")
            print(nume2,"a ales randul", rand, "si a taiat", nr_ales, "bete.")

            # aplicare alegeri
            if (rand == 1):
                for i in range(0, nr_ales):
                    del list1[-1]
            elif (rand == 2):
                for i in range(0, nr_ales):
                    del list2[-1]
            elif (rand == 3):
                for i in range(0, nr_ales):
                    del list3[-1]

            # afisare noua tabela de joc
            print("Randul 1   ", end=' ')
            for i in range(0, len(list1)):
                print(list1[i], end=' ')
            print("\n")
            print("Randul 2   ", end=' ')
            for i in range(0, len(list2)):
                print(list2[i], end=' ')
            print("\n")
            print("Randul 3   ", end=' ')
            for i in range(0, len(list3)):
                print(list3[i], end=' ')
            print("\n")
            if (len(list1) + len(list2) + len(list3) == 0):
                print(nume1 + " a castigat!")
                loop = 0;
            else:
                jucator = 0

elif ((nr_juc==2) and (dificultate==2)):
    loop = 10;
    while (loop != 0):
        if (jucator==0):

            # selectare rand
            loop1=10
            while (loop1 != 0):
                print("Muta ",nume1)
                print("Introdu randul pe care il alegi:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 3)):
                        if ((rand == 1) and (len(list2) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 2) and (len(list3) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 3) and (len(list4) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        else:
                            loop1=0
                    else:
                        print("Ai introdus o optiune gresita!")
                        loop1=10
                except ValueError:
                    print("Ai introdus o optiune gresita!")

            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("Cate bete vrei sa tai? ")
                try:
                    nr_ales=int(input())
                    if ((rand == 1) and ((nr_ales == 0) or (nr_ales > len(list2)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 2) and ((nr_ales == 0) or (nr_ales > len(list3)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 3) and ((nr_ales == 0) or (nr_ales > len(list4)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    else:
                        loop1=0;
                except ValueError:
                    print("Ai introdus o optiune gresita!")

            print(nume1,"a ales randul",rand, "si a taiat",nr_ales,"bete.")

            # aplicare alegeri
            if (rand == 1):
                for i in range (0,nr_ales):
                    del list2[-1]
            elif (rand == 2):
                for i in range (0,nr_ales):
                    del list3[-1]
            elif (rand == 3):
                for i in range (0,nr_ales):
                    del list4[-1]

            # afisare noua tabela de joc
            print("Randul 1   ",end=' ')
            for i in range (0,len(list2)):
                print(list2[i],end=' ')
            print("\n")
            print("Randul 2   ",end=' ')
            for i in range (0,len(list3)):
                print(list3[i],end=' ')
            print("\n")
            print("Randul 3   ",end=' ')
            for i in range (0,len(list4)):
                print(list4[i],end=' ')
            print("\n")
            if (len(list2) + len(list3) + len(list4) == 0):
                print(nume2 + " a castigat!")
                loop=0;
            else:
                jucator=1

        else:
            # selectare rand
            loop1 = 10
            while (loop1 != 0):
                print("Muta ", nume2)
                print("Introdu randul pe care il alegi:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 3)):
                        if ((rand == 1) and (len(list2) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 2) and (len(list3) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 3) and (len(list4) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        else:
                            loop1 = 0
                    else:
                        print("Ai introdus o optiune gresita!")
                        loop1 = 10;
                except ValueError:
                    print("Ai introdus o optiune gresita!")
            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("Cate bete vrei sa tai? ")
                try:
                    nr_ales = int(input())
                    if ((rand == 1) and ((nr_ales == 0) or (nr_ales > len(list2)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 2) and ((nr_ales == 0) or (nr_ales > len(list3)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 3) and ((nr_ales == 0) or (nr_ales > len(list4)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    else:
                        loop1 = 0
                except ValueError:
                    print("Ai introdus o optiune gresita!")

            print(nume2,"a ales randul", rand, "si a taiat", nr_ales, "bete.")

            # aplicare alegeri
            if (rand == 1):
                for i in range(0, nr_ales):
                    del list2[-1]
            elif (rand == 2):
                for i in range(0, nr_ales):
                    del list3[-1]
            elif (rand == 3):
                for i in range(0, nr_ales):
                    del list4[-1]

            # afisare noua tabela de joc
            print("Randul 1   ", end=' ')
            for i in range(0, len(list2)):
                print(list2[i], end=' ')
            print("\n")
            print("Randul 2   ", end=' ')
            for i in range(0, len(list3)):
                print(list3[i], end=' ')
            print("\n")
            print("Randul 3   ", end=' ')
            for i in range(0, len(list4)):
                print(list4[i], end=' ')
            print("\n")
            if (len(list2) + len(list3) + len(list4) == 0):
                print(nume1 + " a castigat!")
                loop = 0;
            else:
                jucator = 0

elif ((nr_juc==2) and (dificultate==3)):
    loop = 10;
    while (loop != 0):
        if (jucator==0):

            # selectare rand
            loop1=10
            while (loop1 != 0):
                print("Muta ",nume1)
                print("Introdu randul pe care il alegi:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 4)):
                        if ((rand == 1) and (len(list1) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 2) and (len(list2) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 3) and (len(list3) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 4) and (len(list4) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        else:
                            loop1=0
                    else:
                        print("Ai introdus o optiune gresita!")
                        loop1=10
                except ValueError:
                    print("Ai introdus o optiune gresita!")

            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("Cate bete vrei sa tai? ")
                try:
                    nr_ales=int(input())
                    if ((rand == 1) and ((nr_ales == 0) or (nr_ales > len(list1)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 2) and ((nr_ales == 0) or (nr_ales > len(list2)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 3) and ((nr_ales == 0) or (nr_ales > len(list3)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 4) and ((nr_ales == 0) or (nr_ales > len(list4)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    else:
                        loop1=0
                except ValueError:
                    print("Ai introdus o optiune gresita!")

            print(nume1,"a ales randul",rand, "si a taiat",nr_ales,"bete.")

            # aplicare alegeri
            if (rand == 1):
                for i in range (0,nr_ales):
                    del list1[-1]
            elif (rand == 2):
                for i in range (0,nr_ales):
                    del list2[-1]
            elif (rand == 3):
                for i in range (0,nr_ales):
                    del list3[-1]
            elif (rand == 4):
                for i in range (0,nr_ales):
                    del list4[-1]

            # afisare noua tabela de joc
            print("Randul 1   ",end=' ')
            for i in range (0,len(list1)):
                print(list1[i],end=' ')
            print("\n")
            print("Randul 2   ",end=' ')
            for i in range (0,len(list2)):
                print(list2[i],end=' ')
            print("\n")
            print("Randul 3   ",end=' ')
            for i in range (0,len(list3)):
                print(list3[i],end=' ')
            print("\n")
            print("Randul 4   ", end=' ')
            for i in range(0, len(list4)):
                print(list4[i], end=' ')
            print("\n")
            if (len(list1) + len(list2) + len(list3) + len(list4) == 0):
                print(nume2 + " a castigat!")
                loop=0;
            else:
                jucator=1

        else:
            # selectare rand
            loop1 = 10
            while (loop1 != 0):
                print("Muta ", nume2)
                print("Introdu randul pe care il alegi:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 4)):
                        if ((rand == 1) and (len(list1) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 2) and (len(list2) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 3) and (len(list3) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        elif ((rand == 4) and (len(list4) == 0)):
                            print("Rand gresit! Introdu randul pe care il alegi:")
                        else:
                            loop1 = 0
                    else:
                        print("Ai introdus o optiune gresita!")
                        loop1 = 10
                except ValueError:
                    print("Ai introdus o optiune gresita!")

            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("Cate bete vrei sa tai? ")
                try:
                    nr_ales = int(input())
                    if ((rand == 1) and ((nr_ales == 0) or (nr_ales > len(list1)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 2) and ((nr_ales == 0) or (nr_ales > len(list2)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 3) and ((nr_ales == 0) or (nr_ales > len(list3)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    elif ((rand == 4) and ((nr_ales == 0) or (nr_ales > len(list4)))):
                        print("Numar gresit! Introdu numarul de bete:")
                    else:
                        loop1 = 0
                except ValueError:
                    print("Ai introdus o optiune gresita!")

            print(nume2,"a ales randul", rand, "si a taiat", nr_ales, "bete.")

            # aplicare alegeri
            if (rand == 1):
                for i in range(0, nr_ales):
                    del list1[-1]
            elif (rand == 2):
                for i in range(0, nr_ales):
                    del list2[-1]
            elif (rand == 3):
                for i in range(0, nr_ales):
                    del list3[-1]
            elif (rand == 4):
                for i in range(0, nr_ales):
                    del list4[-1]

            # afisare noua tabela de joc
            print("Randul 1   ", end=' ')
            for i in range(0, len(list1)):
                print(list1[i], end=' ')
            print("\n")
            print("Randul 2   ", end=' ')
            for i in range(0, len(list2)):
                print(list2[i], end=' ')
            print("\n")
            print("Randul 3   ", end=' ')
            for i in range(0, len(list3)):
                print(list3[i], end=' ')
            print("\n")
            print("Randul 4   ", end=' ')
            for i in range(0, len(list4)):
                print(list4[i], end=' ')
            print("\n")
            if (len(list1) + len(list2) + len(list3) + len(list4) == 0):
                print(nume1 + " a castigat!")
                loop = 0;
            else:
                jucator = 0
# terminare joc


