# Plan des Tutoriels : D.321.1 — Développement Web avec Laravel

> **Domaine :** `D.321.1` | **Compétence :** `C.321` — Développer une application Web avec le framework Laravel | **Session :** S01  
> **Niveau de Maturité :** UA-Lab (Atelier pratique guidé)  
> **Branche Git de Travail :** `sprint1`  
> **Projet Référence :** Projet d'imitation (*Blog des Lauréats*)  
> **Référentiels Liés :** [`../../3.sprints/flux-travail-n3.md`](../../3.sprints/flux-travail-n3.md) | [`../../3.sprints/stack-technique-n3.md`](../../3.sprints/stack-technique-n3.md)

---

## 1. Description des Unités d'Apprentissage du Domaine

### UA.321.11 — Hello World Laravel : Route et Vue

- **Code :** `UA.321.11`
- **Maturité :** `UA-Lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 09
- **Positionnement Flux de Travail :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.1 — Routage Web & Page d'Accueil
- **Briques Stack Technique :** Laravel 12 Router, Moteur Blade, Tailwind CSS utilitaire
- **Compétence :** `C.321` — Développer une application Web avec le framework Laravel
- **Domaine :** `D.321.1` — Développement Web avec Laravel
- **Durée estimée :** 4 heures
- **Objectif :** S'approprier le fonctionnement initial du framework Laravel 12 et livrer la page d'accueil du Blog des Lauréats en configurant le routage web déclaratif et un premier gabarit Blade sous Tailwind CSS.
- **Description :** Premier contact opérationnel avec Laravel 12. L'apprenant découvre l'écosystème Laravel et le cycle de vie d'une requête HTTP, puis configure sa première route web déclarative et sa vue d'accueil.
- **Notions Clés Utilisées dans le Sprint :**
  - Cycle de vie d'une requête HTTP sous Laravel 12 (`public/index.php` $\to$ Kernel $\to$ Router $\to$ Vue $\to$ Réponse 200).
  - Routage déclaratif dans `routes/web.php` : façade `Route::get()`, closures anonymes.
  - Moteur de gabarit Blade : syntaxe d'interpolation `{% raw %}{{ $variable }}{% endraw %}`, directives de base.
  - Intégration Tailwind CSS : classes utilitaires et structure responsive.
- **Livrables :** Route d'accueil fonctionnelle et vue Blade (`routes/web.php`, `resources/views/welcome.blade.php`) sur la branche `sprint1`.
- **Travail à Faire :** Assimiler les bases de Laravel, configurer la route GET racine et concevoir la page d'accueil du Blog des Lauréats.

---

### UA.321.12 — Démarrage rapide Laravel : Contrôleur et Vue

- **Code :** `UA.321.12`
- **Maturité :** `UA-Lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 10
- **Positionnement Flux de Travail :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.2 — Contrôleur HTTP & Rendu de Collection
- **Briques Stack Technique :** Artisan Controller, Contrôleur HTTP, Directives Blade itératives
- **Compétence :** `C.321` — Développer une application Web avec le framework Laravel
- **Domaine :** `D.321.1` — Développement Web avec Laravel
- **Durée estimée :** 6 heures
- **Objectif :** Mettre en œuvre le pattern MVC en isolant l'orchestration HTTP dans un contrôleur dédié pour afficher dynamiquement la collection des catégories d'articles à travers des boucles Blade stylisées.
- **Description :** Structuration MVC du code applicatif. L'apprenant remplace les closures directes par un contrôleur HTTP mince créé avec la CLI Artisan, transmet des données structurées et compose une vue Blade itérative dynamique.
- **Notions Clés Utilisées dans le Sprint :**
  - Rôle du contrôleur HTTP dans l'architecture MVC : récepteur de `Request`, coordinateur et fournisseur de `Response`.
  - Commande de scaffolding Artisan : `php artisan make:controller Public/CategoryController`.
  - Transmission de données structurées : fonction d'assistance `view('vue', compact('categories'))`.
  - Directives de boucle Blade : `@foreach`, `@forelse`, `@empty`, `@endforeach`.
- **Livrables :** Contrôleur HTTP et vue de collection (`app/Http/Controllers/Public/CategoryController.php`, `resources/views/categories/index.blade.php`, `routes/web.php`) sur la branche `sprint1`.
- **Travail à Faire :** Générer le contrôleur avec Artisan, implémenter l'action de collection et composer la vue Blade en grille de cartes.

---

### UA.321.13 — Contrôleur, Classe Service et Vue détaillée

