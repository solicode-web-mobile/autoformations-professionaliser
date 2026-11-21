# -*- coding: utf-8 -*-
"""
Script to generate Milestones 2, 3, 4, 5 for UA.351.11 (Initiation Scrum).
Generates tutorial stubs (_tutos) and reference lab realizations (ua-lab).
All files encoded in UTF-8 without BOM.
"""
import os

BASE_DIR = r"d:\solicode-web-mobile\autoformations-professionaliser"

def write_utf8_file(filepath, content):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"Written: {filepath}")

# ==============================================================================
# MILESTONE 2: T.351.112 (vision-besoins)
# ==============================================================================

TUTO_2_MD = """---
layout: tuto
title: "Définir la vision produit et exprimer les besoins en User Stories"
sous_titre: "Formuler la Vision Produit, concevoir les Personas cibles et rédiger les User Stories avec critères d'acceptation"
slug: "vision-besoins"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
permalink: /tutos/vision-besoins/
tuto_id: "T.351.112"
version: "normal"
ua: "UA.351.11"
type: "tuto-atelier-notions"
nav_order: 2
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
sprint: "sprint1"
statut_realisation: "realise"
livrables:
  - chemin: "ua-lab/scrum/initiation-scrum/vision-besoins/vision-besoins.md"
    version: "1.0.0"
  - chemin: "ua-lab/scrum/initiation-scrum/vision-besoins/presentation-vision-besoins.md"
    version: "1.0.0"
---

## 1. Contexte & Enjeux
L'expression claire et partagée du besoin utilisateur est la condition fondamentale du succès d'un projet web. Dans une démarche agile, l'équipe ne part pas d'un cahier des charges rigide de cinquante pages, mais d'une Vision Produit claire, de profils utilisateurs vivants (les Personas) et de fonctionnalités découpées du point de vue de l'utilisateur final : les User Stories. Cet atelier d'initiation permet d'acquérir les réflexes méthodologiques pour formuler la vision d'une application, caractériser ses utilisateurs cibles et définir des critères d'acceptation précis pour sécuriser la qualité des développements.

## 2. Ce que vous devez apprendre
- Formuler une Vision Produit synthétique et impactante pour guider les choix fonctionnels.
- Concevoir des Personas cibles réalistes afin d'ancrer le développement dans des attentes concrètes.
- Rédiger des User Stories conformes au gabarit standard : *En tant que... je veux... afin de...*.
- Définir des critères d'acceptation concrets, mesurables et directement testables.
- Délimiter le périmètre initial du produit (MVP) pour éviter la dérive des fonctionnalités.

## 3. Travail à faire
Vous devez concevoir et préparer une **présentation synthétique** sur l'expression des besoins et la formalisation des User Stories :
1. **Rechercher et expliquer les notions fondamentales :** Définir avec vos propres mots le rôle de la Vision Produit, la technique des Personas, la structure canonique d'une User Story, l'utilité des critères d'acceptation et le principe de sélection du Minimum Viable Product (MVP).
2. **Illustrer par un exemple concret :** Choisir un cas d'usage ou vous appuyer sur votre projet technique pour formuler une vision produit, dresser le portrait de 2 personas distincts et rédiger 3 à 5 User Stories majeures avec leurs critères d'acceptation.
3. **Produire vos livrables de soutenance :**
   - Rédiger votre fiche technique d'atelier synthétisant votre analyse et vos spécifications.
   - Concevoir votre support de présentation au format Marp (16:9).

> [!TIP]
> **Solution de référence de l'atelier :**
> Le concepteur a réalisé une solution de référence complète appliquée au cas d'école de l'application **TodoList**, consultable ci-dessous pour vous guider dans la formalisation de vos livrables :

{% include tuto-livrables.html %}

## 4. Pistes de recherche active
- En quoi la Vision Produit protège-t-elle l'équipe contre la « dérive des objectifs » (scope creep) ?
- Pourquoi est-il risqué de concevoir une application pour un « utilisateur universel » plutôt que pour des Personas précis ?
- Quelle est la différence fondamentale entre une exigence technique et un besoin exprimé en User Story ?
- Pourquoi des critères d'acceptation flous ou incomplets pénalisent-ils directement les développeurs lors de la phase de test ?

## 5. Livrables attendus & Critères de validation
- **Fiche technique d'atelier :** `tutoriels/scrum/initiation-scrum/vision-besoins/vision-besoins.md`
- **Diaporama Marp de restitution :** `tutoriels/scrum/initiation-scrum/vision-besoins/presentation-vision-besoins.md`
- **Critères de validation :**
  - [ ] La Vision Produit est formulée de manière claire, concise et orientée valeur utilisateur.
  - [ ] Au moins 2 Personas contrastés sont décrits avec leurs objectifs et leurs contraintes spécifiques.
  - [ ] Les User Stories respectent rigoureusement la syntaxe *En tant que... je veux... afin de...*.
  - [ ] Chaque User Story comporte au moins 2 critères d'acceptation concrets et vérifiables.
  - [ ] Le périmètre du MVP est nettement distingué des fonctionnalités reportées aux versions futures.
"""

LAB_2_MD = """---
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
"""

PRES_2_MD = """---
layout: presentation
title: "Présentation : T.351.112 — Vision Produit et User Stories (Cas TodoList)"
marp: true
theme: default
paginate: true
header: "T.351.112 : Vision Produit et User Stories"
footer: "Scrum & Ingénierie Agile"
nav_exclude: true
---

<!-- _class: lead -->
# T.351.112 : Définir la vision produit et exprimer les besoins en User Stories
### Cas d'étude didactique : Application TodoList
**Unité d'Apprentissage : UA.351.11 — Initiation Scrum**

- **Public** : Développeurs Web (Niveau N3)
- **Domaine** : Scrum & Ingénierie Agile (`D.351.1`)
- **Compétence** : `C.351` — Piloter et animer la démarche Scrum

---

## 1. La Vision Produit : La boussole du projet

> *"Pour les étudiants et professionnels submergés par leurs tâches, l'application **TodoList** est un gestionnaire personnel en ligne, fluide et responsive, qui permet de capturer, visualiser et valider ses tâches en un instant, sans inscription ni configuration."*

- **Pourquoi une vision produit ?**
  - Fédère toute l'équipe autour d'une ambition commune.
  - Évite la dispersion et la « dérive des objectifs » (*scope creep*).
  - Sert de critère d'arbitrage pour refuser les fonctionnalités superflues.

---

## 2. Les Personas cibles de la TodoList

- **Yassine (21 ans, Étudiant en déplacement) :**
  - **Usage :** 100% Smartphone en mobilité (entre deux cours, transports).
  - **Objectif :** Noter une tâche en 3 secondes et cocher d'un geste du pouce.
  - **Attente clé :** Boutons tactiles larges, saisie immédiate par la touche Entrée.

- **Nadia (28 ans, Coordinatrice de projet) :**
  - **Usage :** Ordinateur de bureau multi-écrans.
  - **Objectif :** Vue d'ensemble claire, filtrage des tâches terminées et compteur dynamique.
  - **Attente clé :** Interface aérée, aucun rechargement de page.

---

## 3. Le Gabarit d'une User Story & Critères d'Acceptation

### Structure canonique :
- **En tant que** [rôle de l'utilisateur]
- **Je veux** [action ou fonctionnalité souhaitée]
- **Afin de** [bénéfice tangible ou valeur métier]

### Les Critères d'Acceptation :
- Fixent le contrat de succès clair entre le Product Owner et les Développeurs.
- Rédigés sous forme de scénarios testables et vérifiables.
- Servent de guide pour les tests fonctionnels avant la livraison.

---

## 4. Les 5 User Stories du Backlog TodoList

1. **US-01 (Ajout rapide) :** En tant qu'utilisateur, je veux saisir et valider une tâche par bouton ou touche Entrée.
2. **US-02 (Affichage & Compteur) :** En tant qu'utilisateur, je veux visualiser ma liste et le décompte des tâches en cours.
3. **US-03 (Cochage & Achèvement) :** En tant qu'utilisateur, je veux cocher une tâche pour la marquer barrée.
4. **US-04 (Filtrage 3 vues) :** En tant qu'utilisateur, je veux basculer entre Toutes / En cours / Terminées.
5. **US-05 (Suppression & Purge) :** En tant qu'utilisateur, je veux effacer une tâche ou nettoyer la liste.

---

## 5. Périmètre MVP vs Évolutions reportées

- **Cœur du MVP (Sprint 1) :**
  - US-01 (Ajout via formulaire avec focus).
  - US-02 (Affichage dynamique de la liste et compteur).
  - US-03 (Cochage interactif avec style barré).

- **Incrément du Sprint 2 :**
  - US-04 (Boutons de filtre Toutes / En cours / Terminées).
  - US-05 (Bouton de suppression unitaire et purge globale).

- **Reporté post-MVP :** LocalStorage, Dark Mode, rappels horaires.

---

<!-- _class: lead -->
# Conclusion de l'Atelier T.351.112
### Prêt pour l'estimation du Backlog

- La vision et les User Stories définissent avec précision **CE QU'IL FAUT CONSTRUIRE**.
- **Prochaine étape (T.351.113) :** Créer, estimer et ordonner le Product Backlog avec les Story Points et la méthode MoSCoW.
"""

