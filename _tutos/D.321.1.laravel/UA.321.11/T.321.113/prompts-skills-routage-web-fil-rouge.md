---
layout: tuto
title: "Prompts & Skills : Routage Web Fil Rouge"
sous_titre: "Concevoir le prompt RIO réutilisable pour initialiser la route et l'accueil du Projet Fil Rouge"
slug: "prompts-skills-routage-web-fil-rouge"
permalink: /tutos/prompts-skills-routage-web-fil-rouge/
tuto_id: "T.321.113"
version: "normal"
ua: "UA.321.11"
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
- Transposition de l'Étape 4.1 (Routage Web & Page d'Accueil) vers le Projet Fil Rouge (ex : Plateforme Cinéma).

## 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-routage-web.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA d'initialiser la route et la page d'accueil adaptées au Projet Fil Rouge.

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Développeur Fullstack Laravel 12 & expert Blade / Tailwind CSS.
- **Instruction :** Prendre en entrée les paramètres du projet Fil Rouge `[THEME_PROJET]` et générer le code de `routes/web.php` et `resources/views/welcome.blade.php` avec identité visuelle adaptée.
- **Output :** Deux blocs de code clairement séparés avec chemins relatifs stricts.
- **Contraintes Négatives :** Pas de JavaScript complexe à ce stade, pas de persistance en base.

## 4. Critères de Validation
- [ ] Le prompt est testé sur l'application Fil Rouge.
- [ ] Le code produit s'exécute immédiatement sans erreur de syntaxe PHP ou Blade.
