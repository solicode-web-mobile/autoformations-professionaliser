---
layout: tuto
title: "Construire le Product Backlog initial selon INVEST et MoSCoW"
sous_titre: "Découper les exigences en User Stories testables avec critères d'acceptation et prioriser le carnet de produit"
slug: "construire-product-backlog-initial"
slug_domaine: "realisation-projet"
slug_ua: "vision-backlog-ui-flow"
permalink: /tutos/construire-product-backlog-initial/
tuto_id: "T.351.012"
version: "normal"
ua: "UA.351.01"
maturite: "UA-Tâche"
nav_order: 2
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
  - chemin: "scrum/product-backlog.md"
    version: "1.0.0"
  - chemin: "tutoriels/realisation-projet/vision-backlog-ui-flow/construire-product-backlog-initial/construire-product-backlog-initial.md"
    version: "1.0.0"
---

## 1. Travail à faire
Construire le carnet de produit initial (*Product Backlog*) du *Blog des Lauréats* avec le **Groupe 1** (Product Owner) : découper les exigences en User Stories respectant le standard INVEST, doter chaque story de critères d'acceptation précis, attribuer des Story Points sur l'échelle de Fibonacci, prioriser le carnet selon la grille MoSCoW et enregistrer le document sous `scrum/product-backlog.md`.

## 2. Notions fondamentales
- **Le Standard INVEST pour les User Stories :**
  - **I**ndependent (Indépendante), **N**egotiable (Négociable), **V**aluable (Porteuse de valeur), **E**stimable (Estimable), **S**mall (Courte / dimensionnée), **T**estable (Testable).
- **La Priorisation MoSCoW :**
  - **Must have :** Indispensable pour le MVP (ex : consultation publique d'un article en S1).
  - **Should have :** Forte valeur ajoutée mais non bloquant pour le premier incrément.
  - **Could have :** Fonctionnalité d'agrément réalisée si le temps le permet.
  - **Won't have :** Fonctionnalité exclue du périmètre actuel.
- **DoR et DoD :**
  - *Definition of Ready (DoR) :* Critères requis pour sélectionner une story en Sprint Planning.
  - *Definition of Done (DoD) :* Critères de conformité technique et fonctionnelle pour valider la livraison.

## 3. Application pratique sur le Blog des Lauréats
- **User Stories prioritaires du MVP (Must Have) :**
  - Consultation publique de la fiche détaillée d'un article via `/articles/{id}` (Cœur du Sprint 1).
  - Catalogue responsive des articles avec tri par catégories et lauréats.
  - Affichage du profil détaillé du lauréat auteur.
- **Arborescence cible :** Enregistrement sous `scrum/product-backlog.md`.

## 4. Livrables & Critères de validation
- **Livrables attendus :**
  - Product Backlog ordonné : `scrum/product-backlog.md sur la branche sprint0`.
  - Fiche de synthèse backlog : `tutoriels/realisation-projet/vision-backlog-ui-flow/construire-product-backlog-initial/construire-product-backlog-initial.md sur la branche sprint0`.
- **Critères de validation :**
  - [ ] Les User Stories respectent le formalisme canonique *En tant que... Je veux... Afin de...*.
  - [ ] Chaque story est estimée en Story Points et classée selon la méthode MoSCoW.
  - [ ] Les critères d'acceptation de chaque story du MVP sont testables sans ambiguïté.
