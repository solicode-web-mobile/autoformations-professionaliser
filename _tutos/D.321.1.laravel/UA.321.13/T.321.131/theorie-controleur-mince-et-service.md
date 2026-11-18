---
layout: tuto
title: "Théorie : Injection de dépendances et Classe Service"
sous_titre: "Comprendre le conteneur IoC, l'injection par le constructeur, la résilience 404 et le layout maître Blade"
slug: "service-csv-ioc"
slug_domaine: "laravel"
slug_ua: "tranche-verticale"
permalink: /tutos/service-csv-ioc/
tuto_id: "T.321.131"
version: "normal"
ua: "UA.321.13"
maturite: "UA-Lab"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Travail à faire
Effectuer les recherches documentaires nécessaires, concevoir une fiche de synthèse personnelle et préparer un diaporama de restitution Marp expliquant le fonctionnement du conteneur d'inversion de contrôle (IoC Container) de Laravel, l'injection de dépendances par le constructeur, le rôle d'encapsulation de la classe Service pour la persistance des données, la gestion des erreurs d'absence de ressource via l'exception HTTP 404 et le patron d'héritage de gabarit maître sous Blade.

## 2. Notions fondamentales
- **Le Conteneur d'Inversion de Contrôle (IoC Container & Auto-wiring) :**
  - Cœur de l'architecture Laravel : il inspecte le typage des paramètres déclarés dans le constructeur d'un contrôleur et injecte automatiquement l'instance requise (`public function __construct(ArticleService $articleService)`).
  - Évite l'instanciation manuelle (`new ArticleService()`) et facilite grandement le remplacement de composants pour les tests unitaires.
- **La Classe Service Découplée :**
  - Classe PHP pure située sous `app/Services/` (ex: `ArticleService.php`), totalement indépendante de la couche HTTP (ne manipule ni `Request` ni `Response`).
  - Fournit des méthodes métier claires : `find(int $id): ?array` et `all(): array`.
  - En Sprint 1, elle abstrait l'ouverture et le parsing du fichier tabulaire `articles.csv` via la fonction native `fgetcsv()`.
- **Gestion Résiliente de l'Erreur HTTP 404 :**
  - Lorsque la méthode `find($id)` renvoie `null`, le contrôleur interrompt immédiatement l'exécution via la fonction d'assistance `abort(404)`.
  - Laravel capture l'exception `NotFoundHttpException` et restitue automatiquement la vue d'erreur personnalisée située dans `resources/views/errors/404.blade.php`.
- **Héritage de Layout Maître Blade :**
  - Gabarit maître (`resources/views/layouts/app.blade.php`) définissant la coquille HTML5, la barre de navigation, le pied de page et le point d'injection dynamique `@yield('content')`.
  - Vues enfants (`resources/views/articles/show.blade.php`) déclarant `@extends('layouts.app')` et encapsulant leur contenu propre dans `@section('content') ... @endsection`.

## 3. Recherches à effectuer
- Analyser la mécanique de résolution de dépendance par réflexion (*PHP Reflection API*) utilisée en coulisse par le conteneur IoC de Laravel.
- Étudier comment créer et enregistrer un `ServiceProvider` pour lier une interface abstraite à une implémentation concrète de service.
- Examiner la directive Blade `@yield` face aux nouveaux composants anonymes Blade (`<x-layout>`) introduits dans les versions récentes de Laravel.

## 4. Livrable attendu
- **Fiche technique de synthèse :** `tutoriels/laravel/tranche-verticale/service-csv-ioc/service-csv-ioc.md` sur la branche `sprint1`.
- **Diaporama Marp de restitution :** `tutoriels/laravel/tranche-verticale/service-csv-ioc/presentation-service-csv-ioc.md` sur la branche `sprint1`.
- **Contenu attendu :** Synthèse personnelle structurée reprenant les notions fondamentales (IoC, Classe Service, gestion 404, layout maître Blade) et les réponses documentées aux recherches à effectuer.
