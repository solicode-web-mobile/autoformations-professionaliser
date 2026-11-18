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
maturite: "UA-Lab"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase B — Analyse, Conception & Planification / Étape 3.1 — Découplage Architectural.
- **Branche Git :** `sprint1`
- **Stack mobilisée :** Principes SOLID (Single Responsibility), architecture 2 couches (Contrôleur / Service), formalisme ADR.

## 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches nécessaires et formaliser une fiche de synthèse expliquant le principe de séparation des responsabilités, les dangers des « contrôleurs obèses » (*Fat Controllers*), l'intérêt du patron Classe Service pour isoler l'accès aux données et la méthodologie de traçabilité des choix par les ADRs.

## 3. Répartition Didactique (Règle des 20/80)

### Les 20% fournis directement au tutoriel :
- **Architecture 2 couches :**
  - **Couche Présentation (Contrôleur HTTP mince) :** Réceptionne la requête HTTP, valide les entrées élémentaires, délègue le traitement métier au Service et retourne la réponse (vue Blade ou redirection). Il ne contient aucune logique de persistance ni algorithme métier lourd.
  - **Couche Métier / Données (Classe Service) :** Encapsule l'accès aux données et la logique métier. En Sprint 1, elle abstrait la lecture du fichier tabulaire `articles.csv` pour préparer une transition transparente vers un ORM/SGBD au sprint suivant.
- **Principe SoC (Separation of Concerns) :** Chaque composant logiciel doit avoir une responsabilité unique et bien délimitée.
- **Structure canonique d'un ADR (Architecture Decision Record) :** Titre, Statut (Accepté), Contexte, Décision retenue, Conséquences (positives et négatives), Alternatives écartées.

### Les 80% recherchés par l'apprenant :
- Analyser les risques de dette technique liés aux *Fat Controllers* (couplage fort, impossibilité de tester unitairement, non-réutilisabilité).
- Comparer les bénéfices et compromis d'un amorçage rapide par source tabulaire CSV par rapport à l'installation immédiate d'un SGBD relationnel.

## 4. Livrable Attendu
- Fiche de synthèse d'architecture intégrée dans le journal d'apprentissage personnel de l'apprenant.