- **Code :** `UA.321.13`
- **Maturité :** `UA-Lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 11
- **Positionnement Flux de Travail :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.3 — Tranche Verticale Complète & Étape 4.4 — Résilience & Erreurs HTTP
- **Briques Stack Technique :** Routes dynamiques, Injection IoC, Classe Service CSV, Layout maître Blade, abort(404), Prompts IA Backend & Frontend, Live Coding
- **Compétence :** `C.321` — Développer une application Web avec le framework Laravel
- **Domaine :** `D.321.1` — Développement Web avec Laravel
- **Durée estimée :** 32 heures
- **Objectif :** Livrer la fonctionnalité centrale de consultation détaillée d'un article en implémentant l'architecture en deux couches (contrôleur mince IoC et classe service tabulaire), concevoir les deux prompts spécialisés (`prompt-back-end` et `prompt-front-end`) et réussir l'évaluation de Live Coding en 40 minutes.
- **Description :** Réalisation majeure du Sprint 1. L'apprenant construit la tranche verticale complète de consultation d'article, sécurise les identifiants inexistants via `abort(404)`, encapsule l'accès CSV dans une classe Service injectée automatiquement, outille son agent IA avec deux prompts ciblés (backend et frontend) et s'entraîne à reproduire la tranche en 40 minutes chrono.
- **Notions Clés Utilisées dans le Sprint :**
  - Routes paramétrées : `Route::get('/articles/{id}', ...)` avec contrainte `whereNumber('id')`.
  - Injection de dépendances IoC : résolution automatique de `ArticleService` par le conteneur Laravel.
  - Classe Service découplée : classe `ArticleService` dans `app/Services/` lisant `database/data/articles.csv`.
  - Résilience HTTP : interception de ressource absente via `abort(404)` et gabarit personnalisé `errors/404.blade.php`.
  - Héritage de layout maître Blade : structure `layouts/app.blade.php` avec `@yield('content')`, `@extends` et `@section`.
  - Automatisation IA : prompts séparés backend et frontend.
- **Livrables :** Tranche logicielle complète (`ArticleService.php`, `ArticleController.php`, `app.blade.php`, `show.blade.php`, `404.blade.php`), prompt backend (`livrables/ia/prompts/prompt-back-end.prompt.md`), prompt frontend (`livrables/ia/prompts/prompt-front-end.prompt.md`) et simulation de Live Coding validée sur la branche `sprint1`.
- **Travail à Faire :** Implémenter la tranche verticale complète, tester le cas 404, concevoir les deux prompts IA et réaliser l'entraînement chronométré au Live Coding.

---

## 2. Plan des Tutoriels : UA.321.11

### T.321.111 — Théorie : Routage et Vues sous Laravel

- **Code :** `T.321.111`
- **Maturité :** `UA-Lab` (Présentation théorique & assimilation)
- **Unité d'Apprentissage parente :** `UA.321.11`
- **Titre Canonique :** Théorie : Routage et Vues sous Laravel
- **Position dans le Flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.1 — Routage & Vues.
- **Branche Git de travail :** `sprint1`
- **Objectif Opérationnel :** Comprendre l'architecture de base du framework Laravel, le traitement d'une requête HTTP et la syntaxe Blade.
- **Répartition Didactique (Règle des 20/80) :**
  - **Les 20% fournis directement au tutoriel :**
    - Qu'est-ce que Laravel : framework PHP moderne adoptant le modèle MVC.
    - Le cycle d'une requête : point d'entrée unique `public/index.php`, passage au routeur `routes/web.php` et retour d'une vue.
    - Syntaxe élémentaire de Blade : balises d'interpolation `{% raw %}{{ $variable }}{% endraw %}` avec protection XSS intégrée et localisation dans `resources/views/`.
  - **Les 80% recherchés par l'apprenant :**
    - Organisation des répertoires du framework Laravel (`app/`, `config/`, `database/`, `resources/`, `routes/`).
    - Rôle du CLI Artisan et commandes de diagnostic (`php artisan route:list`).
- **Critère de Réussite :** Fiche d'assimilation des principes Laravel intégrée au journal d'apprentissage.

---

### T.321.112 — Pratique : Route et page d'accueil

- **Code :** `T.321.112`
- **Maturité :** `UA-Lab` (Pratique guidée sur projet d'imitation)
- **Unité d'Apprentissage parente :** `UA.321.11`
- **Titre Canonique :** Pratique : Route et page d'accueil
- **Position dans le Flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.1 — Page d'Accueil.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `routes/web.php`, `resources/views/welcome.blade.php`
- **Objectif Opérationnel :** Déclarer la route racine et créer la vue de bienvenue du Blog des Lauréats stylisée sous Tailwind CSS.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Lancer le serveur local de test via `php artisan serve`.
  2. *Étape 2 :* Dans `routes/web.php`, déclarer la route GET `/` retournant la vue `welcome`.
  3. *Étape 3 :* Concevoir `resources/views/welcome.blade.php` avec bannière de titre, message d'introduction et structure Tailwind CSS responsive.
  4. *Étape 4 :* Vérifier l'affichage dans le navigateur (`http://127.0.0.1:8000`).
