---
layout: tuto
title: "Création du prompt-front-end & Entraînement Live Coding"
sous_titre: "Concevoir le prompt prompt-front-end et s'entraîner à reproduire la tranche verticale en 40 minutes"
slug: "prompt-frontend"
slug_domaine: "laravel"
slug_ua: "tranche-verticale"
permalink: /tutos/prompt-frontend/
tuto_id: "T.321.134"
version: "normal"
ua: "UA.321.13"
maturite: "lab"
type: "tuto-atelier"
nav_order: 4
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Travail à faire
1. Concevoir et tester le prompt d'ingénierie réutilisable nommé `prompt-front-end.prompt.md` selon la méthode RIO pour automatiser la génération des interfaces Blade responsives.
2. Réaliser une simulation chronométrée d'entraînement à l'épreuve certificative de Live Coding (coder la tranche verticale complète en moins de 40 minutes en totale autonomie).

Vous devez concevoir :
1. Le fichier de prompt réutilisable : `prompt-front-end.prompt.md`.
2. Le compte-rendu d'entraînement au Live Coding : `prompt-frontend.md`.

## 2. Missions Concrètes Réalisées par le Prompt Front-End
1. Générer le layout maître Blade responsive avec navigation et pied de page Tailwind CSS.
2. Générer la vue de consultation détaillée d'une entité héritant du layout maître via `@extends` et `@section`.
3. Générer la vue d'erreur 404 personnalisée.

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle (Persona) :** Développeur Frontend Laravel & Designer Tailwind CSS senior.
- **Instruction (Contexte & Tâche) :** Prendre en entrée les champs d'une entité métier `[ENTITE_METIER]` et générer le gabarit maître, la vue de consultation responsive et la page 404.
- **Output (Format de sortie) :** Fichiers Blade complets et stylisés sous Tailwind CSS.
- **Contraintes Négatives :**
  - Zéro CSS inline (`style="..."`). Utiliser exclusivement les classes utilitaires Tailwind CSS.
  - Mise en page obligatoirement mobile-first.
  - Zéro bavardage conversationnel.

## 4. Protocole d'Entraînement au Live Coding (40 Minutes Chrono)
Pour valider l'épreuve individuelle (65% de la note certificative) :
1. *Chrono 00–10 min :* Coder `RealisationService::find($id)` et déclarer la route paramétrée.
2. *Chrono 10–20 min :* Développer le contrôleur mince `RealisationController` avec injection IoC et `abort(404)`.
3. *Chrono 20–35 min :* Composer le layout maître Blade et la vue détaillée `show.blade.php`.
4. *Chrono 35–40 min :* Vérifier les scénarios nominal (200) et d'erreur (404) sur le navigateur.

## 5. Livrables & Critères de validation
- **Livrables attendus :**
  - Fichier de prompt : `tutoriels/laravel/tranche-verticale/prompt-frontend/prompt-front-end.prompt.md` sur la branche `sprint1`.
  - Compte-rendu d'entraînement : `tutoriels/laravel/tranche-verticale/prompt-frontend/prompt-frontend.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le prompt `prompt-front-end.prompt.md` génère des vues Blade valides sans CSS inline.
  - [ ] L'entraînement au Live Coding est réussi en moins de 40 minutes sans aucune assistance extérieure.
  - [ ] L'ensemble des 7 critères de la DoD est validé lors de la simulation.
