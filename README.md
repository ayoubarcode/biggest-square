#   <center> Test Python  : Le plus grande carré
## Le plus grand carré :
>  ◦ Il s'agit de trouver le plus grand carré possible sur un plateau en évitant des obstacles.
```    
◦ Un plateau vous est transmis dans un fichier passé en argument du
programme.
     ◦ La première ligne du plateau contient les informations pour lire
la carte :
         – Le nombre de lignes du plateau ;
         – Le caractère "vide" ;
         – Le caractère "obstacle" ;
         – Le caractère "plein".
     ◦ Le plateau est composé de lignes de 'caractère "vide"' et de
'caractère "obstacle"'.
     ◦ Le but du programme est de remplacer les 'caractère "vide"' par
des 'caractère "plein"' pour représenter le plus grand carré possible.
     ◦ Dans le cas où il y en a plusieurs solutions, on choisira de
représenter le carré le plus en haut à gauche.
• Carte valide :
     ◦ Toutes les lignes doivent avoir la même longueur.
     ◦ Il y a au moins une ligne d'au moins une case.
     ◦ À la fin de chaque ligne il y a un retour à la ligne.
     ◦ Les caractères présent dans la carte doivent être uniquement ceux
présenté à la première ligne.
     ◦ En cas de carte invalide vous afficherez sur la sortie d'erreur :
map error suivi d'un retour à la ligne puis il passera au traitement du
plateau suivant.
```

``` ./map_gen.py [nombres de colonnes]  [nombres de lignes]  [densité des obstacles]  > example_file  && python solv.py example_file ```
- Version: 1.0.0
- Author : Ayoub Arahmat