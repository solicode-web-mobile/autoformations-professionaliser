---
layout: tuto
title: "Justifier et valider le choix de la stack technique (Laravel & NativePHP)"
sous_titre: "Documenter les choix d'ingénierie logicielle : Laravel, MySQL, Tailwind CSS, Preline UI, Alpine.js et NativePHP Mobile"
slug: "justifier-stack-laravel"
slug_domaine: "realisation-projet"
slug_ua: "UA.351.21"
permalink: "/tutos/justifier-stack-laravel/"
tuto_id: "T.351.213"
version: "normal"
ua: "UA.351.21"
maturite: "projet"
type: "tuto-tache"
etape: 3
nav_order: 3
simplified: true
en_construction: false
branche: "sprint0"
sprint: "Sprint 0"
statut_realisation: "a_realiser"
livrables:
  - chemin: "docs/cadrage/stack-technique.md"
    version: "0.1.0"
---

## 1. Travail à faire
Justifiez et documentez l'ensemble des choix technologiques structurant le *Blog des Lauréats* :
1. **Étape 1 — Analyser les exigences techniques :** Reprenez la note de cadrage pour déterminer les besoins de performance, de modularité, de sécurité, d'ergonomie responsive et d'accès nomade sur mobile (affichage et lecture des articles).
2. **Étape 2 — Justifier le framework backend :** Documentez les raisons techniques du choix de **Laravel** (architecture MVC robuste, ORM Eloquent puissant, moteur de templates Blade, écosystème de tests automatisés PHPUnit/Pest, middleware d'authentification).
3. **Étape 3 — Justifier le système de gestion de base de données :** Documentez le choix de **MySQL** relationnel (conformité aux standards industriels, cohérence relationnelle et robustesse transactionnelle ACID).
4. **Étape 4 — Justifier la stack frontend :** Documentez l'intégration de **Tailwind CSS** et de la bibliothèque de composants **Preline UI** pour l'ergonomie responsive multi-écrans, combinés à **Alpine.js** pour les interactions dynamiques légères côté client sans complexité SPA.
5. **Étape 5 — Justifier le développement mobile avec NativePHP :** Documentez le choix de **NativePHP for Mobile** (https://nativephp.com/) pour concevoir et packager l'application mobile de consultation des articles. Expliquez comment NativePHP permet d'embarquer le runtime PHP/Laravel directement dans une application mobile native (Android), garantissant une réutilisation directe du code applicatif, des modèles, des contrôleurs et des vues Blade sans devoir redévelopper un projet séparé dans un autre framework.
6. **Étape 6 — Justifier l'outillage de test et d'Agent IA :** Documentez le protocole TDD et l'utilisation de l'Agent IA copilote sous Windows PowerShell.
7. **Étape 7 — Rédiger le dossier technique :** Renseignez le fichier `docs/cadrage/stack-technique.md`.

## 2. Consignes de Réalisation
- Créez le fichier de documentation technique :
  ```bash
  echo "" > docs/cadrage/stack-technique.md
  ```
- Structurez le document avec les arguments comparatifs suivants :
  - **1. Framework Backend & Socle Unifié (Laravel) :** Architecture MVC élégante, sécurité native (CSRF, XSS, injection SQL), migrations déclaratives, socle mutualisé entre l'application web et le build mobile.
  - **2. Persistance des Données (MySQL) :** Modélisation relationnelle rigoureuse, intégrité référentielle, compatibilité PDO/Eloquent.
  - **3. Couche Présentation & Design (Tailwind CSS / Preline UI) :** Approche utilitaire moderne, gain de temps, composants pré-conçus accessibles et parfaitement adaptés aux formats mobile et desktop.
  - **4. Réactivité Frontend (Alpine.js) :** Interactions déclaratives légères, intégration harmonieuse avec Blade sans compilation lourde.
  - **5. Développement & Déploiement Mobile (NativePHP) :**
    - *Principe technique :* Packaging et exécution de l'application Laravel sous forme d'application native mobile via le framework NativePHP (https://nativephp.com/).
    - *Bénéfice d'ingénierie :* Réutilisation de 100% de la logique métier Laravel et des interfaces Blade, élimination de la duplication de code, respect strict du périmètre In-Scope de consultation/lecture seule des articles.
    - *Comparatif :* Évite la complexité de maintenance d'une double stack distincte (ex : API REST séparée + Flutter/React Native) pour un besoin ciblé de lecture nomade.
  - **6. Qualité & Tests Automatisés (TDD) :** Couverture de tests unitaires et fonctionnels pour sécuriser chaque incrément de sprint.
  - **7. Environnement de Développement :** Windows avec terminal PowerShell, Composer, Node.js, Android Studio (SDK/émulateur Android) et Git.

## 3. Livrable attendu
- **Fichier de projet :** `docs/cadrage/stack-technique.md`.
- **Critère de conformité :** Chaque composant technologique (Laravel, MySQL, Tailwind CSS, Preline UI, Alpine.js et NativePHP pour le mobile) est justifié techniquement par rapport aux exigences et au périmètre du Blog des Lauréats.