- **Critère de Réussite :** La page d'accueil s'affiche avec code HTTP 200 sur la branche `sprint1`.

---

## 3. Plan des Tutoriels : UA.321.12

### T.321.121 — Théorie : Contrôleur et Vues dynamiques

- **Code :** `T.321.121`
- **Maturité :** `UA-Lab` (Présentation théorique & assimilation)
- **Unité d'Apprentissage parente :** `UA.321.12`
- **Titre Canonique :** Théorie : Contrôleur et Vues dynamiques
- **Position dans le Flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.2 — Contrôleur HTTP.
- **Branche Git de travail :** `sprint1`
- **Objectif Opérationnel :** Comprendre le rôle du contrôleur HTTP dans le patron MVC et les directives de boucle Blade.
- **Répartition Didactique (Règle des 20/80) :**
  - **Les 20% fournis directement au tutoriel :**
    - Rôle du contrôleur : séparer la réception de la requête web de la restitution visuelle.
    - Génération via Artisan : `php artisan make:controller Public/CategoryController`.
    - Transmission de variables avec le helper `view('vue', compact('categories'))`.
    - Directives de boucle Blade : `@foreach` et `@forelse` avec clause `@empty`.
  - **Les 80% recherchés par l'apprenant :**
    - Différence entre contrôleur classique et contrôleur invocable (`__invoke`).
    - Mécanismes de manipulation des collections en PHP / Laravel.
- **Critère de Réussite :** Fiche de synthèse sur les contrôleurs intégrée au journal d'apprentissage.

---

### T.321.122 — Pratique : Contrôleur et liste des catégories

