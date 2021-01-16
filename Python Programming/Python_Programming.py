import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from random import choice
#1st task
fail=open("dannie.txt","r")
mas1=[]
mas2=[]
for line in fail:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(int(line[n+1:len(line)].strip()))
fail.close()

title = "Data about IT safety"
plt.grid(True)

color_rectangle = np.random.rand(7, 3)
plt.barh(mas1, mas2, color=color_rectangle)

plt.show()
#2nd task
a=False
t=1
s=0
answer=""
#List of colours to be picked at random
colours=["BlueViolet","Brown","CadetBlue","Crimson","ForestGreen","Gold","Sienna","Violet","Black","RoyalBlue"]
#list of lines to be picked at random
lines=["dashed","dotted","solid","dashdot"]
#Glasses
x1_gl=np.arange(-9,0)
x2_gl=np.arange(1,10)
x3_gl=np.arange(-9,-5)
x4_gl=np.arange(6,10)
x5_gl=np.arange(-1,1.5,0.5)
glasses={"x1_gl":[(-1/16)*(x1_gl+5)**2+2,(1/4)*(x1_gl+5)**2-3],#two y's have the same x
         "x2_gl":[(-1/16)*(x2_gl-5)**2+2,(1/4)*(x2_gl-5)**2-3],#two y's have the same x
         "x3_gl":[-1*(x3_gl+7)**2+5],
         "x4_gl":[-1*((x4_gl-7)**2)+5],
         "x5_gl":[-0.5*x5_gl**2+1.5]}
#Boat
x1_b=np.arange(-3,1)
x2_b=[5,6,7,8,9,10,11]#this is y
x3_b=np.arange(-8,9)
x4_b=np.arange(-6,7)
x5_b=np.arange(-8,-5)
x6_b=np.arange(6,9)
x7_b=np.arange(-10,1)
x8_b=np.arange(0,11)
boat={"x1_b":[(-1/3)*x1_b**2+11,(1/3)*x1_b**2+5],#two y's have the same x
      "x2_b":[0]*len(x2_b),#this is x
      "x3_b":[[5]*len(x3_b)],
      "x4_b":[[3]*len(x4_b)],
      "x5_b":[-1*x5_b-3],
      "x6_b":[x6_b-3],
      "x7_b":[(-3/25)*(x7_b+5)**2+3],
      "x8_b":[(-3/25)*(-1*x8_b+5)**2+3]
      }
#Umbrella
x1_u=np.arange(-12,13,2)
x2_u=np.arange(-4,5,1)
x3_u=np.arange(-12,-3,2)
x4_u=np.arange(4,13,2)
x5_u=np.arange(-4,-0.2,0.1)
x6_u=np.arange(-4,0.1,0.1)
umbrella={"x1_u":[(-1/18)*x1_u**2+12],
          "x2_u":[(-1/8)*x2_u**2+6],
          "x3_u":[(-1/8)*(x3_u+8)**2+6],
          "x4_u":[(-1/8)*(x4_u-8)**2+6],
          "x5_u":[2*(x5_u+3)**2-9],
          "x6_u":[1.5*(x6_u+3)**2-10]
          }
#Butterfly
x1_f=np.arange(-9,0)
x2_f=np.arange(1,10)
x3_f=np.arange(-9,-7)
x4_f=np.arange(8,10)
x5_f=np.arange(-8,0)
x6_f=np.arange(1,9)
x7_f=np.arange(-8,-1)
x8_f=np.arange(2,9)
x9_f=np.arange(-2,0)
x10_f=np.arange(1,3)
x11_f=np.arange(-1,2)
x12_f=np.arange(-2,1)
x13_f=np.arange(0,3)
butterfly={"x1_f":[(-1/8)*(x1_f+9)**2+8],
           "x2_f":[(-1/8)*(x2_f-9)**2+8],
           "x3_f":[7*(x3_f+8)**2+1],
           "x4_f":[7*(x4_f-8)**2+1],
           "x5_f":[(1/49)*(x5_f+1)**2,(-4/49)*(x5_f+1)**2],#two y's have the same x
           "x6_f":[(1/49)*(x6_f-1)**2,(-4/49)*(x6_f-1)**2],#two y's have the same x
           "x7_f":[(1/3)*(x7_f+5)**2-7],
           "x8_f":[(1/3)*(x8_f-5)**2-7],
           "x9_f":[-2*(x9_f+1)**2-2],
           "x10_f":[-2*(x10_f-1)**2-2],
           "x11_f":[-4*x11_f**2+2,4*x11_f**2-6],#two y's have the same x
           "x12_f":[-1.5*x12_f+2],
           "x13_f":[1.5*x13_f+2]
           }
#Frog/Toad
x1_t=np.arange(-7,8)
x2_t=np.arange(-6.8,-1.9,0.1)
x3_t=np.arange(2,6.9,0.1)
x4_t=np.arange(-5.8,-2.9,0.2)
x5_t=np.arange(2.8,5.9,0.2)
x6_t=np.arange(-4,5)
x7_t=np.arange(-5.2,5.3,0.1)
x8_t=np.arange(-7,-2.56,0.01)#being more precise to make the upper feet connect
x9_t=np.arange(2.57,7.01,0.01)#being more precise to make the upper feet connect
x10_t=np.arange(-7,1)
x11_t=np.arange(0,8)
x12_t=np.arange(-7,-4.6,0.1)
x13_t=np.arange(4.5,7.1,0.5)
x14_t=np.arange(-3,4)
toad={"x1_t":[(-3/49)*x1_t**2+8,(4/49)*x1_t**2+1],#two y's have the same x
      "x2_t":[-0.75*(x2_t+4)**2+11],
      "x3_t":[-0.75*(x3_t-4)**2+11],
      "x4_t":[-1*(x4_t+4)**2+9],
      "x5_t":[-1*(x5_t-4)**2+9],
      "x6_t":[(4/9)*x6_t**2-5],
      "x7_t":[(4/9)*x7_t**2-9],
      "x8_t":[(-1/4)*(x8_t+3)**2-6],#different formula
      "x9_t":[(-1/4)*(x9_t-3)**2-6],#different formula
      "x10_t":[(1/9)*(x10_t+4)**2-11],
      "x11_t":[(1/9)*(x11_t-4)**2-11],
      "x12_t":[-1*(x12_t+5)**2],
      "x13_t":[-1*(x13_t-5)**2],
      "x14_t":[(2/9)*x14_t**2+2]
      }
pictures=[butterfly,umbrella,boat,glasses,toad]
for k in pictures:
    if s<4:
        s+=1
        plt.subplot(2,2,s)
    crng=choice(colours)
    lrng=choice(lines)
    for j in k:
        for i in k[j]:
            if j=="x2_b":#an exception for this specific x, I switched the values of x and y for them to work and here i switch tehm back
                y=x2_b
                x=boat[j]
            else:
                x=eval(j)
                y=i
            plt.plot(x,y,ls=f"{lrng}",c=f"{crng}",lw=3)#random colour and linestyle
            t+=1
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(axis="y",c="black",alpha=0.4,lw=1)
    plt.grid(axis="x",alpha=0)
    plt.xticks(np.arange(-15,16,5))
    if k==boat:#Doing this to make the boat look better, it looked a little squished before
        plt.yticks(np.arange(-9,16,3))
    else:
        plt.yticks(np.arange(-15,16,3))
    plt.grid(True)
    if s==4:
        plt.show()
