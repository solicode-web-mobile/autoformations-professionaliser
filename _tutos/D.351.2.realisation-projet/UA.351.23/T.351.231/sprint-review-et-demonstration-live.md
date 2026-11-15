---
layout: tuto
title: "Sprint Review et démonstration live"
sous_titre: "Conduire la démonstration de l'incrément fonctionnel et valider la Definition of Done"
slug: "sprint-review-et-demonstration-live"
permalink: /tutos/sprint-review-et-demonstration-live/
tuto_id: "T.351.231"
version: "normal"
ua: "UA.351.23"
maturite: "UA-Tâche"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Objectif Opérationnel & Prérequis
- **Position dans le flux :** Phase D — Clôture de Sprint, Rétrospective & Bilan / Étape 5.1 — Démonstration Live.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `scrum/revue-s1.md`
- **Objectif :** Conduire la démonstration live de l'incrément face au formateur Product Owner et valider critère par critère la DoD.
- **Prérequis :** Code applicatif Laravel 12 stabilisé sur la branche `sprint1`.

## 2. Déroulement Pas-à-Pas de la Tâche
1. **Étape 1 — Préparation de la Démonstration :** Démarrer le serveur de test local (`php artisan serve`) et s'assurer que les jeux de données tabulaires CSV sont présents.
2. **Étape 2 — Conduite de la Démonstration :** Présenter l'accès à la page d'accueil, la navigation vers un article existant (scénario nominal) et le comportement lors de la saisie d'un identifiant inexistant (scénario d'erreur 404 propre).
3. **Étape 3 — Émargement de la DoD :** Auditer et valider formellement les 7 critères bloquants dans le procès-verbal `scrum/revue-s1.md`.

## 3. Livrables & Critères de Réussite
- **Livrable attendu :** Procès-verbal de démonstration `scrum/revue-s1.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] L'incrément fonctionne en direct sans plantage ni régression.
  - [ ] Les 7 critères de la DoD sont validés avec le formateur Product Owner.