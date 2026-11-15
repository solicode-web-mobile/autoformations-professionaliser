---
title: "Contrôleur, Classe Service et Vue détaillée"
layout: ua
code: "UA.321.13"
maturite: "UA-Lab"
ordre: 11
competence: "C.321"
domaine: "D.321.1"
duree: 14
objectif: >
  Livrer la fonctionnalité centrale de consultation détaillée d'un article du Blog des Lauréats en implémentant une architecture découplée en deux couches (contrôleur mince IoC et classe service sur persistance tabulaire) avec gestion sécurisée de l'erreur 404.
description: >
  Point culminant de la réalisation logicielle du Sprint 1, cette unité livre la tranche verticale complète de l'application sans base relationnelle active. L'apprenant professionnalise son code en encapsulant la lecture tabulaire dans une classe Service injectée automatiquement par le conteneur IoC, et garantit la robustesse utilisateur face aux identifiants inexistants.
notions:
  - "Routes paramétrées dynamiques : paramètres d'URL Route::get('/articles/{id}', ...), contraintes whereNumber('id'), routes nommées name('articles.show')"
  - "Injection de dépendances IoC : déclaration du service dans le constructeur de ArticleController pour résolution automatique par le conteneur Laravel"
  - "Classe Service découplée : classe ArticleService dans app/Services/, méthode find(int $id), extraction et parsing des données tabulaires CSV (fgetcsv())"
  - "Gestion d'erreurs et résilience HTTP : interception d'absence d'article via abort(404), gabarit personnalisé resources/views/errors/404.blade.php"
  - "Héritage de gabarit maître Blade : structure maître resources/views/layouts/app.blade.php avec @yield('content'), héritage par @extends('layouts.app') et @section('content')"
  - "Composants d'interface partagés : barre de navigation (navbar), pied de page (footer) et bouton de retour consultation"
livrable: >
  Incrément logiciel complet et fonctionnel (routes, contrôleur, service, vues de détail et 404) et prompt complet (livrables/ia/prompts/prompt-service-detail.prompt.md).
travail_a_faire: >
  Coder la route nommée, la classe ArticleService, le contrôleur mince, la vue Blade avec gabarit maître et le prompt d'ingénierie réutilisable.
---
