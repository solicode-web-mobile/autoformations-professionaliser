# Profil Pédagogique & Technique du Niveau N3 (Développer / Réaliser)

> **Ressource Spécifique au Niveau N3 — Solicode**  
> Ce document définit le profil des apprenants, les prérequis validés, et le périmètre technique cible pour le niveau N3.

---

## 1. Profil des Apprenants & Prérequis Validés

Les apprenants abordant le niveau N3 ont validé avec succès :
1. **Niveau N1 (Découvrir) :**
   - Syntaxe fondamentale HTML5 sémantique, CSS3 (mise en forme et flexbox/grid), JavaScript client (DOM, événements, fetch).
   - PHP procédural et modulaire (fonctions, inclusion, formulaires GET/POST, sessions).
   - SQL relationnel de base et requêtes préparées PDO avec MySQL.
   - Méthodologie d'autoformation pas-à-pas et utilisation fondamentale de Git (add, commit, push).
2. **Niveau N2 (Prototyper) :**
   - Programmation Orientée Objet (POO) en PHP : classes, instanciation, encapsulation (`private`/`protected`/`public`), héritage, interfaces.
   - Architecture en couches 3-tiers : Présentation (UI), Traitement (Métier), Données (DAO/Repository).
   - Modélisation Objet avec UML : diagrammes de classes, modélisation des relations (association, composition, agrégation).
   - Réalisation de prototypes dirigés autonomes.

---

## 2. Périmètre & Technologies Cibles en N3

En Niveau N3 (**Développer / Réaliser**), les apprenants acquièrent des compétences professionnelles complètes :

- **Framework Backend :** **Laravel**
  - Architecture MVC moderne, routage avancé, middlewares.
  - ORM Eloquent, migrations, seeders, factories, relations de base de données.
  - Blade templating, validation de formulaires, authentification et autorisations (Policies/Gates).
  - Conception d'APIs RESTful avec gestion des ressources JSON et codes HTTP standards.
- **Frontend Léger & Réactif :** **Alpine.js**
  - Composants dynamiques réactifs, liaisons de données (`x-data`, `x-bind`, `x-model`), gestion d'événements (`x-on`).
  - Intégration harmonieuse avec Blade et Tailwind CSS sans lourdeur de bundler complexe.
- **Assurance Qualité & Tests :** **TDD (Test-Driven Development)**
  - Tests unitaires et d'intégration avec Pest ou PHPUnit.
  - Cycle Red-Green-Refactor : écrire le test d'abord, implémenter le code minimum, puis refactoriser.
- **Conception & Principes Logiciels :** **Principes SOLID**
  - **S** : Single Responsibility Principle (Responsabilité Unique).
  - **O** : Open/Closed Principle (Ouvert à l'extension, fermé à la modification).
  - **L** : Liskov Substitution Principle (Substitution de Liskov).
  - **I** : Interface Segregation Principle (Ségrégation des interfaces).
  - **D** : Dependency Inversion Principle (Inversion des dépendances / Injection de dépendances).
- **Méthodologie & Travail d'Équipe :** **Scrum / Méthodes Agiles**
  - Découpage du besoin en User Stories avec critères d'acceptation précis.
  - Organisation en Sprints, gestion de backlog (Kanban/GitHub Projects), revues de sprint et démonstrations.

---

## 3. Format des Livrables en N3

- **Code source :** Dépôt GitHub professionnel avec arborescence claire, respect des standards PSR-12, historique de commits atomiques conventionnels (`feat:`, `fix:`, `test:`, `refactor:`).
- **Tests :** Suite de tests automatisés validée (`php artisan test`).
- **Documentation :** README complet expliquant le projet, les prérequis, la procédure d'installation (`composer install`, migrations), et le guide d'utilisation.

