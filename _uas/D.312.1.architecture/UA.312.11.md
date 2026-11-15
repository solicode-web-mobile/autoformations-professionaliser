---
title: "Architecture logicielle 2 couches"
layout: ua
code: "UA.312.11"
maturite: "UA-Lab"
ordre: 10
competence: "C.312"
domaine: "D.312.1"
duree: 8
objectif: >
  Concevoir une architecture logicielle découplée en deux couches (Contrôleur mince IoC / Classe Service) et documenter la décision dans un ADR formel.
description: >
  Isoler la logique de présentation de la logique métier et d'accès aux données. L'apprenant conçoit l'architecture en deux couches, rédige l'ADR-01 justifiant le choix sans base de données relationnelle initiale et modélise la séquence HTTP.
notions:
  - "Principe de séparation des responsabilités (SoC) : découplage strict entre couche de présentation HTTP et logique métier/données"
  - "Patron architectural en 2 couches : Contrôleur mince (orchestration HTTP) -> Classe Service (métier et abstraction des données)"
  - "Décision technique de persistance transitoire : choix délibéré d'une source tabulaire CSV en mémoire (articles.csv), zéro SGBD relationnel en amorçage S1"
  - "Architecture Decision Record (ADR) : formalisation standardisée de l'ADR-01 (Titre, Statut, Contexte, Décision, Alternatives écartées, Conséquences)"
  - "Modélisation de flux HTTP en séquence : diagramme Mermaid sequenceDiagram illustrant le parcours complet de la requête (cas nominal et cas d'erreur 404)"
livrable: >
  Dossier d'architecture S1 et ADR-01 (livrables/architecture/architecture-sprint1.md) et prompt réutilisable (livrables/ia/prompts/prompt-architecture.prompt.md).
travail_a_faire: >
  Rédiger l'ADR-01, modéliser le diagramme de séquence en Mermaid.js et concevoir le prompt d'ingénierie d'architecture.
---
