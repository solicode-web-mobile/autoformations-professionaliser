---
layout: tuto
title: "Création du prompt-back-end"
sous_titre: "Concevoir le prompt d'ingénierie prompt-back-end pour générer la couche service, le contrôleur mince et les routes"
slug: "prompt-backend"
slug_domaine: "laravel"
slug_ua: "tranche-verticale"
permalink: /tutos/prompt-backend/
tuto_id: "T.321.133"
version: "normal"
ua: "UA.321.13"
maturite: "UA-Lab"
nav_order: 3
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.3 — Automatisation Backend.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-back-end.prompt.md`

## 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-back-end.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de générer l'ensemble de la couche backend d'une entité (Service, Contrôleur avec injection IoC, Route et gestion 404).

## 3. Missions Concrètes Réalisées par le Prompt
1. Générer la classe Service métier encapsulant l'accès aux données tabulaires avec typage strict PHP 8.3 (`?array`).
2. Générer le contrôleur HTTP mince avec injection de dépendances IoC et déclenchement d'erreur `abort(404)`.
3. Déclarer la route web paramétrée avec contrainte numérique `whereNumber()` et nommage explicite `name(...)`.

## 4. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Développeur Backend Laravel 12 senior expert en Clean Code et conteneur IoC.
- **Instruction :** Prendre en entrée les spécifications d'une entité métier `[ENTITE_METIER]` et générer le code PHP complet (Service, Contrôleur, Route) sans omission de typage.
- **Output :** Fichiers PHP complets avec chemins stricts.
- **Contraintes Négatives :** Zéro logique de persistance dans le contrôleur ; interdiction de retourner des tableaux non typés.

## 5. Critères de Validation
- [ ] Le fichier `livrables/ia/prompts/prompt-back-end.prompt.md` est testé et validé sur la branche `sprint1`.
- [ ] Le code backend produit s'exécute sans erreur de syntaxe ni avertissement de typage.