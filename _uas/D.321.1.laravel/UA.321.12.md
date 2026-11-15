---
title: "Démarrage rapide Laravel : Contrôleur et Vue"
layout: ua
code: "UA.321.12"
maturite: "UA-Lab"
ordre: 10
competence: "C.321"
domaine: "D.321.1"
duree: 8
objectif: >
  Mettre en œuvre le pattern MVC en isolant l'orchestration HTTP dans un contrôleur dédié pour extraire et afficher dynamiquement la collection des catégories d'articles à travers des boucles Blade stylisées.
description: >
  L'apprenant franchit une étape clé de structuration en éliminant les closures directes dans les routes au profit d'un contrôleur HTTP mince. Il apprend à séparer la réception de la requête, la préparation des données et leur restitution visuelle dynamique sous forme de grille responsive.
notions:
  - "Rôle du contrôleur HTTP dans l'architecture MVC : récepteur de Request, orchestrateur d'action et fournisseur de Response"
  - "Commande de scaffolding Artisan : php artisan make:controller Public/CategoryController"
  - "Transmission de données structurées : fonction d'assistance view('vue', compact('categories')) et tableaux associatifs"
  - "Directives de boucle Blade : @foreach, @forelse, @empty, @endforeach pour itérer de manière résiliente sur une collection"
  - "Grille de cartes responsive sous Tailwind CSS (grid grid-cols-1 md:grid-cols-3 gap-6)"
livrable: >
  Contrôleur HTTP et vue de collection (app/Http/Controllers/Public/CategoryController.php, resources/views/categories/index.blade.php) et prompt (livrables/ia/prompts/prompt-controleur-collection.prompt.md).
travail_a_faire: >
  Créer le contrôleur avec artisan, définir l'action d'affichage de liste, composer la vue avec directive de boucle et concevoir le prompt de transposition.
---
