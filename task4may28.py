
# You need to design a quick application that will collect the user's name and phone number and store it to the dictionary!

def file_addfunc(namepage):
    with open("contactpage.txt", "a") as f:
        for k in namepage:
            f.write(f'{k} : {namepage[k]}\n') 

def file_delfunc(name):
    with open("contactpage.txt", "r") as f:
        lines = f.readlines()
    with open("contactpage.txt", "w") as f:
        for line in lines:
            if line[:line.index(':')-1] !=  name:
                f.write(line)



def main():
    choose = int(input('enter your choice, 1 for add a new contacts, 2 for delete contracts, 0 for quit: '))
    namepage = {}
    while choose:
        while choose == 1:
            name = input('enter the contact\'s name: ')
            if name == '0':
                break
            phonenum = input('enter the contact\'s phonenum: ')
            namepage[name] = phonenum
            file_addfunc(namepage)
        while choose == 2:
            name = input('enter the contact\'s name: ')
            if name == '0':
                break
            file_delfunc(name)
        if choose != 1 and choose != 2:
            print('wrong choice, choose again')
        choose = int(input('enter your choice, 1 for add a new contacts, 2 for delete contracts, 0 for quit: '))
    else:
        print('Okay!')


if __name__ == '__main__':
    main()
    