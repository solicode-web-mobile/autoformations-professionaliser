---
title: "Contrôleur et Vue de collection"
layout: ua
code: "UA.321.12"
maturite: "UA-Lab"
ordre: 12
competence: "C.321"
domaine: "D.321.1"
duree: 8
objectif: >
  Découpler la logique de requête par un contrôleur HTTP dédié et afficher une collection de données structurées avec les directives de boucle Blade.
description: >
  Implémenter le pattern MVC au niveau du contrôleur. L'apprenant génère un contrôleur HTTP avec artisan, extrait la logique de la route vers une méthode d'action et transmet un jeu de données à une vue Blade itérative.
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
