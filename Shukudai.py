import time
import os
import shutil

def Animation_Effect(Transition_Words):

    import time 
    import os

    clear = lambda: os.system('cls')
    
    y = str(Transition_Words)
    l = list(y)

    a = []
    i = 0

    for k in l:
        
        i += 1
        a.append(k)
        print('        '+''.join(a))
        time.sleep(.1)
        if i < len(l):
            clear()

def Transition_Effect(Transition_Words):

    import time 
    import os

    clear = lambda: os.system('cls')
    
    y = str(Transition_Words)
    l = list(y)

    a = []
    i = 0

    for k in l:
        
        i += 1
        a.append(k)
        print('''
        ░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░
        ░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░
        ░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌
        ░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░
        ░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░
        ▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░
        ▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░
        ░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄
        ░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒
        ▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒\n''')
        print('        '+''.join(a))
        time.sleep(.1)
        if i < len(l):
            clear()
        else:
            time.sleep(1)

def anime():
    print('''
    ░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░
    ░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░
    ░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌
    ░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░
    ░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░
    ▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░
    ▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░
    ░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄
    ░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒
    ▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒''')
    print('\n   B')
    time.sleep(.1)
    clear()
    print('''
    ░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░
    ░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░
    ░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌
    ░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░
    ░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░
    ▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░
    ▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░
    ░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄
    ░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒
    ▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒''')
    print('\n   By')
    time.sleep(.1)
    clear()
    print('''
    ░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░
    ░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░
    ░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌
    ░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░
    ░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░
    ▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░
    ▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░
    ░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄
    ░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒
    ▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒''')
    print('\n   Bye')
    time.sleep(.1)
    clear()
    print('''
    ░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░
    ░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░
    ░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌
    ░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░
    ░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░
    ▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░
    ▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░
    ░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄
    ░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒
    ▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒''')
    print('\n   Byee')
    time.sleep(.1)
    clear()
    print('''
    ░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░
    ░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░
    ░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌
    ░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░
    ░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░
    ▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░
    ▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░
    ░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄
    ░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒
    ▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒''')
    print('\n   Byeee')
    time.sleep(.1)
    clear()
    print('''
    ░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░
    ░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░
    ░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌
    ░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░
    ░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░
    ▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░
    ▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░
    ░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄
    ░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒
    ▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒''')
    print('\n   Byeeee')
    time.sleep(.1)
    clear()
    print('''
    ░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░
    ░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░
    ░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌
    ░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░
    ░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░
    ▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░
    ▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░
    ░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄
    ░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒
    ▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒''')
    print('\n   Byeeeee')
    time.sleep(.1)
    clear()
    print('''
    ░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░
    ░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░
    ░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌
    ░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░
    ░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░
    ▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░
    ▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░
    ░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄
    ░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒
    ▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒''')
    print('\n   Byeeeeee')
    time.sleep(.1)
    clear()
    print('''
    ░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░
    ░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░
    ░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌
    ░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░
    ░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░
    ▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░
    ▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░
    ░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄
    ░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒
    ▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒''')
    print('\n   Byeeeeeee')
    time.sleep(.1)
    clear()
    print('''
    ░░░░█▐▄▒▒▒▌▌▒▒▌░▌▒▐▐▐▒▒▐▒▒▌▒▀▄▀▄░
    ░░░█▐▒▒▀▀▌░▀▀▀░░▀▀▀░░▀▀▄▌▌▐▒▒▒▌▐░
    ░░▐▒▒▀▀▄▐░▀▀▄▄░░░░░░░░░░░▐▒▌▒▒▐░▌
    ░░▐▒▌▒▒▒▌░▄▄▄▄█▄░░░░░░░▄▄▄▐▐▄▄▀░░
    ░░▌▐▒▒▒▐░░░░░░░░░░░░░▀█▄░░░░▌▌░░░
    ▄▀▒▒▌▒▒▐░░░░░░░▄░░▄░░░░░▀▀░░▌▌░░░
    ▄▄▀▒▐▒▒▐░░░░░░░▐▀▀▀▄▄▀░░░░░░▌▌░░░
    ░░░░█▌▒▒▌░░░░░▐▒▒▒▒▒▌░░░░░░▐▐▒▀▀▄
    ░░▄▀▒▒▒▒▐░░░░░▐▒▒▒▒▐░░░░░▄█▄▒▐▒▒▒
    ▄▀▒▒▒▒▒▄██▀▄▄░░▀▄▄▀░░▄▄▀█▄░█▀▒▒▒▒''')
    print('\n   Byeeeeeeee')
    time.sleep(3)

