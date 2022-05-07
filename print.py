import numpy as np
import os
from PIL import Image


tsne_plot=np.load('tsne_plot.npy')
print(tsne_plot.shape)
print(np.max(tsne_plot[:,0]))
print(np.min(tsne_plot[:,0]))
print(np.max(tsne_plot[:,1]))
print(np.min(tsne_plot[:,1])) 

print('\n')
for i in range(1000):
    print('p'+str(i),end=',') 
print('\n')

v=10
for i in range(100):
    for j in range(v):
        print('p'+str(i*v+j)+' = new vertice(sc*'+str(55.5+tsne_plot[i*v+j,0])+',sc*'+str(110.5-55-tsne_plot[i*v+j,1])+','+str(i*v+j+12000)+', [255, 0, 255])',end=';') 

print('\n')
for i in range(1000):
    print('p'+str(i)+'.draw()',end=';') 

print('\n')

print('\n')
for i in range(1000):
    print('p'+str(i)+'.clicked(mouseX, mouseY)',end=';') 

print('\n')

# p1.clicked(mouseX, mouseY)
#     p2.clicked(mouseX, mouseY)
