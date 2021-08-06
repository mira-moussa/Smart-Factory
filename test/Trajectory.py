import numpy as np
from matplotlib import pyplot as plt


#This function is to get a0,a1,a2,a3 to form the cubic function
def func(theta0,thetaf,t):
    a0=theta0
    a1=0
    a2=(3/(t**2))*(thetaf-theta0)-(2/t)*0-(1/t)*0
    a3=-(2/(t**3))*(thetaf-theta0)-(1/(t**2))*0

    return a0,a1,a2,a3

#This function is to get the angles for one theta along the period
def position(a0,a1,a2,a3,t,N):
    dt=t/(N-1)
    theta_t=np.zeros(shape=(N,1))
    for i in range (0,N):
        t=dt*i

        #function of theta(t)
        theta_t_i=a0+a1*t+a2*(t**2)+a3*(t**3)

        #creating the column vector for positions
        theta_t[i][0]=theta_t_i
    return theta_t

#this function is to get the velocities for one theta along
# the desired period
def speed(a1,a2,a3,t,N):
    dt = t / (N - 1)
    theta_dot_t=np.zeros(shape=(N,1))
    for i in range(0, N):
        t = dt * i
        #function of theta dot(t)
        theta_dot_t_i = a1 + 2 * a2 * t + 3 * a3 * t ** 2

        # creating the column vector for speeds
        if theta_dot_t_i<0:
            theta_dot_t_i=theta_dot_t_i*-1

        theta_dot_t[i][0]=theta_dot_t_i
    return theta_dot_t

#this function is to get the accelerations for one theta along
# the desired period
def acceleration(a2,a3,t,N):

    dt = t / (N - 1)
    theta_2dot_t =np.zeros(shape=(N,1))
    for i in range(0, N, 1):
        t = dt * i

        #the function of theta double dot(t)
        theta_2dot_t_i =  2 * a2 + 6 * a3 * t

        # creating the column vector for accelerations
        theta_2dot_t[i][0]=theta_2dot_t_i*(np.pi/180)
    return theta_2dot_t

#This function is to get the angles, speeds and accelerations
# for the three thetas along the desired period
def traj (theta0,thetaf,t,N,figure):
    plt.figure(figure)
    #define variables
    profile_position=np.empty((N,1))
    profile_speed=np.empty((N,1))
    profile_acc=np.empty((N,1))
    dt = t / (N - 1)
    time=np.zeros(shape=(N,1))

    #Create time column vector for plotting
    for r in range (0,N):
        a=r*dt
        time[r][0]=a

    for i in range (3):
        [a0,a1,a2,a3]=func(theta0[i],thetaf[i],t)


    #positions and ploting
        theta1=position(a0,a1,a2,a3,t,N)

        #fig,(positions1, speeds1, acceleration1)=plt.subplots(3)
        plt.subplot(1, 4, 1)
        positions1=plt.plot(time,theta1)
        plt.title("Positions")
        plt.legend(["Θ1", "Θ2", "Θ3"])
        plt.xlabel("Time(s)")
        plt.ylabel("Position(Deg)")
    #speeds and plotting
        theta1_speed=speed(a1,a2,a3,t,N)
        theta1_speed=theta1_speed

        plt.subplot(1,4,2)
        speeds1=plt.plot(time, theta1_speed)
        plt.title("Speeds")
        plt.legend(["ω1", "ω2", "ω3"])
        plt.xlabel("Time(s)")
        plt.ylabel("Speed(rad/s)")


    #acceleration and plotting
        theta1_acc=acceleration(a2,a3,t,N)

        plt.subplot(1,4,3)
        acceleration1=plt.plot(time, theta1_acc)
        plt.title("Accelerations")
        plt.legend(["α1", "α2", "α3"])
        plt.xlabel("Time(s)")
        plt.ylabel("Acc(rad/s^2)")


        #concatenating all thetas in one matrix
        profile_position=np.hstack((profile_position,theta1))
        profile_speed = np.hstack((profile_speed, theta1_speed))
        profile_acc= np.hstack((profile_acc, theta1_acc))

#deleting the random numbers which created from the empty func.
    profile_speed=np.delete(profile_speed,0,1)
    profile_position=np.delete(profile_position,0,1)
    profile_acc=np.delete(profile_acc,0,1)

#returned positions1,speeds1, accelerations1 for plotting them in the main code
    return profile_position,profile_speed, profile_acc, positions1,speeds1,acceleration1

def ik (p):
    x = p[0]
    y = p[1]
    z = p[2]
    l1 = 8.4
    l2 = 8.8
    l3 = 9.2
    r = np.sqrt(x * x + y * y)

    P = np.sqrt((z - l1) * (z - l1) + r * r)
    V = (l3 * l3 - l2 * l2 - P * P) / (-2 * P)
    N = np.sqrt(l2 * l2 - V * V)

    theta1 = np.rad2deg(np.arctan2(y, x))
    theta2 = np.rad2deg(np.arctan2((z - l1), r) + np.arctan2(N, V))
    theta3 =np.rad2deg(-np.arctan2(N, (P - V)) - np.arctan2(N, V))
    if theta1<0 :
        theta1=theta1+360

    if theta2<0:
        theta2=theta2+360

    if theta3<0:
        theta3 = theta3 + 360

    Solved_joints = [theta1, theta2, theta3]
    return Solved_joints




#this function is for forward kinematics
def fk(theta,alpha,a,d):
    x=np.cos(theta[0])*(a[2]*np.cos(theta[1]+theta[2])+a[1]*np.cos(theta[1]))
    y=np.sin(theta[0])*(a[2]*np.cos(theta[1]+theta[2])+a[1]*np.cos(theta[1]))
    z=a[2]*np.sin(theta[1]+theta[2])+a[1]*np.sin(theta[1])+d[0]
    P=[x,y,z]
    return P
