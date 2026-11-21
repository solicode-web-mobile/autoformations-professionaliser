---
layout: tuto
title: "Sprint Review et démonstration live"
sous_titre: "Conduire la démonstration de l'incrément fonctionnel et valider la Definition of Done"
slug: "review-demonstration"
slug_domaine: "realisation-projet"
slug_ua: "cloture-sprint"
permalink: /tutos/review-demonstration/
tuto_id: "T.351.231"
version: "normal"
ua: "UA.351.23"
maturite: "projet"
type: "tuto-tache"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Objectif Opérationnel & Prérequis
- **Position dans le flux :** Phase D — Clôture de Sprint, Rétrospective & Bilan / Étape 12.1 — Démonstration Live.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `scrum/revue-s1.md`.
- **Objectif :** Conduire la démonstration live de l'incrément déployable du *Blog des Lauréats* face au Product Owner et valider critère par critère les 7 éléments de la Definition of Done (DoD).
- **Prérequis :** Tranche verticale complète Laravel stabilisée (`UA.321.13`) sur la branche `sprint1`.

## 2. Déroulement Pas-à-Pas de la Tâche

1. **Étape 1 — Préparation de l'Environnement de Démonstration :**  
   Démarrez le serveur local et préparez les jeux d'essais :

```bash
cd src
php artisan serve
```

   Vérifiez que le fichier de données tabulaires `src/database/data/articles.csv` contient au moins 3 articles complets pour la démonstration.

2. **Étape 2 — Conduite de la Démonstration Fonctionnelle en Direct :**  
   Sous la conduite du Product Owner (formateur) :
   - Présentez la page d'accueil responsive (`/`).
   - Accédez à la liste des articles (`/articles`).
   - Cliquez sur un article et démontrez l'affichage complet de sa vue détaillée (`/articles/1`).
   - Modifiez manuellement l'URL avec un identifiant inexistant (`/articles/999`) et démontrez l'interception propre par la page d'erreur 404 personnalisée.

3. **Étape 3 — Émargement et Validation Formelle de la DoD :**  
   Renseignez le procès-verbal `scrum/revue-s1.md` en auditant les 7 critères bloquants :
   - [x] Code source versionné sur la branche de sprint active (`sprint1`).
   - [x] Architecture 2 couches respectée (Contrôleur mince $\to$ Classe Service).
   - [x] Gabarit Blade responsive sous Tailwind CSS sans CSS inline.
   - [x] Scénario nominal (HTTP 200) fonctionnel en direct.
   - [x] Scénario d'exception (HTTP 404) géré de manière résiliente.
   - [x] Code conforme aux standards PSR-12 et sans warning.
   - [x] Prompts d'ingénierie réutilisables opérationnels.

4. **Étape 4 — Journalisation des commandes :**  
   Consignez la commande de démarrage dans `tutoriels/realisation-projet/cloture-sprint/review-demonstration/review-demonstration.command.md` :

```bash
cd src
php artisan serve
```

## 3. Livrables & Critères de Réussite
- **Livrables attendus :**
  - Procès-verbal de démonstration : `scrum/revue-s1.md` sur la branche `sprint1`.
  - Journal des commandes : `tutoriels/realisation-projet/cloture-sprint/review-demonstration/review-demonstration.command.md`.
- **Critères de validation :**
  - [ ] L'incrément logiciel fonctionne en démonstration réelle sans anomalie bloquante.
  - [ ] Les 7 critères de la DoD sont formellement validés avec le Product Owner dans `scrum/revue-s1.md`.
  - [ ] Le journal consigne fidèlement les commandes opérationnelles exécutées.
