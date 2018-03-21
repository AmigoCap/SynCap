"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""
from matplotlib import pyplot as plt
from matplotlib import animation
import csv
import math 
import matplotlib as mtp
import numpy as np
'''Méthode DTW avec recalage des trajectoires générées.'''



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
    l=P[-1][1]+1
    c=P[-1][0]+1
    grid=[]
    for i in range(l):
        ligne=[]
        for j in range(c):
            ligne.append(0)
        grid.append(ligne)
    
    for i in P:
        grid[i[1]][i[0]]=1
        
    return grid
    
        
    
        
                
    
def draw_grid(Pgrid):
    
    matrix=np.matrix(Pgrid)

    my_cmap = mtp.colors.ListedColormap(['k','w'])
    
    fig = plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_aspect(20)
    ax.xaxis.tick_top()
    
    #ax.grid(color='k',linestyle='-',linewidth=2)
    
    plt.imshow(matrix,interpolation='none',cmap=my_cmap)
    plt.show
    
def draw_traj_rec(traj1,traj2,P):
    '''
    Affichage du recalage des trajectoires
    '''
    
    
    xt1=[]; 
    yt1=[];
    xt2=[];
    yt2=[];
    
    for i in range(len(traj1)):
        xt1.append(0);
        yt1.append(0);
    
    for i in range(len(traj2)):
        xt2.append(0);
        yt2.append(0);
        
    #Affichage trajectoire en bleu
    plt.figure()
    for i in range(len(traj1)):
        xt1[i],yt1[i]=(traj1[i]);
    plt.plot(xt1,yt1,'bo')
                
    
    #Affichage trajectoire 2 en rouge
    for i in range(len(traj2)):
        xt2[i],yt2[i]=traj2[i]
    plt.plot(xt2,yt2,'ro-')
            
    #Recalage des points en noir
    for i in range(len(P)):
          i1,i2=P[i]
          x1,y1 = traj1[i1]
          x2,y2 = traj2[i2]
          plt.plot([x1,x2],[y1,y2],'k-')
          i=i+1;   
    
    plt.show

#Déclaration des trajectoires pour affichage           
traj11 = []
traj21 = []
traj1x = []
traj2x = []
traj12 = []
traj22 = []
traj1y = []
traj2y = []
    
def main():
    
    #import la trajectoire de réference
    with open ("ref.csv","r") as csvfile:
        traj1_file=csv.reader(csvfile)
        traj1=[]
        for row in traj1_file:
            x=float(row[0])
            y=float(row[1])
            traj1.append([x,y])
            #Separation partie x et y des coodonées pour la premiere trajectoire
            traj1x.append(x)
            traj1y.append(y)
            
    #import la trajectoire aleatoire 
    with open ("alt.csv","r") as csvfile:
        traj2_file=csv.reader(csvfile)
        traj2=[]
        for row in traj2_file:
            x=float(row[0])
            y=float(row[1])
            traj2.append([x,y])
            #Separation partie x et y des coodonées pour la deuxième trajectoire
            traj2x.append(x)
            traj2y.append(y)
    
    cout,P,distances = dtw(traj1,traj2)
    Pgrid=numerical_grid(P)
    draw_grid(Pgrid)
    print('J =',cout)
    draw_traj_rec(traj1,traj2,P)
    
    for i in range(len(P)):
        x = P[i]
        traj11.append(traj1x[x[0]])
        traj21.append(traj2x[x[1]])
        traj12.append(traj1y[x[0]])
        traj22.append(traj2y[x[1]])    
    
main()

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()   
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.set_xlim(0,50)
ax1.set_ylim(min(traj21)-5, max(traj21)+5)
line, = ax1.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init1():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate11(i):
    x = np.linspace(0, len(traj11)-1, len(traj11));
    y = traj11;
    oi = traj11[0];
    traj11.remove(oi);
    traj11.append(oi);
    line.set_data(x, y);
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate11, init_func=init1,frames=200, interval=20, blit=False)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('DTW.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()

ax3.set_xlim(0,50)
ax3.set_ylim(min(traj21)-5, max(traj21)+5)
line2, = ax3.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init2():
    line2.set_data([], [])
    return line2,
            
# animation function.  This is called sequentially
def animate21(i):
    x = np.linspace(0, len(traj21)-1, len(traj21));
    y = traj21;
    oi = traj21[0];
    traj21.remove(oi);
    traj21.append(oi);
    line2.set_data(x, y);
    return line2,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim2 = animation.FuncAnimation(fig, animate21, init_func=init2,frames=200, interval=20, blit=False)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim2.save('DTW.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()

ax2.set_xlim(0,50)
ax2.set_ylim(min(traj22)-5, max(traj22)+5)
line3, = ax2.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init3():
    line3.set_data([], [])
    return line3,
            
# animation function.  This is called sequentially
def animate12(i):
    x = np.linspace(0, len(traj12)-1, len(traj12));
    y = traj12;
    oi = traj12[0];
    traj12.remove(oi);
    traj12.append(oi);
    line3.set_data(x, y);
    return line3,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim3 = animation.FuncAnimation(fig, animate12, init_func=init3,frames=200, interval=20, blit=False)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim3.save('DTW.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()

ax4.set_xlim(0,50)
ax4.set_ylim(min(traj22)-5, max(traj22)+5)
line4, = ax4.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init4():
    line4.set_data([], [])
    return line4,


            
# animation function.  This is called sequentially
def animate22(i):
    x = np.linspace(0, len(traj22)-1, len(traj22));
    y = traj22;
    oi = traj22[0];
    traj22.remove(oi);
    traj22.append(oi);
    line4.set_data(x, y);
    return line4,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim4 = animation.FuncAnimation(fig, animate22, init_func=init4,frames=200, interval=20, blit=False)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
fig.savefig('DTW.png', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()