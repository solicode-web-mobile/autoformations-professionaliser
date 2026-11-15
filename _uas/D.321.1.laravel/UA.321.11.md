---
title: "Routage et Vues Laravel"
layout: ua
code: "UA.321.11"
maturite: "UA-Lab"
ordre: 11
competence: "C.321"
domaine: "D.321.1"
duree: 8
objectif: >
  Initialiser le socle Laravel 12, configurer le routage web de base et produire un premier rendu visuel via le moteur de gabarit Blade.
description: >
  Prendre en main le framework Laravel 12 et son cycle de requête HTTP. L'apprenant valide l'environnement de développement, déclare sa première route GET et retourne une vue Blade enrichie sous Tailwind CSS.
notions:
  - "Cycle de vie d'une requête HTTP sous Laravel 12 (public/index.php -> Kernel HTTP -> Middlewares -> Routeur -> Vue -> Réponse 200)"
  - "Routage déclaratif dans routes/web.php : façade Route::get(), closures anonymes function () { return view(...); }"
  - "Moteur de gabarit Blade : convention d'arborescence resources/views/*.blade.php, syntaxe d'interpolation {{ $variable }}, protection XSS native"
  - "Intégration CSS utilitaire : intégration de Tailwind CSS (via CDN/Vite), conteneurs centrés, typographie responsive"
livrable: >
  Route d'accueil fonctionnelle et vue Blade stylisée (routes/web.php, resources/views/welcome.blade.php) et prompt (livrables/ia/prompts/prompt-routage-web.prompt.md).
travail_a_faire: >
  Configurer la route GET racine, créer la vue de bienvenue responsive et concevoir le prompt de transposition.
---
