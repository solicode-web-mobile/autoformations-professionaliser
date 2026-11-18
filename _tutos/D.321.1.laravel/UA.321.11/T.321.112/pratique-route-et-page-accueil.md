---
layout: tuto
title: "Pratique : Route et page d'accueil"
sous_titre: "Déclarer la route racine et créer la vue de bienvenue du Blog des Lauréats avec Tailwind CSS"
slug: "route-accueil-blade"
slug_domaine: "laravel"
slug_ua: "hello-world"
permalink: /tutos/route-accueil-blade/
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

## 1. Travail à faire
Configurer le premier incrément visible de l'application *Blog des Lauréats* sous Laravel 12 : lancer le serveur de test local, déclarer la route GET racine dans `src/routes/web.php` et composer la vue d'accueil `src/resources/views/welcome.blade.php` avec une mise en page responsive stylisée sous Tailwind CSS.

Vous devez concevoir :
1. La route racine déclarative dans `src/routes/web.php`.
2. Le gabarit d'accueil dans `src/resources/views/welcome.blade.php`.
3. Le compte-rendu technique de vérification : `route-accueil-blade.md`.
4. Le diaporama Marp de restitution : `presentation-route-accueil-blade.md`.
5. Le journal des commandes exécutées : `route-accueil-blade.command.md`.

## 2. Consignes & Spécifications de Réalisation

1. **Jalon 1 — Démarrage de l'Environnement Local :**  
   Déplacez-vous dans le dossier de l'application Laravel (`src/`) et lancez le serveur de développement local :

```bash
cd src
php artisan serve
```

   Vérifiez que le serveur écoute correctement sur `http://127.0.0.1:8000`.

2. **Jalon 2 — Configuration de la Route Racine :**  
   Dans le fichier de routage `src/routes/web.php`, déclarez la route GET sur l'URI racine `/` retournant la vue `welcome` :
   - Utilisez la façade `Route::get('/', function () { return view('welcome'); });`.
   - Attribuez un nom explicite à la route avec la méthode `->name('home')`.

3. **Jalon 3 — Composition du Gabarit Blade Responsive :**  
   Dans `src/resources/views/welcome.blade.php`, composez la page de bienvenue du *Blog des Lauréats* :
   - Intégrez la structure HTML5 complète avec la balise viewport pour le responsive design.
   - Ajoutez le lien CDN Tailwind CSS ou la directive de build des assets.
   - Composez une bannière d'en-tête percutante valorisant les lauréats de Solicode.
   - Intégrez un bouton d'action invitant à découvrir les articles publiés.
   - *Garde-fou :* Interdiction formelle de CSS inline (`style="..."`). Utilisez exclusivement les classes utilitaires Tailwind CSS (`flex`, `grid`, `text-center`, `p-6`, `rounded-lg`).

4. **Jalon 4 — Validation Navigateur & Journalisation :**  
   Accédez à `http://127.0.0.1:8000/` depuis votre navigateur et contrôlez le bon affichage sur écran desktop et mobile (outils de développement F12).  
   Consignez les commandes exécutées dans `tutoriels/laravel/hello-world/route-accueil-blade/route-accueil-blade.command.md` :

```bash
cd src
php artisan serve
```

## 3. Livrables & Critères de validation
- **Livrables attendus :**
  - Fichiers de code source : `src/routes/web.php` et `src/resources/views/welcome.blade.php` sur la branche `sprint1`.
  - Compte-rendu technique : `tutoriels/laravel/hello-world/route-accueil-blade/route-accueil-blade.md` sur la branche `sprint1`.
  - Diaporama Marp : `tutoriels/laravel/hello-world/route-accueil-blade/presentation-route-accueil-blade.md` sur la branche `sprint1`.
  - Journal des commandes : `tutoriels/laravel/hello-world/route-accueil-blade/route-accueil-blade.command.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le serveur local répond avec un code HTTP 200 sur `http://127.0.0.1:8000/`.
  - [ ] La vue `welcome.blade.php` est responsive et exempte de CSS inline.
  - [ ] La route est nommée et déclarée de manière propre dans `src/routes/web.php`.
  - [ ] Le journal `route-accueil-blade.command.md` consigne fidèlement les commandes.
