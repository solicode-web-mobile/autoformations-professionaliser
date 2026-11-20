---
name: tutorial-architecture-writer
description: Règles de rédaction didactiques et techniques spécifiques au domaine Architecture logicielle (D.312.1, Compétence C.312). Membre de l'écosystème tutorial-*-writer sous la gouvernance de tutorial-writer.
version: 1.0.0
inspiration:
  source: "solicode-pedagogy"
  plugin: "pedagogy-referential"
  pattern: "domain-specific-tutorial-writer"
---

# 1. Mission & Périmètre
Expert de domaine au sein de l'écosystème `tutorial-*-writer`, chargé de prescrire les standards techniques, syntaxes, outils et critères de validation propres au domaine **Architecture logicielle** (D.312.1, Compétence C.312).
Applique le socle transversal et la synchronisation gouvernés par [tutorial-writer](../tutorial-writer/SKILL.md).

# 2. Déclenchement & Limites
- **Activer :** Rédaction, audit ou adaptation de tutoriels du domaine Architecture (découpage en couches, ADR, principes SOLID, flux de données).
- **Ne PAS activer :** Modélisation purement UML ➔ `tutorial-uml-writer` | Implémentation de code d'application ➔ `tutorial-laravel-writer` | Gouvernance transversale ➔ `tutorial-writer`.

# 3. Stack Technique & Outils du Domaine
- **Modèles architecturaux :** Architecture en couches (2 couches en initiation, 3 couches en approfondissement), modèle MVC.
- **Documentation de décision :** ADR (Architecture Decision Records) au format Markdown standardisé.
- **Modélisation de flux :** Diagrammes de séquences Mermaid (`sequenceDiagram`).
- **Principes cardinaux :** Principes SOLID, séparation des responsabilités, contrôleurs minces, injection de dépendances.

# 4. Règles Spécifiques de Rédaction Architecture
1. **Formalisation Systématique des ADR :** Toute décision d'architecture majeure (choix de stack, découpage en couches, pattern de persistance) doit faire l'objet d'une fiche ADR structurée : Contexte, Décision, Conséquences.
2. **Modélisation Déclarative des Flux :** Tout flux architectural transverse (ex: requête HTTP -> contrôleur -> service -> repository) doit être illustré par un `sequenceDiagram` Mermaid calé colonne 0.
3. **Contrôleurs Minces :** Les tutoriels doivent proscrire la logique métier dans les contrôleurs et orienter vers les services ou actions dédiées.
4. **Zéro Dépendance Circulaire :** Interdire explicitement tout couplage bidirectionnel entre couches.

# 5. Formats de Livrables & Validation
- **Fiches didactiques :** `tutoriels/architecture/[slug-ua]/[slug-tuto]/[slug-tuto].md`
- **Fiches ADR :** `tutoriels/architecture/[slug-ua]/[slug-tuto]/adr-[sujet].md`
- **Critères de validation :**
  - Respect du gabarit ADR tripartite (Contexte, Décision, Conséquences).
  - Diagrammes Mermaid de séquence valides.
  - Conformité stricte aux principes SOLID prescrits.
