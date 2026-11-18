---
layout: tuto
title: "Pratique : Contrôleur et liste d'articles"
sous_titre: "Créer ArticleController avec Artisan, transmettre la collection et afficher une grille responsive Blade"
slug: "liste-articles"
slug_domaine: "laravel"
slug_ua: "controleur-vue"
permalink: /tutos/liste-articles/
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

## 1. Travail à faire
Développer la première action de contrôleur MVC pour le *Blog des Lauréats* sous Laravel 12 : générer `ArticleController` avec la CLI Artisan, coder l'action `index()` transmettant une collection d'articles modèles à la vue, déclarer la route GET `/articles` et composer la vue `src/resources/views/articles/index.blade.php` avec affichage d'une grille de cartes responsive sous Tailwind CSS.

Vous devez concevoir :
1. Le contrôleur HTTP : `src/app/Http/Controllers/Public/ArticleController.php`.
2. La route déclarative dans `src/routes/web.php`.
3. Le gabarit itératif dans `src/resources/views/articles/index.blade.php`.
4. Le compte-rendu technique : `liste-articles.md`.
5. Le diaporama Marp de restitution : `presentation-liste-articles.md`.
6. Le journal des commandes exécutées : `liste-articles.command.md`.

## 2. Consignes & Spécifications de Réalisation

1. **Jalon 1 — Génération du Contrôleur HTTP :**  
   Depuis le dossier `src/`, exécutez la commande Artisan pour générer le contrôleur dans le sous-espace `Public` :

```bash
cd src
php artisan make:controller Public/ArticleController
```

2. **Jalon 2 — Implémentation de l'Action `index()` :**  
   Dans `src/app/Http/Controllers/Public/ArticleController.php`, codez la méthode publique `index()` :
   - Déclarez un tableau associatif de plusieurs articles représentatifs (id, titre, extrait, nom du lauréat, date de publication).
   - Retournez la vue `articles.index` en transmettant la variable via `view('articles.index', compact('articles'))`.
   - Typage de retour strict : `public function index(): \Illuminate\View\View`.

3. **Jalon 3 — Déclaration de la Route dans `routes/web.php` :**  
   Associez l'URL `/articles` à l'action du contrôleur :
   - Importez la classe avec `use App\Http\Controllers\Public\ArticleController;`.
   - Déclarez la route nommée : `Route::get('/articles', [ArticleController::class, 'index'])->name('articles.index');`.

4. **Jalon 4 — Composition de la Vue Blade Itérative :**  
   Dans `src/resources/views/articles/index.blade.php` :
   - Structurez une grille responsive Tailwind CSS (`grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6`).
   - Utilisez la directive `@forelse ($articles as $article) ... @empty ... @endforelse`.
   - Chaque carte d'article doit afficher le titre, l'auteur, un court extrait et un bouton invitant à lire l'article complet.
   - Dans le bloc `@empty`, affichez un message élégant indiquant qu'aucun article n'est disponible.
   - Zéro CSS inline.

5. **Jalon 5 — Validation Navigateur & Journalisation :**  
   Testez l'accès sur `http://127.0.0.1:8000/articles`. Vérifiez le comportement de la grille lors du redimensionnement de l'écran.  
   Consignez les commandes exécutées dans `tutoriels/laravel/controleur-vue/liste-articles/liste-articles.command.md` :

```bash
cd src
php artisan make:controller Public/ArticleController
```

## 3. Livrables & Critères de validation
- **Livrables attendus :**
  - Fichiers de code source : `src/app/Http/Controllers/Public/ArticleController.php`, `src/resources/views/articles/index.blade.php` et `src/routes/web.php` sur la branche `sprint1`.
  - Compte-rendu technique : `tutoriels/laravel/controleur-vue/liste-articles/liste-articles.md` sur la branche `sprint1`.
  - Diaporama Marp : `tutoriels/laravel/controleur-vue/liste-articles/presentation-liste-articles.md` sur la branche `sprint1`.
  - Journal des commandes : `tutoriels/laravel/controleur-vue/liste-articles/liste-articles.command.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le contrôleur `ArticleController` est généré sous le namespace `App\Http\Controllers\Public`.
  - [ ] L'accès à `http://127.0.0.1:8000/articles` affiche la grille de cartes sans erreur PHP.
  - [ ] La directive `@forelse` gère de manière résiliente le cas d'une collection vide.
  - [ ] Le journal `liste-articles.command.md` consigne fidèlement les commandes Artisan.
