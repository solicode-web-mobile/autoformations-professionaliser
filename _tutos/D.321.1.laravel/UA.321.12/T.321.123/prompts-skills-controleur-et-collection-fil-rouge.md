---
layout: tuto
title: "Prompts & Skills : Contrôleur et collection Fil Rouge"
sous_titre: "Concevoir le prompt RIO réutilisable pour générer le contrôleur et la vue de collection Fil Rouge"
slug: "prompts-skills-controleur-et-collection-fil-rouge"
permalink: /tutos/prompts-skills-controleur-et-collection-fil-rouge/
tuto_id: "T.321.123"
version: "normal"
ua: "UA.321.12"
maturite: "UA-Lab"
nav_order: 3
simplified: true
en_construction: true
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux Fil Rouge
- Transposition de l'Étape 4.2 (Contrôleur HTTP & Rendu de Collection) vers le Projet Fil Rouge (ex : Plateforme Cinéma).

## 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-controleur-collection.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de générer le contrôleur et la vue de collection d'une entité métier du Projet Fil Rouge (ex : Genres de films).

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Développeur backend Laravel 12 & spécialiste Blade.
- **Instruction :** Générer le contrôleur HTTP avec namespace propre et la vue Blade associée stylisée avec Tailwind CSS à partir des données de l'entité `[ENTITE_COLLECTION]`.
- **Output :** Fichiers PHP et Blade complets prêts à l'intégration.
- **Contraintes Négatives :** Pas de requêtes SQL directes, utiliser des données structurées propres.

## 4. Critères de Validation
- [ ] Le prompt est testé sur l'application Fil Rouge.
- [ ] La collection d'entités métier s'affiche harmonieusement sous forme de cartes responsive.