VERSION_2_YML = """vision-besoins.md: "1.0.0"
presentation-vision-besoins.md: "1.0.0"
"""

# ==============================================================================
# MILESTONE 3: T.351.113 (product-backlog)
# ==============================================================================

TUTO_3_MD = """---
layout: tuto
title: "Créer, estimer et ordonner le Product Backlog"
sous_titre: "Estimer l'effort en Story Points, appliquer la méthode MoSCoW et contractualiser la DoR et la DoD"
slug: "product-backlog"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
permalink: /tutos/product-backlog/
tuto_id: "T.351.113"
version: "normal"
ua: "UA.351.11"
type: "tuto-atelier-notions"
nav_order: 3
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
sprint: "sprint1"
statut_realisation: "realise"
livrables:
  - chemin: "ua-lab/scrum/initiation-scrum/product-backlog/product-backlog.md"
    version: "1.0.0"
  - chemin: "ua-lab/scrum/initiation-scrum/product-backlog/presentation-product-backlog.md"
    version: "1.0.0"
---

## 1. Contexte & Enjeux
Une fois les besoins recueillis et formulés en User Stories, l'équipe ne peut pas tout développer en même temps. Elle doit organiser son carnet de produit (Product Backlog), évaluer l'effort de chaque fonctionnalité et prioriser selon la valeur ajoutée réelle. Cet atelier enseigne les techniques d'estimation relative en Story Points avec la suite de Fibonacci, la méthode de priorisation MoSCoW, ainsi que la contractualisation de la *Definition of Ready* (DoR) et de la *Definition of Done* (DoD).

## 2. Ce que vous devez apprendre
- Structurer et ordonner un Product Backlog sous la responsabilité du Product Owner.
- Évaluer l'effort relatif en Story Points à l'aide de la suite de Fibonacci (1, 2, 3, 5, 8).
- Appliquer la méthode de priorisation MoSCoW (Must, Should, Could, Won't) pour dégager le MVP.
- Formaliser la Definition of Ready (DoR) pour valider la maturité d'une story avant engagement.
- Établir la Definition of Done (DoD) pour garantir un standard de qualité strict et non négociable.

## 3. Travail à faire
Vous devez concevoir et préparer une **présentation synthétique** sur l'estimation et l'ordonnancement du Product Backlog :
1. **Rechercher et expliquer les notions fondamentales :** Définir avec vos propres mots le rôle du Product Backlog, les principes de l'estimation en Story Points vs les heures fermes, l'utilisation de la suite de Fibonacci, la méthode MoSCoW, ainsi que la différence essentielle entre la DoR et la DoD.
2. **Illustrer par un exemple concret :** Choisir un cas d'usage ou vous appuyer sur votre projet technique pour chiffrer en Story Points au moins 5 User Stories, les ordonner selon MoSCoW, et rédiger votre grille de DoR et DoD.
3. **Produire vos livrables de soutenance :**
   - Rédiger votre fiche technique d'atelier synthétisant vos estimations et vos contrats qualité.
   - Concevoir votre support de présentation au format Marp (16:9).

> [!TIP]
> **Solution de référence de l'atelier :**
> Le concepteur a réalisé une solution de référence complète appliquée au cas d'école de l'application **TodoList**, consultable ci-dessous pour vous guider dans la formalisation de vos livrables :

{% include tuto-livrables.html %}

## 4. Pistes de recherche active
- Pourquoi l'estimation relative en Story Points est-elle plus fiable que l'estimation en heures au début d'un projet ?
- Quel est le risque majeur d'une mauvaise utilisation de MoSCoW (ex: classer 90% des stories en « Must Have ») ?
- Que se passe-t-il pendant un sprint si les développeurs démarrent une tâche qui ne respecte pas la DoR ?
- Comment la Definition of Done protège-t-elle le projet contre la dette technique cumulative ?

## 5. Livrables attendus & Critères de validation
- **Fiche technique d'atelier :** `tutoriels/scrum/initiation-scrum/product-backlog/product-backlog.md`
- **Diaporama Marp de restitution :** `tutoriels/scrum/initiation-scrum/product-backlog/presentation-product-backlog.md`
- **Critères de validation :**
  - [ ] Le Product Backlog recense toutes les stories avec leur valeur métier et leur estimation.
  - [ ] L'effort est chiffré en Story Points sur l'échelle de Fibonacci sans dérive vers les heures.
  - [ ] La priorisation MoSCoW est appliquée de façon réaliste pour isoler le MVP du Sprint 1.
  - [ ] Les grilles DoR et DoD sont explicitement formalisées avec des critères vérifiables.
"""

