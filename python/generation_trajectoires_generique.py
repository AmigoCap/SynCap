'''
Génération de trajectoires aléatoires et de réference
'''

import csv
import math
import random
import matplotlib.pyplot as plt

def fonction_ref(k,N):
    '''
    Cette fonction reçoit le choix de fonction à appliquer pour modéliser la trajectoire ainsi que la valeur
    de x pour réaliser le calcul
    A changer selon la trajectoire souhaité
    '''
    #return math.sin(k/N*math.pi*3)*10
    return rectangle(50,100,k,N)
    #on veut dessiner un rectangle 

def fonction_aleat(k,N,axe,brt):
    f = fonction_ref(k,N)
    al = aleatoire(axe)
    b = bruit(brt,len(axe))
    if type(f)==list:
        point=[]
        for i in range(len(axe)):
            point.append(f[i]+al[i]+b[i])
    else:
        point=f+al[0]+b
    return point
    

def traj_reference(N):
    '''
    Cette fonction reçoit la taille du vecteur souhaité pour la trajectoire de réference et retourne 
    une liste avec les valeurs générées
    '''
    y = [] #création d'une liste vide pour la trajectoire
    
    for i in range(N):
        y.append(fonction_ref(i,N))
   
    return y
    
def traj_aleatoire(N,brt,axes):
    '''
    Cette fonction reçoit la taille du vecteur souhaité pour la trajectoire aléatoire et retourne 
    une liste avec les valeurs générées
    '''
    y = [] #création d'une liste vide pour la trajectoire

    
    for i in range(N):
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
            aleat.append (random.uniform(-1, 1))
        elif i=="y":
            aleat.append (random.uniform(-1, 1))
        elif i=="z":
            aleat.append (random.uniform(-5, 5))
        else : 
            aleat.append(0)
    return(aleat)

def bruit(choix,dim):
    if not choix:
        if dim==2: 
            return [0,0]
        else:
            return 0            
    else:
        if dim==2: 
            return [1,1]
        else:
            return 0  

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
    if type(traj[0])!=list:
        x=traj
        y=list(range(0,len(traj)))
    elif len(traj[0])==2:
        x=[]
        y=[]
        for i in traj:
            x.append(i[0])
            y.append(i[1])
    plt.scatter(y,x)
            


def main():  
    axes=["x","y"]
    ref=traj_reference(200)
    print(ref)
    alt=traj_aleatoire(100,False,axes)
    graphique(ref)
    graphique(alt)
    export("ref",ref)
    export("alt",alt)



main()