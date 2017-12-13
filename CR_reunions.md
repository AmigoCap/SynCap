# Compte-rendu
Compilation des compte-rendus des réunions

## Réunion du 13 décembre 2017
* Commencer par idéntifier un problème simple qu'on veut étudier (cf. article [Data Mining]()) comme la correspondance de trajectoires
* A partir d'un problème simple, générer des données pour pouvoir implémenter le code (voir les librairies nécessaires)
* Dans le cas du *carré* : à partir d'un carré théorique, générer tranjectoires aléatoires (à la main, en utilisant random ...) en réalisant une segmentation (trajectoire théorique -> segmentation -> génération de trajectoire aléatoire)
[x,y,t,id]
* Calcul des distances (quelle trajectoire est la plus proche de la théorique ?)
* Problème des différentes segmentations -> comment faire pour synchroniser les données et les rélier à la trajectoire initiale ?
* A faire : 
 * Définir des points d'intêret d'un modèle
 * Définir un indicateur de taux d'erreur
 * Corréction de bruit (comment faire pour enléver le bruit et le corriger)
 * ségmentation
 * réduire le taux d'erreur
* Problème possible : corriger le trajectoire pour qu'elle passe par une route possible
* Définir différentes méthodes de synchronisation et les comparer
* Tester aussi avec d'autres formes géométriques (tester la robustesse)

## Réunion du 7 novembre 2017
* Réaliser une première capture de mouvement :
  *  créer une méthodologie avant la capture
  * choisir un mouvement simple (stylo qui dessine un cercle)
  * visualiser les données brutes
* Ne pas faire un planning temporel : définir combien de captures de données différentes, ce qu'on prévoit faire pensant le projet
* Suivre la démarche : poser le problème -> capturer les données -> analyser les données -> poser un autre problème
* Réaliser une *méthodologie* pour réaliser les captures de mouvement et pour comparer avec la capture précendente
* À chaque nouvelle capture, ajouter un élement nouveau

### RVP1
* Réflechir sur les problématiques de comparaison du mouvement
* Expliquer les différents capteurs, expliciter les capteurs qui nous sont intéressants
* Expliquer le contexte (pourquoi c'est important)
* Présenter une première capture d'un mouvement simple dans un environnement contrôlé
* Expliciter les autres types de mouvement et les autres types de capteur auxquels on s'intéresse



## Réunion du 24 octobre 2017
### RVP1
* Faire une présentation rapide du sujet (le conseiller ne connait pas encore notre projet)
* Présenter les capteurs qu'on va utiliser (MoCap, accéléromètres ...)
* Trouver une *histoire à raconter* pour justifier notre travail (un contexte d'application de notre projet)
* Faire une capture de données avant le RVP1
  * Pour avoir une notion de ce qu'on a besoin
  * Bien noter toutes les étapes, s'il y a des problèmes opérationnels, analytiques, physiques... 
* Réaliser un planning *prévisionnel*

### Benchmark
* Liste des capteurs auxquels on peut s'intéresser
* Faire une grille d’analyse : prix, qu’est-ce qu’il va nous apporter, autonomie, chargeur, dans quel environnement il fonctionne, photos, comment extraire les données (il faut qu’on puisse récupérer les données comme on veut, on s’intéresse aux données brutes)
* **A ENVOYER AVANT LE 5 NOVEMBRE SI ON VEUT ACHETER UN NOUVEAU CAPTEUR**

### Sur le sujet
* **Mouvements qui peuvent nous intéresser**
  * Ne pas se concentrer sur les mouvements humains
  * Pour chaque mouvement : caractérisation, possibilité de réproduction (une expérience de physique - comme étudier des vagues), une voiture télécommandé) -> **penser aux mouvements qu'on peut réproduire dans une petite salle**
  * Plusieurs capteurs = plusieurs point de vue ==> peut aider dans la compréhension d'un phénomène
  * Types de capteurs à disposition : MoCap (40mil euros), accéléromètres (quelques dizaines), camera vidéo (quelques dizaines)
* **OBJECTIF**
  * peut-être calculer le taux d’erreur entre l’acquisition de mouvement du mocap par rapport aux autres capteurs… 
  * reconstruire les mouvements du mocap à partir d’autres capteurs -> donc problème de synchronisation des données
* **LIVRABLE** : ce qu’on va présenter à la fin pour dire ce qu’on a obtenu, si on a réussi (une vidéo, un rapport, une démonstration)
* **LANGAGE INFORMATIQUE** : si on connait matlab, on peut l'utiliser, mais on peut reprendre les routines d'autres travaux sur le traitement du signal qui sont en python. *NB :  au début on n’a pas forcément besoin de réaliser le traitement du signal.*
* **PARTIE BIBLIOGRAPHIQUE** : utiliser au fûr et à mesure du développement du projet

### Capteurs
* réaliser une prémière acquisiton des données
* faire un tutoriel pour les accéléromètres (en markdown)
