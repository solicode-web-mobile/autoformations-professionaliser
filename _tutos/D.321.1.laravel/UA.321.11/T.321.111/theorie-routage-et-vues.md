---
layout: tuto
title: "Théorie : Routage et Vues"
sous_titre: "Comprendre le cycle de requête HTTP Laravel, routes/web.php et le moteur Blade"
slug: "theorie-routage-et-vues"
permalink: /tutos/theorie-routage-et-vues/
tuto_id: "T.321.111"
version: "normal"
ua: "UA.321.11"
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
- **Position dans le flux :** Phase 4 — Réalisation Applicative & Code Cible / Étape 4.1 — Routage Web & Page d'Accueil.
- **Stack mobilisée :** Framework Laravel 12, Routeur web, Moteur de gabarit Blade, Tailwind CSS.

## 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches nécessaires et concevoir une présentation synthétique (support visuel ou mémo écrit) expliquant le cycle de traitement d'une requête web dans Laravel 12, le fonctionnement du fichier `routes/web.php` et les mécanismes de rendu HTML sécurisé sous Blade.

## 3. Notions Clés du Sprint à Ne Pas Oublier
- Le point d'entrée unique `public/index.php` et le rôle du routeur.
- La syntaxe déclarative `Route::get('/chemin', $action)`.
- La convention d'emplacement des vues dans `resources/views/`.
- La syntaxe d'interpolation `{{ $variable }}` et l'échappement XSS automatique.

## 4. Points de Réflexion & Auto-Évaluation
- *Pourquoi ne doit-on jamais coder de logique métier complexe ni de requêtes SQL directement dans une closure de `routes/web.php` ?*
- *Quelle commande Artisan permet de lister l'ensemble des routes déclarées dans l'application ?*