LAB_3_MD = """---
layout: default
title: "Fiche d'Atelier : T.351.113 — Estimation et Product Backlog (Cas TodoList)"
tuto_id: "T.351.113"
type: "tuto-notion"
ua: "UA.351.11"
slug: "product-backlog"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
nav_exclude: true
---
# T.351.113 : Créer, estimer et ordonner le Product Backlog

- **Unité d'apprentissage** : [UA.351.11 — Initiation à la Démarche Agile et Cadre Scrum](#)
- **Diaporama de soutenance** : [presentation-product-backlog.html](./presentation-product-backlog.html)
- **Domaine** : Scrum & Méthodes Agiles
- **Cas d'étude didactique** : Application TodoList (Gestionnaire de tâches)

---

## 1. Contexte & Objectif de l'Atelier
Cet atelier traite de la structuration quantitative et qualitative du carnet de produit (*Product Backlog*). L'objectif est d'assimiler l'estimation relative de l'effort par les Story Points (suite de Fibonacci), de prioriser rationnellement les exigences grâce à la méthode MoSCoW et d'instaurer des garde-fous qualité avec la Definition of Ready (DoR) et la Definition of Done (DoD) sur le cas de l'application TodoList.

## 2. Données de Référence
- **Projet support** : Application TodoList (gestionnaire de tâches responsive).
- **Ressources associées** : Support de présentation Marp (`presentation-product-backlog.md`).
- **Périmètre cible** : Estimation des 5 User Stories initiales + 2 évolutions, sélection MoSCoW et contractualisation DoR/DoD.

## 3. Notions Essentielles

### 3.1 Qu'est-ce que le Product Backlog ?
Le **Product Backlog** est la source unique et vivante de toutes les exigences d'un produit logiciel. Ce n'est pas un document statique figé au début du projet, mais une liste dynamique ordonnée par le Product Owner.

Au fur et à mesure que le projet avance, de nouvelles idées apparaissent, certaines priorités changent suite aux retours utilisateurs et des fonctionnalités superflues sont éliminées. Le haut du backlog regroupe les éléments les plus urgents, les mieux décrits et estimés avec précision, tandis que le bas contient des besoins plus généraux qui seront affinés plus tard.

### 3.2 L'Estimation Relative par Story Points : Pourquoi bannir les heures ?
Les humains sont notoirement médiocres pour estimer une tâche en heures absolues (*« Est-ce que ce formulaire prendra 4h30 ou 6h15 ? »*). En revanche, nous sommes excellents pour comparer deux choses entre elles (*« Ce formulaire est deux fois plus complexe à coder que cette page statique »*).

Le **Story Point** est une unité de mesure abstraite et relative. Il ne mesure pas du temps, mais combine trois dimensions indissociables :
1. **La quantité de travail :** Combien de code, de structure et de styles faut-il produire ?
2. **La complexité technique :** Y a-t-il des algorithmes délicats, des manipulations de DOM imbriquées ou des calculs d'états ?
3. **L'incertitude et le risque :** Maîtrisons-nous la technologie, ou devrons-nous faire des recherches préalables ?

### 3.3 La Suite de Fibonacci et le Planning Poker
Pour éviter les débats stériles (*« Est-ce du 4 ou du 5 ? »*), Scrum utilise l'échelle non linéaire de la suite de Fibonacci adaptée : **1, 2, 3, 5, 8, 13**.
- **1 point :** Tâche triviale, immédiate (modifier un titre, corriger un lien).
- **2 points :** Tâche très simple, répétitive et sans surprise (ajouter un paragraphe, styliser un bouton).
- **3 points :** Tâche standard bien maîtrisée (créer un formulaire basique avec un champ).
- **5 points :** Tâche de complexité moyenne comportant de la logique dynamique (manipulation d'événements, filtrage de tableau).
- **8 points :** Tâche complexe avec plusieurs dépendances techniques.
- **13 points et plus :** Tâche trop volumineuse (un « Epic ») qu'il faut obligatoirement découper en plusieurs stories indépendantes.

La progression exponentielle de Fibonacci reflète une loi naturelle de l'ingénierie : **plus un travail est grand, plus l'incertitude grandit**.

Lors de l'atelier de **Planning Poker**, toute l'équipe de développement vote simultanément avec des cartes pour éviter le biais d'autorité (l'avis du plus bavard ou du plus ancien). En cas d'écart (ex: un vote à 2 et un vote à 8), les extrêmes s'expliquent et l'équipe converge rapidement.

### 3.4 La Méthode de Priorisation MoSCoW
La méthode MoSCoW classe les exigences en 4 catégories rigoureuses :
- **M — Must Have (Indispensable) :** Sans ces fonctionnalités, le produit est inutilisable. C'est le cœur absolu du MVP.
- **S — Should Have (Important) :** Fonctionnalités à forte valeur ajoutée, mais le produit reste exploitable sans elles pour une première livraison.
- **C — Could Have (Souhaitable) :** Améliorations de confort ou de design réalisées s'il reste du temps et de la bande passante.
- **W — Won't Have this time (Reporté) :** Fonctionnalités reconnues comme utiles mais explicitement exclues du sprint en cours.

### 3.5 La Definition of Ready (DoR) : Le filtre d'entrée
La **Definition of Ready** est le contrat garantissant qu'une User Story est suffisamment mûre pour être embarquée dans un sprint de développement. Elle évite aux développeurs de commencer à coder sur des besoins flous. Une story est « Ready » si :
- Son intitulé suit la syntaxe standard (*En tant que...*).
- Ses critères d'acceptation sont clairs et non ambigus.
- Elle a été estimée en Story Points par l'équipe.
- Elle ne dépend d'aucun blocage technique externe non résolu.

### 3.6 La Definition of Done (DoD) : Le filtre de sortie
La **Definition of Done** est la grille d'exigence qualité non négociable indispensable pour déclarer une tâche terminée. Elle empêche de livrer du code bâclé ou instable. Si une story ne respecte pas l'un des critères de la DoD, elle **n'est pas terminée** et ne peut pas être présentée en revue.

---

## 4. Pratique & Réalisation Guidée (Cas d'école TodoList)

Pour donner du sens à ces méthodes, voici le travail d'estimation et d'ordonnancement réalisé sur l'application **TodoList** :

| Étape | Action d'ingénierie agile | Décision prise sur la TodoList | Résultat opérationnel |
| :-: | :--- | :--- | :--- |
| 1 | Estimer l'effort relatif | Utilisation de l'échelle Fibonacci (2, 3, 5 pts) | Chiffrage transparent et consensuel des 5 stories initiales |
| 2 | Appliquer la méthode MoSCoW | Isoler le MVP indispensable pour le Sprint 1 | 3 stories Must Have (8 points au total) engagées |
| 3 | Formaliser la Definition of Ready | Définir 4 conditions d'entrée strictes | Aucune story ambigüe n'entre dans le sprint |
| 4 | Formaliser la Definition of Done | Établir 5 critères d'exigence qualité | Standards stricts : responsive, console 0 erreur, code propre |

### 4.1 Product Backlog Ordonné et Chiffré de la TodoList

| Réf | Fonctionnalité | Rôle & Action | Estimation | Priorité MoSCoW | Cible |
| :-: | :--- | :--- | :-: | :-: | :-: |
| **US-02** | Affichage & Compteur | Visualiser la liste et le nombre de tâches restantes | **2 pts** | **Must Have** | Sprint 1 |
| **US-01** | Ajout de tâche | Saisir et valider une nouvelle tâche via formulaire | **3 pts** | **Must Have** | Sprint 1 |
| **US-03** | Validation & Cochage | Cocher une tâche pour la marquer accomplie | **3 pts** | **Must Have** | Sprint 1 |
| **US-04** | Filtrage 3 vues | Filtrer entre Toutes, En cours et Terminées | **5 pts** | **Should Have** | Sprint 2 |
| **US-05** | Suppression & Purge | Effacer une tâche unitaire ou vider les cochées | **3 pts** | **Should Have** | Sprint 2 |
| **US-06** | Sauvegarde locale | Persister les tâches dans le LocalStorage | **5 pts** | **Could Have** | Sprint 3 |
| **US-07** | Thème sombre | Basculer l'affichage en mode nuit (Dark Mode) | **2 pts** | **Could Have** | Sprint 3 |

> **Bilan de charge engagée pour le Sprint 1 :** 8 Story Points (US-02 + US-01 + US-03). Ce périmètre représente le cœur opérationnel indispensable du produit.

### 4.2 Definition of Ready (DoR) adoptée pour la TodoList
Une User Story ne peut entrer dans le Sprint Planning que si elle remplit 100% des critères suivants :
1. L'énoncé est rédigé selon le gabarit *En tant que... je veux... afin de...*.
2. Au moins 2 critères d'acceptation concrets sont rédigés et validés par le PO.
3. La complexité a été estimée en Story Points par les développeurs (Fibonacci).
4. La maquette ou le gabarit visuel associé est disponible et compris.

### 4.3 Definition of Done (DoD) adoptée pour la TodoList
Une tâche ou User Story n'est déclarée « Terminée » (*Done*) que si elle valide l'ensemble des critères suivants :
1. **Conformité HTML/CSS :** Balisage HTML5 sémantique, structure CSS propre et responsive validée sur écran mobile (largeur 375px) sans débordement horizontal.
2. **Qualité JavaScript :** Aucun message d'erreur ni d'avertissement dans la console du navigateur.
3. **Tests fonctionnels :** Tous les critères d'acceptation de la story ont été testés et validés manuellement.
4. **Lisibilité du code :** Indentation rigoureuse, noms de variables explicites et suppression de tout code mort ou `console.log` de débogage.
5. **Gestion de version :** Code versionné proprement sur la branche active du sprint (`sprint1`) avec message conventionnel clair.

---

## 5. Livrables de Référence Produits & Critères

- **Fiche technique d'atelier** : `ua-lab/scrum/initiation-scrum/product-backlog/product-backlog.md`
- **Diaporama Marp de restitution** : `ua-lab/scrum/initiation-scrum/product-backlog/presentation-product-backlog.md`
- **Critères de réussite validés** :
  - [x] Product Backlog chiffré sur l'échelle de Fibonacci (Story Points relatifs).
  - [x] Priorisation MoSCoW argumentée avec périmètre Sprint 1 calibré à 8 points.
  - [x] Grille DoR formalisée avec critères de maturité d'entrée.
  - [x] Grille DoD formalisée avec critères qualité non négociables.
  - [x] Fichiers UTF-8 sans BOM et conformes aux directives du projet.

## 6. Glossaire Pédagogique
- **Product Backlog :** Carnet d'exigences priorisé et dynamique représentant l'ensemble des fonctionnalités attendues sur le produit.
- **Story Point :** Unité d'estimation relative combinant effort, complexité technique et incertitude.
- **Suite de Fibonacci :** Série mathématique (1, 2, 3, 5, 8...) utilisée en agilité pour modéliser l'incertitude croissante avec la taille des tâches.
- **MoSCoW :** Cadre de priorisation classant les besoins en Must Have, Should Have, Could Have et Won't Have.
- **DoR (Definition of Ready) :** Conditions préalables qu'une story doit remplir pour être sélectionnée en sprint.
- **DoD (Definition of Done) :** Exigences de qualité et de tests indispensables pour déclarer un incrément officiellement terminé.
"""

