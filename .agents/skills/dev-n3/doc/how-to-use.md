# Guide d'Utilisation : Skill dev-n3

## 1. Rôle du Skill
Le skill `dev-n3` est l'ingénieur logiciel et coach technique dédié au **Niveau N3 (Développer / Réaliser)** de Solicode. Il prend en charge le développement, l'audit d'architecture, la mise en place de tests automatisés (TDD) et la revue de code sur la stack professionnelle : **Laravel**, **Alpine.js**, **Pest/PHPUnit**, **SOLID** et **Scrum**.

---

## 2. Cas d'Usage Principaux

1. **Développement de fonctionnalités Laravel :**
   - Création de modèles Eloquent, migrations, contrôleurs, requêtes de formulaires (Form Requests) et vues Blade.
2. **Intégration d'interactions frontend avec Alpine.js :**
   - Mise en place de composants interactifs réactifs légers (`x-data`, `x-show`, `x-model`).
3. **Mise en œuvre du TDD :**
   - Rédaction de tests unitaires et de fonctionnalités avant ou pendant le développement.
4. **Revue de code & Refactorisation SOLID :**
   - Audit d'un code existant pour isoler les responsabilités, découpler les services et éliminer la dette technique.
5. **Cadrage Scrum & Découpage Technique :**
   - Transformation d'un besoin fonctionnel en User Stories avec critères d'acceptation exploitables.

---

## 3. Prompts Types pour Invoquer le Skill

- *« Agis en tant que dev-n3 pour créer le modèle Eloquent et la migration de gestion des articles avec leurs catégories dans Laravel. »*
- *« Écris les tests Pest pour valider l'enregistrement d'un utilisateur selon le cycle TDD. »*
- *« Audite ce contrôleur Laravel selon les principes SOLID et propose un refactoring avec une couche Service. »*
- *« Crée un composant dynamique de filtrage en temps réel avec Alpine.js pour la liste des projets. »*

---

## 4. Prérequis & Ressources
- Consulter la fiche de profil `.agents/resources/n3/profil-n3.md`.
- Respecter les directives pédagogiques de `.agents/rules/pedagogie-spartel-n3.md` (français A1-A2, impératif direct).
- Respecter les standards techniques `.agents/rules/standards-techniques.md` (UTF-8 sans BOM, GitHub).

---

## 5. Méthode de Vérification des Livrables
1. **Tests au vert :** La suite de tests passe avec succès (`php artisan test`).
2. **Conformité aux standards :** Code conforme aux conventions PSR-12 (`./vendor/bin/pint` ou `phpcs`).
3. **Qualité architecturale :** Les principes SOLID sont respectés et documentés.

