---
layout: tuto
title: "Théorie : Contrôleur et Vues dynamiques"
sous_titre: "Comprendre le rôle du contrôleur HTTP dans l'architecture MVC et les directives de boucle Blade"
slug: "requete-action-http"
slug_domaine: "laravel"
slug_ua: "controleur-vue"
permalink: /tutos/requete-action-http/
tuto_id: "T.321.121"
version: "normal"
ua: "UA.321.12"
maturite: "lab"
type: "tuto-atelier"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Travail à faire
Effectuer les recherches documentaires nécessaires, concevoir une fiche de synthèse personnelle et préparer un diaporama de restitution Marp expliquant le rôle coordinateur du contrôleur HTTP dans le modèle MVC, les avantages d'extraire la logique de traitement hors des fichiers de routes, la commande de génération Artisan et la restitution dynamique de collections de données via les directives itératives Blade.

## 2. Notions fondamentales
- **Rôle du Contrôleur HTTP dans l'Architecture MVC :**
  - Le contrôleur agit comme un chef d'orchestre : il réceptionne la requête entrante (`Request`), orchestre les actions requises, prépare les données et retourne une réponse (`Response` ou vue).
  - Il élimine les closures anonymes complexes dans `routes/web.php` pour garantir la lisibilité et la testabilité du code.
- **Génération par la CLI Artisan :**
  - Commande standard de scaffolding : `php artisan make:controller Public/ArticleController`.
  - La classe générée hérite de `App\Http\Controllers\Controller` et prend place sous `app/Http/Controllers/Public/`.
- **Transmission de Données vers la Vue Blade :**
  - Utilisation du helper `view('articles.index', compact('articles'))` ou transmission par tableau associatif `view('articles.index', ['articles' => $articles])`.
  - La variable `$articles` devient immédiatement accessible dans le gabarit Blade correspondant sous `resources/views/articles/index.blade.php`.
- **Directives de Boucle Blade :**
  - Directive `@foreach ($articles as $article) ... @endforeach` pour itérer sur une collection.
  - Directive résiliente `@forelse ($articles as $article) ... @empty ... @endforelse` : affiche automatiquement le bloc alternatif `@empty` lorsqu'aucun élément n'est présent dans la collection, évitant les erreurs de variables indéfinies.

## 3. Recherches à effectuer
- Analyser la différence conceptuelle entre un contrôleur conventionnel à actions multiples et un contrôleur à action unique (*Single Action Controller* implémentant la méthode magique `__invoke`).
- Étudier les méthodes utilitaires de la classe `Illuminate\Support\Collection` de Laravel pour trier, filtrer et transformer des données tabulaires avant transmission à la vue.
- Examiner comment passer des paramètres d'URL nommés aux actions de contrôleur.

## 4. Livrable attendu
- **Fiche technique de synthèse :** `tutoriels/laravel/controleur-vue/requete-action-http/requete-action-http.md` sur la branche `sprint1`.
- **Diaporama Marp de restitution :** `tutoriels/laravel/controleur-vue/requete-action-http/presentation-requete-action-http.md` sur la branche `sprint1`.
- **Contenu attendu :** Synthèse personnelle structurée reprenant les notions fondamentales (contrôleurs MVC, Artisan make:controller, directives Blade `@forelse`) et les réponses argumentées aux recherches à effectuer.