PRES_3_MD = """---
layout: presentation
title: "Présentation : T.351.113 — Estimation et Product Backlog (Cas TodoList)"
marp: true
theme: default
paginate: true
header: "T.351.113 : Estimation et Product Backlog"
footer: "Scrum & Ingénierie Agile"
nav_exclude: true
---

<!-- _class: lead -->
# T.351.113 : Créer, estimer et ordonner le Product Backlog
### Cas d'étude didactique : Application TodoList
**Unité d'Apprentissage : UA.351.11 — Initiation Scrum**

- **Public** : Développeurs Web (Niveau N3)
- **Domaine** : Scrum & Ingénierie Agile (`D.351.1`)
- **Compétence** : `C.351` — Piloter et animer la démarche Scrum

---

## 1. Pourquoi estimer en Story Points relatifs ?

- **Les limites des heures absolues :**
  - Forte subjectivité et sous-estimation systématique des imprévus.
  - Varie considérablement selon l'expérience individuelle du développeur.

- **La force des Story Points relatifs :**
  - Mesure abstraite combinant : **effort**, **complexité**, **incertitude**.
  - Comparaison directe entre éléments connus.
  - Échelle de Fibonacci : **1, 2, 3, 5, 8, 13** (l'incertitude grandit avec la taille).

---

## 2. La Méthode de Priorisation MoSCoW

- **Must Have (Indispensable) :**
  - Cœur vital du MVP, non négociable pour le premier livrable.
- **Should Have (Important) :**
  - Forte valeur ajoutée mais n'empêche pas l'usage immédiat.
- **Could Have (Souhaitable) :**
  - Options de confort réalisées s'il reste du temps.
- **Won't Have (Reporté) :**
  - Exigences écartées pour le sprint en cours.

---

## 3. Le Product Backlog Chiffré de la TodoList

| Réf | Fonctionnalité | Points | MoSCoW | Cible |
| :-: | :--- | :-: | :-: | :-: |
| **US-02** | Affichage liste & compteur | **2 pts** | **Must Have** | Sprint 1 |
| **US-01** | Ajout d'une tâche via formulaire | **3 pts** | **Must Have** | Sprint 1 |
| **US-03** | Cochage et validation de tâche | **3 pts** | **Must Have** | Sprint 1 |
| **US-04** | Filtrage 3 vues (Toutes/En cours/Fait) | 5 pts | Should Have | Sprint 2 |
| **US-05** | Suppression et purge | 3 pts | Should Have | Sprint 2 |
| **US-06** | Sauvegarde LocalStorage | 5 pts | Could Have | Sprint 3 |

> **Périmètre engagé Sprint 1 : 8 Story Points (MVP vital).**

---

## 4. Les Contrats Qualité : DoR vs DoD

### Definition of Ready (DoR) — Filtre d'entrée :
- Story rédigée au gabarit standard (*En tant que...*).
- Critères d'acceptation clairs et testables.
- Complexité votée en Story Points par l'équipe.

### Definition of Done (DoD) — Filtre de sortie :
- HTML5 sémantique et responsive mobile 375px sans débordement.
- Console du navigateur 100% propre (zéro warning, zéro erreur).
- Critères d'acceptation validés manuellement.
- Code versionné proprement sur la branche active.

---

<!-- _class: lead -->
# Conclusion de l'Atelier T.351.113
### Prêt pour la Planification du Sprint

- Le backlog est chiffré, priorisé et encadré par des contrats qualité stricts.
- **Prochaine étape (T.351.114) :** Planifier, découper et piloter un Sprint de développement avec le tableau Kanban et le Daily Scrum.
"""

VERSION_3_YML = """product-backlog.md: "1.0.0"
presentation-product-backlog.md: "1.0.0"
"""

# ==============================================================================
# MILESTONE 4: T.351.114 (sprint-planning-execution)
# ==============================================================================

TUTO_4_MD = """---
layout: tuto
title: "Planifier, découper et piloter un Sprint de développement"
sous_titre: "Fixer le Sprint Goal, constituer le Sprint Backlog, découper en tâches techniques et animer le Kanban"
slug: "sprint-planning-execution"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
permalink: /tutos/sprint-planning-execution/
tuto_id: "T.351.114"
version: "normal"
ua: "UA.351.11"
type: "tuto-atelier-notions"
nav_order: 4
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
sprint: "sprint1"
statut_realisation: "realise"
livrables:
  - chemin: "ua-lab/scrum/initiation-scrum/sprint-planning-execution/sprint-planning-execution.md"
    version: "1.0.0"
  - chemin: "ua-lab/scrum/initiation-scrum/sprint-planning-execution/presentation-sprint-planning-execution.md"
    version: "1.0.0"
---

## 1. Contexte & Enjeux
Le passage de la théorie à la production commence véritablement lors du Sprint Planning. L'équipe se réunit pour définir le but du sprint (*Sprint Goal*), sélectionner les User Stories du *Sprint Backlog*, et les découper en micro-tâches techniques courtes (1 à 3 heures). Au quotidien, l'avancement est piloté de façon transparente grâce au management visuel (tableau Kanban) et au rituel du Daily Scrum de 15 minutes. Cet atelier permet d'acquérir les réflexes de planification et de coordination quotidienne indispensables à tout développeur professionnel.

## 2. Ce que vous devez apprendre
- Formuler un Sprint Goal fédérateur donnant une orientation claire à l'itération.
- Constituer un Sprint Backlog équilibré en fonction des priorités du Product Owner.
- Découper une User Story en micro-tâches techniques élémentaires (1 à 3 heures).
- Structurer et animer un tableau de flux Kanban avec limitation du travail en cours (WIP).
- Conduire un Daily Scrum efficace de 15 minutes pour identifier et éliminer les blocages.

## 3. Travail à faire
Vous devez concevoir et préparer une **présentation synthétique** sur la planification opérationnelle et le pilotage quotidien d'un Sprint :
1. **Rechercher et expliquer les notions fondamentales :** Définir avec vos propres mots le déroulement du Sprint Planning, le rôle du Sprint Goal, la règle d'or du découpage en micro-tâches techniques courtes, le fonctionnement d'un tableau Kanban (colonnes de flux, limitation du travail en cours WIP), et les 3 questions rituelles du Daily Scrum.
2. **Illustrer par un exemple concret :** Choisir un cas d'usage ou vous appuyer sur votre projet technique pour définir un Sprint Goal, sélectionner vos User Stories, décomposer chaque story en 2 à 4 micro-tâches techniques chiffrées en heures, et simuler la levée d'un obstacle technique lors d'un Daily Scrum.
3. **Produire vos livrables de soutenance :**
   - Rédiger votre fiche technique d'atelier synthétisant votre plan de sprint et votre organisation.
   - Concevoir votre support de présentation au format Marp (16:9).

> [!TIP]
> **Solution de référence de l'atelier :**
> Le concepteur a réalisé une solution de référence complète appliquée au cas d'école de l'application **TodoList**, consultable ci-dessous pour vous guider dans la formalisation de vos livrables :

{% include tuto-livrables.html %}

## 4. Pistes de recherche active
- Pourquoi une tâche technique ne doit-elle jamais dépasser une durée maximale d'une demi-journée ?
- En quoi la limitation du travail en cours (WIP Limit) évite-t-elle le piège de « commencer dix choses sans en finir une seule » ?
- Quel est le risque si le Daily Scrum se transforme en rapport hiérarchique au lieu d'un échange d'équipe ?
- Comment le Scrum Master intervient-il lorsqu'un développeur signale un obstacle technique bloquant ?

## 5. Livrables attendus & Critères de validation
- **Fiche technique d'atelier :** `tutoriels/scrum/initiation-scrum/sprint-planning-execution/sprint-planning-execution.md`
- **Diaporama Marp de restitution :** `tutoriels/scrum/initiation-scrum/sprint-planning-execution/presentation-sprint-planning-execution.md`
- **Critères de validation :**
  - [ ] Le Sprint Goal est formulé de manière claire, concise et orientée valeur.
  - [ ] Le Sprint Backlog est découpé en micro-tâches techniques courtes (1 à 3h chacune).
  - [ ] Le fonctionnement du tableau Kanban (colonnes, règles WIP) est explicité.
  - [ ] Le protocole du Daily Scrum (3 questions, identification d'un blocage) est illustré.
"""

