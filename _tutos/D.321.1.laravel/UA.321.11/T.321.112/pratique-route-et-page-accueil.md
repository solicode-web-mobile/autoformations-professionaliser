---
layout: tuto
title: "Pratique : Route et page d'accueil"
sous_titre: "Déclarer la route racine et créer la vue de bienvenue du Blog des Lauréats avec Tailwind CSS"
slug: "pratique-route-et-page-accueil"
permalink: /tutos/pratique-route-et-page-accueil/
tuto_id: "T.321.112"
version: "normal"
ua: "UA.321.11"
maturite: "UA-Lab"
nav_order: 2
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.1 — Page d'Accueil.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `routes/web.php`, `resources/views/welcome.blade.php`
- **Stack mobilisée :** Laravel 12 Router, Blade, Tailwind CSS.

## 2. Travail à Faire (Projet d'Imitation)
Bâtir l'écran d'accueil du *Blog des Lauréats* en respectant ces jalons :
1. **Lancement du Serveur Local :** Démarrer le serveur de test local via `php artisan serve` et valider l'accès sur `http://127.0.0.1:8000`.
2. **Configuration de la Route Racine :** Dans `routes/web.php`, déclarer la route GET `/` appelant la vue `welcome`.
3. **Composition de la Vue Blade :** Concevoir `resources/views/welcome.blade.php` avec bannière d'en-tête, message d'introduction et mise en page responsive avec Tailwind CSS.
4. **Validation Navigateur :** S'assurer de la réponse HTTP 200 et du bon comportement sur écran mobile et desktop.

## 3. Critères de Validation
- [ ] La navigation sur `http://127.0.0.1:8000/` affiche la page d'accueil sans déformation visuelle sur la branche `sprint1`.
- [ ] Le code HTML généré est valide et exempt d'erreur de rendu.