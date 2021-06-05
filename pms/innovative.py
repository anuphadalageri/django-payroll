import matplotlib.pyplot as plt

#plt.scatter([1,2,3,4,5,6],[2,4,6,8,10,14])
#plt.axis([0,6,1,12])
x= ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec']
y= [1,3,5,0,2,2,4,6,0,0,1,3]
plt.subplot(131)
plt.bar(x,y)
plt.subplot(132)
#plt.figure()
plt.plot(x,y)
plt.title('Leaves per month')
plt.xlabel('Months')
plt.ylabel('Leaves')
plt.show()