LAB_4_MD = """---
layout: default
title: "Fiche d'Atelier : T.351.114 — Sprint Planning et Pilotage Kanban (Cas TodoList)"
tuto_id: "T.351.114"
type: "tuto-notion"
ua: "UA.351.11"
slug: "sprint-planning-execution"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
nav_exclude: true
---
# T.351.114 : Planifier, découper et piloter un Sprint de développement

- **Unité d'apprentissage** : [UA.351.11 — Initiation à la Démarche Agile et Cadre Scrum](#)
- **Diaporama de soutenance** : [presentation-sprint-planning-execution.html](./presentation-sprint-planning-execution.html)
- **Domaine** : Scrum & Méthodes Agiles
- **Cas d'étude didactique** : Application TodoList (Gestionnaire de tâches)

---

## 1. Contexte & Objectif de l'Atelier
Cet atelier organise la transition opérationnelle entre les exigences fonctionnelles et la réalisation technique concrète. L'objectif est d'apprendre à animer la réunion de planification de sprint (*Sprint Planning*), de formuler un Objectif de Sprint (*Sprint Goal*) rassembleur, de découper les User Stories en micro-tâches techniques courtes (1 à 3 heures), et de piloter l'avancement au quotidien grâce au tableau Kanban et à la mêlée quotidienne (*Daily Scrum*) sur le cas de l'application TodoList.

## 2. Données de Référence
- **Projet support** : Application TodoList (gestionnaire de tâches responsive).
- **Ressources associées** : Support de présentation Marp (`presentation-sprint-planning-execution.md`).
- **Périmètre cible** : Sprint 1 (8 Story Points, découpés en 9 tâches techniques d'ingénierie web).

## 3. Notions Essentielles

### 3.1 La Réunion de Planification de Sprint (Sprint Planning)
Le **Sprint Planning** est le rituel formel ouvrant chaque nouvelle itération de développement. Il est animé par le Scrum Master et réunit obligatoirement toute l'équipe. Il répond à 3 questions séquentielles :
1. **Pourquoi ce Sprint a-t-il de la valeur ?** Le Product Owner expose la priorité stratégique du moment et l'équipe s'accorde sur le *Sprint Goal*.
2. **Que peut-on réaliser pendant ce Sprint ?** En s'appuyant sur les estimations en Story Points et la capacité disponible, les développeurs sélectionnent le lot de User Stories à réaliser.
3. **Comment le travail sera-t-il réalisé techniquement ?** Les développeurs décomposent chaque story en tâches techniques précises pour concevoir l'incrément.

### 3.2 L'Objectif de Sprint (Sprint Goal) : Donner du sens
Une erreur fréquente chez les débutants consiste à résumer le sprint à une simple liste de courses (*« Faire US-01, US-02 et US-03 »*). Si un imprévu survient, l'équipe ne sait plus quoi sacrifier.

Le **Sprint Goal** est une phrase synthétique qui donne la finalité globale du sprint. Il apporte une souplesse indispensable : si une difficulté technique imprévue survient au milieu du sprint, l'équipe et le Product Owner peuvent renégocier les détails mineurs d'une story tout en conservant le Sprint Goal intact.

### 3.3 Du Besoin Fonctionnel à la Tâche Technique : Le découpage court
Une User Story décrit un besoin utilisateur (*« Je veux cocher une tâche »*). Mais un développeur ne code pas directement une story : il manipule du HTML, du CSS et du JavaScript.

La **règle d'or de l'ingénierie agile** impose de décomposer chaque User Story en **micro-tâches élémentaires d'une durée comprise entre 1 et 3 heures** (4 heures au grand maximum). 
- **Pourquoi ?** Si une tâche dure 2 jours, un développeur bloqué passera deux jours entiers sans que personne ne s'en aperçoive. Avec des micro-tâches de 2h, un blocage devient visible en une demi-journée et l'équipe intervient immédiatement pour aider.

### 3.4 Le Management Visuel avec le Tableau Kanban
Pour piloter l'activité de manière transparente, l'équipe utilise un tableau visuel comportant 4 colonnes canoniques :
1. **À faire (To Do) :** Les micro-tâches prêtes à être prises en charge.
2. **En cours (In Progress) :** Les tâches actuellement développées.
3. **En revue / Test (Review / QA) :** Tâches codées en attente de vérification DoD par un pair.
4. **Terminé (Done) :** Tâches 100% conformes à la Definition of Done.

> **Le principe du WIP Limit (Work In Progress) :**
> L'équipe s'interdit d'avoir plus de 2 tâches en cours simultanément par développeur. Le mot d'ordre agile est : **« Arrêter de commencer, commencer à terminer ! »**. Il vaut mieux finir complètement une fonctionnalité avant d'en ouvrir une autre.

### 3.5 Le Daily Scrum : La synchronisation quotidienne
Le **Daily Scrum** est une réunion quotidienne de **15 minutes maximum**, réalisée debout devant le tableau de suivi. Ce n'est pas un rapport hiérarchique au chef de projet, mais une concertation entre développeurs où chacun répond à 3 questions simples :
1. *Qu'ai-je accompli hier qui a aidé l'équipe à atteindre le Sprint Goal ?*
2. *Que vais-je accomplir aujourd'hui pour aider l'équipe ?*
3. *Quels sont les obstacles ou blocages qui me ralentissent ?*

Dès qu'un obstacle (*impediment*) est formulé, le Scrum Master prend en charge sa résolution après la réunion pour ne pas pénaliser le temps de travail des développeurs.

---

## 4. Pratique & Réalisation Guidée (Cas d'école TodoList)

Voici le plan opérationnel appliqué au **Sprint 1** de l'application **TodoList** :

| Étape | Action d'ingénierie agile | Décision prise sur la TodoList | Résultat opérationnel |
| :-: | :--- | :--- | :--- |
| 1 | Formuler le Sprint Goal | Cadrer le premier incrément logiciel utilisable | « Livrer une première version One-Page permettant de saisir, d'afficher et de cocher ses tâches » |
| 2 | Constituer le Sprint Backlog | Sélection des 3 stories Must Have (8 Story Points) | US-01 (Ajout), US-02 (Affichage & Compteur), US-03 (Cochage) |
| 3 | Découper en micro-tâches | Décomposition technique en 9 tâches de 1h à 2h30 | 14h30 de développement total réparties sur l'itération |
| 4 | Piloter le flux Kanban & Daily Scrum | Simulation du tableau avec WIP Limit = 2 et détection d'un blocage formulaire | Résolution immédiate du bug `e.preventDefault()` le Jour 3 |

### 4.1 Sprint Goal du Sprint 1
> *"Livrer une première version opérationnelle permettant de saisir, d'afficher et de cocher ses tâches quotidiennes en toute fluidité sur mobile et ordinateur."*

### 4.2 Découpage Détaillé du Sprint Backlog en 9 Micro-Tâches Techniques

#### Lot US-02 : Structure & Affichage de la Liste (2 Story Points)
- **T-01 [HTML] — Structure sémantique de base (1h30) :** Créer le fichier `index.html`, baliser le conteneur principal `<main>`, l'en-tête de l'application et la liste ordonnée `<ul>` dédiée aux tâches.
- **T-02 [CSS] — Styles et conteneur responsive (2h00) :** Concevoir la feuille de style avec typographie moderne, centrage de la carte principale et adaptation mobile 375px sans ascenseur horizontal.
- **T-03 [JS] — Affichage du compteur dynamique (1h00) :** Écrire la fonction JavaScript qui compte les éléments actifs et met à jour le texte du compteur dans le pied de liste.

#### Lot US-01 : Formulaire & Ajout de Tâche (3 Story Points)
- **T-04 [HTML/CSS] — Intégration du formulaire de saisie (1h00) :** Baliser le `<form>` avec champ `<input type="text">` et bouton `<button type="submit">`, styliser avec focus visible.
- **T-05 [JS] — Écoute de l'événement submit et validation (1h30) :** Capter la soumission, bloquer le rafraîchissement par défaut, vérifier que la saisie n'est pas vide et réinitialiser le champ.
- **T-06 [JS] — Création dynamique du nœud DOM (2h00) :** Construire l'élément `<li>` contenant le libellé de la tâche et l'insérer proprement dans la liste `<ul>`.

#### Lot US-03 : Cochage & Validation de Tâche (3 Story Points)
- **T-07 [HTML/JS] — Intégration de la checkbox interactive (1h30) :** Ajouter une boîte à cocher devant chaque tâche générée et relier son état à un écouteur d'événement `change`.
- **T-08 [CSS/JS] — Bascule de style terminé et recalcul du compteur (1h30) :** Appliquer la classe CSS `.completed` (texte barré, opacité réduite) lors du cochage et décrémenter le compteur dynamique.
- **T-09 [QA/Test] — Contrôle qualité DoD & validation responsive (2h30) :** Tester l'application sur émulateur mobile (375px), vérifier l'absence d'erreur console et valider tous les critères d'acceptation.

> **Volume horaire estimé :** 14 heures 30 minutes de travail effectif.

### 4.3 Simulation du Flux Kanban et Résolution d'un Blocage lors du Daily Scrum
- **Jour 3 (Mêlée quotidienne à 9h00) :**
  - Le développeur chargé de la tâche `T-05` signale un problème : *« Quand j'appuie sur la touche Entrée dans le formulaire, la page se recharge immédiatement et la tâche n'est pas conservée »*.
  - **Intervention du Scrum Master :** Il identifie le comportement natif du formulaire HTML. Après la mêlée, il oriente le développeur vers l'utilisation de `event.preventDefault()` dans le gestionnaire d'événement JavaScript.
  - **Résultat :** Le blocage est levé en 10 minutes. La tâche `T-05` passe dans la colonne *Terminé* l'après-midi même sans impacter le calendrier global du sprint.

---

## 5. Livrables de Référence Produits & Critères

- **Fiche technique d'atelier** : `ua-lab/scrum/initiation-scrum/sprint-planning-execution/sprint-planning-execution.md`
- **Diaporama Marp de restitution** : `ua-lab/scrum/initiation-scrum/sprint-planning-execution/presentation-sprint-planning-execution.md`
- **Critères de réussite validés** :
  - [x] Sprint Goal formulé de façon claire et orientée utilisateur.
  - [x] Sprint Backlog découpé en 9 micro-tâches élémentaires de 1h à 2h30.
  - [x] Organisation Kanban avec règles de WIP Limit formalisées.
  - [x] Cas d'usage Daily Scrum simulé avec identification et levée d'un obstacle technique.
  - [x] Encodage UTF-8 sans BOM et conformité rigoureuse aux standards du projet.

## 6. Glossaire Pédagogique
- **Sprint Planning :** Rituel de démarrage du sprint où l'équipe définit l'objectif, sélectionne les stories et découpe les tâches techniques.
- **Sprint Goal :** But collectif unique donnant la direction générale et la raison d'être du sprint.
- **Sprint Backlog :** Ensemble des User Stories sélectionnées pour l'itération accompagnées de leurs tâches techniques d'exécution.
- **Kanban :** Système visuel de pilotage du flux de travail matérialisant l'avancement à travers des colonnes d'états.
- **WIP Limit (Work In Progress) :** Plafond limitant le nombre de tâches pouvant être traitées simultanément pour éviter l'éparpillement.
- **Daily Scrum :** Point de synchronisation quotidien de 15 minutes debout centré sur l'avancement et la suppression des obstacles.
"""

