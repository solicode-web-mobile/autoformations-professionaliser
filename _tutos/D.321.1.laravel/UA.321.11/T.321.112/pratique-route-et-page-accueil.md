---
layout: tuto
title: "Pratique : Route et page d'accueil"
sous_titre: "Configurer la route racine GET / et composer la vue d'accueil responsive sous Tailwind CSS"
slug: "pratique-route-et-page-accueil"
permalink: /tutos/pratique-route-et-page-accueil/
tuto_id: "T.321.112"
version: "normal"
ua: "UA.321.11"
maturite: "UA-Lab"
nav_order: 2
simplified: true
en_construction: true
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Livrable Attendu
- `routes/web.php` : Déclaration de la route racine `/`.
- `resources/views/welcome.blade.php` : Gabarit d'accueil complet et stylisé sous Tailwind CSS.

## 2. Consignes & Jalons de Réalisation
Bâtir l'écran d'accueil en respectant ces 4 jalons :
1. **Lancement du Serveur Local :** Exécuter `php artisan serve` à la racine et vérifier l'accès sur `http://127.0.0.1:8000`.
2. **Configuration de la Route Racine :** Déclarer la route GET `/` appelant explicitement la vue `welcome`.
3. **Composition de la Vue Blade :** Créer la page HTML5 sémantique, intégrer Tailwind CSS, concevoir la bannière d'accueil du *Blog des Lauréats* et le message d'introduction.
4. **Vérification Navigateur :** S'assurer de la réponse HTTP 200 et de l'adaptation sur mobile (responsive).

## 3. Points de Vigilance
- ⚠️ Attention à la casse du nom du fichier de vue (toujours en minuscules sous Linux).
- ⚠️ Exécuter impérativement la commande artisan à la racine du projet Laravel.

## 4. Critères de Validation
- [ ] La navigation sur `http://127.0.0.1:8000/` affiche la page d'accueil sans déformation visuelle.
- [ ] Le code HTML généré est valide et sémantique.
- [ ] Le commit Git respecte la convention d'équipe.
