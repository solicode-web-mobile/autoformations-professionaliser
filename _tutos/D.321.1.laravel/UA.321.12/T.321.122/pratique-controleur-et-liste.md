---
layout: tuto
title: "Pratique : Contrôleur et liste des catégories"
sous_titre: "Créer un contrôleur HTTP avec Artisan, transmettre des données et afficher une grille responsive Blade"
slug: "pratique-controleur-et-liste"
permalink: /tutos/pratique-controleur-et-liste/
tuto_id: "T.321.122"
version: "normal"
ua: "UA.321.12"
maturite: "UA-Lab"
nav_order: 2
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.2 — Rendu de Collection.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :**
  - `app/Http/Controllers/Public/CategoryController.php`
  - `resources/views/categories/index.blade.php`
  - `routes/web.php`
- **Stack mobilisée :** Artisan make:controller, Contrôleur HTTP, Blade (@forelse), Tailwind CSS.

## 2. Travail à Faire (Projet d'Imitation)
Bâtir la liste des catégories en respectant ces jalons :
1. **Génération du Contrôleur :** Créer `CategoryController` dans le namespace `App\Http\Controllers\Public` via la commande `php artisan make:controller Public/CategoryController`.
2. **Définition de l'Action :** Coder la méthode `index()` initialisant un jeu de données de catégories et le transmettant à la vue via `compact()`.
3. **Déclaration de la Route :** Déclarer la route GET `/categories` pointant vers `CategoryController@index` dans `routes/web.php`.
4. **Composition de la Vue Blade :** Concevoir `resources/views/categories/index.blade.php` avec directive `@forelse` affichant une grille de cartes responsive avec Tailwind CSS.

## 3. Critères de Validation
- [ ] La navigation sur `http://127.0.0.1:8000/categories` affiche la grille sans erreur sur la branche `sprint1`.
- [ ] Le contrôleur délègue l'affichage à la vue sans accumuler de logique métier superflue.
- [ ] Le cas d'une collection vide est géré proprement via `@empty`.