clear = lambda: os.system('cls')

Transition_Effect('Enter the absolute path of file (For example : C:\\User\\abc.txt):\n')
File_Name = input('        ')

if os.path.exists(File_Name):
    
        clear()

        print('Prompt Menu\n')

        print('For reading an existing file : 1')

        print('For writing  a new file : 2')

        print('For appending in an existing file : 3')

        print('For editing an existing file : 4')

        print('For searching in an existing file : 5')

        print('For copying an existing file : 6')

        print('For deleting an existing file : 7')

        input('Press Enter')
        Transition_Effect('\nEnter the Command:\n')
        command = int(input('        ' ))

        clear()
        
        if command == 1:
            print('If you want to read the whole document : 1')
            print('If you want to read specific lines : 2')
            print('If you want to read a specific line : 3')
            print('If you want to read some words from the start : 4')
            
            input('Press Enter')
            Transition_Effect('\nEnter the Command:\n')
            command_1 = int(input('        '))
            
            clear()
            
            if command_1 == 1:

                f = open(File_Name)
                s = f.read()
                Transition_Effect(s)
                Animation_Effect('\nPress Enter')
                input()
                clear()
                anime()
                f.close()
                
                exit

            elif command_1 == 2:

                try:
                    
                    Transition_Effect('Enter the line number from which you want to read:\n')
                    Starting_line = int(input('        '))
                    clear()
                    Transition_Effect('Enter the line number till which you want to read:\n')
                    Ending_line = int(input('        '))
                    clear()
                    f = open(File_Name)
                    s = f.readlines()
                    
                    for i in range(Starting_line - 1,Ending_line):

                        print(s[i])

                    input('Press Enter')
                    f.close()
                
                except EOFError:

                    Transition_Effect('There are not enough lines in the file.')                

                Animation_Effect('\nPress Enter')
                input()
                clear()
                anime()
                
                exit

            elif command_1 == 3:

                try:
                    
                    Transition_Effect('Enter the line number:')
                    Line_number = int(input('        '))
                    
                    clear()
                    
                    f = open(File_Name)
                    
                    for i in range(Line_number):

                        s = f.readline()
                        print(s)
                
                    input('Press Enter')
                    Transition_Effect('{}'.format(s))
                    f.close()

                except EOFError:

                    Transition_Effect('There are not enough lines in the file.')

                Animation_Effect('\nPress Enter')
                input('        ')
                clear()
                anime()
                
                exit

            elif command_1 == 4:

                try:

                    Transition_Effect('Enter the number of words you want to read:\n')
                    Number_of_Words = int(input('        '))
                    
                    clear()
                    
                    f = open(File_Name)
                    s = f.read()
                    w = s.split()
                    
                    for i in range(Number_of_Words):

                        print(w[i],end = ' ') 
                
                    input('Press Enter')
                    f.close()
                
                except EOFError:

                    Transition_Effect('There are not enough words in the file.')                
                
                Transition_Effect('\nPress Enter')
                input()
                anime()
                
                exit

        elif command == 2:

            print('If you want to write words : 1')
            print('If you want to write lines : 2')
            print('If you want to write the document : 3')
            
            input('Press Enter')
            Transition_Effect('\nEnter the Command:\n')
            command_2 = int(input('        '))

            clear()
            
            if command_2 == 1:

                f = open(File_Name,'w')
                Transition_Effect('Enter the number of words you want to enter:\n')
                x = int(input('        '))
                y = 0

                while y <= x:

                    Transition_Effect('Enter the Word:\n')
                    s = input('        ')    

                    if ' ' in s:

                        y -= 1

                        if y < 0:

                            y += 1
                        Transition_Effect('The entered string is not a word.')
                    
                    else:
                    
                        f.write(s + '\n')
                    
                    y +=1
            
                f.close()
            
                Transition_Effect('File written successfully.')
                time.sleep(2)
                Transition_Effect('\nPress Enter')

                clear()

                Transition_Effect('Do you want to want to see the written file.\n\nEnter Yes/No:\n')

                Choice = input('        ')

                clear()
                
                if Choice in 'YesyesYESYEsyEsyESyeS':

                    for saachi in range(10):

                        prachi = 'Loading' + 'g' * saachi
                        print(prachi)
                        time.sleep(.5)
                        clear()                     
            
                    Path = os.path.abspath(File_Name)
                    os.startfile(Path)
                    exit

                else:

                    exit   
            
            elif command_2 == 2:
            
                f = open(File_Name,'w')
                Transition_Effect('Enter the number of lines you want to enter:\n')
                x = int(input('        '))

                clear()
            
                for i in range(x):
                    
                    Transition_Effect('Enter the line:\n')
                    s = input('        ')
                    f.write(s)
            
                f.close()
            
                Transition_Effect('File written successfully.')
                time.sleep(2)
                Transition_Effect('\nPress Enter')

                clear()

                Transition_Effect('Do you want to want to see the written file.\n\nEnter Yes/No:\n')

                Choice = input('        ')

                clear()
            
                if Choice in 'YesyesYESYEsyEsyESyeS':
            
                    for saachi in range(10):

                        prachi = 'Loading' + 'g' * saachi
                        print(prachi)
                        time.sleep(.5)
                        clear() 
            
                    Path = os.path.abspath(File_Name)
                    os.startfile(Path)        
                    exit

                else:
            
                    exit   
                
            elif command_2  == 3:
            
                f = open(File_Name,'w')
                Transition_Effect('Write the file:\n')
                s = input('        ')
                f.write(s)
                f.close()
            
                Transition_Effect('File written successfully.')
                time.sleep(2)
                Transition_Effect('\nPress Enter')

                clear()

                Transition_Effect('Do you want to want to see the written file.\n\nEnter Yes/No:\n')
            
                Choice = input("        ")

                clear()
            
                if Choice in 'YesyesYESYEsyEsyESyeS':
            
                    for saachi in range(10):

                        prachi = 'Loading' + 'g' * saachi
                        print(prachi)
                        time.sleep(.5)
                        clear()             
                    
                    Path = os.path.abspath(File_Name)
                    os.startfile(Path)
                    exit

                else:
            
                    exit   

        if command == 3:
            
            print('If you want to append words : 1') 
            print('If you want to append lines : 2')
            print('If you want to append dictionaries : 3')
            print('If you want to append another document : 4')
            
            input('Press Enter')
            Transition_Effect('\nEnter the Command:\n')
            command_3 = int(input('        '))

            clear()

            if command_3 == 1:
                
                f = open(File_Name,'a')
                Transition_Effect('Enter the number of words you want to enter:\n')
                x = int(input('        '))
                y = 0
                
                clear()
                
                while y <= x:
                    
                    Transition_Effect('Enter the Word:\n')
                    s = input('        ')    
                
                    if ' ' in s:
                
                        y -= 1
            
                        if y < 0:
            
                            y += 1
                        Transition_Effect('The entered string is not a word.\n')
                
                    else:
                
                        f.write(s + '\n')
                        Transition_Effect('Word is written succesfully.\n ')

                    y +=1
            
                f.close()

                time.sleep(2)
                Transition_Effect('\nPress Enter')

                clear()

                Transition_Effect('Do you want to want to see the written file.\n\nEnter Yes/No:\n')
            
                Choice = input("        ")

                clear()
                
                if Choice in 'YesyesYESYEsyEsyESyeS':
                
                    for saachi in range(10):

                        prachi = 'Loading' + 'g' * saachi
                        print(prachi)
                        time.sleep(.5)
                        clear() 
            
                    Path = os.path.abspath(File_Name)
                    os.startfile(Path)
                    exit

                else:
                
                    exit   
            
            elif command_3 == 2:
            
                f = open(File_Name,'a')
                Transition_Effect('Enter the number of lines you want to enter:\n')
                x = int(input('        '))
            
                clear()
                
                for i in range(x):
                    
                    Transition_Effect('Enter the line:\n')
                    s = input('        ')
                    f.write(s)
                    Transition_Effect('Line written successfully.\n')
            
                f.close()

                time.sleep(2)
                Transition_Effect('\nPress Enter')
                
                clear()
            
                Transition_Effect('Do you want to want to see the written file.\n\nEnter Yes/No:\n')

                Choice = input("        ")

                clear()

                if Choice in 'YesyesYESYEsyEsyESyeS':
            
                    for saachi in range(10):

                        prachi = 'Loading' + 'g' * saachi
                        print(prachi)
                        time.sleep(.5)
                        clear() 
            
                    Path = os.path.abspath(File_Name)
                    os.startfile(Path)
                    exit

                else:
            
                    exit   
                
            elif command_3 == 3:
            
                f = open(File_Name,'a')
                Transition_Effect('Enter the number of dictionaries you want to enter:\n')
                x = int(input('        '))
            
                clear()

                for i in range(x):
                    
                    l = []
                    Transition_Effect('Enter the number of keys in dictionary:\n')
                    y = int(input('        '))
                    f.write('{')
            
                    for j in range(y):    
                        
                        Transition_Effect('Enter the key:\n')
                        K = input('        ')
                        Transition_Effect('Enter the value:\n')
                        V = input('        ')
                        l.append('{}'.format(K)+':'+'{}'.format(V))
            
                    f.write(','.join(l)+'}'+'\n')
                    
                f.close()
            
                Transition_Effect('Dictionaries written successfully.')
                time.sleep(2)
                Transition_Effect('\nPress Enter')

                clear()

                Transition_Effect('Do you want to want to see the written file.\n\nEnter Yes/No:\n')

                Choice = input("         ")

                clear()
            
                if Choice in 'YesyesYESYEsyEsyESyeS':
            
                    for saachi in range(10):

                        prachi = 'Loading' + 'g' * saachi
                        print(prachi)
                        time.sleep(.5)
                        clear() 

                    Path = os.path.abspath(File_Name)
                    os.startfile(Path)
                    exit

                else:
            
                    exit   
            
            elif command_3 == 4:
            
                f = open(File_Name,'a')
                Transition_Effect('How many files do you want to append:\n')
                K = int(input('        '))

                clear()
            
                for i in range(K):
                    
                    Transition_Effect('Enter the path of another file that you want to append:\n')
                    k = input('        ')
                    F = open('{}.txt'.format(k))
                    s = F.read()
                    f.write(s+'\n')
            
                f.close()

                Transition_Effect('File appended successfully.')   
                time.sleep(2)
                Transition_Effect('\nPress Enter')

                clear()

                Transition_Effect('Do you want to want to see the written file.\n\nEnter Yes/No:\n')
            
                Choice = input("        ")

                clear()
            
                if Choice in 'YesyesYESYEsyEsyESyeS':
            
                    for saachi in range(10):

                        prachi = 'Loading' + 'g' * saachi
                        print(prachi)
                        time.sleep(.5)
                        clear() 

                    Path = os.path.abspath(File_Name)
                    os.startfile(Path)
                    exit

                else:
            
                    exit

        elif command == 4:
            
            print('Change the name of file : 1')
            print('Replace any word : 2')
            print('Delete any word : 3')
            print('Delete any line : 4')

            Transition_Effect('\nEnter the Command:\n')
            command_4 = int(input('        '))

            clear()

            if command_4 == 1:

                Transition_Effect('Do you want to keep the renamed file in same directory : 1')
                Transition_Effect('Do you want to keep the renamed file in different directory : 2')

                Transition_Effect('\nEnter the Command:\n')
                command_4_1 = int(input('        '))

                clear()

                if command_4_1 == 1:

                    try:

                        Transition_Effect('Enter the name of new file:\n')
                        New_name = input('        ')
                        clear()
                        Directory = os.path.dirname(File_Name)
                        os.rename(File_Name,'{}{}.txt'.format(Directory,New_name))
                        Transition_Effect('File renamed succesfully.')
                    
                    except FileNotFoundError as n:
                    
                        print(n)
                    
                    except PermissionError as p:
                    
                        print(p)
                    
                    Transition_Effect('\nPress Enter')
                    input('        ')
                    anime()
                    
                    exit

                elif command_4_1 == 2:

                    try:

                        Transition_Effect('Enter the name of new file:\n')
                        New_name = input('        ')
                        clear()
                        Transition_Effect('Enter the new path:\n')
                        New_Directory = input('        ')
                        clear()
                        Directory = os.path.dirname(File_Name)
                        os.rename(File_Name,'{}\\{}.txt'.format(New_Directory,New_name))
                        Transition_Effect('File renamed successfully.')

                    except FileNotFoundError as F:
                    
                        print(F)
                    
                    except PermissionError as P:
                    
                        print(P)
                    
                    Transition_Effect('\nPress Enter')
                    input()
                    anime()
                    
                    exit
            
            elif command_4 == 2:

                Transition_Effect('Enter the number of words you want to get completely replaced:\n')
                Number_of_words = int(input('        '))

                clear()
                
                for i in range(Number_of_words):

                    Transition_Effect('Enter the word to be replaced:\n')
                    Word_to_be_replaced = input('        ')
                    clear()
                    Transition_Effect('Enter the new word:\n')
                    Replaced_word = input('        ')
                    clear()
                
                    f = open(File_Name)
                    s =str(f.read())
                    s = s.replace(Word_to_be_replaced,Replaced_word)
                    Transition_Effect(s)
                    f.close()

                    f = open(File_Name,'w')
                    f.write(s)
                    f.close()

                time.sleep(1)
                clear()
                
                Transition_Effect('Words replaced successfully.')
                clear()
                time.sleep(2)
                Transition_Effect('\nPress Enter')
                
                clear()
                
                Transition_Effect('Do you want to want to see the new file.\n\nEnter Yes/No:\n')

                Choice = input("        ")

                clear()
            
                if Choice in 'YesyesYESYEsyEsyESyeS':
            
                    for saachi in range(10):

                        prachi = 'Loading' + 'g' * saachi
                        print(prachi)
                        time.sleep(.5)
                        clear() 
                    
                    Path = os.path.abspath(File_Name)
                    os.startfile(Path)
                    exit

                else:
            
                    exit   

            elif command_4 == 3:
                
                Transition_Effect('Enter the number of words you want to get completely deleted:\n')
                Number_of_words = int(input('        '))
                
                clear()
                
                for i in range(Number_of_words):

                    Transition_Effect('Enter the word to be deleted:\n')
                    Word_to_be_deleted = input('        ')

                    f = open(File_Name)
                    s =str(f.read())
                    s = s.replace(Word_to_be_deleted,'')
                    Transition_Effect(s)
                    f.close()

                    f = open(File_Name,'w')
                    f.write(s)
                    f.close()

                Transition_Effect('Words deleted successfully.')
                clear()
                time.sleep(2)
                Transition_Effect('\nPress Enter')

                clear()
            
                Transition_Effect('Do you want to want to see the new file.\n\nEnter Yes/No:\n')

                Choice = input("        ")

                clear()
            
                if Choice in 'YesyesYESYEsyEsyESyeS':
            
                    for saachi in range(10):

                        prachi = 'Loading' + 'g' * saachi
                        print(prachi)
                        time.sleep(.5)
                        clear() 

                    Path = os.path.abspath(File_Name)
                    os.startfile(Path)
                    exit

                else:
            
                    exit   

            elif command_4 == 4:

                Transition_Effect('Enter the number of lines you want to be deleted:\n')
                Number_of_lines = int(input('        '))

                clear() 

                for i in range(Number_of_lines):
                    
                    Transition_Effect('Enter the line number:\n')
                    Line = int(input('        '))           
                    
                    f = open('{}.txt')
                    s =f.readlines()
                    s.remove(s[Line - 1])
                    Transition_Effect(s)
                    f.close()

                    f = open(File_Name,'w')
                    
                    for i in range(len(s)):
                    
                        f.write(s[i])
                    
                    f.close()

                Transition_Effect('Lines deleted successfully.')
                clear()
                time.sleep(2)
                Transition_Effect('\nPress Enter')

                clear()

                Transition_Effect('Do you want to want to see the new file.\n\nEnter Yes/No:\n')

                Choice = input("        ")

                clear()
            
                if Choice in 'YesyesYESYEsyEsyESyeS':
            
                    for saachi in range(10):

                        prachi = 'Loading' + 'g' * saachi
                        print(prachi)
                        time.sleep(.5)
                        clear() 

                    Path = os.path.abspath(File_Name)
                    os.startfile(Path)
                    exit

                else:
            
                    exit   

        elif command == 5:

            Transition_Effect('Enter the number of words you want to be searched:\n')
            Number_of_words_to_be_searched = int(input('        '))

            clear()

            for z in range(Number_of_words_to_be_searched):

                Transition_Effect('Enter the word to be searched:\n')
                Word_to_be_searched = input('        ')

                f = open(File_Name)
                a = f.readlines()
                b = len(a)
                f.close()

                k = open(File_Name)

                l = []
                x = 0

                for i in range(b):
                    x += 1
                    s = str(k.readline())
                    w = s.split( )

                    if Word_to_be_searched in s:

                        c = w.count(Word_to_be_searched)
                        l.append(c)

                        for j in range(c):

                            d = w.index(Word_to_be_searched) + j +1
                            Animation_Effect('{} found in line {} at position {}.'.format(Word_to_be_searched,x,d))
                            w.remove(Word_to_be_searched)
                    
                    else:

                        pass

                k.close()

                if sum(l) == 0:

                    Animation_Effect('{} is not found in the document'.format(Word_to_be_searched))

                else:

                    pass

            Animation_Effect('\nPress Enter')
            input()
            clear()
            anime()
            
            exit    

        elif command == 6:

            Transition_Effect('Enter the name for the copied file:\n')
            New_name = input('        ')
            clear()
            Transition_Effect('Enter the path for copied file:\n')
            Destination = input('        ')
            clear()
            New_Absolute_Path = Destination + '\\' + '{}.txt'.format(New_name)
            Original_Absolute_Path = os.path.abspath(File_Name)
                
            try:    
                
                for saachi in range(10):

                        prachi = 'Loading' + 'g' * saachi
                        print(prachi)
                        time.sleep(.5)
                        clear() 
                
                shutil.copy(Original_Absolute_Path,New_Absolute_Path)
                Transition_Effect('File copied successfully')
            
            except shutil.SameFileError:
            
                Transition_Effect('New absolute path and the old absolute path are the same.')
            
            except PermissionError:

                Transition_Effect('Permission Denied')
            
            except:

                Transition_Effect('There is some error occuring while copying the file.')

            Animation_Effect('\nPress Enter')
            input()
            clear()
            anime()
            
            exit

        elif command == 7:

            if os.path.exists(File_Name):

                for saachi in range(10):

                        prachi = 'Loading' + 'g' * saachi
                        print(prachi)
                        time.sleep(.5)
                        clear()                 
                
                os.remove(File_Name)
                Transition_Effect('File deleted successfully')

            else:

                Transition_Effect('The file does not exist.')

            Animation_Effect('\nPress Enter')
            input()
            clear()
            anime()
            
            exit

else:

        Transition_Effect('The latter file does not exists')
        Animation_Effect('\nPress Enter')
        input()
        clear()
        anime()

exit