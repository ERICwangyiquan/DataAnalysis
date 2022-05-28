from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt

#1
data = pd.read_csv("./T5DATA1.csv")
print(data)
print('-------------------------------------------------')

#2
cntm = data['Module'].nunique()
print(cntm, 'subjects are taught in this school.')
cntm_list = data['Module'].unique()
print('They are', cntm_list)
print('-------------------------------------------------')

#3
cnts = data['Student Name'].nunique()
print(cnts, 'students in the school.')
print('-------------------------------------------------')

#4
cntt = data['Teacher Name'].nunique()
print(cntt, 'teachers in the school.')
cntt_list = data['Teacher Name'].unique()
print('They are', cntt_list)
print('-------------------------------------------------')

#5  
avg_5 = data['sum'] = (data.iloc[:,5:10].sum(axis=1))/5     #rule: each term takes 20% in final grade
print("the average of student's grades is", avg_5.sum(axis=0)/cnts)
print(data['Student Name'][avg_5.idxmax()], 'achieved the highest grade')
print(data['Student Name'][avg_5.idxmin()], 'achieved the lowest grade')
print('-------------------------------------------------')

#6
print('teacher', data['Teacher Name'][avg_5.idxmax()],"is the best teacher in terms of students' grades.")
print('-------------------------------------------------')

#7
namedict = defaultdict(float)
cntdict1 = defaultdict(int)
for i in range(cnts):
    namedict[data['Teacher Name'][i]] += data['sum'][i]    
    cntdict1[data['Teacher Name'][i]] += 1
for name in cntdict1:
    namedict[name] /= cntdict1[name]     #devide by the time it occurs in total

gradelist1 = []
for name in namedict:
    gradelist1.append(namedict[name])
plt.subplot(2, 2, 1)            
plt.pie(gradelist1,     #each teacher's average grades (for all modules in their classes)
        labels=cntt_list,
        autopct='%.2f%%')
plt.title("each teacher's average grades")
plt.subplot(2, 2, 3)            
plt.bar(cntt_list, gradelist1)      #each teacher's average grades (for all modules in their classes)
plt.title("each teacher's average grades")

#8
moddict = defaultdict(float)
cntdict2 = defaultdict(int)
for i in range(cnts):
    moddict[data['Module'][i]] += data['sum'][i]
    cntdict2[data['Module'][i]] += 1
for name in cntdict2:
    moddict[name] /= cntdict2[name]

gradelist2 = []
for name in moddict:
    gradelist2.append(moddict[name])
plt.subplot(2, 2, 2)
plt.pie(gradelist2,     #average grade for each module. 
        labels=cntm_list,
        autopct='%.2f%%')
plt.title("each module's average grades")
plt.subplot(2, 2, 4)
plt.bar(cntm_list, gradelist2)      #average grade for each module. 
plt.title("each module's average grades")
plt.suptitle("Data analysis of T5DATA1.csv")
plt.tight_layout()
plt.show()