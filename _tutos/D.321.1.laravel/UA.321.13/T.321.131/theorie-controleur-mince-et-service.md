---
layout: tuto
title: "Théorie : Contrôleur mince et Service"
sous_titre: "Comprendre l'injection IoC, les routes nommées paramétrées, la résilience 404 et le layout Blade maître"
slug: "theorie-controleur-mince-et-service"
permalink: /tutos/theorie-controleur-mince-et-service/
tuto_id: "T.321.131"
version: "normal"
ua: "UA.321.13"
maturite: "UA-Lab"
nav_order: 1
simplified: true
en_construction: true
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase 4 — Réalisation Applicative & Code Cible / Étape 4.3 — Tranche Verticale Complète & Étape 4.4 — Résilience & Erreurs HTTP.
- **Stack mobilisée :** Laravel IoC Container, Dependency Injection, Routes dynamiques, Exceptions HTTP 404, Héritage Blade.

## 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches nécessaires et concevoir une présentation synthétique (support visuel ou mémo écrit) expliquant le fonctionnement de l'injection de dépendances dans Laravel, le rôle de la classe Service comme passerelle vers les données, les mécanismes de capture d'erreurs 404 et le principe d'héritage de gabarit maître sous Blade.

## 3. Notions Clés du Sprint à Ne Pas Oublier
- Les routes dynamiques paramétrées `{id}` et la contrainte de type `whereNumber('id')`.
- L'injection de dépendances automatique par le constructeur (IoC).
- L'encapsulation de la lecture des données (CSV) dans `ArticleService`.
- Le déclenchement de `abort(404)` et la personnalisation de la réponse d'erreur.
- L'architecture de gabarit maître Blade (`@extends`, `@yield`, `@section`).

## 4. Points de Réflexion & Auto-Évaluation
- *Pourquoi est-il crucial de restreindre le paramètre `{id}` avec `whereNumber()` dès la déclaration de route ?*
- *Quel est l'avantage docimologique et professionnel d'avoir un layout maître partagé par toutes les vues de l'application ?*
