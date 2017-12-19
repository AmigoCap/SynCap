# Génération de deux trajectoires aléatoires

Nous nous intéressons à créer deux trajectoires pour simuler une capture réelle. D'abord, on s'intéresse à une trajectoire rectangulaire, de dimensions 100x200.
Il fallait ajouter à ces trajectoires un aspect plus aléatoire. À partir de la trajectoire théorique, nous avons réalisé une segmentation de chaque arête du rectangle.
A chaque point nous avons ajouté un *random* qui pouvait le faire varier vers la droite ou la gauche, vers l'arrière ou l'avant. 
Nous n'avos pas encore ajouté le bruit éventuel qui une trajectoire réelle peut avoir. 

# Comparaison entre les trajectoires

Nous nous intéressons à découvrir quelle trajectoire générée semble le plus à la trajectoire théorique. Pour cela, nous avons réalisé l'étude des distances euclidiennes entre les points réels et ceux générés. On cherche à savoir quelle trajectoire a la somme des distances euclidiennes la plus basse.
Il faut remarquer que ce type d'analyse est possible car on connaît bien le trajectoire étudiée. Dans un cas plus réel, où on dispose seulement des données de différentes captures, on peut pas définir exactement la trajectoire réelle. Dans ces cas plus complexes, la distance euclidienne ne sera pas pertinente. 