PRES_4_MD = """---
layout: presentation
title: "Présentation : T.351.114 — Sprint Planning et Pilotage Kanban (Cas TodoList)"
marp: true
theme: default
paginate: true
header: "T.351.114 : Sprint Planning et Pilotage Kanban"
footer: "Scrum & Ingénierie Agile"
nav_exclude: true
---

<!-- _class: lead -->
# T.351.114 : Planifier, découper et piloter un Sprint de développement
### Cas d'étude didactique : Application TodoList
**Unité d'Apprentissage : UA.351.11 — Initiation Scrum**

- **Public** : Développeurs Web (Niveau N3)
- **Domaine** : Scrum & Ingénierie Agile (`D.351.1`)
- **Compétence** : `C.351` — Piloter et animer la démarche Scrum

---

## 1. Le Sprint Planning & Le Sprint Goal

- **Les 3 questions du Sprint Planning :**
  1. *Pourquoi ce sprint a-t-il de la valeur ?* $\rightarrow$ Le **Sprint Goal**.
  2. *Que peut-on faire ?* $\rightarrow$ Sélection du **Sprint Backlog**.
  3. *Comment allons-nous le concevoir ?* $\rightarrow$ Découpage technique.

- **Sprint Goal du Sprint 1 (TodoList) :**
  > *"Livrer une première version opérationnelle permettant de saisir, d'afficher et de cocher ses tâches quotidiennes en toute fluidité."*

---

## 2. Découpage en Micro-Tâches Techniques Courtes

### La règle d'or : Tâches de 1 à 3 heures
- Évite les retards invisibles et les blocages prolongés.
- Facilite l'entraide immédiate au sein de l'équipe.

### Découpage des 8 Story Points en 9 micro-tâches :
- **US-02 (2 pts) :** T-01 Squelette HTML (1h30), T-02 CSS responsive (2h), T-03 Compteur dynamique (1h).
- **US-01 (3 pts) :** T-04 Formulaire (1h), T-05 Écouteur submit (1h30), T-06 Création nœud DOM (2h).
- **US-03 (3 pts) :** T-07 Checkbox interactive (1h30), T-08 Style barré & recalcul (1h30), T-09 Test DoD (2h30).

---

## 3. Le Management Visuel Kanban

- **Les 4 colonnes du tableau :**
  - **À faire (To Do)**
  - **En cours (In Progress)** $\rightarrow$ *WIP Limit : maximum 2 tâches en cours simultanées*.
  - **En revue (Review / QA)**
  - **Terminé (Done)** $\rightarrow$ *100% conforme à la Definition of Done*.

> **Devise Agile :** « Arrêter de commencer, commencer à terminer ! »

---

## 4. Le Daily Scrum & La Levée d'Obstacles

- **Le rituel en 15 minutes chrono (debout) :**
  - *Qu'ai-je accompli hier ?*
  - *Que vais-je faire aujourd'hui ?*
  - *Quels sont les obstacles qui me bloquent ?*

- **Cas vécu sur la TodoList (Jour 3) :**
  - **Obstacle :** Rechargement intempestif de la page lors de la touche Entrée.
  - **Action du Scrum Master :** Conseil technique post-réunion pour injecter `event.preventDefault()`.
  - **Résultat :** Blocage résolu en 10 minutes, livraison sécurisée dans les temps.

---

<!-- _class: lead -->
# Conclusion de l'Atelier T.351.114
### Prêt pour la Démonstration et la Rétrospective

- Le sprint s'exécute avec fluidité grâce au découpage court et au Kanban.
- **Prochaine étape (T.351.115) :** Valider l'incrément en direct lors de la Sprint Review et animer la Sprint Retrospective.
"""

VERSION_4_YML = """sprint-planning-execution.md: "1.0.0"
presentation-sprint-planning-execution.md: "1.0.0"
"""

# ==============================================================================
# MILESTONE 5: T.351.115 (revue-retrospective)
# ==============================================================================

TUTO_5_MD = """---
layout: tuto
title: "Valider l'incrément, animer la Sprint Review et la Rétrospective"
sous_titre: "Faire la démonstration de l'incrément en direct, collecter les feedbacks et définir le plan d'actions d'amélioration"
slug: "revue-retrospective"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
permalink: /tutos/revue-retrospective/
tuto_id: "T.351.115"
version: "normal"
ua: "UA.351.11"
type: "tuto-atelier-notions"
nav_order: 5
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
sprint: "sprint1"
statut_realisation: "realise"
livrables:
  - chemin: "ua-lab/scrum/initiation-scrum/revue-retrospective/revue-retrospective.md"
    version: "1.0.0"
  - chemin: "ua-lab/scrum/initiation-scrum/revue-retrospective/presentation-revue-retrospective.md"
    version: "1.0.0"
---

## 1. Contexte & Enjeux
La fin d'un Sprint ne se limite pas à valider du code sur GitHub. Elle articule deux rituels fondamentaux et complémentaires : la Sprint Review, dédiée à la démonstration concrète du produit devant les parties prenantes, et la Sprint Retrospective, dédiée à l'amélioration interne du fonctionnement de l'équipe. Cet atelier enseigne comment préparer et animer une démonstration en direct d'un incrément fonctionnel répondant à la Definition of Done, comment recueillir des retours d'usage concrets et comment formaliser un plan d'actions d'amélioration continue pour le sprint suivant.

## 2. Ce que vous devez apprendre
- Préparer et animer une démonstration en direct (Sprint Review) sur un logiciel fonctionnel.
- Contrôler l'adéquation stricte de l'incrément avec la Definition of Done (DoD).
- Collecter et convertir les retours utilisateurs en ajustements concrets du Product Backlog.
- Conduire une Sprint Retrospective réflexive et bienveillante autour des 3 questions clés.
- Élaborer un plan de 2 à 3 actions d'amélioration concrètes, mesurables et directement applicables.

## 3. Travail à faire
Vous devez concevoir et préparer une **présentation synthétique** sur la clôture d'un Sprint agile (Revue et Rétrospective) :
1. **Rechercher et expliquer les notions fondamentales :** Définir avec vos propres mots la distinction fondamentale entre la Sprint Review (axée produit) et la Sprint Retrospective (axée équipe), les principes d'une démonstration live sans slides passives, les modalités de recueil de feedback, et la structure d'une rétrospective d'équipe efficace.
2. **Illustrer par un exemple concret :** Choisir un cas d'usage ou vous appuyer sur votre projet technique pour simuler la démonstration en direct de votre incrément, lister les retours obtenus d'un utilisateur externe, et formaliser le bilan de votre rétrospective avec 3 actions d'amélioration prioritaires pour le Sprint 2.
3. **Produire vos livrables de soutenance :**
   - Rédiger votre fiche technique d'atelier synthétisant votre revue et votre plan d'actions.
   - Concevoir votre support de présentation au format Marp (16:9).

> [!TIP]
> **Solution de référence de l'atelier :**
> Le concepteur a réalisé une solution de référence complète appliquée au cas d'école de l'application **TodoList**, consultable ci-dessous pour vous guider dans la formalisation de vos livrables :

{% include tuto-livrables.html %}

## 4. Pistes de recherche active
- Pourquoi une démonstration lors de la Sprint Review doit-elle impérativement se faire sur un logiciel fonctionnel et non sur des diapositives ?
- En quoi la Sprint Review est-elle une séance de travail collaboratif plutôt qu'un simple examen sanctionnant ?
- Quel climat relationnel le Scrum Master doit-il instaurer pour que la rétrospective soit constructive ?
- Pourquoi est-il déconseillé de voter plus de 3 actions d'amélioration lors d'une rétrospective de sprint ?

## 5. Livrables attendus & Critères de validation
- **Fiche technique d'atelier :** `tutoriels/scrum/initiation-scrum/revue-retrospective/revue-retrospective.md`
- **Diaporama Marp de restitution :** `tutoriels/scrum/initiation-scrum/revue-retrospective/presentation-revue-retrospective.md`
- **Critères de validation :**
  - [ ] La démonstration en direct de l'incrément s'appuie sur des scénarios d'usage réels et vérifie la DoD.
  - [ ] Les feedbacks collectés sont documentés et traduits en ajustements du carnet de produit.
  - [ ] La rétrospective analyse en toute transparence les succès et les axes d'apprentissage.
  - [ ] 2 à 3 actions d'amélioration concrètes, attribuées et mesurables sont définies pour le sprint suivant.
"""

