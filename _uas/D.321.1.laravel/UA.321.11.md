---
title: "Hello World Laravel : Route et Vue"
layout: ua
code: "UA.321.11"
slug: "hello-world"
maturite: "UA-Lab"
ordre: 11
competence: "C.321"
domaine: "D.321.1"
duree: 4
objectif: >
  Valider le bon fonctionnement de l'environnement d'exécution Laravel 12 et livrer la page d'accueil minimale du Blog des Lauréats en configurant le routage web déclaratif et un premier gabarit Blade responsive sous Tailwind CSS.
description: >
  Cette unité d'apprentissage constitue le premier contact opérationnel avec Laravel 12. L'apprenant s'approprie le framework, le pattern MVC et le cycle de vie d'une requête HTTP, et produit le premier incrément visible du Blog des Lauréats : une page d'accueil responsive.
notions:
  - "Qu'est-ce que Laravel 12 : framework PHP full-stack moderne, architecture MVC, conteneur IoC, CLI Artisan et moteur Blade"
  - "Cycle de vie d'une requête HTTP sous Laravel 12 (public/index.php -> Kernel HTTP -> Routeur -> Vue -> Réponse 200)"
  - "Routage déclaratif dans routes/web.php : façade Route::get(), closures anonymes function () { return view(...); }"
  - "Moteur de gabarit Blade : convention d'arborescence resources/views/*.blade.php, syntaxe d'interpolation {{ $variable }}, protection XSS native"
livrable: >
  Route d'accueil fonctionnelle et vue Blade stylisée (routes/web.php, resources/views/welcome.blade.php) sur la branche sprint1.
travail_a_faire: >
  Configurer la route GET racine et créer la vue de bienvenue responsive pour le Blog des Lauréats.
---
