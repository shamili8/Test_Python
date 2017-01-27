# f1 = open('transactions4.txt','w')
# #writing into files
# f1.write('"1","Shamili","5000"\n')
# f1.write('"2","Shamu","6000"\n')
# f1.write('"3","shalini","3000"\n')
# f1.write('"4","Prathista","1000"\n')
# f1.write('"5","Shreshta","7000"\n')
# f1.write('"6","Anoop","2000"\n')
f2 = open('reverseData.txt','w')
with open('transactions4.txt', 'r') as f:
    lines = f.readlines()
    lines.reverse()
    for line in lines:
        f2.write(line)

f2.close()