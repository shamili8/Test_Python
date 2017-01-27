#open files
# f1 = open('transactions1.txt','w')
# f2 = open('transactions2.txt','w')
# #writing into files
# f1.write('"1","Shamili","5000"\n')
# f1.write('"2","Shamu","6000"\n')
# f1.write('"3","shalini","3000"\n')
# f1.write('"4","Prathista","1000"\n')
# f1.write('"5","Shreshta","7000"\n')
# f1.write('"6","Anoop","2000"\n')
#
# f2.write('"1","shanthi","2000"\n')
# f2.write('"2","Shamu","6000"\n')
# f2.write('"3","sravani","3000"\n')
# f2.write('"4","Prathista","1000"\n')
# f2.write('"5","pramela","2000"\n')
# f2.write('"6","lucky","5000"\n')
# f1 = open('transactions1.txt','r')
# f2 = open('transactions2.txt','r')
# f3 = open('transactions3.txt','w')
# for line1 in f1:
#     for line2 in f2:
#         if line1 == line2 :
#              f3.write("%s\n" %(line1))
# f3.close()
# f1.close()
# f2.close()

with open('transactions1.txt','r') as f1:
    with open('transactions2.txt', 'r') as f2:
        intersection = set(f1).intersection(f2)
        with open('transactions3.txt', 'w') as f3:
            for line in intersection:
                f3.write(line)
f3.close()


