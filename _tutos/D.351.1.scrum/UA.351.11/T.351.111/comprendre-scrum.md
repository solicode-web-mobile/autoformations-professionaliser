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

## 1. Contexte & Enjeux
Dans le développement logiciel moderne, la gestion de projet traditionnelle en cascade (cycle en V) montre rapidement ses limites face à l'évolution constante des besoins utilisateurs. Cet atelier introduit la rupture fondamentale apportée par le Manifeste Agile et pose le cadre méthodologique Scrum : ses 3 piliers empiriques, ses 3 rôles clés et ses 5 événements réguliers.

## 2. Notions fondamentales

### A. Rupture Agile vs Approche en Cascade (Cycle en V)
- **Le cycle en V (Cascade) :** Spécifications initiales exhaustives, conception puis réalisation en tunnel. Le client découvre le produit tardivement, avec un risque majeur d'inadéquation ou de dérive calendaire.
- **La démarche Agile :** Progression itérative et incrémentale par cycles courts (**Sprints**). Chaque cycle produit un incrément logiciel fonctionnel, testé et vérifié. Les retours utilisateurs sont intégrés en continu.

### B. Les 4 Valeurs du Manifeste Agile (2001)
1. **Les individus et leurs interactions** de préférence aux processus et aux outils.
2. **Un logiciel opérationnel** de préférence à une documentation exhaustive.
3. **La collaboration avec les clients** de préférence à la négociation contractuelle.
4. **L'adaptation au changement** de préférence au suivi d'un plan initial.

### C. Les 3 Piliers du Cadre Scrum
- **Transparence :** Tous les aspects critiques du projet sont visibles et partagés.
- **Inspection :** Vérification fréquente des artéfacts et de l'avancement.
- **Adaptation :** Ajustement immédiat en cas d'écart constaté par rapport aux objectifs.

### D. Les 3 Rôles Centraux de Scrum
- **Product Owner (PO) :** Porte la vision produit, recueille les besoins utilisateurs et ordonne les priorités dans le Product Backlog selon la valeur métier.
- **Scrum Master (SM) :** Facilitateur et garant du cadre Scrum, anime les rituels et élimine les blocages de l'équipe de développement.
- **Développeurs :** Équipe pluridisciplinaire et autonome responsable de la conception, du code et des tests techniques pour livrer un incrément de qualité.

### E. Les 5 Événements Fondamentaux
1. **Le Sprint :** Boîte de temps fixe (timebox) contenant tous les autres événements.
2. **Le Sprint Planning :** Cadrage du Sprint Goal et sélection des fonctionnalités à réaliser.
3. **Le Daily Scrum :** Point de synchronisation quotidien de 15 minutes pour lever les obstacles.
4. **La Sprint Review :** Démonstration en direct de l'incrément fonctionnel aux parties prenantes.
5. **La Sprint Retrospective :** Réunion d'amélioration continue pour adopter 2 à 3 actions correctives.

## 3. Application didactique : Cas d'étude TodoList
Pour illustrer concrètement ces principes, l'atelier s'appuie sur le développement d'une application **TodoList** (gestionnaire de tâches) :
- Démonstration de l'échec d'un cycle en V face aux besoins réels d'une TodoList épurée.
- Cartographie des responsabilités des 3 rôles pour l'équipe TodoList.
- Cadrage d'un Sprint 1 livrant un MVP opérationnel (saisie, affichage et validation).

{% include tuto-livrables.html %}

## 4. Pistes de recherche active
- Analyser les 3 risques majeurs d'un développement en cascade sur votre propre projet.
- Identifier qui incarne le rôle de Product Owner dans votre contexte de projet.
- Déterminer quelle fonctionnalité minimale constitue votre premier incrément logiciel utilisable.

## 5. Livrables attendus & Critères de validation
- **Livrables à produire :**
  - Fiche technique de cadrage : `tutoriels/scrum/initiation-scrum/comprendre-scrum/comprendre-scrum.md`
  - Diaporama de restitution Marp : `tutoriels/scrum/initiation-scrum/comprendre-scrum/presentation-comprendre-scrum.md`
- **Critères de validation :**
  - [ ] La rupture entre cycle en V et démarche agile est explicitée de manière concrète.
  - [ ] Les responsabilités des 3 rôles Scrum sont clairement identifiées.
  - [ ] Les 5 rituels Scrum sont planifiés avec leurs objectifs respectifs.
  - [ ] Le support Marp est rédigé au format 16:9 et prêt pour la soutenance.
