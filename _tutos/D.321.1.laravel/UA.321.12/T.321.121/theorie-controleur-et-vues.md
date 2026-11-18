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
maturite: "UA-Lab"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.2 — Contrôleur HTTP.
- **Branche Git :** `sprint1`
- **Stack mobilisée :** Pattern MVC, Contrôleur HTTP Laravel, Directives Blade itératives.

## 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches nécessaires et formaliser une fiche de synthèse expliquant le rôle du contrôleur dans le découpage MVC, l'intérêt d'extraire la logique hors des routes, et l'usage des directives Blade pour afficher des collections de données.

## 3. Répartition Didactique (Règle des 20/80)

### Les 20% fournis directement au tutoriel :
- **Rôle du Contrôleur HTTP :** Agir comme coordinateur entre la requête entrante et la vue. Il élimine le code métier des fichiers de routage (`routes/web.php`), prépare les données et retourne une `Response`.
- **Scaffolding Artisan :** Commande `php artisan make:controller Public/CategoryController` pour générer une classe standard dans `app/Http/Controllers/`.
- **Passage de variables à la vue :** Utilisation de la fonction helper `view('categories.index', compact('categories'))` ou d'un tableau associatif clé-valeur.
- **Directives itératives Blade :**
  - `@foreach ($items as $item) ... @endforeach` pour boucler sur une collection.
  - `@forelse ($items as $item) ... @empty ... @endforelse` pour gérer de manière robuste l'affichage alternatif lorsque la collection est vide.

### Les 80% recherchés par l'apprenant :
- Différence architecturale entre un contrôleur conventionnel (avec plusieurs méthodes d'action) et un contrôleur à action unique (*Single Action Controller* utilisant `__invoke`).
- Manipulation fluide des collections PHP / Laravel pour trier et filtrer les données avant affichage.

## 4. Livrable Attendu
- Fiche de synthèse sur les contrôleurs MVC intégrée dans le journal d'apprentissage personnel de l'apprenant.