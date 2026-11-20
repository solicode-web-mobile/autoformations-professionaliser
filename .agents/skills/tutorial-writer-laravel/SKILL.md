---
name: tutorial-writer-laravel
description: Règles de rédaction didactiques et techniques spécifiques au domaine Laravel (D.321.1, Compétence C.321). Membre de l'écosystème tutorial-writer sous la gouvernance de tutorial-writer.
version: 1.0.0
---

# 1. Mission & Périmètre
Expert de domaine au sein de l'écosystème `tutorial-writer`, chargé de prescrire les standards techniques, conventions de code et critères de validation propres au domaine **Laravel** (D.321.1, Compétence C.321).
Applique le socle transversal et la synchronisation gouvernés par [tutorial-writer](../tutorial-writer/SKILL.md).

# 2. Déclenchement & Limites
- **Activer :** Rédaction, audit ou adaptation de tutoriels du domaine Laravel (routing, contrôleurs, Eloquent, FormRequest, Blade, Alpine.js, Live Coding).
- **Ne PAS activer :** Conception architecturale pure / ADR ➔ `tutorial-writer-architecture` | Tâches de cérémonie de sprint ➔ `tutorial-writer-scrum` | Gouvernance transversale ➔ `tutorial-writer`.

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

# 5. Formats de Livrables & Validation
- **Fiches didactiques :** `tutoriels/laravel/[slug-ua]/[slug-tuto]/[slug-tuto].md`
- **Journal CLI :** `tutoriels/laravel/[slug-ua]/[slug-tuto]/[slug-tuto].command.md`
- **Critères de validation :**
  - Séparation stricte Back-end (FormRequest/Eloquent) et Front-end (Blade/Alpine.js).
  - Code calé à la marge gauche (colonne 0) sans indentation de bloc.
  - Commandes Artisan exemptes de toute commande Git.
