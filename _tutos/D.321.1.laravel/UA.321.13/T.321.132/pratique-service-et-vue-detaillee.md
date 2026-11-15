---
layout: tuto
title: "Pratique : Service et vue détaillée"
sous_titre: "Développer ArticleService (CSV), ArticleController mince, layout Blade maître et gestion 404"
slug: "pratique-service-et-vue-detaillee"
permalink: /tutos/pratique-service-et-vue-detaillee/
tuto_id: "T.321.132"
version: "normal"
ua: "UA.321.13"
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
- `app/Services/ArticleService.php` : Classe de service lisant les articles depuis le CSV.
- `app/Http/Controllers/Public/ArticleController.php` : Contrôleur mince avec injection IoC.
- `resources/views/layouts/app.blade.php` : Gabarit maître responsive (navbar, footer).
- `resources/views/articles/show.blade.php` : Vue de consultation détaillée d'un article.
- `resources/views/errors/404.blade.php` : Vue personnalisée d'erreur 404.
- `routes/web.php` : Route nommée `articles.show`.

## 2. Consignes & Jalons de Réalisation
Bâtir la tranche verticale complète en respectant ces 5 jalons :
1. **Création de la Classe Service :** Coder `ArticleService` dans `app/Services/` avec la méthode `find(int $id)` qui parcourt `database/data/articles.csv` via `fgetcsv()` et retourne un tableau ou `null`.
2. **Implémentation du Contrôleur Mince :** Injecter `ArticleService` dans le constructeur de `ArticleController`. Dans la méthode `show(int $id)`, appeler le service et déclencher `abort(404)` si l'article n'existe pas.
3. **Déclaration de la Route Nommée :** Configurer `Route::get('/articles/{id}', [ArticleController::class, 'show'])->whereNumber('id')->name('articles.show');`.
4. **Mise en Place du Layout Maître :** Créer `resources/views/layouts/app.blade.php` avec en-tête de navigation, conteneur `@yield('content')` et pied de page Tailwind.
5. **Vues de Détail et 404 :** Développer `show.blade.php` héritant du layout avec affichage complet de l'article, et personnaliser `errors/404.blade.php`.

## 3. Points de Vigilance
- ⚠️ Ne pas oublier de fermer le pointeur de fichier CSV (`fclose()`) après lecture.
- ⚠️ Tester expressément le scénario d'erreur en saisissant un identifiant inexistant dans l'URL (ex: `/articles/9999`).

## 4. Critères de Validation
- [ ] La navigation sur un article existant (ex: `http://127.0.0.1:8000/articles/1`) affiche l'article complet dans le gabarit maître.
- [ ] La navigation sur un identifiant inexistant renvoie une page 404 propre avec code HTTP 404.
- [ ] Le Live Coding 40 min d'évaluation est réalisable à partir de ce modèle.