LAB_5_MD = """---
layout: default
title: "Fiche d'Atelier : T.351.115 — Sprint Review et Rétrospective (Cas TodoList)"
tuto_id: "T.351.115"
type: "tuto-notion"
ua: "UA.351.11"
slug: "revue-retrospective"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
nav_exclude: true
---
# T.351.115 : Valider l'incrément, animer la Sprint Review et la Rétrospective

- **Unité d'apprentissage** : [UA.351.11 — Initiation à la Démarche Agile et Cadre Scrum](#)
- **Diaporama de soutenance** : [presentation-revue-retrospective.html](./presentation-revue-retrospective.html)
- **Domaine** : Scrum & Méthodes Agiles
- **Cas d'étude didactique** : Application TodoList (Gestionnaire de tâches)

---

## 1. Contexte & Objectif de l'Atelier
Cet atelier traite de la conclusion formelle du Sprint Scrum à travers ses deux cérémonies d'inspection et d'adaptation : la **Sprint Review**, dédiée à la validation de la valeur du produit devant les parties prenantes, et la **Sprint Retrospective**, dédiée à l'analyse critique et constructive du fonctionnement de l'équipe. L'objectif est d'apprendre à animer une démonstration en direct, à intégrer des retours d'utilisateurs et à concevoir un plan d'actions d'amélioration continue pour le cycle suivant sur le cas de l'application TodoList.

## 2. Données de Référence
- **Projet support** : Application TodoList (gestionnaire de tâches responsive).
- **Ressources associées** : Support de présentation Marp (`presentation-revue-retrospective.md`).
- **Périmètre cible** : Clôture du Sprint 1 (Incrément MVP), revue de la Definition of Done et plan d'amélioration pour le Sprint 2.

## 3. Notions Essentielles

### 3.1 La Sprint Review : L'inspection du produit en direct
La **Sprint Review** a lieu au dernier jour du sprint. Elle réunit le Product Owner, l'équipe de développement, le Scrum Master et les parties prenantes (utilisateurs, formateur, clients).

Dans Scrum, la Sprint Review répond à une règle d'or non négociable : **aucune présentation PowerPoint abstraite, mais une démonstration en direct d'un logiciel réellement fonctionnel**.
- L'équipe manipule le produit sous les yeux des utilisateurs.
- On vérifie que chaque fonctionnalité démontrée satisfait à 100% à la **Definition of Done (DoD)**.
- Le Product Owner valide ou refuse formellement chaque User Story présentée.

Ce rituel n'est pas un tribunal ni une évaluation punitive : c'est un atelier collaboratif d'échange où l'on découvre comment les utilisateurs réagissent devant le logiciel pour décider ensemble de la suite.

### 3.2 Le Recueil de Feedbacks et la Réorientation du Backlog
L'intérêt majeur d'une livraison courte réside dans le feedback direct. Face à l'écran, les utilisateurs émettent des remarques spontanées (*« Le texte est un peu petit sur smartphone »*, *« J'aimerais pouvoir cacher les tâches terminées sans les effacer »*).

Le Product Owner recueille ces retours et les traduit immédiatement en ajustements dans le Product Backlog :
- Création de nouvelles User Stories.
- Réordonnancement des priorités pour le sprint suivant.
- Clarification ou durcissement de certains critères d'acceptation.

### 3.3 La Sprint Retrospective : L'inspection du collectif de travail
Juste après la revue du produit, l'équipe se réunit seule avec le Scrum Master pour la **Sprint Retrospective**.

Tandis que la Revue inspecte le **produit**, la Rétrospective inspecte **l'équipe et ses méthodes de travail** : la communication interne, les outils techniques, la fluidité du tableau Kanban et l'ambiance générale.

Pour qu'une rétrospective porte ses fruits, le Scrum Master instaure un climat de **sécurité psychologique** basé sur la Directive Première de la Rétrospective (Norman Kerth) :
> *"Quelles que soient les erreurs commises, nous comprenons et croyons sincèrement que chacun a fait de son mieux, compte tenu de ce qu'il savait, de ses compétences et des ressources disponibles à ce moment-là."*

L'équipe analyse son travail autour de 3 axes fondamentaux :
1. **Ce qui a bien fonctionné :** Les succès, bonnes pratiques et automatismes à préserver.
2. **Ce qui a posé des difficultés :** Les ralentissements, incompréhensions ou bugs techniques rencontrés.
3. **Ce que nous voulons améliorer :** Les actions concrètes à mettre en œuvre dès demain.

### 3.4 Le Plan d'Actions d'Amélioration : Limiter pour réussir
Une erreur courante consiste à lister 15 bonnes résolutions vagues que personne n'appliquera. 

La règle d'or de l'amélioration continue consiste à choisir **2 à 3 actions correctives concrètes et mesurables au maximum**. Ces actions sont alors inscrites directement dans le Sprint Backlog du sprint suivant comme des tâches prioritaires.

---

## 4. Pratique & Réalisation Guidée (Cas d'école TodoList)

Voici le déroulé complet de la clôture du **Sprint 1** de l'application **TodoList** :

| Étape | Action d'ingénierie agile | Décision prise sur la TodoList | Résultat opérationnel |
| :-: | :--- | :--- | :--- |
| 1 | Animer la Sprint Review en direct | Démonstration live de la saisie, de l'affichage et du cochage de 3 tâches réelles | Validation officielle des stories US-01, US-02 et US-03 par le Product Owner |
| 2 | Contrôler la Definition of Done | Contrôle visuel 375px mobile, console d'inspection 0 erreur, code sémantique | 100% des critères DoD validés |
| 3 | Collecter les feedbacks utilisateurs | Remarque d'un utilisateur sur le besoin d'isoler les tâches actives | US-04 (Filtrage) avancée en priorité numéro 1 pour le Sprint 2 |
| 4 | Conduire la Sprint Retrospective | Bilan transparent : réussite du découpage court, mais test responsive trop tardif | Vote de 3 actions concrètes pour le Sprint 2 |

### 4.1 Déroulement de la Démonstration Live (Sprint Review)
1. **Scénario d'usage :** Devant les utilisateurs, le développeur ouvre l'application dans le navigateur et saisit 3 tâches : *« Acheter du pain »*, *« Réviser cours Scrum »*, *« Finaliser CSS responsive »*. Chaque saisie est validée par la touche Entrée. Les éléments s'insèrent immédiatement dans la liste et le compteur affiche *« 3 tâches restantes »*.
2. **Scénario de cochage :** Le développeur clique sur la case de la deuxième tâche (*« Réviser cours Scrum »*). Le texte se barre instantanément, sa couleur s'atténue et le compteur s'ajuste à *« 2 tâches restantes »*.
3. **Contrôle de conformité DoD :**
   - Bascule en mode simulation mobile (375 x 667 px) : la mise en page s'adapte sans ascenseur horizontal.
   - Ouverture des DevTools : l'onglet Console affiche un journal 100% propre (zéro warning, zéro message d'erreur rouge).
   - **Verdict du PO :** Les 3 User Stories sont formellement acceptées. Le Sprint Goal du Sprint 1 est pleinement atteint.

### 4.2 Feedbacks Utilisateurs & Arbitrage Backlog pour le Sprint 2
- **Feedback 1 (Besoin ergonomique) :** L'utilisateur constate que lorsque la liste grandit, les tâches terminées encombrent visuellement l'espace. Il demande de pouvoir masquer les tâches faites.
  - *Décision PO :* La story **US-04 (Filtrage 3 vues)** est immédiatement placée en première position du Sprint 2.
- **Feedback 2 (Accessibilité tactile) :** Sur smartphone, le bouton d'ajout est jugé un peu étroit pour les gros pouces.
  - *Décision PO :* Une micro-tâche d'agrandissement de la zone tactile (taille minimale de 44x44px) est ajoutée à la dette CSS pour le Sprint 2.

### 4.3 Rétrospective d'Équipe du Sprint 1 (Bilan Réflexif)

#### Ce qui a bien fonctionné (À conserver) :
- Le découpage en micro-tâches courtes (1h à 2h30) a permis une visibilité parfaite de l'avancement chaque matin.
- La communication lors du Daily Scrum : le bug de soumission du formulaire a été identifié et débloqué en 10 minutes grâce à l'intervention du Scrum Master.
- La clarté de la Definition of Done a évité les débats subjectifs sur la qualité du code.

#### Ce qui a posé des difficultés (Axes de progrès) :
- Les tests d'adaptation mobile n'ont été exécutés qu'à la fin du sprint sur la tâche T-09, ce qui a imposé des retouches CSS de dernière minute sous pression.
- L'oubli initial du rafraîchissement formulaire (`e.preventDefault()`) aurait pu être anticipé par une réflexion préalable sur le comportement des événements DOM.

#### Les 3 Actions d'Amélioration Concrètes pour le Sprint 2 :
1. **Action 1 [Organisationnelle] :** Vérifier l'affichage responsive (vue mobile 375px) dans les DevTools dès la fin de chaque sous-tâche CSS, sans attendre l'étape finale de test.
2. **Action 2 [Technique] :** Écrire la signature des fonctions d'événements et documenter les interactions DOM avant d'écrire le code fonctionnel.
3. **Action 3 [Priorisation] :** Préparer la persistance LocalStorage (US-06) pour le Sprint 3 afin de garantir la sauvegarde des données entre deux sessions.

---

## 5. Livrables de Référence Produits & Critères

- **Fiche technique d'atelier** : `ua-lab/scrum/initiation-scrum/revue-retrospective/revue-retrospective.md`
- **Diaporama Marp de restitution** : `ua-lab/scrum/initiation-scrum/revue-retrospective/presentation-revue-retrospective.md`
- **Critères de réussite validés** :
  - [x] Démonstration en direct de l'incrément opérationnel avec validation stricte de la DoD.
  - [x] Collecte et traçabilité des feedbacks utilisateurs traduits dans le Product Backlog.
  - [x] Bilan réflexif de la rétrospective conduit avec franchise et bienveillance.
  - [x] 3 actions concrètes et mesurables adoptées pour l'amélioration du Sprint 2.
  - [x] Fichiers en UTF-8 sans BOM et conformes à l'ensemble des règles du projet.

## 6. Glossaire Pédagogique
- **Sprint Review :** Cérémonie d'inspection du produit en direct réunissant l'équipe et les parties prenantes pour valider l'incrément réalisé.
- **Incrément Opérationnel :** Version concrète, testée et immédiatement utilisable du logiciel répondant à la Definition of Done.
- **Feedback :** Retour d'expérience formulé par les utilisateurs permettant d'adapter la trajectoire du produit.
- **Sprint Retrospective :** Cérémonie interne d'inspection de l'équipe dédiée à l'amélioration continue de ses méthodes et de sa communication.
- **Sécurité Psychologique :** Climat de confiance au sein d'une équipe où chacun peut exprimer ses doutes, difficultés et erreurs sans crainte de jugement.
- **Plan d'Actions d'Amélioration :** Sélection restreinte de 2 à 3 mesures correctives concrètes intégrées en priorité dans le prochain sprint.
"""

