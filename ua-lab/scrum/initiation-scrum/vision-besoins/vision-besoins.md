---
layout: default
title: "Fiche d'Atelier : T.351.112 — Vision Produit et User Stories (Cas TodoList)"
tuto_id: "T.351.112"
type: "tuto-notion"
ua: "UA.351.11"
slug: "vision-besoins"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
nav_exclude: true
---
# T.351.112 : Définir la vision produit et exprimer les besoins en User Stories

- **Unité d'apprentissage** : [UA.351.11 — Initiation à la Démarche Agile et Cadre Scrum](#)
- **Diaporama de soutenance** : [presentation-vision-besoins.html](./presentation-vision-besoins.html)
- **Domaine** : Scrum & Méthodes Agiles
- **Cas d'étude didactique** : Application TodoList (Gestionnaire de tâches)

---

## 1. Contexte & Objectif de l'Atelier
Cet atelier pratique guide la formalisation des besoins fonctionnels en amont du premier sprint de développement. L'objectif est de définir une Vision Produit porteuse de sens, d'incarner les besoins à travers deux profils Personas concrets et de rédiger le socle des 5 User Stories majeures du Minimum Viable Product (MVP) pour l'application TodoList.

## 2. Données de Référence
- **Projet support** : Application TodoList (gestionnaire de tâches responsive).
- **Ressources associées** : Support de présentation Marp (`presentation-vision-besoins.md`).
- **Périmètre cible** : Cadrage fonctionnel complet du MVP et sélection des 5 User Stories initiales.

## 3. Notions Essentielles

### 3.1 La Vision Produit : La boussole du projet
Dans tout projet logiciel, le risque le plus insidieux est l'éparpillement : chacun imagine une application différente, les idées fusent et l'équipe perd de vue l'objectif initial. C'est ce que l'on appelle la « dérive des objectifs » (*scope creep*).

La **Vision Produit** (*Product Vision*) agit comme une boussole stratégique. Formulée en deux à trois phrases par le Product Owner, elle répond à quatre questions vitales :
1. **Pour qui ?** Quel est le public cible précis ?
2. **Quel problème ?** Quelle difficulté concrète le produit résout-il ?
3. **Quelle solution ?** De quelle nature est l'application ?
4. **Quelle valeur ajoutée ?** Pourquoi l'utilisateur choisira-t-il cette application plutôt qu'un bloc-notes papier ?

Une vision claire permet d'arbitrer chaque décision : lorsqu'une idée de fonctionnalité émerge, l'équipe se demande simplement : *« Est-ce que cette idée contribue directement à notre Vision Produit ? »*. Si la réponse est non, l'idée est écartée ou différée.

### 3.2 La Méthode des Personas : Donner un visage aux utilisateurs
Concevoir un logiciel pour « tout le monde », c'est concevoir pour personne. Un débutant n'a pas les mêmes besoins qu'un utilisateur expert, et un étudiant pressé sur son smartphone n'a pas les mêmes contraintes qu'une responsable administrative sur un grand écran de bureau.

