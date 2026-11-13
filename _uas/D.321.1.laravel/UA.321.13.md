---
title: "Contrôleur, Classe Service et Vue détaillée"
layout: ua
code: "UA.321.13"
ordre: 13
competence: "C.321"
domaine: "D.321.1"
duree: 12
objectif: >
  Développer l'incrément logiciel principal du sprint en architecture 2 couches sous Laravel 12 avec route dynamique, contrôleur mince, classe Service et gestion 404.
description: >
  Développer l'incrément logiciel principal du sprint en architecture 2 couches sous Laravel 12 : déclaration d'une route paramétrée dynamique, contrôleur mince avec injection d'une classe Service de lecture de données tabulaires (CSV), rendu d'une vue Blade responsive et déclenchement de l'erreur HTTP 404 (abort(404)).
notions:
  - "Paramètres d'URL Dynamiques & Routes Nommées : Routes avec paramètres {id} ou {slug} et génération d'URL via route()"
  - "Contrôleur Mince & Injection IoC : Injection de ArticleService dans le contrôleur via le constructeur"
  - "Classe Service & Lecture Tabulaire : Encapsulation de la lecture CSV sans base relationnelle"
  - "Gestion de l'Erreur HTTP 404 : Interception du cas de ressource non trouvée via abort(404) et personnalisation de errors/404.blade.php"
  - "Gabarit Blade Maître : Héritage structurel (layouts/app.blade.php, @extends, @section)"
livrable: >
  Code source complet de la consultation détaillée : routes/web.php (articles.show), ArticleController.php, ArticleService.php, layouts/app.blade.php, articles/show.blade.php et errors/404.blade.php.
travail_a_faire: >
  Développer l'incrément complet de consultation d'article avec ArticleController, ArticleService (données CSV) et les vues Blade responsive.
---

