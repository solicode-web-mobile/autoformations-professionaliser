---
title: "Architecture logicielle en deux couches"
layout: ua
code: "UA.312.11"
ordre: 10
competence: "C.312"
domaine: "D.312.1"
duree: 10
objectif: >
  Concevoir l'architecture logicielle initiale séparant strictement l'orchestration HTTP de la logique de données sans base de données relationnelle.
description: >
  Concevoir l'architecture logicielle initiale séparant strictement l'orchestration HTTP (contrôleur mince) de la logique de données (classe Service) sans base de données relationnelle, formaliser une décision d'architecture (ADR-01) et schématiser la trajectoire cible globale du produit.
notions:
  - "Limites du Pattern MVC Naïf : Écueil des Fat Controllers, couplage fort et difficulté des tests unitaires"
  - "Principe de Responsabilité Unique (SRP) : Séparation étanche de la couche Présentation (ArticleController) et de la couche Métier/Données (ArticleService)"
  - "Isolation de la Persistance Tabulaire : Encapsulation de la lecture CSV dans la classe Service sans dépendance physique SQL"
  - "Formalisation des Choix Techniques par les ADR : Structure d'une fiche ADR (Titre, Statut, Contexte, Décision, Justification, Conséquences)"
  - "Vision Cible Macroscopique : Anticipation de la trajectoire d'évolution vers l'ORM Eloquent"
livrable: >
  Description détaillée de l'architecture 2 couches minimale du Sprint 1 (conception-technique/architecture-sprint1.md), fiche de décision technique ADR-01 (conception-technique/decision-technique-bdd-csv.md) et schéma directeur cible (conception-technique/architecture-cible-macro.md).
travail_a_faire: >
  Concevoir le schéma d'architecture 2 couches et rédiger la décision technique ADR-01 justifiant l'utilisation d'une source CSV in-memory.
---