- **Code :** `T.321.122`
- **Maturité :** `UA-Lab` (Pratique guidée sur projet d'imitation)
- **Unité d'Apprentissage parente :** `UA.321.12`
- **Titre Canonique :** Pratique : Contrôleur et liste des catégories
- **Position dans le Flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.2 — Rendu de Collection.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :**
  - `app/Http/Controllers/Public/CategoryController.php`
  - `resources/views/categories/index.blade.php`
  - `routes/web.php`
- **Objectif Opérationnel :** Créer un contrôleur HTTP, transmettre une liste de catégories et l'afficher dans une grille responsive Blade.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Générer `CategoryController` via Artisan dans `App\Http\Controllers\Public`.
  2. *Étape 2 :* Implémenter la méthode `index()` initialisant un jeu de données de catégories et retournant la vue avec `compact()`.
  3. *Étape 3 :* Déclarer la route GET `/categories` dans `routes/web.php`.
  4. *Étape 4 :* Concevoir `resources/views/categories/index.blade.php` avec la directive `@forelse` affichant une grille de cartes Tailwind CSS.
- **Critère de Réussite :** La navigation sur `/categories` affiche dynamiquement la liste de catégories sans erreur sur la branche `sprint1`.

---

## 4. Plan des Tutoriels : UA.321.13

### T.321.131 — Théorie : Injection de dépendances et Classe Service

- **Code :** `T.321.131`
- **Maturité :** `UA-Lab` (Présentation théorique & assimilation)
- **Unité d'Apprentissage parente :** `UA.321.13`
- **Titre Canonique :** Théorie : Injection de dépendances et Classe Service
- **Position dans le Flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.3 — Découplage & Injection.
- **Branche Git de travail :** `sprint1`
- **Objectif Opérationnel :** Maîtriser le conteneur IoC de Laravel, l'injection de dépendances par le constructeur, la gestion des erreurs 404 et l'héritage de layout Blade.
- **Répartition Didactique (Règle des 20/80) :**
  - **Les 20% fournis directement au tutoriel :**
    - Conteneur de services (IoC) : injection automatique des dépendances typées dans le constructeur du contrôleur.
    - Classe Service découplée : isolation de la logique d'accès aux données (lecture CSV) hors du contrôleur.
    - Déclenchement d'exception HTTP : fonction `abort(404)` et gabarit dédié `resources/views/errors/404.blade.php`.
    - Héritage de layout maître Blade : `@extends('layouts.app')`, `@yield('content')`, `@section('content')`.
  - **Les 80% recherchés par l'apprenant :**
    - Cycle de résolution des dépendances par le Service Container de Laravel.
    - Typage strict PHP 8.3 et retours de fonctions (`?array`, `void`).
- **Critère de Réussite :** Fiche d'assimilation des patrons Service et IoC intégrée au journal d'apprentissage.

---

### T.321.132 — Pratique : Tranche verticale complète et gestion 404

- **Code :** `T.321.132`
- **Maturité :** `UA-Lab` (Pratique guidée sur projet d'imitation)
- **Unité d'Apprentissage parente :** `UA.321.13`
- **Titre Canonique :** Pratique : Tranche verticale complète et gestion 404
- **Position dans le Flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.3 & 4.4 — Tranche Verticale & Résilience.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :**
  - `app/Services/ArticleService.php`
  - `app/Http/Controllers/Public/ArticleController.php`
  - `resources/views/layouts/app.blade.php`
  - `resources/views/articles/show.blade.php`
  - `resources/views/errors/404.blade.php`
  - `routes/web.php`
- **Objectif Opérationnel :** Implémenter la tranche verticale complète de consultation d'un article avec injection IoC du service CSV, layout maître Blade et gestion d'erreur 404.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Développer `ArticleService` dans `app/Services/` avec la méthode `find(int $id)` lisant `database/data/articles.csv`.
  2. *Étape 2 :* Développer `ArticleController` avec injection de `ArticleService` dans le constructeur et méthode `show(int $id)` déclenchant `abort(404)` si l'article est absent.
  3. *Étape 3 :* Configurer la route nommée `Route::get('/articles/{id}', ...)->whereNumber('id')->name('articles.show');`.
  4. *Étape 4 :* Créer le layout maître `resources/views/layouts/app.blade.php` (navbar, `@yield('content')`, footer Tailwind).
  5. *Étape 5 :* Développer `resources/views/articles/show.blade.php` et personnaliser `resources/views/errors/404.blade.php`.
- **Critère de Réussite :** L'accès à `/articles/1` affiche l'article complet et l'accès à `/articles/999` renvoie une page 404 personnalisée sur la branche `sprint1`.

---

### T.321.133 — Création du prompt-back-end

- **Code :** `T.321.133`
- **Maturité :** `UA-Lab` (Automatisation & Ingénierie IA)
- **Unité d'Apprentissage parente :** `UA.321.13`
- **Titre Canonique :** Création du prompt-back-end
- **Position dans le Flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.3 — Automatisation Backend.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-back-end.prompt.md`
- **Objectif Opérationnel :** Concevoir le prompt d'ingénierie réutilisable permettant à un agent IA de générer l'ensemble de la couche backend d'une entité.
- **Missions Concrètes Réalisées par le Prompt :**
  1. Générer la classe Service métier encapsulant l'accès aux données tabulaires avec typage strict.
  2. Générer le contrôleur HTTP mince avec injection de dépendances IoC et déclenchement d'erreur `abort(404)`.
  3. Déclarer la route web paramétrée avec contrainte numérique et nommage explicite.
- **Cahier des Charges du Prompt (Méthode RIO) :**
  - **Rôle :** Développeur Backend Laravel 12 senior expert en Clean Code et conteneur IoC.
  - **Instruction :** Prendre en entrée les spécifications d'une entité métier `[ENTITE_METIER]` et générer le code PHP complet (Service, Contrôleur, Route) sans omission de typage.
  - **Output :** Fichiers PHP complets avec chemins stricts.
  - **Contraintes Négatives :** Zéro logique de persistance dans le contrôleur ; interdiction de retourner des tableaux non typés.
- **Critère de Réussite :** Le prompt est testé et validé dans `livrables/ia/prompts/prompt-back-end.prompt.md` sur la branche `sprint1`.

---

### T.321.134 — Création du prompt-front-end & Entraînement Live Coding

- **Code :** `T.321.134`
- **Maturité :** `UA-Lab` (Automatisation IA & Entraînement Technique)
- **Unité d'Apprentissage parente :** `UA.321.13`
- **Titre Canonique :** Création du prompt-front-end & Entraînement Live Coding
- **Position dans le Flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.4 — Automatisation Frontend & Évaluation.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-front-end.prompt.md`
- **Objectif Opérationnel :** Concevoir le prompt d'ingénierie pour la couche frontend et s'entraîner à reproduire la tranche verticale complète en 40 minutes chrono.
- **Missions Concrètes Réalisées par le Prompt :**
  1. Générer le layout maître Blade responsive avec navigation et pied de page Tailwind CSS.
  2. Générer la vue de consultation détaillée de l'entité héritant du layout maître.
  3. Générer la vue personnalisée d'erreur 404.
- **Entraînement au Live Coding (40 minutes) :**
  - Simulation chronométrée : reproduction de la tranche verticale sur une nouvelle entité sans aide extérieure.
  - Validation des 7 critères de la Definition of Done en conditions réelles d'évaluation.
- **Critère de Réussite :** Le prompt `prompt-front-end.prompt.md` est consigné dans `livrables/ia/prompts/` et l'entraînement de Live Coding est réussi en moins de 40 minutes sur la branche `sprint1`.