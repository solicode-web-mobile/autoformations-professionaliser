---
layout: tuto
title: "Pratique : Tranche verticale complète et gestion 404"
sous_titre: "Développer ArticleService (CSV), ArticleController mince, layout Blade maître et gestion 404"
slug: "pratique-service-et-vue-detaillee"
permalink: /tutos/pratique-service-et-vue-detaillee/
tuto_id: "T.321.132"
version: "normal"
ua: "UA.321.13"
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
- **Position dans le flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.3 & 4.4 — Tranche Verticale & Résilience.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :**
  - `app/Services/ArticleService.php`
  - `app/Http/Controllers/Public/ArticleController.php`
  - `resources/views/layouts/app.blade.php`
  - `resources/views/articles/show.blade.php`
  - `resources/views/errors/404.blade.php`
  - `routes/web.php`

## 2. Travail à Faire (Projet d'Imitation)
Bâtir la tranche verticale complète de consultation d'un article en respectant ces jalons :
1. **Création de la Classe Service :** Coder `ArticleService` dans `app/Services/` avec la méthode `find(int $id)` qui parcourt `database/data/articles.csv` via `fgetcsv()` et retourne un tableau associatif complet ou `null`.
2. **Implémentation du Contrôleur Mince :** Injecter `ArticleService` dans le constructeur de `ArticleController`. Dans la méthode `show(int $id)`, interroger le service et déclencher `abort(404)` si l'article n'existe pas.
3. **Déclaration de la Route Nommée :** Configurer `Route::get('/articles/{id}', [ArticleController::class, 'show'])->whereNumber('id')->name('articles.show');`.
4. **Mise en Place du Layout Maître :** Créer `resources/views/layouts/app.blade.php` avec en-tête de navigation, conteneur `@yield('content')` et pied de page Tailwind.
5. **Vues de Détail et 404 :** Développer `show.blade.php` héritant du layout avec affichage complet de l'article, et personnaliser `errors/404.blade.php`.

## 3. Critères de Validation
- [ ] La navigation sur `http://127.0.0.1:8000/articles/1` affiche l'article complet dans le gabarit maître sur la branche `sprint1`.
- [ ] La navigation sur un identifiant inexistant (ex: `/articles/999`) renvoie une page d'erreur 404 propre avec code HTTP 404.
- [ ] Le code respecte scrupuleusement les 7 critères de la Definition of Done.