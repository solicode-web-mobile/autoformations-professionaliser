---
title: "Architecture logicielle en couches & classe service"
layout: ua
code: "UA.312.11"
ordre: 6
competence: "C.312"
domaine: "D.312.1"
duree: 10
objectif: >
  Concevoir l'architecture logicielle initiale séparant strictement l'orchestration HTTP de la logique de données sans base relationnelle.
description: >
  Concevoir l'architecture logicielle initiale séparant strictement l'orchestration HTTP (contrôleur mince) de la logique de données (classe Service) sans base de données relationnelle, formaliser une décision d'architecture (ADR-01) et schématiser la trajectoire cible globale du produit.
notions:
  - "Limites du pattern MVC naïf (écueil des Fat Controllers, couplage fort)"
  - "Principe de Responsabilité Unique (SRP) appliqué aux contrôleurs minces et classes Services"
  - "Isolation de la persistance tabulaire (encapsulation de la lecture CSV dans un Service)"
  - "Formalisation des choix techniques par les fiches ADR (Architecture Decision Records)"
  - "Vision cible macroscopique et anticipation vers l'ORM Eloquent"
livrable: >
  Schéma d'architecture 2 couches minimale (conception-technique/architecture-sprint1.md), fiche de décision technique ADR-01 (conception-technique/decision-technique-bdd-csv.md) et schéma directeur cible (conception-technique/architecture-cible-macro.md).
travail_a_faire: >
  Concevoir le schéma d'architecture 2 couches de l'application et rédiger la fiche de décision d'architecture ADR-01 pour la persistance CSV temporaire.
---

