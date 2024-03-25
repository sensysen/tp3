[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/5LAXpUGp)
# TP03: Librairies scientifiques et graphiques

- [TP03: Librairies scientifiques et graphiques](#tp03-librairies-scientifiques-et-graphiques)
  - [Directives particulières](#directives-particulières)
  - [Introduction](#introduction)
  - [Objectifs](#objectifs)
  - [Analyse d'un Pokédex 🔎](#analyse-dun-pokédex-)
    - [Préparation du dataset](#préparation-du-dataset)
      - [1.0 Chargement des données](#10-chargement-des-données)
      - [1.1 Suppression des colonnes non pertinentes](#11-suppression-des-colonnes-non-pertinentes)
      - [1.2 Renommage des colonnes restantes](#12-renommage-des-colonnes-restantes)
      - [1.3. Nettoyage des données](#13-nettoyage-des-données)
      - [1.4 Correction des types de données](#14-correction-des-types-de-données)
      - [1.5 Ajout d'une colonne](#15-ajout-dune-colonne)
    - [Visualisation de données](#visualisation-de-données)
      - [Quelques méthodes utiles pour les prochaines étapes](#quelques-méthodes-utiles-pour-les-prochaines-étapes)
      - [1.6 Le Spectre des Types](#16-le-spectre-des-types)
      - [1.7 Le Grand Recensement](#17-le-grand-recensement)
      - [1.8 L'Ascension Générationnelle](#18-lascension-générationnelle)
      - [1.9 Le Radar des Éléments](#19-le-radar-des-éléments)
    - [Filtrage, tri et agrégation](#filtrage-tri-et-agrégation)
      - [1.10 Le Panthéon des Spécialistes](#110-le-panthéon-des-spécialistes)
      - [1.11 Les Liens Invisibles](#111-les-liens-invisibles)
      - [1.12 Exploration Créative (Bonus)](#112-exploration-créative-bonus)
  - [Remise](#remise)
  - [Barème](#barème)
  - [Annexe: Guide et normes de codage](#annexe-guide-et-normes-de-codage)

:alarm_clock: Date de remise le Dimanche 24 mars 23h59

## Directives particulières

- Le fichier requirements.txt contient les librairies à installer pour faire le laboratoire;
- Il est suggéré de respecter le [guide de codage](https://github.com/INF1007-Gabarits/Guide-codage-python) et les normes pep8;
- Dans chaque programme, vous pouvez ajouter d’autres fonctions à celles décrites dans l’énoncé pour améliorer la lisibilité.

## Introduction

<p align="justify"> Bienvenue dans ce projet sur le monde fascinant des Pokémon ! Ce projet va nous emmener dans un voyage d'exploration à travers le Pokédex, où nous utiliserons nos talents d'analystes pour visualiser, filtrer et agréger des données, grâce à un ensemble de données spécialement choisi par le Professeur Chen. C'est une occasion unique de découvrir les secrets des Pokémon et de développer nos compétences d'analyse de manière ludique et passionnante. Alors, prêt à relever le défi et à devenir un des dresseurs de légende ?</p>

![Pythonmon](/assets/pythonmon.webp)

<p align="left"> <i>Crédits: <a href="https://openai.com/blog/dall-e/">DALLE 3</a></i></p>

## Objectifs

- Se familiariser avec des techniques de visualisation de données;
- Appliquer des méthodes de filtrage, de tri et d'agrégation sur des ensembles de données;

## Analyse d'un Pokédex 🔎

Dans cette première étape de notre aventure, nous allons explorer les données disponibles dans un Pokédex. Un Pokédex, pour ceux qui ne sont pas familiers avec le terme, est un appareil électronique de poche que les dresseurs de Pokémon portent sur eux pour garder des informations sur toutes les différentes espèces de Pokémon. Pour cette analyse, nous utiliserons un dataset publiquement disponible sur [Kaggle](https://www.kaggle.com/datasets/rounakbanik/pokemon). Ce dataset a été légèrement modifié pour les besoins de ce projet. Il contient divers attributs sur chaque Pokémon, tels que leur type, leur génération, et bien sûr, leurs statistiques de combat. Nous allons employer différentes techniques de visualisation et d'analyse de données pour obtenir des insights intéressants sur ces créatures fascinantes.

### Préparation du dataset

#### 1.0 Chargement des données

Pour démarrer ce projet, la première étape consiste à charger le dataset dans ce que nous appellerons notre "Pokédex". Vous utiliserez la librairie Pandas pour lire le fichier CSV qui contient toutes les données des Pokémon. Votre tâche est de compléter la fonction `create_pokedex()` qui doit retourner un DataFrame Pandas contenant toutes les données.

![Q1.0-a](/assets/Q1.0.a.png)

Après avoir créé votre Pokédex, jetez un premier coup d'œil aux données en affichant les **5 premières lignes** du DataFrame.

![Q1.0-b](/assets/Q1.0.b.png)

#### 1.1 Suppression des colonnes non pertinentes

Après avoir chargé votre dataset dans le Pokédex, la prochaine étape est de filtrer les colonnes qui nous intéressent vraiment. Pour cela, vous allez compléter la fonction filter_columns() pour ne garder que les colonnes suivantes: **name**, **type1**, **type2**, **attack**, **defense**, **hp**, **speed**, **generation**, **height_m**, **weight_kg**, **capture_rate** et **is_legendary**.

![Q1.1](/assets/Q1.1.png)

#### 1.2 Renommage des colonnes restantes

Une fois que vous avez gardé les colonnes nécessaires, il serait agréable de les renommer pour qu'elles soient plus lisibles. Le nouveau dataframe devrait avoir les colonnes suivantes: **Name**, **Primary Type**, **Secondary Type**, **Attack**, **Defense**, **HP**, **Speed**, **Generation**, **Height**, **Weight**, **Capture Rate** et **Legendary**.

![Q1.2](/assets/Q1.2.png)

#### 1.3. Nettoyage des données

Après avoir supprimé et renommé les colonnes, le prochain pas est de nettoyer les données pour éliminer toute irrégularité qui pourrait affecter nos analyses. Plus spécifiquement, votre tâche consiste à faire les choses suivantes :

- Supprimer les lignes en double;
- Supprimez toutes les lignes avec des valeurs NA dans les colonnes, à l'exception de la colonne "**Secondary Type**" où les valeurs NA sont acceptables (il est possible qu'un Pokémon n'ait qu'un seul type). Votre objectif ici est d'utiliser une approche programmative pour **sélectionner automatiquement les colonnes à inclure dans la méthode `dropna()`, plutôt que de les énumérer manuellement**. Pensez à une manière de sélectionner toutes les colonnes sauf "Secondary Type" pour l'application de dropna().
- Après des suppressions de lignes, les index de votre DataFrame peuvent être en désordre. Réinitialisez-les pour avoir une séquence ordonnée.

![Q1.3](/assets/Q1.3.png)

#### 1.4 Correction des types de données

Après avoir nettoyé votre ensemble de données, l'étape suivante est de vérifier et d'ajuster les types de données pour s'assurer qu'ils reflètent correctement l'information contenue dans chaque colonne. Dans cette phase, votre mission consiste à ajuster les types de certaines colonnes pour améliorer la précision et l'utilité de votre Pokédex.

- **Attack**, **Generation**, **HP**, et **Speed** : Ces colonnes contiennent des valeurs numériques qui représentent respectivement la génération à laquelle appartient un Pokémon, ses points de vie (Health Points), et sa vitesse. Assurez-vous que ces colonnes sont de type `int` pour faciliter les analyses numériques.

- **Legendary** : Actuellement, cette colonne utilise des valeurs `0` et `1` pour indiquer si un Pokémon est légendaire ou non. Pour améliorer la lisibilité et la manipulation de cette donnée, convertissez-la en type `boolean`. Les valeurs booléennes sont plus intuitives pour représenter une condition binaire telle que légendaire/non-légendaire.

![Q1.4](/assets/Q1.4.png)

#### 1.5 Ajout d'une colonne

Maintenant que votre Pokédex est bien organisé et nettoyé, il est temps d'ajouter une nouvelle dimension à notre analyse. Nous allons calculer l'**Agilité** de chaque Pokémon, qui sera le rapport de la vitesse sur le poids du Pokémon. Cette mesure nous donnera une idée de la rapidité d'un Pokémon par rapport à son poids, une donnée cruciale lors des combats. L'agilité peut révéler des stratèges cachés dans votre Pokédex, prêts à surprendre leurs adversaires par leur vivacité.

**Note:** Assurez-vous d'arrondir le résultat à une décimale.

![Q1.5](/assets/Q1.5.png)

### Visualisation de données

#### Quelques méthodes utiles pour les prochaines étapes

Les DataFrame et Series Pandas ont plusieurs méthodes utiles pour effectuer des calculs statistiques et des opérations de filtrage. Voici quelques-unes des méthodes que vous pourriez trouver utiles pour les prochaines étapes:

- [mean](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mean.html): Calcule la moyenne des valeurs d'une colonne
- [groupby](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html): Regroupe les lignes d'un DataFrame selon les valeurs d'une colonne
- [sort_values](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html): Trie les lignes d'un DataFrame selon les valeurs d'une colonne
- [value_counts](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html): Compte le nombre d'occurrences de chaque valeur dans une colonne
- [unique](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html): Retourne les valeurs uniques d'une colonne

#### 1.6 Le Spectre des Types

Une fois votre DataFrame impeccablement nettoyé et typé, vous êtes prêt à passer à quelque chose d'un peu plus visuel : un graphique à secteurs (plus communément appelé "pie chart" en anglais 🥧) ! Vous allez utiliser la librairie **Plotly** pour créer ce graphique. Il représentera la distribution des types primaires parmi tous les Pokémon de votre ensemble de données. Il nous donnera une idée claire de la diversité des types primaires dans l'univers Pokémon.

![Q1.6](/assets/Q1.6.png)

Quelques conseils:

- Ajustez les dimensions de graphique à 800x600 pour une meilleure visualisation.

#### 1.7 Le Grand Recensement

Vous êtes maintenant prêts à vous plonger dans une petite expédition analytique. Il est temps de révéler les secrets de la distribution des Pokémon à travers les différentes époques. En utilisant la librairie **Matplotlib**, vous allez créer un histogramme détaillé qui met en lumière le nombre de Pokémon pour chaque génération. La visualisation doit distinguer les **Pokémon** **Légendaires**, entourés de mystère et d'admiration, et leurs contreparties **Non-Légendaires**, tout aussi importantes et variées. Chaque génération sera représentée par une paire de colonnes dans votre histogramme, vous permettant de comparer visuellement la présence de ces deux groupes au fil du temps.

![Q1.7](/assets/Q1.7.png)

#### 1.8 L'Ascension Générationnelle

Le prochain défi vous mènera à une comparaison multi-dimensionnelle des statistiques moyennes des Pokémon à travers les différentes générations. Vous utiliserez Plotly pour créer un graphique en lignes superposées, une pour chaque statistique suivantes: **Attack**, **Defense**, **HP** et **Speed**. Chaque ligne représentera la moyenne de la statistique pour chaque génération. Cette visualisation vous aidera à comprendre comment les statistiques moyennes des Pokémon ont évolué au fil des générations. Utilisez la librairie **Plotly** pour créer ce graphique.

![Q1.8](/assets/Q1.8.png)

#### 1.9 Le Radar des Éléments

Vous êtes sur le point d'entrer dans la bataille des éléments, où chaque type de Pokémon dévoile ses forces et ses faiblesses en matière d'**Attaque**, de **Défense** et de **HP**. Vous utiliserez **Plotly** pour créer une série de graphiques radars qui captureront ces aspects clés. Chaque graphique radar représentera la performance de tous les types de Pokémon pour une statistique donnée. Vous devez aligner horizontalement les trois graphiques radars pour faciliter la comparaison entre les types de Pokémon. La fonction [make_subplots](https://plotly.com/python/subplots/) peut être utilisée pour créer des sous-graphiques. Cette visualisation vous aidera à comprendre les forces et les faiblesses de chaque type de Pokémon.

![Q1.9](/assets/Q1.9.png)

Quelques conseils:

- Redimensionnez votre figure à 1400x600 pour une meilleure visualisation.

### Filtrage, tri et agrégation

#### 1.10 Le Panthéon des Spécialistes

Dans ce segment, nous allons couronner l'élite des Pokémon en fonction de quelques statistiques clés : **Attack**, **Defense**, **HP** et **Speed**. Utilisez Pandas pour filtrer les **5 meilleurs Pokémon** pour chaque statistique. Ce seront les Pokémon que vous voudriez avoir dans votre équipe si vous cherchez à maximiser une statistique particulière !

![Q1.10](/assets/Q1.10.png)

Quelques conseils:

- Pour une meilleure présentation, utilisez la fonction [display(...)](https://ipython.readthedocs.io/en/stable/api/generated/IPython.display.html) pour afficher les DataFrames au lieu de `print()`.

#### 1.11 Les Liens Invisibles

Dans cette section, nous allons plonger dans les relations intrinsèques entre les différentes statistiques des Pokémon. Une matrice de corrélation vous permettra de mesurer à quel point les statistiques sont interdépendantes. Cela donne une idée de la relation entre, par exemple, la vitesse et l'attaque d'un Pokémon : sont-ils généralement proportionnels ou indépendants?

Utilisez la bibliothèque Seaborn pour générer la matrice de corrélation des statistiques suivantes: **Attack**, **Defense**, **HP**, **Speed**, **Weight** et **Height**.

![Q1.11](/assets/Q1.11.png)

Note: Utilisez la palette de couleurs `crest` pour avoir le même rendu que l'image ci-dessus.

#### 1.12 Exploration Créative (Bonus)

Pour cette tâche bonus, nous invitons les aspirant.e.s analystes Pokémon à laisser libre cours à leur créativité. Sélectionnez une combinaison de données du DataFrame qui pique votre curiosité et utilisez-la pour créer une visualisation unique. Que vous soyez guidés par l'analyse de la force brute des Pokémon, leur agilité, la distribution des types, l'évolution à travers les générations, ou tout autre angle qui vous intrigue, c'est l'occasion de montrer votre créativité et votre flair pour l'analyse de données. Le choix du type de graphique et de la librairie pour cette réalisation vous appartient entièrement.

L'objectif ici est de concevoir une visualisation qui non seulement capture votre intérêt personnel mais pourrait également fournir des observations précieuses à un chasseur de Pokémon en herbe. Comment votre graphique pourrait-il révéler des stratégies cachées, des combinaisons de types efficaces, ou simplement des curiosités amusantes sur le monde des Pokémon ? Une fois votre visualisation achevée, il faudra ajouter un bref commentaire dans le code expliquant comment elle pourrait être utilisée pour guider ou informer un dresseur dans ses aventures.

## Remise

Pour soumettre votre travail, assurez-vous d'abord que tous vos scripts, incluant les solutions et les visualisations, fonctionnent correctement et répondent aux critères de l'exercice. Ensuite, faites un dernier commit de vos changements si nécessaire et faites un `push` sur votre dépôt **GitHub** Classroom.

Il est important de vérifier sur GitHub que vos dernières modifications ont bien été mises en ligne. Aucune étape supplémentaire comme la création d'un fichier zip n'est nécessaire ; votre travail sera évalué directement à partir de votre dépôt GitHub Classroom. Veillez simplement à ce que tout soit à jour avant la date limite de remise.

## Barème

| Question     | Points  |
| ------------ | ------- |
| 1.0          | 2       |
| 1.1          | 3       |
| 1.2          | 4       |
| 1.3          | 8       |
| 1.4          | 4       |
| 1.5          | 4       |
| 1.6          | 10      |
| 1.7          | 10      |
| 1.8          | 15      |
| 1.9          | 20      |
| 1.10         | 10      |
| 1.11         | 10      |
| 1.12 (bonus) | +5      |
| **Total**    | **100** |

## Annexe: Guide et normes de codage

- [Le guide maison](https://github.com/INF1007-Gabarits/Guide-codage-python) de normes supplémentaires à respecter
- [Le plugin Pycharm Pylint](https://plugins.jetbrains.com/plugin/11084-pylint) qui analyse votre code et indique certaines erreurs. Vous avertis aussi si vous ne respectez pas certaines de normes de PEP8.
- [Quelques indications en français sur PEP8](https://openclassrooms.com/fr/courses/4425111-perfectionnez-vous-en-python/4464230-assimilez-les-bonnes-pratiques-de-la-pep-8)
- [La documentation PEP8 Officielle](https://www.python.org/dev/peps/pep-0008/)
"# tp3" 
