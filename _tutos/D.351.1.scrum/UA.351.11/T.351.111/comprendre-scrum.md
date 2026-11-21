---
layout: tuto
title: "Comprendre l'approche Agile et le cadre Scrum"
sous_titre: "Assimiler la rupture Agile vs Cascade, les 3 rôles Scrum et les 5 événements sur l'application TodoList"
slug: "comprendre-scrum"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
permalink: /tutos/comprendre-scrum/
tuto_id: "T.351.111"
version: "normal"
ua: "UA.351.11"
type: "tuto-atelier-notions"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint0"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
sprint: "Sprint 0"
statut_realisation: "realise"
livrables:
  - chemin: "ua-lab/scrum/initiation-scrum/comprendre-scrum/comprendre-scrum.md"
    version: "1.0.0"
  - chemin: "ua-lab/scrum/initiation-scrum/comprendre-scrum/presentation-comprendre-scrum.md"
    version: "1.0.0"
---

## 1. Travail à faire

Dans cet atelier d'initiation, vous devez appréhender la démarche Agile et le fonctionnement opérationnel du cadre Scrum.  
Pour vous guider, une solution complète et commentée a été réalisée sur l'application didactique **TodoList**.

Votre travail consiste à :
1. **Consulter la solution de référence :** Prenez connaissance de la fiche technique et du diaporama de l'application TodoList disponibles dans l'encadré de consultation ci-dessous.
2. **Transposer la démarche sur votre Projet Technique individuel :**
   - Comparer l'impact du cycle en V et de l'approche Agile sur votre propre projet.
   - Identifier et cartographier les 3 rôles Scrum (Product Owner, Scrum Master, Développeurs) adaptés à votre contexte d'équipe.
   - Définir le rythme de vos sprints et le format de votre incrément logiciel.
3. **Formaliser vos livrables :** Rédiger votre fiche de synthèse et votre support de présentation dans votre espace de travail personnel : `tutoriels/scrum/initiation-scrum/comprendre-scrum/`.

## 2. Notions fondamentales

### A. Rupture Agile vs Approche Traditionnelle en Cascade (Cycle en V)
- **Le cycle en V (Cascade) :**
  - Le périmètre est figé au départ à travers un cahier des charges rigide.
  - Le client et les utilisateurs découvrent le logiciel uniquement à la fin (effet tunnel).
  - Tout changement en cours de route entraîne des coûts élevés et des retards importants.
- **L'approche Agile :**
  - Le travail est découpé en cycles courts et réguliers appelés **Sprints**.
  - À chaque fin de cycle, l'équipe produit un **incrément logiciel opérationnel**, visible et testable.
  - Les retours utilisateurs sont intégrés en continu pour faire évoluer le produit sans friction.

### B. Les 4 Valeurs du Manifeste Agile (2001)
1. **Les individus et leurs interactions** avant les processus et les outils.
2. **Un logiciel opérationnel** avant une documentation exhaustive.
3. **La collaboration avec les clients** avant la négociation contractuelle stricte.
4. **L'adaptation au changement** avant le suivi rigide d'un plan initial.

### C. Les 3 Rôles Centraux de Scrum
- **Le Product Owner (PO) :**
  - Porte la vision produit et représente les besoins des utilisateurs.
  - Rédige et priorise le Product Backlog selon la valeur métier.
  - Accepte ou rejette les fonctionnalités développées.
- **Le Scrum Master (SM) :**
  - Garantit l'application des règles et des valeurs du cadre Scrum.
  - Facilite les réunions et aide l'équipe à s'organiser de manière autonome.
  - Élimine les obstacles techniques ou méthodologiques qui ralentissent l'équipe.
- **L'Équipe de Développement :**
  - Équipe pluridisciplinaire responsable de la conception, du code et des tests.
  - Décide de la façon de réaliser techniquement les fonctionnalités retenues.
  - S'engage collectivement sur la qualité de l'incrément livré.

### D. Les 5 Événements Fondamentaux
1. **Le Sprint :** Le conteneur temporel régulier dans lequel tous les autres événements prennent place.
2. **Le Sprint Planning :** Réunion d'ouverture pour définir l'objectif du sprint (*Sprint Goal*) et sélectionner les éléments du backlog à réaliser.
3. **Le Daily Scrum :** Point synchronisé quotidien de 15 minutes pour inspecter l'avancement et lever les blocages.
4. **La Sprint Review :** Démonstration en direct de l'incrément fonctionnel aux parties prenantes pour recueillir leurs retours.
5. **La Sprint Retrospective :** Réunion d'amélioration continue pour analyser le fonctionnement interne de l'équipe et adopter 2 à 3 actions correctives.

## 3. Application pratique sur le cas d'étude (Exemple TodoList)

Pour visualiser concrètement ces principes sur un cas épuré, étudions le développement d'une application **TodoList** (gestionnaire de tâches) :

- **Pourquoi le cycle en V échoue sur une TodoList :**
  - Si vous spécifiez toutes les fonctionnalités à l'avance (sous-tâches, synchronisation cloud, rappels), vous livrez après des mois un outil trop complexe alors que l'utilisateur voulait simplement cocher une tâche rapidement sur mobile.
  - En Agile, le premier sprint livre l'essentiel : ajouter et afficher une tâche. Les besoins réels (ex : filtrer les tâches actives) sont constatés dès la première démonstration.
- **Les Rôles appliqués à la TodoList :**
  - *Product Owner :* Définit l'expérience utilisateur idéale et priorise les actions d'ajout et de suppression.
  - *Scrum Master :* S'assure que le tableau de suivi Kanban est à jour et que l'équipe ne se disperse pas.
  - *Développeurs :* Conçoivent l'interface HTML/CSS et le comportement JavaScript réactif.

{% include tuto-livrables.html %}

## 4. Pistes de recherche active

Pour préparer votre transposition sur votre Projet Technique, investiguez les questions suivantes :
1. Quels sont les 3 risques majeurs identifiés si votre projet technique était développé selon un cycle en V classique ?
2. Dans le cadre de votre formation, qui jouera le rôle de Product Owner (partie prenante / formateur) pour arbitrer vos choix de fonctionnalités ?
3. Quelle est la plus petite fonctionnalité de votre projet qui constitue un incrément logiciel utilisable dès la fin d'un premier sprint ?

## 5. Livrables attendus & Critères d'acceptation

### Livrables à produire sur votre Projet Technique
- **Fiche technique de cadrage :** `tutoriels/scrum/initiation-scrum/comprendre-scrum/comprendre-scrum.md`
- **Diaporama de présentation :** `tutoriels/scrum/initiation-scrum/comprendre-scrum/presentation-comprendre-scrum.md`

### Critères d'acceptation
- [ ] La comparaison entre cycle en V et démarche itérative est appliquée de façon concrète à votre propre projet.
- [ ] Les 3 rôles Scrum sont précisément affectés et décrits pour votre équipe de développement.
- [ ] Les 5 rituels Scrum sont planifiés avec leurs objectifs spécifiques.
- [ ] Le support de présentation est rédigé au format Marp (16:9) sans surcharge de texte.
