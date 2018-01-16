#

import csv
import math 

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
    
    #creation de la matrice de synchronisation (chemin optimal)
    for i in range(len(ref)):
        ligne=[]
        for j in range(len(traj)):
            ligne.append(-1)
        matrice_distance_total.append(ligne)
    
    chemin=[] #montre le point anterieur
    
    #on va parcourir les trajectoires en commençant par i=j=0
    for i in range(len(ref)):
        for j in range(len(traj)):

            if i==0 and j==0:
                matrice_distance_total[i][j] = distance(ref[i],traj[j])
                chemin.append([None,None])
                
            elif i==0:

                matrice_distance_total[i][j] = matrice_distance_total[i][j-1]+distance(ref[i],traj[j])
                
            elif j==0:
                matrice_distance_total[i][j] = matrice_distance_total[i-1][j]+distance(ref[i],traj[j])
                
            else:
                dist_min=
                matrice_distance_total[i][j] = distance(ref[i],traj[j])+min(matrice_distance_total[i-1][j],matrice_distance_total[i][j-1],matrice_distance_total[i-1][j-1])
                
    return matrice_distance_total[len(ref)-1][len(traj)-1]
    


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
    
    cout = dtw(traj1,traj2)
    print(cout)
            

main()