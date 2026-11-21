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
maturite: "lab"
type: "tuto-atelier"
nav_order: 3
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Travail à faire
Concevoir et tester le prompt d'ingénierie réutilisable nommé `prompt-back-end.prompt.md` selon la méthode RIO.

Ce prompt est un composant agentique réutilisable permettant à un Agent IA de générer automatiquement la couche backend complète pour n'importe quelle entité métier du Projet Fil Rouge : classe Service avec lecture de données, contrôleur HTTP mince avec injection IoC, routage paramétré et déclenchement d'erreur 404.

## 2. Missions Concrètes Réalisées par le Prompt
1. Générer la classe Service métier encapsulant l'accès aux données tabulaires avec typage strict PHP 8.3 (`?array`, `array`).
2. Générer le contrôleur HTTP mince avec injection de dépendances IoC par le constructeur et déclenchement d'erreur `abort(404)`.
3. Déclarer la route web paramétrée avec contrainte numérique `whereNumber()` et nommage explicite `name(...)`.

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle (Persona) :** Développeur Backend Laravel senior expert en Clean Code, conteneur IoC et principes SOLID.
- **Instruction (Contexte & Tâche) :** Prendre en entrée les champs et spécifications d'une entité métier `[ENTITE_METIER]` et générer le code PHP backend complet (Service, Contrôleur, Route) sans omission de typage.
- **Output (Format de sortie) :** Fichiers PHP complets avec chemins stricts et balises ```` ```php ````.
- **Contraintes Négatives :**
  - Zéro logique de persistance ou de lecture de fichiers dans le contrôleur.
  - Interdiction de retourner des tableaux associatifs sans typage explicite.
  - Zéro bavardage conversationnel.

## 4. Livrables & Critères de validation
- **Livrable attendu :**
  - Fichier de prompt réutilisable : `ua-lab/laravel/tranche-verticale/prompt-backend/prompt-back-end.prompt.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le prompt est rédigé selon la méthode RIO avec contraintes négatives explicites.
  - [ ] Testé sur une nouvelle entité métier (ex : Réalisation, Film), il génère un code PHP backend syntaxiquement valide et prêt à l'emploi.
  - [ ] La séparation stricte entre contrôleur mince et classe service est garantie.
