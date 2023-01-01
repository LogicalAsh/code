def display1():
    file = open('ashwin.txt','w+')
    data = ['ashwin\n','is good boy']
    file.writelines(data)
    file.seek(0)
    data1 = file.readlines()
    for i in data1:
        s=i.split()
        for j in s:
            print(j,'#',end='')

def count():
    file=open('ashwin.txt','r')
    vow,cons,up,lo,o=0,0,0,0,0
    data = file.readlines()
    vowlel='aeiou'
    for i in data:
        for j in i:
            if j.isalpha():
                if j.lower() in vowlel:
                    vow+=1
                else:
                    cons+=1
                if j.isupper:
                    up+=1
                if j.islower:
                    lo+=1
            else:
                o+=1
    print(f'vowels is           :{vow}')
    print(f'consones is         :{cons}')
    print(f'uppercase is        :{up}')
    print(f'lowecase is         :{lo}')
    print(f'Other tha alfa is   :{o}')

def binary_file():
    import pickle
    file = open('ashwin.txt','wb+')
    dic=[]
    c='y'
    while c=='y':
        roll = input('Enter the roll number      :')
        name = input('Enter the name             :')
        dic.append([roll,name])
        c=     input('you  want to add more(Y/n) :').lower()
    pickle.dump(dic,file)
    r = input('Enter the roll number to be searched :')
    stu = []
    file.seek(0)
    try:
        while True:
            #print('while loop starts')
            stu = pickle.load(file)
            for i in stu:
                #print(f'for loop ran {flag}')
                if i[0]==r:
                    print(f'The name of the student with roll number as {r} is :{i[1]}')
    except:
        print('Thank you :)')
        file.close()

def binary_update():
    import pickle
    file = open('ashwin.txt','wb+')
    lis = []
    ch='y'
    while ch=='y':
        roll = int(input('Enter the roll number  :'))
        name =     input('Enter the name         :')
        mark = int(input('Enter the mark         :'))
        ch = input('Do you want to continue(Y/n) :')
        lis.append([roll,name,mark])
    pickle.dump(lis,file)
    file.seek(0)
    try:
        while True:
            intial_pos = file.tell()
            data = pickle.load(file)
            print(data)
            oldData = int(input('Enter the old roll number :'))
            for i in data:
                if i[0]==oldData:
                    print(f'The name of the student is  :{i[1]}')
                    print(f'The mark of the student is  :{i[2]}')
                    newRoll = int(input('Enter the new roll number :'))
                    i[0]=newRoll
                    file.seek(intial_pos)
                    pickle.dump(i,file)

    except:
        print('Updated')
        file.seek(0)
    try:
        while True:
            print('The updataed data :)')
            stu = pickle.load(file)
            print(stu)
    except:
        file.close()




def csvfile():
    import csv
    file = open('ashwin.csv','w+',newline='\n')
    wo = csv.writer(file)
    c='y'
    while c=='y':
        empname =input('Enter the name of EMP  :')
        empnum  = int(input('Enter the emp number   :'))
        empsal  = int(input('Enter the emp salary   :'))
        wo.writerow([empname,empnum,empsal])
        c=input('Add one more(Y/n)      : ')
    #searching the emp
    fkemp = int(input('Enter the empnumber :'))
    file.seek(0)
    ro = csv.reader(file)
    #print(ro)
    for i in ro:
        if int(i[0])==fkemp:
            print('emp found :)')
            print(f'emp name is      : {i[1]}')
            print(f'emp salary is    : {i[2]}')
    
def stack():
    stack = []
    def push(ele):
        stack.append(ele)
    def display():
        if len(stack)!=0:
            for i in range(len(stack)-1,-1,-1):
                print(stack[i])
        else:
            print('Underflow :(')
    def pop():
        stack.pop()
    while True:
        print('1)   DISPLAY \n2)   PUSH \n3)   POP')
        op=int(input('Option :'))
        if op==1:
            display()
        if op==2:
            ele = int(input('Enter the element :'))
            push(ele)
        if op==3:
            pop()
def mysql():
    import mysql.connector as mysql
    m = mysql.connect(host='localhost',user='root',passwd='root')
    if m.is_connected():
        print('connected :)')
        cur = m.cursor()
    commands = ['create database sam1;', 'use sam1;' ,'create table t1(name varchar(20) , class int(20));']
    try:
        cur.execute(commands[1])
    except:
        for i in commands:
            cur.execute(i)
            m.commit()
    c='y'
    while c=='y':
        name = input('Enter the name    :')
        clas = input('Enter the class   :')
        q = f'insert into t1 values("{name}","{clas}");'
        cur.execute(q)
        m.commit()
        c = input('Do you want to conitine(Y/n)').lower()
    cur.execute('select * from t1;')
    data = cur.fetchall()
#    print(data)
    for i in data:
        print(i)
def two_files():
    file1 = open('ashwin.txt','r')
    file2 = open('ashwin1.txt','w')
    data =file1.readlines()
    for i in data:
        if 'a' not in i:
            file2.write(i)
two_files()

 