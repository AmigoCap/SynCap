'''
Génération de trajectoires aléatoires et de réference
'''
import csv
import math
import random
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


def fonction_ref(k,N):
    '''
    Cette fonction reçoit le choix de fonction à appliquer pour modéliser la trajectoire ainsi que la valeur
    de x pour réaliser le calcul
    A changer selon la trajectoire souhaité
    '''
    #return rectangle(50,100,k,N) #on veut dessiner un rectangle 
    #return ([k**5 - k**3/2-3,2*np.pi*k**2,10]) #pour simuler une traj polynomiale du mocap
    return ([20*k**2-3*(k), 3*2*2*np.pi,-9.81]) #pour simuler un accelerometre correspondant à la traj mocap ci-dessus


def fonction_aleat(k,N,axe,brt):
    f = fonction_ref(k,N)
    al = aleatoire(axe)
    b = bruit(brt,len(axe))
    if type(f)==list:
        point=[]
        for i in range(len(axe)):
            point.append(f[i]+al[i]+b[i])
    else:
        point=f+al[0]+b[0]
    return point
    

def traj_reference(N):
    '''
    Cette fonction reçoit la taille du vecteur souhaité pour la trajectoire de réference et retourne 
    une liste avec les valeurs générées
    '''
    y = [] #création d'une liste vide pour la trajectoire
    t = np.linspace(0,1,N)
    for i in t:
        y.append(fonction_ref(i,N))
   
    return y
    
def traj_aleatoire(N,brt,axes):
    '''
    Cette fonction reçoit la taille du vecteur souhaité pour la trajectoire aléatoire et retourne 
    une liste avec les valeurs générées
    '''
    y = [] #création d'une liste vide pour la trajectoire
    
    t = np.linspace(0,1,N)
    
    for i in t:
        y.append(fonction_aleat(i,N,axes,brt))
    return(y)    

def aleatoire(axe):
    '''
    Cette fonction retourne une valeur aleatoire à ajouter sur la trajectoire 
    Changer le return selon votre besoin
    '''
    aleat=[]
    for i in axe:
        if i=="x":
            #aleat.append(np.random.normal(0.0003863,0.0002474)) #mocap
            aleat.append(np.random.normal(-0.06,0.02))
        elif i=="y":
            #aleat.append(np.random.normal(0.0003863,0.0002474)) #mocap
            aleat.append(np.random.normal(-0.08,0.02))
        elif i=="z":
            #aleat.append(np.random.normal(0.0003863,0.0002474)) #mocap
            aleat.append(np.random.normal(0.03,0.03))
        else : 
            aleat.append(0)
    return(aleat)

def bruit(choix,dim):
    bruit_dim=[]
    if not choix:
        for i in range(dim):
            bruit_dim.append(0)
        return (bruit_dim)
    else:
        if dim==2: 
            '''
            Bruit Gaussien
            '''
            sigma = 3.0;
            U1 = random.random();
            U2 = random.random();
            b1 = sigma*math.sqrt(-2*math.log(U1))*math.cos(2*math.pi*U2) ;
            
            U1 = random.random();
            U2 = random.random();
            b2 = sigma*math.sqrt(-2*math.log(U1))*math.cos(2*math.pi*U2) ;
            return [b1,b2];
            
            '''
            Bruit Impulsif
            '''            
#            prob = random.randint(1,100);
#            if prob>90:
#                nmax = random.randint(30,50);
#                nmin = random.randint(-50,-30);
#                return [int(random.randint(nmin,nmax)),int(random.randint(nmin,nmax))];
#            else:
#                return [0,0];
#        else:
#            return 0;

def export(nom,trajectoire):
    '''
    Cette fonction reçoit le nom du fichier à exporter et la liste qui contient la trajectoire    
    OBS : il faut fournir un str sans l'extension à la fin
    '''
    title=nom+".csv"
    with open(title,"w",newline="") as f:  
        writer=csv.writer(f,delimiter=',')
        for i in trajectoire:
            writer.writerow(i)
    
def rectangle(l,h,k,n):
    '''
    l : longueur du rectangle
    h : hauteur du rectangle
    n : nb total de points à réaliser sur le carré
    k : nb du échantillon
    '''
    pas = (2*h+2*l)/n
    if k>=0:
        if k*pas<h:
            x=0
            y=k*pas
        elif k*pas<(h+l):
            x=k*pas-h
            y=h
        elif k*pas<(2*h+l):
            x=l
            y=h-(k*pas-h-l)
        elif k<n:
            x=l-((k*pas-2*h-l))
            y=0
    return([x,y])
            
def graphique(traj):
    '''
    Affichage Graphique d'une trajectoire
    '''
    if type(traj[0])!=list:
        x=traj
        y=list(range(0,len(traj)))
        plt.scatter(x,y)

    elif len(traj[0])==2:
        x=[]
        y=[]
        for i in traj:
            x.append(i[0])
            y.append(i[1])
        plt.scatter(x,y)
    elif len(traj[0])==3:
        x=[]
        y=[]
        z=[]
        for i in traj:
            x.append(i[0])
            y.append(i[1])
            z.append(i[2])
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        ax.scatter3D(x, y, z, cmap='Greens')
        


def main():  
    dim=3
    axes=["x","y","z"]
    ref=traj_reference(200)
    bruit=False;
    print(ref)
    alt=traj_aleatoire(200,bruit,axes)
    graphique(ref)
    graphique(alt)
    #export("ref",ref)
    export("Accelerometer_3D_polynomial_200",alt)



main()