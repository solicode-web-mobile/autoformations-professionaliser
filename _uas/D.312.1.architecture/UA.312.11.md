---
title: "Architecture logicielle en deux couches"
layout: ua
code: "UA.312.11"
maturite: "UA-Lab"
ordre: 8
competence: "C.312"
domaine: "D.312.1"
duree: 4
objectif: >
  Concevoir une architecture logicielle découplée isolant le contrôleur mince de la persistance tabulaire via une classe Service dédiée et formaliser ce choix technique stratégique dans un ADR opposable avec diagramme de séquence HTTP.
description: >
  Isoler la logique de présentation de la logique métier et d'accès aux données sur le Projet d'imitation. L'apprenant conçoit l'architecture en deux couches, rédige l'ADR-01 justifiant le stockage CSV en amorçage sans base de données relationnelle et modélise la séquence HTTP en Mermaid.
notions:
  - "Principe de séparation des responsabilités (SoC) : découplage strict entre couche de présentation HTTP et logique métier/données"
  - "Patron architectural en 2 couches : Contrôleur mince (orchestration HTTP) -> Classe Service (métier et abstraction des données)"
  - "Décision technique de persistance transitoire : choix délibéré d'une source tabulaire CSV en mémoire (articles.csv), zéro SGBD relationnel en amorçage S1"
  - "Architecture Decision Record (ADR) : formalisation standardisée de l'ADR-01 (Titre, Statut, Contexte, Décision, Alternatives écartées, Conséquences)"
  - "Modélisation de flux HTTP en séquence : diagramme Mermaid sequenceDiagram illustrant le parcours complet de la requête (cas nominal et cas d'erreur 404)"
livrable: >
  Dossier d'architecture S1 et ADR-01 (livrables/architecture/architecture-sprint1.md) sur la branche sprint1.
travail_a_faire: >
  Rédiger l'ADR-01 et modéliser le diagramme de séquence en Mermaid.js pour le Blog des Lauréats.
---
