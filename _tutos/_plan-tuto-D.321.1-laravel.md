# Plan des Tutoriels : D.321.1 — Développement Web avec Laravel

> **Domaine :** `D.321.1` | **Compétence :** `C.321` — Développer une application Web avec le framework Laravel | **Session :** S01  
> **Niveau de Maturité :** UA-Lab (Atelier pratique guidé)  
> **Référentiels Liés :** [`../../3.sprints/flux-travail-n3.md`](../../3.sprints/flux-travail-n3.md) | [`../../3.sprints/stack-technique-n3.md`](../../3.sprints/stack-technique-n3.md)

---

## 1. Description des Unités d'Apprentissage du Domaine

### UA.321.11 — Hello World Laravel : Route et Vue

- **Code :** `UA.321.11`
- **Maturité :** `UA-lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 09
- **Positionnement Flux de Travail :** Phase 4 — Réalisation Applicative & Code Cible / Étape 4.1 — Routage Web & Page d'Accueil
- **Briques Stack Technique :** Laravel 12 Router, Moteur Blade, Tailwind CSS utilitaire
- **Compétence :** `C.321` — Développer une application Web avec le framework Laravel
- **Domaine :** `D.321.1` — Développement Web avec Laravel
- **Durée estimée :** 8 heures
- **Objectif :** Valider le bon fonctionnement de l'environnement d'exécution Laravel 12 et livrer la page d'accueil minimale du Blog des Lauréats en configurant le routage web déclaratif et un premier gabarit Blade responsive sous Tailwind CSS.
- **Description :** Cette unité d'apprentissage constitue le premier contact opérationnel avec Laravel 12. L'apprenant valide sa chaîne d'outillage locale en instanciant le serveur web, s'approprie le cycle de vie d'une requête HTTP, et produit le premier incrément visible de l'application : une page d'accueil sécurisée et mise en page de manière moderne.
- **Notions Clés Utilisées dans le Sprint :**
  - Cycle de vie d'une requête HTTP sous Laravel 12 (`public/index.php` $\to$ Kernel HTTP $\to$ Middlewares $\to$ Routeur $\to$ Vue $\to$ Réponse 200).
  - Routage déclaratif dans `routes/web.php` : façade `Route::get()`, closures anonymes `function () { return view(...); }`.
  - Moteur de gabarit Blade : convention d'arborescence `resources/views/*.blade.php`, syntaxe d'interpolation `{{ $variable }}`, protection XSS native.
  - Intégration CSS utilitaire : intégration de Tailwind CSS (via CDN/Vite), conteneurs centrés, typographie responsive.
- **Livrables :** Route d'accueil fonctionnelle et vue Blade stylisée (`routes/web.php`, `resources/views/welcome.blade.php`) et prompt (`livrables/ia/prompts/prompt-route-setup.prompt.md`).
- **Travail à Faire :** Configurer la route GET racine dans `routes/web.php`, concevoir la vue de bienvenue responsive stylisée sous Tailwind CSS et rédiger le prompt de transposition Fil Rouge.

---

### UA.321.12 — Démarrage rapide Laravel : Contrôleur et Vue

- **Code :** `UA.321.12`
- **Maturité :** `UA-lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 10
- **Positionnement Flux de Travail :** Phase 4 — Réalisation Applicative & Code Cible / Étape 4.2 — Contrôleur HTTP & Rendu de Collection
- **Briques Stack Technique :** Artisan Controller, Contrôleur HTTP, Directives Blade itératives, Collections
- **Compétence :** `C.321` — Développer une application Web avec le framework Laravel
- **Domaine :** `D.321.1` — Développement Web avec Laravel
- **Durée estimée :** 8 heures
- **Objectif :** Mettre en œuvre le pattern MVC en isolant l'orchestration HTTP dans un contrôleur dédié pour extraire et afficher dynamiquement la collection des catégories d'articles à travers des boucles Blade stylisées.
- **Description :** L'apprenant franchit une étape clé de structuration en éliminant les closures directes dans les routes au profit d'un contrôleur HTTP mince. Il apprend à séparer la réception de la requête, la préparation des données et leur restitution visuelle dynamique sous forme de grille responsive.
- **Notions Clés Utilisées dans le Sprint :**
  - Rôle du contrôleur HTTP dans l'architecture MVC : récepteur de `Request`, orchestrateur d'action et fournisseur de `Response`.
  - Commande de scaffolding Artisan : `php artisan make:controller Public/ArticleController`.
  - Transmission de données structurées : fonction d'assistance `view('vue', compact('categories'))` et tableaux associatifs.
  - Directives de boucle Blade : `@foreach`, `@forelse`, `@empty`, `@endforeach` pour itérer de manière résiliente sur une collection.
  - Grille de cartes responsive sous Tailwind CSS (`grid grid-cols-1 md:grid-cols-3 gap-6`).
- **Livrables :** Contrôleur HTTP et vue de collection (`app/Http/Controllers/Public/ArticleController.php`, `resources/views/articles/index.blade.php`) et prompt (`livrables/ia/prompts/prompt-controller-blade.prompt.md`).
- **Travail à Faire :** Générer le contrôleur avec Artisan, implémenter la méthode d'affichage de collection, composer la vue Blade en grille de cartes et rédiger le prompt de transposition.

---

### UA.321.13 — Contrôleur, Classe Service et Vue détaillée

- **Code :** `UA.321.13`
- **Maturité :** `UA-lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 11
- **Positionnement Flux de Travail :** Phase 4 — Réalisation Applicative & Code Cible / Étape 4.3 — Tranche Verticale Complète & Étape 4.4 — Résilience & Erreurs HTTP
- **Briques Stack Technique :** Routes dynamiques, Injection IoC, Classe Service CSV, Blade layout maître, abort(404)
- **Compétence :** `C.321` — Développer une application Web avec le framework Laravel
- **Domaine :** `D.321.1` — Développement Web avec Laravel
- **Durée estimée :** 14 heures
- **Objectif :** Livrer la fonctionnalité centrale de consultation détaillée d'un article du Blog des Lauréats en implémentant une architecture découplée en deux couches (contrôleur mince IoC et classe service sur persistance tabulaire) avec gestion sécurisée de l'erreur 404.
- **Description :** Point culminant de la réalisation logicielle du Sprint 1, cette unité livre la tranche verticale complète de l'application sans base relationnelle active. L'apprenant professionnalise son code en encapsulant la lecture tabulaire dans une classe Service injectée automatiquement par le conteneur IoC, et garantit la robustesse utilisateur face aux identifiants inexistants.
- **Notions Clés Utilisées dans le Sprint :**
  - Routes paramétrées dynamiques : paramètres d'URL `Route::get('/articles/{id}', ...)`, contraintes `whereNumber('id')`, routes nommées `name('articles.show')`.
  - Injection de dépendances IoC : déclaration du service dans le constructeur de `ArticleController` pour résolution automatique par le conteneur Laravel.
  - Classe Service découplée : classe `ArticleService` dans `app/Services/`, méthode `find(int $id)`, extraction et parsing des données tabulaires CSV (`fgetcsv()`).
  - Gestion d'erreurs et résilience HTTP : interception d'absence d'article via `abort(404)`, gabarit personnalisé `resources/views/errors/404.blade.php`.
  - Héritage de gabarit maître Blade : structure maître `resources/views/layouts/app.blade.php` avec `@yield('content')`, héritage par `@extends('layouts.app')` et `@section('content')`.
  - Composants d'interface partagés : barre de navigation (navbar), pied de page (footer) et bouton de retour consultation.
- **Livrables :** Tranche verticale logicielle complète (routes, contrôleur, service, vues de détail et 404) et prompt complet (`livrables/ia/prompts/prompt-article-service.prompt.md`).
- **Travail à Faire :** Coder la route nommée, la classe ArticleService de lecture CSV, le contrôleur mince avec injection IoC, la vue Blade avec gabarit maître et le prompt d'ingénierie réutilisable.

---

## 2. Plan des Tutoriels : UA.321.11

### T.321.111 — Théorie : Routage et Vues
*(Tâche 1 — Présentation Théorique & Exercices d'Assimilation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase 4 — Réalisation Applicative & Code Cible / Étape 4.1 — Routage Web & Page d'Accueil.
- **Stack mobilisée :** Framework Laravel 12, Routeur web, Moteur de gabarit Blade, Tailwind CSS.

#### 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches nécessaires et concevoir une présentation synthétique (support visuel ou mémo écrit) expliquant le cycle de traitement d'une requête web dans Laravel 12, le fonctionnement du fichier `routes/web.php` et les mécanismes de rendu HTML sécurisé sous Blade.

#### 3. Notions Clés du Sprint à Ne Pas Oublier
*(L'apprenant doit obligatoirement couvrir ces notions et les enrichir par sa propre recherche) :*
- Le point d'entrée unique `public/index.php` et le rôle du routeur.
- La syntaxe déclarative `Route::get('/chemin', $action)`.
- La convention d'emplacement des vues dans `resources/views/`.
- La syntaxe d'interpolation `{{ $variable }}` et l'échappement XSS automatique.

#### 4. Points de Réflexion & Auto-Évaluation
- *Pourquoi ne doit-on jamais coder de logique métier complexe ni de requêtes SQL directement dans une closure de `routes/web.php` ?*
- *Quelle commande Artisan permet de lister l'ensemble des routes déclarées dans l'application ?*

---

### T.321.112 — Pratique : Route et page d'accueil
*(Tâche 2 — Réalisation Pratique sur le Projet d'Imitation)*

#### 1. Livrable Attendu
- `routes/web.php` : Déclaration de la route racine `/`.
- `resources/views/welcome.blade.php` : Gabarit d'accueil complet et stylisé sous Tailwind CSS.

#### 2. Consignes & Jalons de Réalisation
Bâtir l'écran d'accueil en respectant ces 4 jalons :
1. **Lancement du Serveur Local :** Exécuter `php artisan serve` à la racine et vérifier l'accès sur `http://127.0.0.1:8000`.
2. **Configuration de la Route Racine :** Déclarer la route GET `/` appelant explicitement la vue `welcome`.
3. **Composition de la Vue Blade :** Créer la page HTML5 sémantique, intégrer Tailwind CSS, concevoir la bannière d'accueil du *Blog des Lauréats* et le message d'introduction.
4. **Vérification Navigateur :** S'assurer de la réponse HTTP 200 et de l'adaptation sur mobile (responsive).

#### 3. Points de Vigilance
- ⚠️ Attention à la casse du nom du fichier de vue (toujours en minuscules sous Linux).
- ⚠️ Exécuter impérativement la commande artisan à la racine du projet Laravel.

#### 4. Critères de Validation
- [ ] La navigation sur `http://127.0.0.1:8000/` affiche la page d'accueil sans déformation visuelle.
- [ ] Le code HTML généré est valide et sémantique.
- [ ] Le commit Git respecte la convention d'équipe.

---

### T.321.113 — Prompts & Skills : Routage Web Fil Rouge
*(Tâche 3 — Conception Prompts & Skills Projet Fil Rouge)*

#### 1. Positionnement dans le Flux Fil Rouge
- Transposition de l'Étape 4.1 (Routage Web & Page d'Accueil) vers le Projet Fil Rouge (ex : Plateforme Cinéma).

#### 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-routage-web.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA d'initialiser la route et la page d'accueil adaptées au Projet Fil Rouge.

#### 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Développeur Fullstack Laravel 12 & expert Blade / Tailwind CSS.
- **Instruction :** Prendre en entrée les paramètres du projet Fil Rouge `[THEME_PROJET]` et générer le code de `routes/web.php` et `resources/views/welcome.blade.php` avec identité visuelle adaptée.
- **Output :** Deux blocs de code clairement séparés avec chemins relatifs stricts.
- **Contraintes Négatives :** Pas de JavaScript complexe à ce stade, pas de persistance en base.

#### 4. Critères de Validation
- [ ] Le prompt est testé sur l'application Fil Rouge.
- [ ] Le code produit s'exécute immédiatement sans erreur de syntaxe PHP ou Blade.

---

## 3. Plan des Tutoriels : UA.321.12

### T.321.121 — Théorie : Contrôleur et Vues
*(Tâche 1 — Présentation Théorique & Exercices d'Assimilation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase 4 — Réalisation Applicative & Code Cible / Étape 4.2 — Contrôleur HTTP & Rendu de Collection.
- **Stack mobilisée :** Pattern MVC, Contrôleur HTTP Laravel, Directives Blade itératives.

#### 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches nécessaires et concevoir une présentation synthétique (support visuel ou mémo écrit) expliquant le rôle du contrôleur dans le découpage MVC, l'intérêt d'extraire la logique hors des routes, et l'usage des directives Blade pour afficher des collections de données.

#### 3. Notions Clés du Sprint à Ne Pas Oublier
*(L'apprenant doit obligatoirement couvrir ces notions et les enrichir par sa propre recherche) :*
- Le rôle d'aiguilleur du contrôleur (coordonner sans accumuler la logique métier).
- La génération de contrôleurs via la CLI Artisan (`make:controller`).
- La fonction helper `view()` et le passage de données via `compact()`.
- Les directives Blade itératives (`@foreach`, `@forelse`, `@empty`, `@endforeach`).

#### 4. Points de Réflexion & Auto-Évaluation
- *Pourquoi la directive `@forelse` est-elle plus robuste et élégante qu'un `@if(count(...))` suivi d'un `@foreach` ?*
- *Que se passe-t-il si la variable passée au contrôleur est vide ou nulle ?*

---

### T.321.122 — Pratique : Contrôleur et liste
*(Tâche 2 — Réalisation Pratique sur le Projet d'Imitation)*

#### 1. Livrable Attendu
- `app/Http/Controllers/Public/CategoryController.php` : Contrôleur gérant la collection.
- `resources/views/categories/index.blade.php` : Vue Blade itérant sur les données.

#### 2. Consignes & Jalons de Réalisation
Bâtir la liste en respectant ces 4 jalons :
1. **Génération du Contrôleur :** Créer `CategoryController` dans le namespace `App\Http\Controllers\Public` via Artisan.
2. **Définition de l'Action :** Coder la méthode `index()` initialisant un jeu de données de catégories et le transmettant à la vue.
3. **Déclaration de la Route :** Déclarer la route GET `/categories` pointant vers `CategoryController@index`.
4. **Composition de la Vue :** Concevoir `resources/views/categories/index.blade.php` avec directive `@forelse` affichant une grille de cartes Tailwind CSS.

#### 3. Points de Vigilance
- ⚠️ Veiller à importer correctement le contrôleur dans `routes/web.php` via son namespace complet.
- ⚠️ Prévoir systématiquement le cas d'une collection vide dans la directive `@empty`.

#### 4. Critères de Validation
- [ ] La navigation sur `http://127.0.0.1:8000/categories` affiche la grille de données sans erreur.
- [ ] Le contrôleur reste mince et délègue l'affichage à la vue Blade.
- [ ] Le responsive design est validé sur plusieurs largeurs d'écran.

---

### T.321.123 — Prompts & Skills : Contrôleur et collection Fil Rouge
*(Tâche 3 — Conception Prompts & Skills Projet Fil Rouge)*

#### 1. Positionnement dans le Flux Fil Rouge
- Transposition de l'Étape 4.2 (Contrôleur HTTP & Rendu de Collection) vers le Projet Fil Rouge (ex : Plateforme Cinéma).

#### 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-controleur-collection.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de générer le contrôleur et la vue de collection d'une entité métier du Projet Fil Rouge (ex : Genres de films).

#### 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Développeur backend Laravel 12 & spécialiste Blade.
- **Instruction :** Générer le contrôleur HTTP avec namespace propre et la vue Blade associée stylisée avec Tailwind CSS à partir des données de l'entité `[ENTITE_COLLECTION]`.
- **Output :** Fichiers PHP et Blade complets prêts à l'intégration.
- **Contraintes Négatives :** Pas de requêtes SQL directes, utiliser des données structurées propres.

#### 4. Critères de Validation
- [ ] Le prompt est testé sur l'application Fil Rouge.
- [ ] La collection d'entités métier s'affiche harmonieusement sous forme de cartes responsive.

---

## 4. Plan des Tutoriels : UA.321.13

### T.321.131 — Théorie : Contrôleur mince et Service
*(Tâche 1 — Présentation Théorique & Exercices d'Assimilation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase 4 — Réalisation Applicative & Code Cible / Étape 4.3 — Tranche Verticale Complète & Étape 4.4 — Résilience & Erreurs HTTP.
- **Stack mobilisée :** Laravel IoC Container, Dependency Injection, Routes dynamiques, Exceptions HTTP 404, Héritage Blade.

#### 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches nécessaires et concevoir une présentation synthétique (support visuel ou mémo écrit) expliquant le fonctionnement de l'injection de dépendances dans Laravel, le rôle de la classe Service comme passerelle vers les données, les mécanismes de capture d'erreurs 404 et le principe d'héritage de gabarit maître sous Blade.

#### 3. Notions Clés du Sprint à Ne Pas Oublier
*(L'apprenant doit obligatoirement couvrir ces notions et les enrichir par sa propre recherche) :*
- Les routes dynamiques paramétrées `{id}` et la contrainte de type `whereNumber('id')`.
- L'injection de dépendances automatique par le constructeur (IoC).
- L'encapsulation de la lecture des données (CSV) dans `ArticleService`.
- Le déclenchement de `abort(404)` et la personnalisation de la réponse d'erreur.
- L'architecture de gabarit maître Blade (`@extends`, `@yield`, `@section`).

#### 4. Points de Réflexion & Auto-Évaluation
- *Pourquoi est-il crucial de restreindre le paramètre `{id}` avec `whereNumber()` dès la déclaration de route ?*
- *Quel est l'avantage docimologique et professionnel d'avoir un layout maître partagé par toutes les vues de l'application ?*

---

### T.321.132 — Pratique : Service et vue détaillée
*(Tâche 2 — Réalisation Pratique sur le Projet d'Imitation)*

#### 1. Livrable Attendu
- `app/Services/ArticleService.php` : Classe de service lisant les articles depuis le CSV.
- `app/Http/Controllers/Public/ArticleController.php` : Contrôleur mince avec injection IoC.
- `resources/views/layouts/app.blade.php` : Gabarit maître responsive (navbar, footer).
- `resources/views/articles/show.blade.php` : Vue de consultation détaillée d'un article.
- `resources/views/errors/404.blade.php` : Vue personnalisée d'erreur 404.
- `routes/web.php` : Route nommée `articles.show`.

#### 2. Consignes & Jalons de Réalisation
Bâtir la tranche verticale complète en respectant ces 5 jalons :
1. **Création de la Classe Service :** Coder `ArticleService` dans `app/Services/` avec la méthode `find(int $id)` qui parcourt `database/data/articles.csv` via `fgetcsv()` et retourne un tableau ou `null`.
2. **Implémentation du Contrôleur Mince :** Injecter `ArticleService` dans le constructeur de `ArticleController`. Dans la méthode `show(int $id)`, appeler le service et déclencher `abort(404)` si l'article n'existe pas.
3. **Déclaration de la Route Nommée :** Configurer `Route::get('/articles/{id}', [ArticleController::class, 'show'])->whereNumber('id')->name('articles.show');`.
4. **Mise en Place du Layout Maître :** Créer `resources/views/layouts/app.blade.php` avec en-tête de navigation, conteneur `@yield('content')` et pied de page Tailwind.
5. **Vues de Détail et 404 :** Développer `show.blade.php` héritant du layout avec affichage complet de l'article, et personnaliser `errors/404.blade.php`.

#### 3. Points de Vigilance
- ⚠️ Ne pas oublier de fermer le pointeur de fichier CSV (`fclose()`) après lecture.
- ⚠️ Tester expressément le scénario d'erreur en saisissant un identifiant inexistant dans l'URL (ex: `/articles/9999`).

#### 4. Critères de Validation
- [ ] La navigation sur un article existant (ex: `http://127.0.0.1:8000/articles/1`) affiche l'article complet dans le gabarit maître.
- [ ] La navigation sur un identifiant inexistant renvoie une page 404 propre avec code HTTP 404.
- [ ] Le Live Coding 40 min d'évaluation est réalisable à partir de ce modèle.

---

### T.321.133 — Prompts & Skills : Service métier et détail Fil Rouge
*(Tâche 3 — Conception Prompts & Skills Projet Fil Rouge)*

#### 1. Positionnement dans le Flux Fil Rouge
- Transposition des Étapes 4.3 & 4.4 (Tranche Verticale Complète & Gestion d'Erreurs) vers le Projet Fil Rouge (ex : Consultation détaillée d'un Film).

#### 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-service-detail.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA d'implémenter la tranche verticale complète d'une entité du Projet Fil Rouge (route dynamique, service, contrôleur, layout et gestion 404).

#### 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Architecte applicatif et développeur Laravel 12 senior.
- **Instruction :** Générer l'ensemble des fichiers de la tranche verticale pour l'entité métier `[ENTITE_METIER]` (ex : Film, Séance) en respectant l'architecture 2 couches (Contrôleur mince IoC + Service découplé), le layout Blade Tailwind et le traitement d'erreur 404.
- **Output :** Fichiers complets avec arborescence exacte et instructions de test.
- **Contraintes Négatives :** Zéro code manquant dans les méthodes de service, typage strict imposé.

#### 4. Critères de Validation
- [ ] Le prompt est testé avec l'agent IA sur l'application Fil Rouge.
- [ ] La tranche verticale générée est immédiatement opérationnelle sur serveur local et conforme aux 7 critères de la DoD.
