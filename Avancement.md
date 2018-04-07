# Point d'avancement
Description des tâches réalisés

# 13 Février 2018
* Création d'un code python plus générique pour la génération de trajectoires avec la possibilité d'ajouter un bruit gaussien ou impulsif.
* Recherche d'une méthode plus adaptée pour notre projet. Le DTW n'est pas utilisable pour des données multimodals. Le GTW se montre le meilleur choix jusqu'à ce moment, mais on continue à analyser les options disponibles.
* L'ajout des lignes de recalage entre les points synchronisés des trajectoires pour pouvoir mieux visualiser et analyser la synchronisation.

# 19 décembre 2017
* Géneration des données de trajectoire pour pouvoir les analyser ([code python]() et [fichier txt]())
* Comparaison des trajectoires générées avec la trajectoire théorique (distance euclidienne) (voir rapport_partiel)

# 5 décembre 2017 
* Capture du mouvement d'un stylo qui dessine un carré 
* Exportation des données du [MoCap](https://github.com/AmigoCap/SynCap/blob/master/donnees/carre/MoCap_Carre.csv) et du [Accéléromètre](https://github.com/AmigoCap/SynCap/blob/master/donnees/carre/Accelerometre_Carre.csv)

# 21 novembre 2017
* Création du [tutoriel des accéléromètres](https://github.com/AmigoCap/SynCap/blob/master/Tutoriel_accelerometres.md) (calibration et usage) 

# 14 novembre 2017
* Calibration d'un accéléromètre pour première capture ([tutoriel Youtube](https://www.youtube.com/watch?v=aI2WDecTtfs))
* Capture du mouvement d'un stylo qui dessine un cercle ([méthodologie](https://github.com/AmigoCap/SynCap/blob/master/Methodologie.md))
* Exportation des données du [MoCap](https://github.com/AmigoCap/SynCap/blob/master/donnees/cercle/MoCap_cercle_1411.csv) et du [Accéléromète](https://github.com/AmigoCap/SynCap/blob/master/donnees/cercle/CercleStylo_Session1_PAr146_1_Calibrated_SD.csv)

# 24 octobre 2017
**Fait**
* Installation du logiciel *Consensys* (pour pouvoir utiliser les accéléromètres)
* Création du dossier sur GitHub
* Capture d'un mouvement avec MoCap et Accéléromètres
  * Nous avons réalisé la capture des pieds lorsqu'on marche. L'accéléromètre 3 correspond au pied droit et l'acc 6 correspond au pied gauche. 
  * Nous avons exporté les données des accéléromètres, mais il faut encore exporter ceux du MoCap.

**A faire**
* Tutoriel d'utilisation des Accéléromètres (cf. tutoriel MoCap)
* Récuperer les données du MoCap (avant vendredi 27 oct)
