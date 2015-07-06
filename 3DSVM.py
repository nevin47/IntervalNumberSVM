# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(111)
ax = fig.gca(projection='3d')
ax.set_aspect("equal")

def CreatCube(ax,StartPoint = [0,0,0], EndPoint = [1,1,1],Color = 'b'):
    Point1 = StartPoint
    Point2 = [EndPoint[0],StartPoint[1],StartPoint[2]]
    Point3 = [EndPoint[0],EndPoint[1],StartPoint[2]]
    Point4 = [StartPoint[0],EndPoint[1],StartPoint[2]]
    Point5 = [StartPoint[0],EndPoint[1],EndPoint[2]]
    Point6 = [StartPoint[0],StartPoint[1],EndPoint[2]]
    Point7 = [EndPoint[0],StartPoint[1],EndPoint[2]]
    Point8 = EndPoint
    ax.plot3D(*zip(Point1,Point4), color=Color)
    ax.plot3D(*zip(Point1,Point2), color=Color)
    ax.plot3D(*zip(Point1,Point6), color=Color)
    ax.plot3D(*zip(Point7,Point8), color=Color)
    ax.plot3D(*zip(Point7,Point6), color=Color)
    ax.plot3D(*zip(Point7,Point2), color=Color)
    ax.plot3D(*zip(Point5,Point4), color=Color)
    ax.plot3D(*zip(Point5,Point6), color=Color)
    ax.plot3D(*zip(Point5,Point8), color=Color)
    ax.plot3D(*zip(Point3,Point2), color=Color)
    ax.plot3D(*zip(Point3,Point4), color=Color)
    ax.plot3D(*zip(Point3,Point8), color=Color)
    return 0

CreatCube(ax,[0,0,0],[1,1,2],'b')
CreatCube(ax,[2,2,2],[3,3,5],'b')
CreatCube(ax,[5,5,2],[7,7,5],'b')
CreatCube(ax,[3,4,1],[6,8,-1],'b')
CreatCube(ax,[7,6,5],[9,7,3],'b')
CreatCube(ax,[1,2,-4],[3,2,1],'b')
CreatCube(ax,[5,3,-4],[8,5,-5],'b')


CreatCube(ax,[12,8,2],[13,7,3],'r')
CreatCube(ax,[15,12,2],[13,13,4],'r')
CreatCube(ax,[16,11,3],[14,12,4],'r')
CreatCube(ax,[15,10,3],[12,11,4],'r')
CreatCube(ax,[17,10,5],[19,12,6],'r')
CreatCube(ax,[17,10,5],[19,12,6],'r')
CreatCube(ax,[17,10,5],[19,12,6],'r')
CreatCube(ax,[17,10,5],[19,12,6],'r')
#draw Plane
point1  = np.array([10,-5,17])
normal1 = np.array([1,1,1])

# a plane is a*x+b*y+c*z+d=0
# [a,b,c] is the normal. Thus, we have to calculate
# d and we're set
d1 = -np.sum(point1*normal1)# dot product


# create x,y
xx, yy = np.meshgrid(range(15), range(15))

# calculate corresponding z
z1 = (-normal1[0]*xx - normal1[1]*yy - d1)*1./normal1[2]


# plot the surface
ax.plot_surface(xx,yy,z1, color='w')




plt.show()