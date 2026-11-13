---
title: "Bases de Laravel : routes, contrôleurs & Blade"
layout: ua
code: "UA.321.11"
ordre: 7
competence: "C.321"
domaine: "D.321.1"
duree: 12
objectif: >
  Développer le premier incrément fonctionnel web sous Laravel 12 sans base de données relationnelle active.
description: >
  Développer le premier incrément fonctionnel web sous Laravel 12 sans base de données relationnelle active : configurer le projet, déclarer des routes publiques nommées avec paramètres d'URL dynamiques, créer un contrôleur mince avec injection de dépendance IoC du Service de données CSV, et composer des gabarits Blade responsive intégrant la gestion conviviale de l'erreur 404.
notions:
  - "Initialisation et arborescence standard de Laravel 12 (routes/, app/Http/Controllers/, resources/views/)"
  - "Routage déclaratif modulaire, routes nommées et injection de paramètres dynamiques ({slug})"
  - "Contrôleur HTTP mince avec injection de dépendances IoC et déclenchement d'erreur abort(404)"
  - "Moteur de gabarits Blade (gabarit maître, héritage structurel, affichage sécurisé, directives Tailwind CSS)"
  - "Gestion conviviale des erreurs (personnalisation de la vue d'erreur 404)"
livrable: >
  Code source complet de la consultation d'un article : routes/web.php, ArticleController.php, ArticleService.php, gabarit maître Blade et vue d'erreur 404.
travail_a_faire: >
  Développer sous Laravel 12 la route, le contrôleur ArticleController, le service ArticleService et les vues Blade pour la page de détail d'un article.
---

