---
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
