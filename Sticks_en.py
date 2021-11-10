print("Sticks - Python version")
print("Programmer: Steciuc Angel Florentin")
print("The basic rule is: the one who cuts the last piece has lost the game! \n")
nr_juc=0
nume1=""
nume2=""
rnd=0
bte=0
dificultate=0
loop=10
print("Choose the difficulty level: ")
print("1 - Easy")
print("2 - Standard")
print("3 - Hard")
while (loop!=0):
    try:
        dificultate=int(input("Input the chosen option:"))
        if ((dificultate==1) or (dificultate==2) or (dificultate==3)):
            loop=0
        else:
            print("You have entered a wrong option!")
            loop=10
    except ValueError:
        print("You have entered a wrong option!")


print("Choose the number of players:")
print("1 - One player vs A.I.")
print("2 - Two players")
loop=10
while (loop!=0):
    try:
        nr_juc=int(input("Input the chosen option:"))
        if (nr_juc==1):
            nume1=input("Enter the name of the player:")
            loop=0
        elif (nr_juc==2):
            nume1=input("Enter the name of the first player:")
            nume2=input("Enter the name of the second player:")
            loop=0;
        else:
            print("You have entered a wrong option!")
            loop=10;
    except ValueError:
        print("You have entered a wrong option!")

# creare si afisare initiala a betelor
list1=['|']
list2=['|','|','|']
list3=['|','|','|','|','|']
list4=['|','|','|','|','|','|','|']
if (dificultate==1):
    print("\n","1st Row   ",end='')
    for i in range (0,len(list1)):
        print(list1[i],end=' ')
    print("\n","2nd Row   ",end='')
    for i in range (0,len(list2)):
        print(list2[i],end=' ')
    print("\n","3rd Row   ",end='')
    for i in range (0,len(list3)):
        print(list3[i],end=' ')
    print("\n")
elif (dificultate==2):
    print("\n", "1st Row   ", end='')
    for i in range(0, len(list2)):
        print(list2[i], end=' ')
    print("\n", "2nd Row   ", end='')
    for i in range(0, len(list3)):
        print(list3[i], end=' ')
    print("\n", "3rd Row   ", end='')
    for i in range(0, len(list4)):
        print(list4[i], end=' ')
    print("\n")
