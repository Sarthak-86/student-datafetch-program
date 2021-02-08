l=[]

while True:
    a=int(input('press 1 for add student\npress 2 for check student result\npress 3 for adding marks of student\npress 4 for delete student\npress 5 for exit\n'))
    if a==1:
        nm=input('enter name: ')
        rln=input('enter roll number: ')
        fnm=input('enter father name: ')
        scl=input('enter school name: ')
        cls=input('enter class: ')
        data={'name':nm,'rolnm':rln,'fathernm':fnm,'schoolnm':scl,'class':cls,'rslt':[]}
        l.append(data)



    if a==2:
        b=input('enter student roll number ')
        for i in l:
            if(i['rolnm']==b):
                print('-------MARKSHEET-------')
                print('STUDENT NAME : '+i['name'])
                print('ROLL NUMBER  : ' + i['rolnm'])
                print('FATHERS NAME : '+ i['fathernm'])
                print('SCHOOL NAME  : '+i['schoolnm'])
                print('CLASS        : '+i['class'])
                for j in i['rslt']:
                    v=int(j['mrks'][1])/int(j['mrks'][0])
                    if v>=0.33:
                        print(j['sub']+'--------'+j['mrks'][1]+'/'+j['mrks'][0]+'--------PASS')
                    else:
                        print(j['sub'] + '--------' + j['mrks'][1] + '/' + j['mrks'][0] + '--------FAIL')




    if a==3:
        c=input('enter student roll number ')
        for i in l:
            if (i['rolnm']==c):
                j=0
                while (j==0):
                   d=input('enter subject:')
                   e=input('enter total marks,obtained marks:')
                   marks={'sub':d,'mrks':e.split(',')}
                   i['rslt'].append(marks)
                   f=input('press y to add more subjects or press n:')
                   if f=='n':
                       j+=1



    if a==4:
        k=input('enter student roll number to delete its data: ')
        for i in l:
            if (i['rolnm']==k):
                l.remove(i)


    if a==5:
        break