Un **Persona** est un personnage fictif mais extrêmement réaliste, conçu à partir de profils d'utilisateurs types. Il comporte généralement :
- Un prénom, un âge et une activité professionnelle.
- Ses habitudes technologiques et ses contextes d'utilisation (mobile en déplacement, ordinateur de bureau).
- Ses objectifs principaux (ce qu'il cherche à accomplir vite et bien).
- Ses irritants majeurs (ce qui l'agace dans les outils actuels).

En gardant ses Personas en tête, l'équipe développe pour des personnes vivantes, ce qui oriente instantanément les choix d'ergonomie et de simplicité.

### 3.3 Le Formalisme de la User Story : L'expression du besoin
En gestion agile, on abandonne les phrases passives et techniques des vieux cahiers des charges (*« Le système devra permettre le stockage... »*). On formule chaque exigence du point de vue de l'utilisateur final en utilisant le gabarit canonique en 3 volets :

$$\text{En tant que } [\text{rôle}] \quad\longrightarrow\quad \text{Je veux } [\text{action}] \quad\longrightarrow\quad \text{Afin de } [\text{bénéfice}]$$

Ce formalisme oblige l'équipe à expliciter la **valeur métier** (*Afin de*) : si une story n'apporte aucun bénéfice démontrable à l'utilisateur, elle n'a aucune légitimité dans le carnet de produit.

### 3.4 Les Critères d'Acceptation : Le contrat de succès vérifiable
Une User Story sans critères d'acceptation est une promesse floue propice aux malentendus. Les **Critères d'Acceptation** (*Acceptance Criteria*) définissent la liste exacte des conditions de fonctionnement nécessaires pour que le Product Owner valide la fonctionnalité.

Ces critères constituent le contrat direct entre le Product Owner et les Développeurs : ils permettent aux développeurs de savoir exactement quoi tester avant de déclarer leur travail prêt pour la revue de sprint.

### 3.5 Délimiter le Périmètre : Le Minimum Viable Product (MVP)
Le piège classique de tout projet débutant est de vouloir tout concevoir dès la première version : mode sombre, rappels programmés, synchronisation en ligne, partage collaboratif. 

L'Agilité recommande au contraire d'isoler le **Minimum Viable Product (MVP)** : la version la plus épurée possible du produit qui apporte une valeur fonctionnelle tangible à l'utilisateur. Toutes les fonctionnalités secondaires sont rigoureusement reportées aux sprints ultérieurs.

---

## 4. Pratique & Réalisation Guidée (Cas d'école TodoList)

Pour illustrer concrètement ces principes, examinons le travail de cadrage réalisé sur l'application **TodoList** :

| Étape | Action d'ingénierie agile | Décision prise sur la TodoList | Résultat opérationnel |
| :-: | :--- | :--- | :--- |
| 1 | Formuler la Vision Produit | Définir une interface web épurée, responsive et sans inscription | Vision claire axée sur la saisie express en moins de 3 secondes |
| 2 | Construire 2 Personas contrastés | *Yassine* (étudiant mobile pressé) et *Nadia* (coordinatrice sur ordinateur) | Prise en compte de la taille des boutons tactiles et de la lisibilité des listes |
| 3 | Rédiger les 5 User Stories du MVP | 5 stories couvrant le cycle de vie d'une tâche (créer, lire, cocher, filtrer, supprimer) | Spécifications claires rédigées avec critères d'acceptation |
| 4 | Délimiter le périmètre MVP | Focaliser le Sprint 1 sur la saisie, l'affichage et le cochage | Fonctionnalités de confort (dark mode, rappels) reportées aux sprints 2 et 3 |

### 4.1 Déclaration de Vision de la TodoList
> *"Pour les étudiants et professionnels souvent submergés par leurs tâches quotidiennes, l'application **TodoList** est un gestionnaire personnel en ligne, fluide et responsive, qui permet de capturer, visualiser et valider ses tâches en un instant, sans inscription préalable ni configuration fastidieuse."*

### 4.2 Personas Cibles
- **Persona 1 : Yassine — L'Étudiant en déplacement (Usage Mobile)**
  - **Profil :** 21 ans, étudiant, toujours sur son smartphone entre deux cours.
  - **Objectif :** Noter une tâche en moins de 3 secondes avant d'oublier, et cocher ce qui est fait d'un simple geste du pouce.
  - **Irritant :** Les applications lourdes avec création de compte obligatoire, menus complexes et boutons minuscules difficiles à toucher sur mobile.
- **Persona 2 : Nadia — La Coordinatrice de Projet (Usage Ordinateur)**
  - **Profil :** 28 ans, travaille sur ordinateur de bureau avec plusieurs fenêtres ouvertes.
  - **Objectif :** Voir en un coup d'œil l'état de sa journée, filtrer les tâches terminées et garder un espace de travail visuellement épuré.
  - **Irritant :** Les listes désordonnées sans compteur clair et les applications lentes à charger.

### 4.3 Les 5 User Stories Majeures du Backlog TodoList

#### US-01 : Ajout d'une tâche via formulaire
- **Énoncé :** *En tant qu'utilisateur pressé, je veux saisir l'intitulé d'une tâche et la valider immédiatement, afin de l'enregistrer dans ma liste sans perdre de temps.*
- **Critères d'acceptation :**
  - Le champ de saisie texte dispose d'un placeholder explicite (*« Que devez-vous faire ? »*).
  - La tâche peut être ajoutée en cliquant sur le bouton *« Ajouter »* ou en appuyant sur la touche *Entrée*.
  - Une saisie vide ou composée uniquement d'espaces est bloquée sans créer de ligne inutile.
  - Le champ est automatiquement vidé et le focus est rétabli après l'ajout.

#### US-02 : Affichage de la liste et compteur de tâches
- **Énoncé :** *En tant qu'utilisateur, je veux visualiser toutes mes tâches ordonnées ainsi que le nombre de tâches restantes, afin d'évaluer ma charge de travail en un coup d'œil.*
- **Critères d'acceptation :**
  - Chaque tâche s'affiche sous forme d'une ligne lisible avec un espacement adapté.
  - Un compteur dynamique en bas de liste affiche exactement le nombre de tâches actives non terminées.
  - Si la liste est vide, un message bienveillant s'affiche (*« Aucune tâche pour le moment ! »*).

#### US-03 : Cochage et validation d'une tâche
- **Énoncé :** *En tant qu'utilisateur ayant terminé un travail, je veux cocher la tâche correspondante, afin de matérialiser son accomplissement et la distinguer des tâches en cours.*
- **Critères d'acceptation :**
  - Chaque élément dispose d'une case à cocher interactive (checkbox).
  - Le clic sur la case barre le texte de la tâche et atténue sa couleur de texte.
  - Le compteur de tâches actives est automatiquement décrémenté d'une unité.
  - Il est possible de décocher la tâche pour la remettre en attente si nécessaire.

#### US-04 : Filtrage des tâches selon leur état
- **Énoncé :** *En tant qu'utilisateur organisé, je veux filtrer ma liste selon 3 vues (Toutes, En cours, Terminées), afin de concentrer mon attention sur les tâches prioritaires.*
- **Critères d'acceptation :**
  - Trois boutons de filtrage sont accessibles (*Toutes*, *En cours*, *Terminées*).
  - Le bouton du filtre actuellement actif est visuellement mis en valeur.
  - La sélection d'un filtre met instantanément à jour la liste affichée sans rechargement de page.

#### US-05 : Suppression d'une tâche et nettoyage
- **Énoncé :** *En tant qu'utilisateur, je veux supprimer définitivement une tâche erronée ou obsolète, afin de maintenir une liste propre.*
- **Critères d'acceptation :**
  - Un bouton de suppression discret (icône corbeille ou croix) apparaît sur chaque tâche.
  - Le clic supprime immédiatement l'élément de la liste et met à jour le compteur.
  - Un bouton global *« Effacer les tâches terminées »* permet de purger toutes les tâches cochées en un clic.

### 4.4 Périmètre MVP vs Évolutions reportées
- **Inclus dans le MVP (Sprint 1) :** US-01 (Ajout), US-02 (Affichage & Compteur), US-03 (Cochage).
- **Inclus dans le Sprint 2 :** US-04 (Filtres 3 vues), US-05 (Suppression & Purge).
- **Reporté aux itérations ultérieures :** Persistance LocalStorage, rappels horaires, mode sombre (*Dark Mode*), étiquettes de couleurs.

---

## 5. Livrables de Référence Produits & Critères

- **Fiche technique d'atelier** : `ua-lab/scrum/initiation-scrum/vision-besoins/vision-besoins.md`
- **Diaporama Marp de restitution** : `ua-lab/scrum/initiation-scrum/vision-besoins/presentation-vision-besoins.md`
- **Critères de réussite validés** :
  - [x] Vision Produit formulée clairement et orientée valeur utilisateur.
  - [x] 2 Personas contrastés (Yassine et Nadia) répondant à des contextes réels.
  - [x] 5 User Stories rédigées au format standard avec critères d'acceptation précis.
  - [x] Frontière du MVP explicitement définie sans ambiguïté.
  - [x] Conformité technique : UTF-8 sans BOM, métadonnées complètes, zéro mention d'encadrant.

## 6. Glossaire Pédagogique
- **Vision Produit :** Déclaration synthétique définissant le but, la cible et la valeur ajoutée du logiciel développé.
- **Persona :** Représentation semi-fictive d'un utilisateur cible basée sur des données comportementales réelles.
- **User Story :** Description d'une exigence logicielle rédigée en langage simple du point de vue de l'utilisateur final.
- **Critères d'Acceptation :** Ensemble de conditions vérifiables indispensables pour valider la livraison d'une User Story.
- **MVP (Minimum Viable Product) :** Première version minimale et fonctionnelle d'un produit apportant une valeur concrète aux utilisateurs.
