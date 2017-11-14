# Méthodologie

## Mouvement d'un stylo qui dessine un cercle
- Capture et reconstruction du mouvement.
- Capteurs utilisés : MOCAP et Accéléromètre.

### 1. Calibration
- Calibration des six cameras du MOCAP en utilisant la croix de calibration.
- On n'aura pas le temps pour faire la calibration du senseur Shimmer (Accéléromètre avant le RVP-1.

### 2. Acquisition de données 
- En posant un reflecteur et un senseur Shimmer sur un stylo, capturer les données avec les deux capteurs de façon simultannée
du mouviment du stylo sur la feuille de dessin (c'est important de maintenir le stylo perpendiculaire par rapport à la feuille pour
que le mouvement des capteurssoit seulement dans un plan parallèle au plan de la feuille de dessin).
- Realizer le mouvement du stylo de façon qu'il soit visible pour tous les six cameras pour assurer la bonne reconstrution du mouviment MOCAP.

### Exportation des données
- Exporter les données acquies avec les deux capteurs dans le format .cdv (legible par Excel par exemple).

### Reconstruction du mouvement
- Utilisant les données exportées et la programmation python, reconstruir la trajectoire mouvement à partir des données acquies par
les deux capteurs utilisés.

### Analyse de l'expérimentation
- Comparer les deux trajectoires reconstruites pour analyser la précision des trajectoires reconstruites par rapport à la realité
marquée sur la feuille de dessin utilisée.
