---
title: "Contrôleur, Service et Vue détaillée"
layout: ua
code: "UA.321.13"
maturite: "UA-Lab"
ordre: 13
competence: "C.321"
domaine: "D.321.1"
duree: 14
objectif: >
  Développer l'incrément logiciel principal en architecture deux couches : route dynamique, contrôleur mince avec injection de dépendance, classe Service et gestion HTTP 404.
description: >
  Finaliser la tranche verticale logicielle du Sprint 1. L'apprenant implémente la route paramétrée, injecte la classe Service encapsulant la lecture tabulaire, gère l'exception ressource non trouvée (abort 404) et produit la vue de détail sous gabarit maître responsive.
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
