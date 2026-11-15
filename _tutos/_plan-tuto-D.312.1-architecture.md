# Plan des Tutoriels : D.312.1 — Architecture Logicielle en Couches

> **Domaine :** `D.312.1` | **Compétence :** `C.312` — Concevoir et structurer l'architecture logicielle | **Session :** S01  
> **Niveau de Maturité :** UA-Lab (Atelier pratique guidé)  
> **Branche Git de Travail :** `sprint1`  
> **Projet Référence :** Projet d'imitation (*Blog des Lauréats*)  
> **Référentiels Liés :** [`../../3.sprints/flux-travail-n3.md`](../../3.sprints/flux-travail-n3.md) | [`../../3.sprints/stack-technique-n3.md`](../../3.sprints/stack-technique-n3.md)

---

## 1. Description des Unités d'Apprentissage du Domaine

### UA.312.11 — Architecture logicielle en deux couches

- **Code :** `UA.312.11`
- **Maturité :** `UA-Lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 08
- **Positionnement Flux de Travail :** Phase B — Analyse, Conception & Planification / Étape 3.1 — Découplage Architectural & Décision ADR
- **Briques Stack Technique :** Architecture 2 couches, Contrôleur mince IoC, Classe Service, ADR, Mermaid séquence
- **Compétence :** `C.312` — Concevoir et structurer l'architecture logicielle
- **Domaine :** `D.312.1` — Architecture logicielle en couches
- **Durée estimée :** 4 heures
- **Objectif :** Concevoir une architecture logicielle découplée isolant le contrôleur mince de la persistance tabulaire via une classe Service dédiée et formaliser ce choix technique stratégique dans un ADR opposable avec diagramme de séquence HTTP.
- **Description :** Isoler la logique de présentation de la logique métier et d'accès aux données. L'apprenant conçoit l'architecture en deux couches, rédige l'ADR-01 justifiant le choix sans base de données relationnelle initiale et modélise la séquence HTTP.
- **Notions Clés Utilisées dans le Sprint :**
  - Principe de séparation des responsabilités (SoC) : découplage strict entre contrôleur HTTP et logique métier/données.
  - Patron architectural en 2 couches : Contrôleur mince $\to$ Classe Service.
  - Décision technique de persistance transitoire : choix délibéré d'une source tabulaire CSV en mémoire (`articles.csv`), zéro SGBD relationnel en amorçage S1.
  - Architecture Decision Record (ADR) : formalisation standardisée de l'ADR-01.
  - Modélisation de flux HTTP en séquence : diagramme Mermaid `sequenceDiagram` illustrant le parcours complet de la requête (cas nominal et cas d'erreur 404).
- **Livrables :** Dossier d'architecture S1 et ADR-01 (`livrables/architecture/architecture-sprint1.md`) sur la branche `sprint1`.
- **Travail à Faire :** Rédiger l'ADR-01 et modéliser le diagramme de séquence en Mermaid.js pour le Blog des Lauréats.

---

## 2. Plan des Tutoriels : UA.312.11

### T.312.111 — Théorie : Architecture 2 couches & ADR

- **Code :** `T.312.111`
- **Maturité :** `UA-Lab` (Présentation théorique & assimilation)
- **Unité d'Apprentissage parente :** `UA.312.11`
- **Titre Canonique :** Théorie : Architecture 2 couches & ADR
- **Position dans le Flux :** Phase B — Analyse, Conception & Planification / Étape 3.1 — Découplage Architectural.
- **Branche Git de travail :** `sprint1`
- **Objectif Opérationnel :** Comprendre les fondements de la séparation des responsabilités, le découplage Contrôleur/Service et la structure d'un ADR.
- **Répartition Didactique (Règle des 20/80) :**
  - **Les 20% fournis directement au tutoriel :**
    - Définition de l'architecture 2 couches : Contrôleur mince (aiguilleur HTTP) $\to$ Classe Service (métier et abstraction des données).
    - Principe de séparation des responsabilités (SoC) et risques des « contrôleurs obèses » (*Fat Controllers*).
    - Structure canonique d'un ADR : Titre, Statut, Contexte, Décision, Conséquences positives/négatives, Alternatives écartées.
  - **Les 80% recherchés par l'apprenant :**
    - Analyse comparative : amorçage rapide par source tabulaire CSV vs mise en place immédiate d'un SGBD relationnel.
    - Évolution de l'architecture : identification des composants modifiés lors du passage ultérieur à une base relationnelle.
- **Critère de Réussite :** Fiche d'assimilation des principes d'architecture intégrée au journal d'apprentissage.

---

### T.312.112 — Pratique : Décision d'architecture (ADR-01) & Diagramme de séquence

- **Code :** `T.312.112`
- **Maturité :** `UA-Lab` (Pratique guidée sur projet d'imitation)
- **Unité d'Apprentissage parente :** `UA.312.11`
- **Titre Canonique :** Pratique : Décision d'architecture (ADR-01) & Diagramme de séquence
- **Position dans le Flux :** Phase B — Analyse, Conception & Planification / Étape 3.1 — Rédaction ADR & Séquence.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/architecture/architecture-sprint1.md`
- **Objectif Opérationnel :** Rédiger l'ADR-01 contractualisant l'architecture 2 couches avec persistance CSV et modéliser le flux HTTP sous Mermaid.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Rédiger l'ADR-01 justifiant le choix de l'architecture 2 couches avec lecture tabulaire CSV (`database/data/articles.csv`) pour amorcer le Sprint 1 sans dépendance SGBD.
  2. *Étape 2 :* Lister les conséquences techniques (agilité, simplicité d'amorçage vs absence d'indexation relationnelle).
  3. *Étape 3 :* Modéliser en Mermaid `sequenceDiagram` le parcours de la requête HTTP : Client $\to$ `routes/web.php` $\to$ `ArticleController` $\to$ `ArticleService` $\to$ Vue Blade (cas nominal 200 et cas d'erreur 404).
- **Critère de Réussite :** Le fichier `livrables/architecture/architecture-sprint1.md` contient l'ADR-01 complet et le diagramme de séquence Mermaid valide sur la branche `sprint1`.