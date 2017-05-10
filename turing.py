import re
fr=open('rules.txt','r')
rules=fr.readlines()
regular='^(.)q(\d+)->(.)(q(\d+)|STOP)(.*)$'
fi=open('input.txt','r')
string=fi.readline()
c=string[1]
conf=string[3:]
nrules=[]
for rule in rules:
    rule=re.match(regular, rule).groups()
    nrules.append(rule)
conf=list(conf)
conf.append('B')
position=0
f=0
while 1:
    for i in range(len(nrules)):
        if (nrules[i][0]==conf[position]) and (nrules[i][1]==c):
            conf[position]=nrules[i][2]
            if nrules[i][3]!='STOP':
                c=nrules[i][4]
            if nrules[i][5]=='L':
                if position==0:
                    conf.insert(0,'B')
                else:
                    position-=1
            if nrules[i][5]=='R':
                position+=1
            if nrules[i][3]=='STOP':
                for elem in conf:
                    if elem!='B':
                        print(elem,end='')
                f=1
    if f==1:
        break