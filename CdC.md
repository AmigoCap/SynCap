# Cahier de Charges

1. Prise en main des accéléromètres 
  * Livrable : tutoriel de calibration et utilisation des accéléromètres
2. Génération de données pour réaliser une prémière synchronisation 
  * Livrable : code Python et résultats graphiques
3. Synchronisation des données générées (définition des points d'intêret, taux d'erreur, corréction de bruit)
4. Comparaison de différents méthodes de synchronisation
5. Test de la robustesse
  * Livrable : code Python, analyse des données sous la forme d'un rapport
6. Synchronisation de données pour une trajectoire réellé (données réelles)
7. Création d'un vidéo avec les données d'une capture synchronisés 
  * Livrable : vidéo avec la capture et tutoriel de comment faire ce vidéo 

__________________________________________

Aujourd’hui, nous disposons de plusieurs méthodes d’enregistrement de mouvements et de trajectoires, et qui fournissent différents types d’information concernant ces trajectoires. Par exemple, les téléphones portables qui ont le GPS intégré et fournissent la position géographique de son utilisateur, les accéléromètres qui enregistrent l’accélération des mouvements, les gyroscopes qui fournissent les changements d’orientation, et encore plusieurs autres.  

Dans le cas de l’enregistrement d’une trajectoire en utilisant différents capteurs, un problème fondamental qui apparaît est relié à l’assimilation de ces différentes données. Qu’il soit les différentes dimensions des données (position dans l’espace, accélération selon les trois axes) ou même l’écart temporel qui provient des différentes fréquences de capture, une synchronisation de ces données est nécessaire. 

Nous nous intéressons finalement à la problématique de la synchronisation des données des différents capteurs : le motion capture (MoCap), l’accéléromètre et la caméra vidéo. Ce type d’étude a déjà été réalisé par Zhou et De la Torre [1], mais en s’intéressant à la synchronisation d’un même mouvement avec différentes capteurs réalisée par différents personnes. Pour cela, ils s’appuient sur différents méthodes de synchronisation, spatiale et temporelle, et explorent plus précisément le « Generalized Canonical Time Warping ».  

Pour notre projet, nous envisageons réaliser la synchronisation des données d’un mouvement simple capturé avec les différents capteurs. Pour cela, il est nécessaire une étude préalable des méthodes de synchronisation existants, qu’ils soient temporels, spatiaux ou le deux. 

Dans un premier instant, nous allons générer (à partir d’un code python), trajectoires « aléatoires » qui simulent l’enregistrement du mouvement par un capteur (avec des incertitudes, différentes fréquences, bruit). D’abord on s’intéresse à la comparaison d’une trajectoire dite « aléatoire » avec une trajectoire de référence pour pouvoir réaliser une première synchronisation en s’appuyant sur les différentes méthodes de la bibliographie (dynamic time warping [1], generalized canonical time warping [1], entre autres [2][3]). Nous cherchons trouver parmi les plusieurs méthodes celui qui peut nous servir à atteindre notre but avec l’erreur le plus petit. 

À partir de cette première analyse, nous pouvons nous intéresser alors à plusieurs trajectoires aléatoires qui proviennent d’une même trajectoire de référence avec segmentations distinctes (pour pouvoir simuler les données des capteurs).  En appliquant les méthodes qui semblent les plus pertinents (à partir de notre première analyse), nous souhaitons pouvoir choisir la méthode à appliquer pour la synchronisation des données qui provient d’une capture réelle. 

Avec l’étude préalable des méthodes de synchronisation, la capture d’un mouvement à la salle Amigo en utilisant le MoCap et les accéléromètres est nécessaire. Un tutoriel sur la calibration et l’utilisation des accéléromètres doit être fait. Les données acquises avec cette capture pourront être soumis aux méthodes de synchronisation étudiées avant. 

Ayant réussi la synchronisation des données, il pourrait encore nous intéresser la création d’un vidéo pour l’illustrer, avec les données de chaque capteur apparaissant sur l’écran (comme en [3]). Pour cela, il faut d’abord savoir réaliser ce vidéo dans le contexte où les données ne sont pas forcément synchronisés (un tutoriel est envisageable).
 



[1]	F. Zhou et F. D. la Torre, « Generalized Canonical Time Warping », IEEE Trans. Pattern Anal. Mach. Intell., vol. 38, no 2, p. 279‑294, févr. 2016.
[2]	S. Sankararaman, P. K. Agarwal, T. Mølhave, J. Pan, et A. P. Boedihardjo, « Model-driven Matching and Segmentation of Trajectories », in Proceedings of the 21st ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, New York, NY, USA, 2013, p. 234–243.
[3]	L. Fridman, D. E. Brown, W. Angell, I. Abdić, B. Reimer, et H. Y. Noh, « Automated synchronization of driving data using vibration and steering events », Pattern Recognit. Lett., vol. 75, no Supplement C, p. 9‑15, mai 2016.
