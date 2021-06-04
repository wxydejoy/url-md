f = open('main.txt')
lines = f.readlines()
f.close()
print(lines)
for i in range(len(lines)):
    #lines[i] = "![](" + lines[i].replace('\n','') + ')' + '\n'
    #lines[i] = "- ![" + lines[i].replace('\n','') + "](" + lines[i].replace('\n','') + ')' +'\n'
    lines[i] = "- " + lines[i].replace('\n','') +'\n'
f = open('main.txt','w')
f.writelines(lines)









