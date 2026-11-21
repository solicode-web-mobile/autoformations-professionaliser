---
layout: default
title: "Fiche d'Atelier : T.351.111 — Comprendre l'approche Agile et Scrum (Cas TodoList)"
tuto_id: "T.351.111"
type: "tuto-notion"
ua: "UA.351.11"
slug: "comprendre-scrum"
slug_domaine: "scrum"
slug_ua: "initiation-scrum"
---
# T.351.111 : Comprendre l'approche Agile et le cadre Scrum

- **Unité d'apprentissage** : [UA.351.11 — Initiation à la Démarche Agile et Cadre Scrum](#)
- **Diaporama de soutenance** : [presentation-comprendre-scrum.html](./presentation-comprendre-scrum.html)
- **Domaine** : Scrum & Méthodes Agiles
- **Cas d'étude didactique** : Application TodoList (Gestionnaire de tâches)

---

## 1. Contexte & Objectif de l'Atelier
Cet atelier d'initiation pose les fondations opérationnelles de l'ingénierie logicielle agile. L'objectif est d'assimiler la rupture avec le cycle en V traditionnel, de maîtriser la gouvernance des 3 rôles Scrum et de comprendre le cadencement des 5 rituels à travers l'étude concrète d'une application TodoList.

## 2. Données de Référence
- **Projet support** : Application TodoList (gestionnaire de tâches responsive).
- **Ressources associées** : Diaporama Marp de restitution interactif (`presentation-comprendre-scrum.md`).
- **Périmètre du Sprint 1** : Cadrage du MVP (ajout, affichage et validation d'achèvement d'une tâche).

## 3. Notions Essentielles

### 3.1 Pourquoi abandonner le Cycle en V pour l'Agilité ?
Dans le modèle classique en cascade (cycle en V), le projet avance par étapes séquentielles strictes : on commence par écrire un cahier des charges exhaustif de plusieurs dizaines de pages, puis on réalise l'architecture globale, on programme l'ensemble du code pendant des mois, et l'on ne teste l'application qu'à la toute fin.

Ce modèle pose un problème majeur : **l'effet tunnel**. Pendant plusieurs mois, le client et les utilisateurs ne voient rien fonctionner. Lorsqu'ils découvrent enfin le logiciel terminé, leurs besoins ont déjà changé, ou bien certaines fonctionnalités imaginées sur le papier se révèlent inutiles ou complexes à l'usage. Corriger le tir à ce stade coûte alors une énergie considérable et provoque d'importants retards.

L'**approche Agile** apporte une réponse concrète à ce danger. Au lieu de vouloir tout concevoir d'un coup, on découpe le développement en cycles courts et réguliers de 1 à 2 semaines appelés **Sprints**. À la fin de chaque Sprint, l'équipe livre une version réelle, testée et immédiatement utilisable du logiciel : **l'Incrément**. L'utilisateur teste cette version, donne son avis, et l'équipe adapte ses priorités pour le sprint suivant sans crise ni surcoût.

### 3.2 Les 4 Valeurs du Manifeste Agile expliquées
Rédigé en 2001 par dix-sept experts du logiciel, le Manifeste Agile repose sur 4 arbitrages fondamentaux :

1. **Les individus et leurs interactions avant les processus et les outils :** Une équipe qui se parle directement et résout un problème en 5 minutes est infiniment plus productive qu'une organisation où chacun attend une validation par formulaire ou par email.
2. **Un logiciel opérationnel avant une documentation exhaustive :** Pour l'utilisateur, une page web qui fonctionne et enregistre ses tâches a une valeur immédiate, alors qu'un document de 50 pages qui promet de le faire n'a aucune utilité pratique.
3. **La collaboration avec les clients avant la négociation contractuelle :** Plutôt que de se battre sur les termes figés d'un contrat initial, l'équipe travaille main dans la main avec le client comme un partenaire pour construire le meilleur produit possible.
4. **L'adaptation au changement avant le suivi rigide d'un plan :** Quand une nouvelle opportunité apparaît ou qu'une idée ne fonctionne pas, l'équipe agile sait faire pivoter ses priorités plutôt que de continuer aveuglément un plan devenu obsolète.