elif (dificultate==3):
    print("\n", "1st Row   ", end='')
    for i in range(0, len(list1)):
        print(list1[i], end=' ')
    print("\n", "2nd Row   ", end='')
    for i in range(0, len(list2)):
        print(list2[i], end=' ')
    print("\n", "3rd Row   ", end='')
    for i in range(0, len(list3)):
        print(list3[i], end=' ')
    print("\n", "4th Row   ", end='')
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
                print(nume1 + "'s turn")
                print("Input the row you choose:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 3)):
                        if ((rand == 1) and (len(list1) == 0)):
                            print("Wrong row! Enter the row you choose:")
                        elif ((rand == 2) and (len(list2) == 0)):
                            print("Wrong row! Enter the row you choose:")
                        elif ((rand == 3) and (len(list3) == 0)):
                            print("Wrong row! Enter the row you choose:")
                        else:
                            loop1=0
                    else:
                        print("You have entered a wrong option!")
                        loop1=10
                except ValueError:
                    print("You have entered a wrong option!")


            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("How many sticks do you want to cut? ")
                try:
                    nr_ales=int(input())
                    if ((rand == 1) and ((nr_ales==0) or (nr_ales > len(list1)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 2) and ((nr_ales==0) or (nr_ales > len(list2)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 3) and ((nr_ales==0) or (nr_ales > len(list3)))):
                        print("Wrong number! Enter the number of sticks:")
                    else:
                        loop1=0
                except ValueError:
                    print("You have entered a wrong option!")

            print("You chose the row",rand, "and cut",nr_ales,"sticks.")

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
            print("1st Row   ",end=' ')
            for i in range (0,len(list1)):
                print(list1[i],end=' ')
            print("\n")
            print("2nd Row   ",end=' ')
            for i in range (0,len(list2)):
                print(list2[i],end=' ')
            print("\n")
            print("3rd Row   ",end=' ')
            for i in range (0,len(list3)):
                print(list3[i],end=' ')
            print("\n")
            if (len(list1) + len(list2) + len(list3) == 0):
                print("A.I. won!")
                loop=0;
            else:
                jucator=1

        elif (jucator == 1):
            #Rationament A.I.
            print("\n")
            print("A.I.'s turn")
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

            print("A.I. chose the row ", rnd, "and cut", bte, "sticks.")
            bte=0

            # afisare noua tabela de joc
            print("1st Row   ", end=' ')
            for i in range(0, len(list1)):
                print(list1[i], end=' ')
            print("\n")
            print("2nd Row   ", end=' ')
            for i in range(0, len(list2)):
                print(list2[i], end=' ')
            print("\n")
            print("3rd Row   ", end=' ')
            for i in range(0, len(list3)):
                print(list3[i], end=' ')
            print("\n")
            if (len(list1) + len(list2) + len(list3) == 0):
                print(nume1 + " won!")
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
                print(nume1 + "'s turn")
                print("Input the row you choose:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 3)):
                        if ((rand == 1) and (len(list2) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 2) and (len(list3) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 3) and (len(list4) == 0)):
                            print("Wrong row! Input the row you choose:")
                        else:
                            loop1=0
                    else:
                        print("You have entered a wrong option!")
                        loop1=10
                except ValueError:
                    print("You have entered a wrong option!")

            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("How many sticks do you want to cut? ")
                try:
                    nr_ales=int(input())
                    if ((rand == 1) and ((nr_ales==0) or (nr_ales > len(list2)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 2) and ((nr_ales==0) or (nr_ales > len(list3)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 3) and ((nr_ales==0) or (nr_ales > len(list4)))):
                        print("Wrong number! Enter the number of sticks:")
                    else:
                        loop1=0
                except ValueError:
                    print("You have entered a wrong option!")

            print("You chose the row",rand, "and cut",nr_ales,"sticks.")

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
            print("1st Row   ",end=' ')
            for i in range (0,len(list2)):
                print(list2[i],end=' ')
            print("\n")
            print("2nd Row   ",end=' ')
            for i in range (0,len(list3)):
                print(list3[i],end=' ')
            print("\n")
            print("3rd Row   ",end=' ')
            for i in range (0,len(list4)):
                print(list4[i],end=' ')
            print("\n")
            if (len(list2) + len(list3) + len(list4) == 0):
                print("A.I. won!")
                loop=0;
            else:
                jucator=1

        elif (jucator == 1):
            #Rationament A.I.
            print("\n")
            print("A.I.'s turn")
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

            print(""A.I. chose the row ", rnd, "and cut", bte, "sticks."")
            bte=0

            # afisare noua tabela de joc
            print("1st Row   ", end=' ')
            for i in range(0, len(list2)):
                print(list2[i], end=' ')
            print("\n")
            print("2nd Row   ", end=' ')
            for i in range(0, len(list3)):
                print(list3[i], end=' ')
            print("\n")
            print("3rd Row   ", end=' ')
            for i in range(0, len(list4)):
                print(list4[i], end=' ')
            print("\n")
            if (len(list2) + len(list3) + len(list4) == 0):
                print(nume1 + " won!")
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
                print(nume + "'s turn")
                print("Input the row you choose:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 4)):
                        if ((rand == 1) and (len(list1) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 2) and (len(list2) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 3) and (len(list3) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 4) and (len(list4) == 0)):
                            print("Wrong row! Input the row you choose:")
                        else:
                            loop1=0
                    else:
                        print("You have entered a wrong option!")
                        loop1=10
                except ValueError:
                    print("You have entered a wrong option!")

            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("How many sticks do you want to cut? ")
                try:
                    nr_ales=int(input())
                    if ((rand == 1) and ((nr_ales==0) or (nr_ales > len(list1)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 2) and ((nr_ales==0) or (nr_ales > len(list2)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 3) and ((nr_ales==0) or (nr_ales > len(list3)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 4) and ((nr_ales==0) or (nr_ales > len(list4)))):
                        print("Wrong number! Enter the number of sticks:")
                    else:
                        loop1=0
                except ValueError:
                    print("You have entered a wrong option!")

            print("You chose the row",rand, "and cut",nr_ales,"sticks.")

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
            print("1st Row   ",end=' ')
            for i in range (0,len(list1)):
                print(list1[i],end=' ')
            print("\n")
            print("2nd Row   ",end=' ')
            for i in range (0,len(list2)):
                print(list2[i],end=' ')
            print("\n")
            print("3rd Row   ",end=' ')
            for i in range (0,len(list3)):
                print(list3[i],end=' ')
            print("\n")
            print("4th Row   ", end=' ')
            for i in range(0, len(list4)):
                print(list4[i], end=' ')
            print("\n")
            if (len(list1) + len(list2) + len(list3) + len(list4) == 0):
                print("A.I. won!")
                loop=0;
            else:
                jucator=1

        elif (jucator == 1):
            #Rationament A.I.
            print("\n")
            print("A.I.'s turn")
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


            print(""A.I. chose the row ", rnd, "and cut", bte, "sticks."")
            bte=0

            # afisare noua tabela de joc
            print("1st Row   ", end=' ')
            for i in range(0, len(list1)):
                print(list1[i], end=' ')
            print("\n")
            print("2nd Row   ", end=' ')
            for i in range(0, len(list2)):
                print(list2[i], end=' ')
            print("\n")
            print("3rd Row   ", end=' ')
            for i in range(0, len(list3)):
                print(list3[i], end=' ')
            print("\n")
            print("4th Row   ", end=' ')
            for i in range(0, len(list4)):
                print(list4[i], end=' ')
            print("\n")
            if (len(list1) + len(list2) + len(list3) + len(list4) == 0):
                print(nume1 + " won!")
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
                print(nume1 + "'s turn ")
                print("Input the row you choose:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 3)):
                        if ((rand == 1) and (len(list1) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 2) and (len(list2) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 3) and (len(list3) == 0)):
                            print("Wrong row! Input the row you choose:")
                        else:
                            loop1=0
                    else:
                        print("You have entered a wrong option!")
                        loop1=10
                except ValueError:
                    print("You have entered a wrong option!")
            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("How many sticks do you want to cut? ")
                try:
                    nr_ales=int(input())
                    if ((rand == 1) and ((nr_ales == 0) or (nr_ales > len(list1)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 2) and ((nr_ales == 0) or (nr_ales > len(list2)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 3) and ((nr_ales == 0) or (nr_ales > len(list3)))):
                        print("Wrong number! Enter the number of sticks:")
                    else:
                        loop1=0;
                except ValueError:
                    print("You have entered a wrong option!")

            print(nume1,"chose the row",rand, "and cut",nr_ales,"sticks.")

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
            print("1st Row   ",end=' ')
            for i in range (0,len(list1)):
                print(list1[i],end=' ')
            print("\n")
            print("2nd Row   ",end=' ')
            for i in range (0,len(list2)):
                print(list2[i],end=' ')
            print("\n")
            print("3rd Row   ",end=' ')
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
                print(nume2 + "'s turn")
                print("Input the row you choose:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 3)):
                        if ((rand == 1) and (len(list1) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 2) and (len(list2) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 3) and (len(list3) == 0)):
                            print("Wrong row! Input the row you choose:")
                        else:
                            loop1 = 0
                    else:
                        print("You have entered a wrong option!")
                        loop1 = 10
                except ValueError:
                    print("You have entered a wrong option!")
            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("How many sticks do you want to cut? ")
                try:
                    nr_ales = int(input())
                    if ((rand == 1) and ((nr_ales == 0) or (nr_ales > len(list1)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 2) and ((nr_ales == 0) or (nr_ales > len(list2)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 3) and ((nr_ales == 0) or (nr_ales > len(list3)))):
                        print("Wrong number! Enter the number of sticks:")
                    else:
                        loop1 = 0;
                except ValueError:
                    print("You have entered a wrong option!")
            print(nume2,"chose the row", rand, "and cut", nr_ales, "sticks.")

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
            print("1st Row   ", end=' ')
            for i in range(0, len(list1)):
                print(list1[i], end=' ')
            print("\n")
            print("2nd Row   ", end=' ')
            for i in range(0, len(list2)):
                print(list2[i], end=' ')
            print("\n")
            print("3rd Row   ", end=' ')
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
                print(nume1 + "'s turn")
                print("Input the row you choose:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 3)):
                        if ((rand == 1) and (len(list2) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 2) and (len(list3) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 3) and (len(list4) == 0)):
                            print("Wrong row! Input the row you choose:")
                        else:
                            loop1=0
                    else:
                        print("You have entered a wrong option!")
                        loop1=10
                except ValueError:
                    print("You have entered a wrong option!")

            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("How many sticks do you want to cut? ")
                try:
                    nr_ales=int(input())
                    if ((rand == 1) and ((nr_ales == 0) or (nr_ales > len(list2)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 2) and ((nr_ales == 0) or (nr_ales > len(list3)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 3) and ((nr_ales == 0) or (nr_ales > len(list4)))):
                        print("Wrong number! Enter the number of sticks:")
                    else:
                        loop1=0;
                except ValueError:
                    print("You have entered a wrong option!")

            print(nume1,"chose the row",rand, "and cut",nr_ales,"sticks.")

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
            print("1st Row   ",end=' ')
            for i in range (0,len(list2)):
                print(list2[i],end=' ')
            print("\n")
            print("2nd Row   ",end=' ')
            for i in range (0,len(list3)):
                print(list3[i],end=' ')
            print("\n")
            print("3rd Row   ",end=' ')
            for i in range (0,len(list4)):
                print(list4[i],end=' ')
            print("\n")
            if (len(list2) + len(list3) + len(list4) == 0):
                print(nume2 + " won!")
                loop=0;
            else:
                jucator=1

        else:
            # selectare rand
            loop1 = 10
            while (loop1 != 0):
                print(nume2 + "'s turn")
                print("Input the row you choose:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 3)):
                        if ((rand == 1) and (len(list2) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 2) and (len(list3) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 3) and (len(list4) == 0)):
                            print("Wrong row! Input the row you choose:")
                        else:
                            loop1 = 0
                    else:
                        print("You have entered a wrong option!")
                        loop1 = 10;
                except ValueError:
                    print("You have entered a wrong option!")
            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("How many sticks do you want to cut? ")
                try:
                    nr_ales = int(input())
                    if ((rand == 1) and ((nr_ales == 0) or (nr_ales > len(list2)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 2) and ((nr_ales == 0) or (nr_ales > len(list3)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 3) and ((nr_ales == 0) or (nr_ales > len(list4)))):
                        print("Wrong number! Enter the number of sticks:")
                    else:
                        loop1 = 0
                except ValueError:
                    print("You have entered a wrong option!")

            print(nume2,"chose the row", rand, "and cut", nr_ales, "sticks.")

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
            print("1st Row   ", end=' ')
            for i in range(0, len(list2)):
                print(list2[i], end=' ')
            print("\n")
            print("2nd Row   ", end=' ')
            for i in range(0, len(list3)):
                print(list3[i], end=' ')
            print("\n")
            print("3rd Row   ", end=' ')
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
                print(nume1 + "'s turn")
                print("Input the row you choose:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 4)):
                        if ((rand == 1) and (len(list1) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 2) and (len(list2) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 3) and (len(list3) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 4) and (len(list4) == 0)):
                            print("Wrong row! Input the row you choose:")
                        else:
                            loop1=0
                    else:
                        print("You have entered a wrong option!")
                        loop1=10
                except ValueError:
                    print("You have entered a wrong option!")

            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("How many sticks do you want to cut? ")
                try:
                    nr_ales=int(input())
                    if ((rand == 1) and ((nr_ales == 0) or (nr_ales > len(list1)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 2) and ((nr_ales == 0) or (nr_ales > len(list2)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 3) and ((nr_ales == 0) or (nr_ales > len(list3)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 4) and ((nr_ales == 0) or (nr_ales > len(list4)))):
                        print("Wrong number! Enter the number of sticks:")
                    else:
                        loop1=0
                except ValueError:
                    print("You have entered a wrong option!")

            print(nume1,"chose the row",rand, "and cut",nr_ales,"sticks.")

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
            print("1st Row   ",end=' ')
            for i in range (0,len(list1)):
                print(list1[i],end=' ')
            print("\n")
            print("2nd Row   ",end=' ')
            for i in range (0,len(list2)):
                print(list2[i],end=' ')
            print("\n")
            print("3rd Row   ",end=' ')
            for i in range (0,len(list3)):
                print(list3[i],end=' ')
            print("\n")
            print("4th Row   ", end=' ')
            for i in range(0, len(list4)):
                print(list4[i], end=' ')
            print("\n")
            if (len(list1) + len(list2) + len(list3) + len(list4) == 0):
                print(nume2 + " won!")
                loop=0;
            else:
                jucator=1

        else:
            # selectare rand
            loop1 = 10
            while (loop1 != 0):
                print(nume2 + "'s turn")
                print("Input the row you choose:")
                try:
                    rand = int(input())
                    if ((rand>0) and (rand <= 4)):
                        if ((rand == 1) and (len(list1) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 2) and (len(list2) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 3) and (len(list3) == 0)):
                            print("Wrong row! Input the row you choose:")
                        elif ((rand == 4) and (len(list4) == 0)):
                            print("Wrong row! Input the row you choose:")
                        else:
                            loop1 = 0
                    else:
                        print("You have entered a wrong option!")
                        loop1 = 10
                except ValueError:
                    print("You have entered a wrong option!")

            # selectare numar bete de taiat
            loop1 = 10
            while (loop1 != 0):
                print("How many sticks do you want to cut? ")
                try:
                    nr_ales = int(input())
                    if ((rand == 1) and ((nr_ales == 0) or (nr_ales > len(list1)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 2) and ((nr_ales == 0) or (nr_ales > len(list2)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 3) and ((nr_ales == 0) or (nr_ales > len(list3)))):
                        print("Wrong number! Enter the number of sticks:")
                    elif ((rand == 4) and ((nr_ales == 0) or (nr_ales > len(list4)))):
                        print("Wrong number! Enter the number of sticks:")
                    else:
                        loop1 = 0
                except ValueError:
                    print("You have entered a wrong option!")

            print(nume2,"chose the row", rand, "and cut", nr_ales, "sticks.")

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
            print("1st Row   ", end=' ')
            for i in range(0, len(list1)):
                print(list1[i], end=' ')
            print("\n")
            print("2nd Row   ", end=' ')
            for i in range(0, len(list2)):
                print(list2[i], end=' ')
            print("\n")
            print("3rd Row   ", end=' ')
            for i in range(0, len(list3)):
                print(list3[i], end=' ')
            print("\n")
            print("4th Row   ", end=' ')
            for i in range(0, len(list4)):
                print(list4[i], end=' ')
            print("\n")
            if (len(list1) + len(list2) + len(list3) + len(list4) == 0):
                print(nume1 + " won!")
                loop = 0;
            else:
                jucator = 0
# terminare joc


