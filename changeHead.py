import os
import re


def changeEquall(StringTochange=''):
    elements = re.split(r': |\n', StringTochange)
    print(elements)
    newString = elements[0]+' = "'+elements[1]+'"'+'\n'
    return newString

targetDir = r'/Users/kushnee/kcn_hugo/content/post'
b = os.listdir(targetDir)
for index in range(0, len(b)):
    f = open(targetDir+'/'+b[index], 'r')
    now = f.readlines()
    f.close()
    if now[0] != '+++\n':
        now[0] = '+++\n' + now[0]
    for i in range(0, 5):
        if re.search('title', now[i]):
            if now[i].find(': '):
                if i != 0:
                    now[i] = changeEquall(now[i])
                    #print('current_now[{}]: {}'.format(i, now[i]))
                else:
                    elements = re.split(r': |\n', now[i])
                    #print(now[i])
                    now[i] = elements[0]+'\n'+elements[1]+' = "'+elements[2]+'"\n'
        elif re.search('date', now[i]):
            if now[i].find(': '):
                if i != 0:
                    #print('Find date')
                    now[i] = changeEquall(now[i])
                    #print('current_now[{}]: {}'.format(i, now[i]))
                else:
                    elements = re.split(r': |\n', now[i])
                    #print(now[i])
                    now[i] = elements[0]+'\n'+elements[1]+' = "'+elements[2]+':\n'
    with open(targetDir+'/'+b[index], 'w') as f2:
        f2.writelines(now)
print('All Done')
