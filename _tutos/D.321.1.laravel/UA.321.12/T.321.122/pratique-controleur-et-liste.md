---
layout: tuto
title: "Pratique : Contrôleur et liste"
sous_titre: "Générer CategoryController via Artisan et afficher une collection avec @forelse sous Tailwind"
slug: "pratique-controleur-et-liste"
permalink: /tutos/pratique-controleur-et-liste/
tuto_id: "T.321.122"
version: "normal"
ua: "UA.321.12"
maturite: "UA-Lab"
nav_order: 2
simplified: true
en_construction: true
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Livrable Attendu
- `app/Http/Controllers/Public/CategoryController.php` : Contrôleur gérant la collection.
- `resources/views/categories/index.blade.php` : Vue Blade itérant sur les données.

## 2. Consignes & Jalons de Réalisation
Bâtir la liste en respectant ces 4 jalons :
1. **Génération du Contrôleur :** Créer `CategoryController` dans le namespace `App\Http\Controllers\Public` via Artisan.
2. **Définition de l'Action :** Coder la méthode `index()` initialisant un jeu de données de catégories et le transmettant à la vue.
3. **Déclaration de la Route :** Déclarer la route GET `/categories` pointant vers `CategoryController@index`.
4. **Composition de la Vue :** Concevoir `resources/views/categories/index.blade.php` avec directive `@forelse` affichant une grille de cartes Tailwind CSS.

## 3. Points de Vigilance
- ⚠️ Veiller à importer correctement le contrôleur dans `routes/web.php` via son namespace complet.
- ⚠️ Prévoir systématiquement le cas d'une collection vide dans la directive `@empty`.

## 4. Critères de Validation
- [ ] La navigation sur `http://127.0.0.1:8000/categories` affiche la grille de données sans erreur.
- [ ] Le contrôleur reste mince et délègue l'affichage à la vue Blade.
- [ ] Le responsive design est validé sur plusieurs largeurs d'écran.
