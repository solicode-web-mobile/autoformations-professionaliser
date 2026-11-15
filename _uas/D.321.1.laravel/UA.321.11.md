---
title: "Hello World Laravel : Route et Vue"
layout: ua
code: "UA.321.11"
maturite: "UA-Lab"
ordre: 9
competence: "C.321"
domaine: "D.321.1"
duree: 8
objectif: >
  Valider le bon fonctionnement de l'environnement d'exécution Laravel 12 et livrer la page d'accueil minimale du Blog des Lauréats en configurant le routage web déclaratif et un premier gabarit Blade responsive sous Tailwind CSS.
description: >
  Cette unité d'apprentissage constitue le premier contact opérationnel avec Laravel 12. L'apprenant valide sa chaîne d'outillage locale en instanciant le serveur web, s'approprie le cycle de vie d'une requête HTTP, et produit le premier incrément visible de l'application : une page d'accueil sécurisée et mise en page de manière moderne.
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
