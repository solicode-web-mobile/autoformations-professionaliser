---
layout: tuto
title: "Création du prompt-front-end & Entraînement Live Coding"
sous_titre: "Concevoir le prompt prompt-front-end et s'entraîner à reproduire la tranche verticale en 40 minutes"
slug: "creation-prompt-front-end"
permalink: /tutos/creation-prompt-front-end/
tuto_id: "T.321.134"
version: "normal"
ua: "UA.321.13"
maturite: "UA-Lab"
nav_order: 4
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.4 — Automatisation Frontend & Évaluation.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-front-end.prompt.md`

## 2. Travail à Faire
1. **Création du Prompt Frontend :** Concevoir dans `livrables/ia/prompts/prompt-front-end.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de générer l'ensemble de la couche frontend d'une entité (layout maître Blade, vue de détail responsive et gabarit 404).
2. **Entraînement au Live Coding (40 minutes chrono) :** S'entraîner à reproduire l'implémentation complète de la tranche verticale sur une nouvelle entité sans aide extérieure, en validant l'ensemble des 7 critères de la DoD.

## 3. Missions Concrètes Réalisées par le Prompt Frontend
1. Générer le layout maître Blade responsive avec navigation et pied de page Tailwind CSS.
2. Générer la vue de consultation détaillée de l'entité héritant du layout maître via `@extends` et `@section`.
3. Générer la vue d'erreur 404 personnalisée.

## 4. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Développeur Frontend Laravel 12 & Designer Tailwind CSS senior.
- **Instruction :** Prendre en entrée les champs d'une entité `[ENTITE_METIER]` et générer le gabarit maître, la vue de consultation responsive et la page 404.
- **Output :** Fichiers Blade complets et stylisés sous Tailwind CSS.
- **Contraintes Négatives :** Zéro CSS inline, utiliser exclusivement les classes utilitaires Tailwind ; mise en page obligatoirement mobile-first.

## 5. Critères de Validation
- [ ] Le prompt `prompt-front-end.prompt.md` est consigné dans `livrables/ia/prompts/` sur la branche `sprint1`.
- [ ] La simulation d'épreuve de Live Coding est réussie en moins de 40 minutes avec les 7 critères de la DoD validés.