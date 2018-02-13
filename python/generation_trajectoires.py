import csv
import math
import random
import matplotlib.pyplot as plt

def main():
    sumEucCar = 0
    
    # Dimensions de references
    a = 24
    b = 40
    
    c = 12
    d = 20
    
    time =list(range(1,2*a+2*b-3))
    time2 =list(range(1,2*c+2*d-3))
    
    #f,(a1)=plt.subplots(1,sharey= True)
    f,(a1,a2)=plt.subplots(1,2,sharey= True)
    
    # Creation du vecteur de reference
    tx = []
    ty = []
    
    for i in range(2*a+2*b-4):
        
        if i+1 <= a:
            tx.append(1)
            ty.append(i+1)
        
        elif i+1 <= a+b-1:
            tx.append(i-a+2)
            ty.append(a)
        
        elif i+1 <= 2*a+b-2:
            tx.append(b)
            ty.append(2*a+b-i-2)
            
        else:
            tx.append(2*b-i+2*a-3)
            ty.append(1)
    
    # Generation de la trajectoire de reference (rectangle 100 pour 200)
    a1.scatter(tx,ty)
    a2.scatter(time,tx)
    a2.scatter(time,ty)
    # Creation du vecteur aleatoire
    rntx = []
    rnty = []
    
    for i in range(2*c+2*d-4):
        
        if i+1 <= c:
            rntx.append(2*(1+random.uniform(-0.5, 0.5)))
            rnty.append(2*(i+1+random.uniform(-0.5, 0.5)))
                
        elif i+1 <= c+d-1:
            rntx.append(2*(i-c+2+random.uniform(-0.5, 0.5)))
            rnty.append(2*(c+random.uniform(-0.5, 0.5)))
        
        elif i+1 <= 2*c+d-2:
            rntx.append(2*(d+random.uniform(-0.5, 0.5)))
            rnty.append(2*(2*c+d-i-2+random.uniform(-0.5, 0.5)))
            
        else:
            rntx.append(2*(2*d-i+2*c-3+random.uniform(-0.5, 0.5)))
            rnty.append(2*(1+random.uniform(-0.5, 0.5)))
        
        sumEucCar = sumEucCar + (rntx[i]-tx[i])**2 + (rnty[i]-ty[i])**2
    
    # Generation de la trajectoire aleatoire (proche de la premiere)
    a1.scatter(rntx,rnty)
    a2.scatter(time2,rntx)
    a2.scatter(time2,rnty)
    
    sumEuc = math.sqrt(sumEucCar)
    
    print(sumEuc)
    
    moyDis = sumEuc/(2*a+2*b-4)
    
    print(moyDis)
    
    ref=coord_trajec(tx,ty)
    
    print(ref)
    
    
#    with open("ref.csv","w",newline="") as f:  
#        writer=csv.writer(f,delimiter=',')
#        for i in ref:
#            writer.writerow(i)
    
    export("ref",ref)
     
    
    with open("essai1.csv","w",newline="") as f:
        writer = csv.writer(f)
        for i in range(2*c+2*d-4):
            writer.writerow([(rntx[i])]+[(rnty[i])])
            
def coord_trajec(tx,ty):
    coord=[]
    for i in range (len(tx)):
        coord.append([tx[i],ty[i]])
    return coord

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

main()