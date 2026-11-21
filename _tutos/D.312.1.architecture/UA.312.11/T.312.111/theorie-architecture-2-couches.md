---
layout: tuto
title: "Théorie : Architecture 2 couches & ADR"
sous_titre: "Comprendre le découpage architectural en deux couches, les principes SOLID et la formalisation des choix techniques"
slug: "separation-responsabilites"
slug_domaine: "architecture"
slug_ua: "deux-couches"
permalink: /tutos/separation-responsabilites/
tuto_id: "T.312.111"
version: "normal"
ua: "UA.312.11"
maturite: "lab"
type: "tuto-atelier"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Travail à faire
Effectuer les recherches documentaires nécessaires, concevoir une fiche de synthèse personnelle et préparer un diaporama de restitution Marp expliquant le principe de séparation des responsabilités (SoC), les risques de dette technique liés aux « contrôleurs obèses » (*Fat Controllers*), l'intérêt du patron Classe Service pour découpler l'accès aux données de l'orchestration HTTP, et la méthode de traçabilité des décisions stratégiques par les ADRs (*Architecture Decision Records*).

## 2. Notions fondamentales
- **Le Patron Architectural en 2 Couches :**
  - **Couche Présentation (Contrôleur HTTP mince) :** Réceptionne la requête entrante, valide les paramètres élémentaires, délègue immédiatement le traitement métier à la couche Service et retourne la réponse (vue Blade ou redirection). Il ne contient aucun code SQL, aucun algorithme de calcul lourd, ni accès direct au système de fichiers.
  - **Couche Métier & Abstraction des Données (Classe Service) :** Encapsule l'accès aux données et applique les règles métier. En Sprint 1, elle abstrait la lecture du fichier tabulaire `articles.csv` pour permettre une transition transparente vers un ORM/SGBD relationnel au sprint suivant sans impacter le contrôleur.
- **Principe de Séparation des Responsabilités (SoC / Single Responsibility Principle) :**
  - Chaque classe et chaque couche logicielle doit avoir une responsabilité unique et un seul motif de changement.
  - Le découplage permet de tester unitairement la logique métier sans dépendre de l'environnement HTTP (requêtes, sessions, cookies).
- **Structure Canonique d'un ADR (Architecture Decision Record) :**
  - *Titre :* ADR-01 — Choix d'une architecture en deux couches avec persistance transitoire CSV.
  - *Statut :* Proposé / Accepté / Remplacé.
  - *Contexte :* Problématique technique et contraintes de démarrage du premier sprint.
  - *Décision :* Solution technique retenue et règles d'implémentation.
  - *Conséquences :* Bénéfices obtenus (simplicité, rapidité d'amorce, testabilité) et compromis acceptés (absence de transactions relationnelles).
  - *Alternatives écartées :* Pourquoi l'installation immédiate d'un SGBD MySQL a été reportée au Sprint 2.

## 3. Recherches à effectuer
- Analyser les risques de couplage fort et de régression logicielle provoqués par les *Fat Controllers* en milieu professionnel.
- Étudier les différences entre le patron Classe Service et le patron Repository dans l'écosystème Laravel.
- Comparer les avantages et inconvénients d'un amorçage rapide par source de données tabulaire CSV face à un schéma relationnel avec migrations.

## 4. Livrable attendu
- **Fiche technique de synthèse :** `ua-lab/architecture/deux-couches/separation-responsabilites/separation-responsabilites.md` sur la branche `sprint1`.
- **Diaporama Marp de restitution :** `ua-lab/architecture/deux-couches/separation-responsabilites/presentation-separation-responsabilites.md` sur la branche `sprint1`.
- **Contenu attendu :** Synthèse personnelle structurée reprenant les notions fondamentales (découpage 2 couches, SoC, formalisme ADR) et les réponses argumentées aux recherches à effectuer.
