---
layout: tuto
title: "Théorie : Routage et Vues sous Laravel"
sous_titre: "Découvrir le framework Laravel 12, le cycle de vie d'une requête HTTP et le moteur de templates Blade"
slug: "theorie-routage-et-vues"
permalink: /tutos/theorie-routage-et-vues/
tuto_id: "T.321.111"
version: "normal"
ua: "UA.321.11"
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

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase C — Réalisation & Implémentation Logicielle / Étape 4.1 — Routage & Vues.
- **Branche Git :** `sprint1`
- **Stack mobilisée :** Framework Laravel 12, Routeur web, Moteur Blade, Tailwind CSS.

## 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches nécessaires et formaliser une fiche de synthèse expliquant le rôle de Laravel, le parcours d'une requête HTTP jusqu'à la vue et les mécanismes de rendu HTML sécurisé sous Blade.

## 3. Répartition Didactique (Règle des 20/80)

### Les 20% fournis directement au tutoriel :
- **Qu'est-ce que Laravel :** Framework PHP moderne implémentant le modèle MVC (Modèle - Vue - Contrôleur) et fournissant un écosystème outillé complet (Artisan, Composer, moteur Blade, conteneur d'injection de dépendances).
- **Cycle d'une requête HTTP dans Laravel :**
  1. Point d'entrée unique : `public/index.php`.
  2. Chargement du Kernel HTTP et passage par les middlewares globaux.
  3. Résolution de l'URL par le routeur (`routes/web.php`).
  4. Exécution de l'action associée (closure ou contrôleur).
  5. Rendu d'une vue Blade (`resources/views/`) et émission de la réponse HTTP 200.
- **Moteur de gabarits Blade :** Fichiers `.blade.php`, syntaxe d'interpolation `{% raw %}{{ $variable }}{% endraw %}` avec protection automatique contre les failles XSS (`htmlspecialchars`).

### Les 80% recherchés par l'apprenant :
- Organisation de l'arborescence standard d'un projet Laravel (`app/`, `bootstrap/`, `config/`, `database/`, `resources/`, `routes/`, `storage/`).
- Fonctionnalités de la CLI Artisan (`php artisan list`, `php artisan route:list`).

## 4. Livrable Attendu
- Fiche de synthèse sur les bases de Laravel intégrée dans le journal d'apprentissage personnel de l'apprenant.