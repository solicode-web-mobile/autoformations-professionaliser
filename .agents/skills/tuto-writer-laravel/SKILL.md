---
name: tuto-writer-laravel
description: Règles de rédaction didactiques et techniques spécifiques au domaine Laravel (D.321.1, Compétence C.321). Membre de l'écosystème tuto-writer sous la gouvernance de tuto-writer.
version: 1.0.0
---

# 1. Mission & Périmètre
Expert de domaine au sein de l'écosystème `tuto-writer`, chargé de prescrire les standards techniques, conventions de code et critères de validation propres au domaine **Laravel** (D.321.1, Compétence C.321).
Applique le socle transversal et la synchronisation gouvernés par [tuto-writer](../tuto-writer/SKILL.md).

# 2. Déclenchement & Limites
- **Activer :** Rédaction, audit ou adaptation de tutoriels du domaine Laravel (routing, contrôleurs, Eloquent, FormRequest, Blade, Alpine.js, Live Coding).
- **Ne PAS activer :** Conception architecturale pure / ADR ➔ `tuto-writer-architecture` | Tâches de cérémonie de sprint ➔ `tuto-writer-scrum` | Gouvernance transversale ➔ `tuto-writer`.

# 3. Stack Technique & Outils du Domaine
- **Framework & Écosystème :** Laravel, Blade Components, Tailwind CSS, Alpine.js.
- **CLI & Outillage :** Artisan CLI via PowerShell Windows (`php artisan make:...`), Composer.
- **Persistance & Validation :** Eloquent ORM, Migrations, Seeders, FormRequests dédiés.
- **Format pédagogique :** Live Coding guidé pas-à-pas et injection `window.pageData` si éditeur interactif.

# 4. Règles Spécifiques de Rédaction Laravel
1. **Scission Obligatoire de l'Outillage IA :** Pour tout composant complet, scinder impérativement l'outillage de l'Agent IA en deux missions distinctes : `prompt-back-end` (modèle, migration, FormRequest, contrôleur) et `prompt-front-end` (composant Blade, Alpine.js).
2. **Neutralité de Version du Framework :** Nommer le framework simplement « Laravel » dans le corps du texte (pas de mention « Laravel 12 »). La version exacte est confinée au `README.md` du projet.
3. **Validation par FormRequest :** Interdire la validation directe inline dans le contrôleur (`$request->validate(...)`). Exiger systématiquement un FormRequest dédié.
4. **Commandes PowerShell Compatibles :** Fournir des commandes Artisan et PowerShell directement exécutables sous Windows.
5. **Dualité Ateliers (Projet Technique/TodoList) vs Code Incrémental (Blog) :** Dans les ateliers d'assimilation Laravel, l'apprenant ancre ses exemples et cas pratiques sur son **Projet Technique individuel**, tandis que la solution de référence du formateur sous `ua-lab/` traite **TodoList**. Les tutoriels de code incrémental (`tuto-code`) sont quant à eux développés sur le **Blog des Lauréats** pour livrer le code applicatif du sprint sous `src/`.

# 5. Formats de Livrables & Validation
- **Fiches didactiques :** `tutoriels/laravel/[slug-ua]/[slug-tuto]/[slug-tuto].md`
- **Journal CLI :** `tutoriels/laravel/[slug-ua]/[slug-tuto]/[slug-tuto].command.md`
- **Critères de validation :**
  - Séparation stricte Back-end (FormRequest/Eloquent) et Front-end (Blade/Alpine.js).
  - Code calé à la marge gauche (colonne 0) sans indentation de bloc.
  - Commandes Artisan exemptes de toute commande Git.
