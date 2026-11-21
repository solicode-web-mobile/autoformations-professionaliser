---
layout: tuto
title: "Théorie : Routage et Vues sous Laravel"
sous_titre: "Découvrir le framework Laravel, le cycle de vie d'une requête HTTP et le moteur de templates Blade"
slug: "routage-fondamentaux"
slug_domaine: "laravel"
slug_ua: "hello-world"
permalink: /tutos/routage-fondamentaux/
tuto_id: "T.321.111"
version: "normal"
ua: "UA.321.11"
maturite: "lab"
type: "tuto-atelier"
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
Effectuer les recherches documentaires nécessaires, concevoir une fiche de synthèse personnelle et préparer un diaporama de restitution Marp expliquant l'architecture générale de Laravel, le cycle de vie complet d'une requête HTTP du point d'entrée jusqu'à l'émission de la réponse, le fonctionnement déclaratif du routeur web et les mécanismes de rendu sécurisé sous le moteur de gabarits Blade.

## 2. Notions fondamentales
- **Qu'est-ce que Laravel :**
  - Framework PHP full-stack moderne implémentant l'architecture MVC (Modèle - Vue - Contrôleur).
  - Fournit un écosystème outillé complet : outil en ligne de commande Artisan, conteneur d'inversion de contrôle (IoC), moteur de gabarits Blade, gestion de dépendances via Composer.
- **Cycle de Vie d'une Requête HTTP sous Laravel :**
  1. *Point d'entrée unique :* Le serveur web redirige toute requête HTTP vers `public/index.php`.
  2. *Initialisation du Kernel :* Chargement du conteneur de services et traversée des middlewares globaux de sécurité (protection CSRF, sessions).
  3. *Résolution par le Routeur :* Le fichier déclaratif `routes/web.php` fait correspondre la méthode HTTP (GET, POST) et l'URI à une action logicielle (closure ou contrôleur).
  4. *Exécution & Rendu :* L'action traite la demande, appelle éventuellement une vue Blade et compile le gabarit en code HTML5 pur.
  5. *Émission de la Réponse :* Le Kernel renvoie la `Response` HTTP (statut 200, en-têtes) vers le navigateur de l'utilisateur.
- **Le Moteur de Gabarits Blade :**
  - Fichiers nommés avec l'extension double `.blade.php` situés sous `resources/views/`.
  - Syntaxe d'interpolation `{% raw %}{{ $variable }}{% endraw %}` qui applique automatiquement la fonction PHP `htmlspecialchars()` pour immuniser l'affichage contre les attaques par injection XSS (*Cross-Site Scripting*).
  - Compilation en cache sous `storage/framework/views/` pour une performance optimale sans recalcul à chaque requête.

## 3. Recherches à effectuer
- Analyser l'organisation des répertoires standards d'un projet Laravel (`app/`, `bootstrap/`, `config/`, `database/`, `resources/`, `routes/`, `storage/`).
- Étudier les commandes d'inspection de routes offertes par l'outil Artisan (`php artisan route:list`).
- Comparer le moteur Blade avec d'autres moteurs de templates PHP (Twig, Smarty) sur les critères de simplicité et de sécurité.

## 4. Livrable attendu
- **Fiche technique de synthèse :** `tutoriels/laravel/hello-world/routage-fondamentaux/routage-fondamentaux.md` sur la branche `sprint1`.
- **Diaporama Marp de restitution :** `tutoriels/laravel/hello-world/routage-fondamentaux/presentation-routage-fondamentaux.md` sur la branche `sprint1`.
- **Contenu attendu :** Synthèse personnelle structurée reprenant les notions fondamentales (MVC Laravel, cycle de vie HTTP, routage, Blade et sécurité XSS) et les réponses documentées aux recherches à effectuer.