### 3.3 Les 3 Piliers Empiriques de Scrum
Scrum n'est pas une recette magique mais un cadre de travail basé sur l'empirisme (apprendre par l'expérience et les faits réels) :

- **La Transparence :** Tous les membres de l'équipe et les parties prenantes partagent le même niveau d'information. Le code est accessible sur GitHub, les tâches en cours sont affichées sur un tableau visible par tous, et les difficultés rencontrées ne sont jamais dissimulées.
- **L'Inspection :** L'équipe examine fréquemment l'état du produit et son rythme de travail pour repérer les anomalies dès qu'elles surviennent, et non pas après la livraison finale.
- **L'Adaptation :** Dès qu'un écart ou un problème est constaté lors d'une inspection, l'équipe ajuste immédiatement son code, ses priorités ou sa façon de travailler pour ne pas reproduire l'erreur.

### 3.4 Les 3 Rôles Clés de l'Équipe Scrum
Scrum redéfinit la gouvernance d'une équipe en supprimant la hiérarchie classique au profit de 3 responsabilités complémentaires :

- **Le Product Owner (PO) — Le responsable de la valeur :**
  Il représente les utilisateurs finaux et le client. C'est lui qui porte la vision du produit et décide de **CE QU'IL FAUT FAIRE** et dans quel ordre. Il rédige les besoins sous forme de User Stories dans le *Product Backlog*. Il ne dit jamais aux développeurs comment coder, mais il valide ou refuse chaque fonctionnalité démontrée.
- **Le Scrum Master (SM) — Le coach méthodologique :**
  Ce n'est pas un chef de projet autoritaire. Le Scrum Master est un facilitateur (un « serviteur-leader »). Son rôle est d'aider l'équipe à bien appliquer les règles Scrum, d'animer les réunions pour qu'elles restent courtes et productives, et surtout de **supprimer tous les obstacles** qui ralentissent les développeurs (problème d'environnement technique, accès manquant, conflit d'organisation).
- **L'Équipe de Développement — Les bâtisseurs du produit :**
  C'est un groupe autonome et pluridisciplinaire réunissant toutes les compétences nécessaires pour concevoir, coder et tester le produit (front-end, back-end, qualité). Ce sont les développeurs qui décident **COMMENT RÉALISER** techniquement le travail demandé par le PO. Ils s'engagent collectivement sur la qualité du code produit.

### 3.5 Les 5 Événements Fondamentaux d'un Sprint
Pour maintenir un rythme régulier sans passer ses journées en réunion, Scrum cadence le travail autour de 5 rituels à durée fixe (timeboxés) :

1. **Le Sprint :** La période de travail d'une durée invariable (1 à 2 semaines). Il sert de cadre temporel à tous les autres événements.
2. **Le Sprint Planning (Planification) :** Réunion d'ouverture du sprint où le PO présente ses priorités. L'équipe choisit ce qu'elle est capable de livrer et formule l'objectif du sprint (*Sprint Goal*).
3. **Le Daily Scrum (Mêlée quotidienne) :** Point debout de 15 minutes chaque matin où chaque développeur partage ce qu'il a fait la veille, ce qu'il compte faire aujourd'hui et les blocages qu'il rencontre.
4. **La Sprint Review (Revue de sprint) :** Démonstration en direct du logiciel fonctionnel devant les parties prenantes. Aucune présentation théorique abstraite : on manipule le vrai produit pour recueillir des retours concrets.
5. **La Sprint Retrospective (Rétrospective) :** Réunion interne à l'équipe juste après la revue. L'équipe analyse son propre fonctionnement (communication, outils, qualité) et choisit 2 à 3 actions concrètes pour s'améliorer dès le sprint suivant.

## 4. Pratique & Réalisation Guidée (Cas d'école TodoList)

Pour donner du sens à ces notions, le concepteur illustre la démarche sur le cas d'une application **TodoList** (gestionnaire de tâches) :

| Étape | Action d'ingénierie agile | Décision prise sur la TodoList | Résultat opérationnel |
| :-: | :--- | :--- | :--- |
| 1 | Analyser l'échec d'un cycle en V classique | Refus d'un cahier des charges de 30 pages avec options superflues (cloud, rappels) | Focalisation immédiate sur le besoin vital : noter et cocher une tâche |
| 2 | Répartir les 3 rôles Scrum pour l'équipe | Le PO priorise la saisie express, le SM anime le Kanban, les Devs créent l'interface HTML/CSS/JS | Rôles clairs sans chevauchement ni ambiguïté de responsabilité |
| 3 | Définir le Sprint Goal du premier sprint | « Livrer une version One-Page fonctionnelle pour ajouter, afficher et cocher ses tâches » | Objectif clair et motivant pour l'équipe |
| 4 | Établir la Definition of Done (DoD) | Interface responsive (375px mobile), code propre sans warning console, tests manuels validés | Critères de qualité stricts avant de déclarer une tâche terminée |

- **Analyse du risque d'effet tunnel :** Si nous avions passé 3 mois à développer une synchronisation multi-appareils avant de tester l'application, nous aurions découvert trop tard que le bouton d'ajout était trop petit sur smartphone. Grâce à Scrum, le premier sprint valide immédiatement la taille des boutons sur mobile.
- **Charte d'équipe adoptée :** Transparence totale sur la branche `sprint0` de GitHub, limitation du travail en cours (WIP) sur le tableau Kanban, et refus de déclarer une tâche terminée tant qu'elle ne satisfait pas à 100% à la Definition of Done.

## 5. Livrables de Référence Produits & Critères

- **Fiche technique d'atelier** : `ua-lab/scrum/initiation-scrum/comprendre-scrum/comprendre-scrum.md`
- **Diaporama Marp de restitution** : `ua-lab/scrum/initiation-scrum/comprendre-scrum/presentation-comprendre-scrum.md`
- **Critères de réussite validés** :
  - [x] Analyse comparative Cascade vs Agile appliquée à la TodoList.
  - [x] 3 rôles Scrum et 5 événements expliqués avec une narration pédagogique accessible.
  - [x] Zéro citation d'encadrant et d'établissement conformément aux normes du projet.

## 6. Glossaire Pédagogique
- **Sprint :** Boîte de temps fixe (généralement 1 à 2 semaines) pendant laquelle l'équipe conçoit, code et teste un incrément logiciel utilisable.
- **Product Owner :** Responsable qui porte la vision du produit et priorise le backlog selon la valeur utilisateur.
- **Scrum Master :** Facilitateur méthodologique garant du cadre Scrum et de la levée des obstacles.
- **Incrément :** Version concrète, vérifiée selon la Definition of Done et directement utilisable d'un produit.
- **Effet tunnel :** Risque majeur du cycle en V où l'utilisateur ne découvre le produit qu'à la livraison finale sans validation intermédiaire.
