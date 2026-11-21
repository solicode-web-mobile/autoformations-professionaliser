---
layout: tuto
title: "Sprint Retrospective et dette d'empathie"
sous_titre: "Animer la rétrospective réflexive et acter la dette d'empathie utilisateur"
slug: "retrospective-reflexive"
slug_domaine: "realisation-projet"
slug_ua: "cloture-sprint"
permalink: /tutos/retrospective-reflexive/
tuto_id: "T.351.232"
version: "normal"
ua: "UA.351.23"
maturite: "projet"
type: "tuto-tache"
nav_order: 2
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Objectif Opérationnel & Prérequis
- **Position dans le flux :** Phase D — Clôture de Sprint, Rétrospective & Bilan / Étape 12.2 — Analyse Réflexive.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `scrum/retrospective-s1.md`.
- **Objectif :** Animer la rétrospective réflexive d'équipe, identifier les axes d'amélioration continue et formaliser le constat didactique de « dette d'empathie utilisateur » justifiant l'introduction de la démarche de Design Thinking au Sprint 2.
- **Prérequis :** Démonstration validée en Sprint Review (`T.351.231`).

## 2. Déroulement Pas-à-Pas de la Tâche

1. **Étape 1 — Collecte des Retours d'Équipe :**  
   Examinez le déroulement du Sprint 1 selon 3 axes réflexifs :
   - *Ce qui a bien fonctionné :* Rapidité de scaffolding avec Artisan, découplage net Contrôleur/Service, outillage par les skills agentiques.
   - *Ce qui a posé difficulté :* Parsing manuel du fichier CSV, calibration du gabarit Blade sans maquette préalable.
   - *Ce qu'il faut améliorer pour le Sprint 2 :* Définir les besoins à partir de tests utilisateurs réels avant de coder.

2. **Étape 2 — Analyse Réflexive de la Dette d'Empathie Utilisateur :**  
   Constatez collectivement la limite de la méthode actuelle :
   - L'écran de consultation d'un article a été développé uniquement à partir d'hypothèses de développeurs, sans phase d'immersion ni entretien avec de véritables lecteurs ou lauréats.
   - Ce constat formalise la **dette d'empathie utilisateur** et démontre la nécessité méthodologique d'intégrer le Design Thinking (Immersion, Idéation, Prototypage) au démarrage du Sprint 2.

3. **Étape 3 — Formalisation du Rapport de Rétrospective :**  
   Rédigez le compte-rendu dans `scrum/retrospective-s1.md` en consignant les 3 actions concrètes d'amélioration d'équipe retenues pour le prochain sprint.

## 3. Livrables & Critères de Réussite
- **Livrable attendu :**
  - Compte-rendu de rétrospective : `scrum/retrospective-s1.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Les 3 axes de la rétrospective (succès, freins, actions concrètes) sont documentés avec rigueur.
  - [ ] Le constat de dette d'empathie utilisateur est clairement explicité.
  - [ ] Le compte-rendu prépare méthodologiquement l'introduction du Design Thinking en Session S02.
