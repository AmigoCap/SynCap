#

import csv
import math 
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

def distance(a,b):
    '''
    Calcule la distance entre deux points a et b de coordonnés (x,y)
    '''
    dist=0
    for i in range(len(a)):
        dist+=(a[i]-b[i])**2
    return(math.sqrt(dist))
    

def dtw(ref,traj):
    '''
    Reçoit les deux trajectoires à synchroniser et retourne la matrice
    '''
    matrice_distance_total = []
    sequence_point = []
    
    
    #creation de la matrice de synchronisation (chemin optimal)
    for i in range(len(ref)):
        ligne=[]
        seq_ligne=[]
        for j in range(len(traj)):
            ligne.append(-1)
            seq_ligne.append([None,None])
        matrice_distance_total.append(ligne)
        sequence_point.append(seq_ligne)
    
    
    #on va parcourir les trajectoires en commençant par i=j=0
    for i in range(len(ref)):
        for j in range(len(traj)):

            if i==0 and j==0:
                matrice_distance_total[i][j] = distance(ref[i],traj[j])
                sequence_point[i][j]=[0,0]
                
            elif i==0:

                matrice_distance_total[i][j] = matrice_distance_total[i][j-1]+distance(ref[i],traj[j])
                sequence_point[i][j]=[i,j-1]

                
            elif j==0:
                matrice_distance_total[i][j] = matrice_distance_total[i-1][j]+distance(ref[i],traj[j])
                sequence_point[i][j]=[i-1,j]
            else:
                dist_min=matrice_distance_total[i-1][j]
                sequence_point[i][j]=[i-1,j]
                if dist_min>matrice_distance_total[i][j-1]:
                    dist_min=matrice_distance_total[i][j-1]
                    sequence_point[i][j]=[i,j-1]
                if dist_min>matrice_distance_total[i-1][j-1]:
                    dist_min=matrice_distance_total[i-1][j-1]
                    sequence_point[i][j]=[i-1,j-1]
                matrice_distance_total[i][j] = distance(ref[i],traj[j])+dist_min
               
    
    chemin=recup_chemin(sequence_point)
    
    #verification des conditions aux limites
    print('Les conditions aux limites sont vérifiées : ',verif_limites(chemin,len(ref),len(traj)))
    
    return matrice_distance_total[len(ref)-1][len(traj)-1], chemin, matrice_distance_total

    

def recup_chemin(matrix):
    '''
    Reçoit une liste avec les coordonnées du point précedent et renvoye la matrice d'alignement
    '''
    l=len(matrix) #nombre de lignes
    c=len(matrix[0]) #nombre de colonnes
    alignement=[]
    i=l-1
    j=c-1
    alignement.append([i,j]) #condition aux limites - les derniers points sont synchronisés    
    while (i!=0 or j!=0) and ((i,j)!=(0,0)):
        alignement.append(matrix[i][j])
        i_ant=matrix[i][j][0]
        j_ant=matrix[i][j][1]
        i=i_ant
        j=j_ant
        
        
    alignement.reverse()
    
    return alignement

def verif_limites(P,l,c):
    verif=True
    
    #condition de frontière
    if P[0]!=[0,0] or P[len(P)-1]!=[l-1,c-1]:
        return False
    
    
    #condition de continuité
    for i in range(1,len(P)):
        if (P[i][0]-P[i-1][0])<0 or (P[i][0]-P[i-1][0])>1 or (P[i][1]-P[i-1][1])<0 or (P[i][1]-P[i-1][1])>1:
            return False
        
        
    
    #condition de monotonicité
    for i in range(1,len(P)):
        if P[i][0]<P[i-1][0] or P[i][1]<P[i-1][1]:
            return False
    
    return True

def numerical_grid(P):
    l=P[-1][0]+1
    c=P[-1][1]+1
    grid=[]
    for i in range(l):
        ligne=[]
        for j in range(c):
            ligne.append(0)
        grid.append(ligne)
    
    for i in P:
        grid[i[0]][i[1]]=1
        
    return grid
    
        
    
        
                
    
def draw_grid(Pgrid):
    
    matrix=numpy.matrix(Pgrid)

    my_cmap = matplotlib.colors.ListedColormap(['k','w'])
    
    fig = plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_aspect(20)
    
    #ax.grid(color='k',linestyle='-',linewidth=2)
    
    plt.imshow(matrix,interpolation='none',cmap=my_cmap)
    plt.show
        
    
def main():
    
    #import la trajectoire de réference
    with open ("ref.csv","r") as csvfile:
        traj1_file=csv.reader(csvfile)
        traj1=[]
        for row in traj1_file:
            x=float(row[0])
            y=float(row[1])
            traj1.append([x,y])
            
    #import la trajectoire aleatoire 
    with open ("essai1.csv","r") as csvfile:
        traj2_file=csv.reader(csvfile)
        traj2=[]
        for row in traj2_file:
            x=float(row[0])
            y=float(row[1])
            traj2.append([x,y])
    
    cout,P,distances = dtw(traj1,traj2)
    Pgrid=numerical_grid(P)
    draw_grid(Pgrid)
    print('J =',cout)
    
    
main()

