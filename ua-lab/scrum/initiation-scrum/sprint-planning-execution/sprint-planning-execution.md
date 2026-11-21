---
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
