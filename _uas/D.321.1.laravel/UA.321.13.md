---
title: "Contrôleur, Classe Service et Vue détaillée"
layout: ua
code: "UA.321.13"
slug: "tranche-verticale"
maturite: "UA-Lab"
ordre: 11
competence: "C.321"
domaine: "D.321.1"
duree: 32
objectif: >
  Livrer la fonctionnalité centrale de consultation détaillée d'un article du Blog des Lauréats en implémentant une architecture découplée en deux couches (contrôleur mince IoC et classe service sur persistance tabulaire) avec gestion sécurisée de l'erreur 404.
description: >
  Point culminant de la réalisation logicielle du Sprint 1, cette unité livre la tranche verticale complète de l'application sur le Projet d'imitation. L'apprenant professionnalise son code en encapsulant la lecture CSV dans une classe Service injectée automatiquement par le conteneur IoC, conçoit les deux prompts d'automatisation (Back-End et Front-End) et s'entraîne intensivement à l'épreuve de Live Coding (40 min).
notions:
  - "Routes paramétrées dynamiques : paramètres d'URL Route::get('/articles/{id}', ...), contraintes whereNumber('id'), routes nommées name('articles.show')"
  - "Injection de dépendances IoC : déclaration du service dans le constructeur de ArticleController pour résolution automatique par le conteneur Laravel"
  - "Classe Service découplée : classe ArticleService dans app/Services/, méthode find(int $id), extraction et parsing des données tabulaires CSV (fgetcsv())"
  - "Gestion d'erreurs et résilience HTTP : interception d'absence d'article via abort(404), gabarit personnalisé resources/views/errors/404.blade.php"
  - "Héritage de gabarit maître Blade : structure maître resources/views/layouts/app.blade.php avec @yield('content'), héritage par @extends('layouts.app') et @section('content')"
  - "Composants d'interface partagés : barre de navigation (navbar), pied de page (footer) et bouton de retour consultation"
livrable: >
  Tranche verticale complète (routes/web.php, app/Services/ArticleService.php, app/Http/Controllers/Public/ArticleController.php, resources/views/layouts/app.blade.php, resources/views/articles/show.blade.php, resources/views/errors/404.blade.php) et les deux prompts réutilisables (prompt-back-end.prompt.md, prompt-front-end.prompt.md) sur la branche sprint1.
travail_a_faire: >
  Développer la tranche verticale 2 couches sur le Blog des Lauréats, concevoir les prompts prompt-back-end et prompt-front-end, et réussir l'épreuve de Live Coding 40 min en totale autonomie.
---
