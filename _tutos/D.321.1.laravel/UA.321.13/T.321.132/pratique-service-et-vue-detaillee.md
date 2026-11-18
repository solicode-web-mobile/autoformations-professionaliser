---
layout: tuto
title: "Pratique : Tranche verticale complète et gestion 404"
sous_titre: "Développer ArticleService (CSV), ArticleController mince, layout Blade maître et gestion 404"
slug: "consultation-detaillee-404"
slug_domaine: "laravel"
slug_ua: "tranche-verticale"
permalink: /tutos/consultation-detaillee-404/
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

## 1. Travail à faire
Développer la tranche verticale complète de consultation publique d'un article pour le *Blog des Lauréats* sous Laravel 12 : créer la classe `ArticleService` extrayant les données du fichier tabulaire `src/database/data/articles.csv`, injecter le service dans `ArticleController`, configurer la route dynamique paramétrée `/articles/{id}`, concevoir le layout maître Blade responsive sous Tailwind CSS, composer la vue de détail `show.blade.php` et intercepter de manière résiliente les ressources inexistantes avec une page d'erreur 404 personnalisée.

Vous devez concevoir :
1. La classe Service : `src/app/Services/ArticleService.php`.
2. Le contrôleur enrichi : `src/app/Http/Controllers/Public/ArticleController.php`.
3. Le layout maître : `src/resources/views/layouts/app.blade.php`.
4. La vue de détail : `src/resources/views/articles/show.blade.php`.
5. La vue d'erreur : `src/resources/views/errors/404.blade.php`.
6. La route paramétrée dans `src/routes/web.php`.
7. Le compte-rendu technique : `consultation-detaillee-404.md`.
8. Le diaporama Marp de restitution : `presentation-consultation-detaillee-404.md`.
9. Le journal des commandes : `consultation-detaillee-404.command.md`.

## 2. Consignes & Spécifications de Réalisation

1. **Jalon 1 — Création de la Classe Service Découplée :**  
   Dans `src/app/Services/ArticleService.php` :
   - Déclarez la méthode publique `find(int $id): ?array`.
   - Ouvrez et parcourez le fichier tabulaire `src/database/data/articles.csv` avec la fonction native PHP `fgetcsv()`.
   - Si la ligne correspondante à l'identifiant est trouvée, retournez un tableau associatif complet (`id`, `titre`, `contenu`, `auteur`, `date`).
   - Si l'identifiant est absent ou le fichier non lisible, retournez strictement `null`.

2. **Jalon 2 — Contrôleur Mince avec Injection IoC & Résilience 404 :**  
   Dans `src/app/Http/Controllers/Public/ArticleController.php` :
   - Injectez `ArticleService` dans le constructeur : `public function __construct(protected ArticleService $articleService) {}`.
   - Coder l'action `show(int $id): \Illuminate\View\View` :
     - Interrogez le service : `$article = $this->articleService->find($id);`.
     - Si `$article === null`, déclenchez immédiatement l'exception HTTP : `abort(404);`.
     - Sinon, retournez la vue avec les données : `return view('articles.show', compact('article'));`.

3. **Jalon 3 — Déclaration de la Route Paramétrée :**  
   Dans `src/routes/web.php`, déclarez la route GET dynamique :
   - Définissez l'URI `/articles/{id}` reliée à `ArticleController@show`.
   - Sécurisez le paramètre avec la contrainte numérique `->whereNumber('id')`.
   - Nommez la route : `->name('articles.show')`.

4. **Jalon 4 — Mise en Place du Layout Maître Blade :**  
   Dans `src/resources/views/layouts/app.blade.php` :
   - Structurez le squelette HTML5 responsive avec balises méta et Tailwind CSS.
   - Intégrez une barre de navigation partagée avec le logo du Blog des Lauréats et le lien d'accueil.
   - Positionnez le conteneur principal avec le point d'ancrage `@yield('content')`.
   - Intégrez un pied de page normé Solicode.

5. **Jalon 5 — Vues de Détail et Page 404 Personnalisée :**  
   - `src/resources/views/articles/show.blade.php` : hérite du layout maître (`@extends('layouts.app')`), affiche le titre, l'auteur, la date et le corps de l'article, et fournit un lien de retour fluide vers la liste des articles.
   - `src/resources/views/errors/404.blade.php` : hérite du layout maître et affiche un message clair invitant l'utilisateur à revenir à l'accueil face à un article inexistant.

6. **Jalon 6 — Validation Navigateur & Journalisation :**  
   Vérifiez le fonctionnement nominal sur `http://127.0.0.1:8000/articles/1` et l'affichage propre de l'erreur 404 sur `http://127.0.0.1:8000/articles/999`.  
   Consignez les commandes de test dans `tutoriels/laravel/tranche-verticale/consultation-detaillee-404/consultation-detaillee-404.command.md` :

```bash
cd src
php artisan test --filter=ArticleTest
```

## 3. Livrables & Critères de validation
- **Livrables attendus :**
  - Code applicatif : `src/app/Services/ArticleService.php`, `src/app/Http/Controllers/Public/ArticleController.php`, `src/resources/views/layouts/app.blade.php`, `src/resources/views/articles/show.blade.php`, `src/resources/views/errors/404.blade.php` et `src/routes/web.php` sur la branche `sprint1`.
  - Compte-rendu technique : `tutoriels/laravel/tranche-verticale/consultation-detaillee-404/consultation-detaillee-404.md` sur la branche `sprint1`.
  - Diaporama Marp : `tutoriels/laravel/tranche-verticale/consultation-detaillee-404/presentation-consultation-detaillee-404.md` sur la branche `sprint1`.
  - Journal des commandes : `tutoriels/laravel/tranche-verticale/consultation-detaillee-404/consultation-detaillee-404.command.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le contrôleur délègue 100% de la lecture des données à `ArticleService` (zéro appel CSV direct dans le contrôleur).
  - [ ] La navigation sur un article valide affiche la vue complète dans le layout maître avec code HTTP 200.
  - [ ] La navigation sur un identifiant absent déclenche `abort(404)` et restitue le gabarit 404 personnalisé.
  - [ ] L'ensemble des 7 critères de la Definition of Done est validé.
