import numpy as np
import os
from PIL import Image


tsne_plot=np.load('tsne_plot.npy')
colors=(np.load('colors.npy')*255)
colors=colors.astype('int')
labels=np.load('labels.npy')
print('labels',labels.shape,labels)
print(labels[0])
c1,c2,c3,_=colors[labels[0]]
print(c1)
unique_labels = set(labels)

print(np.max(tsne_plot[:,0]))
print(np.min(tsne_plot[:,0]))
print(np.max(tsne_plot[:,1]))
print(np.min(tsne_plot[:,1])) 
print(colors)

print('\n')
# for i in range(3000):
#     print('p'+str(i),end=',') 
# print('\n')

v=150
for i in range(10):
    for j in range(v):
        c1,c2,c3,_=colors[labels[i*v+j]]
        print('p'+str(i*v+j)+' = new vertice(sc*'+str(55.5+tsne_plot[i*v+j,0])+',sc*'+str(110.5-55-tsne_plot[i*v+j,1])+','+str(i*v+j+12000)+', ['+str(c1)+','+str(c2)+','+str(c3)+'])',end=';') 

print('\n')
# for i in range(3000):
#     print('p'+str(i)+'.draw()',end=';') 

print('\n')

# print('\n')
# for i in range(3000):
#     print('p'+str(i)+'.clicked(mouseX, mouseY)',end=';') 

print('\n')

# p1.clicked(mouseX, mouseY)
#     p2.clicked(mouseX, mouseY)