PRES_5_MD = """---
layout: presentation
title: "Présentation : T.351.115 — Sprint Review et Rétrospective (Cas TodoList)"
marp: true
theme: default
paginate: true
header: "T.351.115 : Sprint Review et Rétrospective"
footer: "Scrum & Ingénierie Agile"
nav_exclude: true
---

<!-- _class: lead -->
# T.351.115 : Valider l'incrément, animer la Sprint Review et la Rétrospective
### Cas d'étude didactique : Application TodoList
**Unité d'Apprentissage : UA.351.11 — Initiation Scrum**

- **Public** : Développeurs Web (Niveau N3)
- **Domaine** : Scrum & Ingénierie Agile (`D.351.1`)
- **Compétence** : `C.351` — Piloter et animer la démarche Scrum

---

## 1. La Sprint Review : Démo en direct du produit

- **La règle d'or Scrum :**
  - Pas de slides abstraites ni de captures d'écran statiques.
  - Démonstration en direct d'un **logiciel opérationnel**.

- **Démonstration du Sprint 1 (TodoList) :**
  - Ajout en direct de 3 tâches réelles avec touche Entrée.
  - Cochage d'une tâche avec bascule visuelle barrée immédiate.
  - Mise à jour instantanée du compteur de tâches actives.

---

## 2. Validation de la Definition of Done (DoD)

- **Contrôle qualité en direct avec le Product Owner :**
  - [x] **Affichage responsive :** Écran mobile 375px parfait sans scroll horizontal.
  - [x] **Console DevTools :** Zéro warning, zéro erreur JavaScript.
  - [x] **Critères d'acceptation :** 100% validés sur US-01, US-02 et US-03.
  - [x] **Code source :** Balisage HTML5 sémantique et styles CSS propres.

> **Verdict du Product Owner :** Sprint Goal validé, incrément accepté !

---

## 3. Feedbacks Utilisateurs & Ajustements Backlog

- **Remarques collectées pendant la démonstration :**
  - *« Les tâches terminées encombrent la liste au fil de la journée. »*
  - *« Le bouton Ajouter est un peu petit sur écran tactile. »*

- **Impacts immédiats sur le Product Backlog :**
  - L'US-04 (Filtrage Toutes / En cours / Terminées) passe en **priorité 1** du Sprint 2.
  - Ajustement CSS de la zone tactile (44x44px minimum) planifié.

---

## 4. La Sprint Retrospective : L'amélioration d'équipe

- **Directive Première de la Rétrospective :**
  - Bienveillance, transparence et sécurité psychologique.

- **Bilan réflexif du Sprint 1 :**
  - **Points forts :** Découpage court en 9 micro-tâches, réactivité au Daily Scrum.
  - **Axe de progrès :** Tests mobiles réalisés trop tardivement en fin de sprint.

- **Les 3 Actions d'Amélioration pour le Sprint 2 :**
  1. Contrôle systématique en vue mobile (375px) dès chaque sous-tâche CSS.
  2. Spécification des événements DOM avant l'écriture du JavaScript.
  3. Cadrage de la persistance LocalStorage pour le Sprint 3.

---

<!-- _class: lead -->
# Synthèse du Cycle Scrum Complet
### Bilan de l'Unité d'Apprentissage UA.351.11

- De la Vision Produit à la Rétrospective, le cadre Scrum garantit :
  - La livraison régulière de **valeur concrète**.
  - La **transparence** totale de l'avancement.
  - L'**adaptation continue** aux besoins réels.
"""

VERSION_5_YML = """revue-retrospective.md: "1.0.0"
presentation-revue-retrospective.md: "1.0.0"
"""

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

if __name__ == "__main__":
    files_to_write = [
        # Milestone 2
        (os.path.join(BASE_DIR, r"_tutos\D.351.1.scrum\UA.351.11\T.351.112\vision-besoins.md"), TUTO_2_MD),
        (os.path.join(BASE_DIR, r"ua-lab\scrum\initiation-scrum\vision-besoins\vision-besoins.md"), LAB_2_MD),
        (os.path.join(BASE_DIR, r"ua-lab\scrum\initiation-scrum\vision-besoins\presentation-vision-besoins.md"), PRES_2_MD),
        (os.path.join(BASE_DIR, r"ua-lab\scrum\initiation-scrum\vision-besoins\version.yml"), VERSION_2_YML),
        
        # Milestone 3
        (os.path.join(BASE_DIR, r"_tutos\D.351.1.scrum\UA.351.11\T.351.113\product-backlog.md"), TUTO_3_MD),
        (os.path.join(BASE_DIR, r"ua-lab\scrum\initiation-scrum\product-backlog\product-backlog.md"), LAB_3_MD),
        (os.path.join(BASE_DIR, r"ua-lab\scrum\initiation-scrum\product-backlog\presentation-product-backlog.md"), PRES_3_MD),
        (os.path.join(BASE_DIR, r"ua-lab\scrum\initiation-scrum\product-backlog\version.yml"), VERSION_3_YML),
        
        # Milestone 4
        (os.path.join(BASE_DIR, r"_tutos\D.351.1.scrum\UA.351.11\T.351.114\sprint-planning-execution.md"), TUTO_4_MD),
        (os.path.join(BASE_DIR, r"ua-lab\scrum\initiation-scrum\sprint-planning-execution\sprint-planning-execution.md"), LAB_4_MD),
        (os.path.join(BASE_DIR, r"ua-lab\scrum\initiation-scrum\sprint-planning-execution\presentation-sprint-planning-execution.md"), PRES_4_MD),
        (os.path.join(BASE_DIR, r"ua-lab\scrum\initiation-scrum\sprint-planning-execution\version.yml"), VERSION_4_YML),
        
        # Milestone 5
        (os.path.join(BASE_DIR, r"_tutos\D.351.1.scrum\UA.351.11\T.351.115\revue-retrospective.md"), TUTO_5_MD),
        (os.path.join(BASE_DIR, r"ua-lab\scrum\initiation-scrum\revue-retrospective\revue-retrospective.md"), LAB_5_MD),
        (os.path.join(BASE_DIR, r"ua-lab\scrum\initiation-scrum\revue-retrospective\presentation-revue-retrospective.md"), PRES_5_MD),
        (os.path.join(BASE_DIR, r"ua-lab\scrum\initiation-scrum\revue-retrospective\version.yml"), VERSION_5_YML),
    ]
    
    for path, content in files_to_write:
        write_utf8_file(path, content.strip() + "\n")
    
    print("\\nAll 16 files for Milestones 2-5 have been generated successfully!")
