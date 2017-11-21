# Tutoriel accéléromètres

NB : Ce tutoriel sert à l'utilisation du shimmer3, les autres versions ne seront pas adaptées. 

Pour pouvoir utiliser les accéléromètres, vous devez avoir installé le programme *Consensys* sur votre ordinateur (disponible pour téléchargement [ici](http://www.shimmersensing.com/support/wireless-sensor-networks-download/). 

Branchez le cable de la base à une prise et ensuite branchez le cable à la base (suivez bien cette ordre). 
Pour allumer un des accéléromètres, appuyez sur le boutton orange. Le led 

## Calibration

Téléchargez le programme *shimmer 9DOF calibration*. La dernière version est disponible sur le site [Shimmer Sensor](http://www.shimmersensing.com/products/shimmer-9dof-calibration#download-tab). Un document sur la calibration (en anglais) est aussi disponible pour téléchargement. 

![](images/download_calibration.JPG)

Il est recommandé d'aussi suivre le [vidéo](https://www.youtube.com/watch?v=aI2WDecTtfs) avec la démonstration de la calibration pour mieux suivre ce tutoriel.

**La calibration doit être faite pour chaque capteur séparamment.**

Avec le programme *shimmer 9DOF calibration* installé, allumez le Bluetooth de votre ordinateur et connectez-le au capteur que vous irez calibrer (PIN : 1234). Il faut que le capteur soit allumé pour pouvoir le connecter. Vous devez laisser le capteur connecté à votre ordianteur pendant tout le processus de calibration. 
Le capteur doit apparaître dans "Appareils bluetooth disponibles" comme "Shimmer3-XXXX" (ou XXXX sera l'ID de votre capteur, par exemple "Shimmer3-8D77"). 

Posez le capteur sur le "*Shimmer3 Calibration Stand*".

![](images/calibration_stand.gif)

Ouvrez le programme *shimmer 9DOF calibration*. Selectionnez l'ID du capteur et cliquez sur "**Connect**"

![](images/calibration_connection_capteur.jpg)

Il va apparaître "Shimmer Connected" sur "Application State" si la connection est réussite. 

![](images/calibration_connection_reussite.jpg)

Pour calibrer, il faut définir les axes du capteur. Dans notre cas, nous utiliserons la convention de l'image ci-dessous. 

![](images/calibration_axez_convention.jpg)

### Calibration du accéléromètre

Vous pouvez choisir le type d'accélération et la gamme d'accélération (cela va dependre de l'application envisagée pour l'accéléromètre). Dans ce tutoriel, on choisit "Low noise" et "2.0g".

![](images/calibration_acc_range_choix.jpg)

Pour commencer la calibration, vous devez choisir une surface planne. Cliquez sur start (en vert) pour lancer le transfert de données du shimmer vers l'ordinateur. Placez votre axe x vers le haut. 

![](images/calibration_axe_x_haute.jpg)

Appuyez sur **X+g** et attendez jusqu'à que le "**wait**" disparaît. 

Tournez le shimmer de façon a placer l'axe x vers le bas. Appuyez sur **X-g** et attendez jusqu'à que le "**wait**" disparaît.

![](images/calibration_axe_x_bas.jpg)

Positionnez l'axe y vers le haut. Appuyez dur "**Y+g**" et attendez jusqu'à que le "**wait**" disparaît.

![](images/calibration_axe_y_haut.jpg)

Tournez le shimmer de façon a placer l'axe y vers le bas. Appuyez sur **Y-g** et attendez jusqu'à que le "**wait**" disparaît.

![](images/calibration_axe_y_bas.jpg)

Positionnez l'axe z vers le haut. Appuyez dur "**Z+g**" et attendez jusqu'à que le "**wait**" disparaît.

![](images/calibration_axe_z_haut.jpg)

Tournez le shimmer de façon a placer l'axe z vers le bas. Appuyez sur **Z-g** et attendez jusqu'à que le "**wait**" disparaît.

![](images/calibration_axe_z_bas.jpg)

Vous pouvez répeter autant de fois que vous voulez chaque axe. Après avoir suivi cette méthode pour les trois axes, cliquez sur "**STOP**". 

Normallement vous devez obtenir un tableau comme celui-ci :

![](images/calibration_parametres_tableau_low_noise.jpg)

Si le tableau en en bleu, la calibration n'a pas encore été transmise au shimmer. Il faut donc appuyer sur "**Save ACCEL to Shimmer**". Vous pouvez aussi enregistrer votre calibration sur votre ordinateur en cliquant sur "**Save ACCEL to file**" (il est recommandé de le faire au cas où la calibration est perdue due à un imprévu).

Après avoir appuyé sur "Save ACCEL to Shimmer" le tableau doit être gris. 

### Calibration du gyroscope







## Utilisation

