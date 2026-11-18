---
title: "Démarrage rapide Laravel : Contrôleur et Vue"
layout: ua
code: "UA.321.12"
slug: "controleur-vue"
maturite: "UA-Lab"
ordre: 11
competence: "C.321"
domaine: "D.321.1"
duree: 6
objectif: >
  Mettre en œuvre le pattern MVC en isolant l'orchestration HTTP dans un contrôleur dédié pour extraire et afficher dynamiquement la collection des articles à travers des boucles Blade stylisées.
description: >
  L'apprenant franchit une étape clé de structuration sur le Projet d'imitation en éliminant les closures directes dans les routes au profit d'un contrôleur HTTP mince. Il apprend à séparer la réception de la requête, la préparation des données et leur restitution visuelle dynamique sous forme de grille responsive.
notions:
  - "Rôle du contrôleur HTTP dans l'architecture MVC : récepteur de Request, orchestrateur d'action et fournisseur de Response"
  - "Commande de scaffolding Artisan : php artisan make:controller Public/ArticleController"
  - "Transmission de données structurées : fonction d'assistance view('vue', compact('articles')) et tableaux associatifs"
  - "Directives de boucle Blade : @foreach, @forelse, @empty, @endforeach pour itérer de manière résiliente sur une collection"
livrable: >
  Contrôleur HTTP et vue de collection (app/Http/Controllers/Public/ArticleController.php, resources/views/articles/index.blade.php) sur la branche sprint1.
travail_a_faire: >
  Créer le contrôleur avec Artisan, définir l'action d'affichage de liste d'articles et composer la vue itérative Blade pour le Blog des Lauréats.
---
