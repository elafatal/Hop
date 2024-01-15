import random

names = [] #esme player ha
records = []#save emtiaz

def game(name, index, first):
    turn = 1
    while True:#halghe tashkil dahandeye bazi
        if turn % 2 != 0 : #nobate cpu
            if turn % index== 0:
                print(">cpu : hop")
            else:
                print(">cpu : ", first)
            turn += 1 #jelo raftane nobat
            first += 1
        else: #nobate player
            n = input(">Player : ")
            if turn % index == 0:
                if n != "hop" and n != "HOP":#sharte bakht1
                    break
            else:
                if n == "hop" or n == "HOP" or int(n) != first:#sharte bakht2
                    break
            turn += 1
            first += 1 #ziad shodan aadad ta payan bazi
    print(name, "    ", turn/2) #namayesh nahayi emtiaz player

    is_exist = False #agar true bashe yaani plauyer ghablan bazi karde
    index2 = -1
    for item in names:
        if item == name:
            is_exist = True
            index2 = names.index(item)
    if not is_exist: #! is_exist
        names.append(name) #add kardan player va emtiazesh
        records.append(turn/2)
    else:
        records[index2] = turn/2 #update emtiaze playere ghadimi



    

def start():
    while True:
        name = input("Please Enter Your name: ")
        print("hi " + name + " :)")
        index = int(input("please enter your index : ")) #zarib hop
        char=random.randint(1,30) #adad random baraye shorooe bazi
        print(char)
        game(name, index, char)
        a = input(">>Play More? (yes/no) : ") #shorooe dobareye bazi baad az bakht
        if a == 'no' or a == 'NO':
            break
    for i in range(len(names)):
        print(names[i], " => ", records[i])


if __name__ == '__main__':
    start()