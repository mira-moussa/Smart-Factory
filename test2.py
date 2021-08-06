

from Trajectory1 import traj
import numpy as np
#from matplotlib import pyplot as plt

# This function is for inverse kinematics
#Problem in theta3 (error around 0.6)

def ik (pose):
    x=pose[0]
    y=pose[1]
    z=pose[2]
    l1=8.4
    l2=8.8
    l3=9.2
    r=np.sqrt(x*x+y*y)

    # theta2= np.arctan2((z-l1),r)+np.arctan2(N,V)
    # theta3= -np.arctan2(N,(P-V))-np.arctan2(N,V)
    P = np.sqrt((z-l1)*(z-l1)+ r*r)
    V = (l3*l3 - l2*l2 - P*P) / (-2 * P)
    N=np.sqrt(l2*l2-V*V)


    theta1= np.arctan2(y,x)
    theta2= np.arctan2((z-l1),r)+np.arctan2(N,V)
    theta3= -np.arctan2(N,(P-V))-np.arctan2(N,V)
    Solved_joints=[theta1, theta2,-theta3]
    return Solved_joints




#this function is for forward kinematics
def fk(theta,alpha,a,d):
    x=np.cos(theta[0])*(a[2]*np.cos(theta[1]+theta[2])+a[1]*np.cos(theta[1]))
    y=np.sin(theta[0])*(a[2]*np.cos(theta[1]+theta[2])+a[1]*np.cos(theta[1]))
    z=a[2]*np.sin(theta[1]+theta[2])+a[1]*np.sin(theta[1])+d[0]
    P=[x,y,z]
    return P

# main code


#theta0=ik (79.0808,136.972,90.4851)
[x,y,z]=fk([0,0,0],[90, 0, 0],[0, 98, 92],[46, 0, 0])
theta0=ik([-14.612,4.384,9.125])
#print([x,y,z])
print(np.rad2deg(theta0))
thetaf=ik([12.195,5.144,17.989])
[x,y,z]=fk(thetaf,[90, 0, 0],[0, 98, 92],[46, 0, 0])

#print([x,y,z])
#print(np.rad2deg(thetaf))
#-15.871718237173141, 31.667258769260926, 87.02603405075686
t=1
N=10
[position,speed,acc]=traj(np.rad2deg(theta0),np.rad2deg(thetaf),t,10)

print(position)
print(speed)
print(acc)

#plt.show()