---
name: tutorial-uml-writer
description: Règles de rédaction didactiques et techniques spécifiques au domaine UML (D.311.2, Compétence C.311). Membre de l'écosystème tutorial-*-writer sous la gouvernance de tutorial-writer.
version: 1.0.0
inspiration:
  source: "solicode-pedagogy"
  plugin: "pedagogy-referential"
  pattern: "domain-specific-tutorial-writer"
---

# 1. Mission & Périmètre
Expert de domaine au sein de l'écosystème `tutorial-*-writer`, chargé de prescrire les standards techniques, syntaxes, outils et critères de validation propres au domaine **UML** (D.311.2, Compétence C.311).
Applique le socle transversal et la synchronisation gouvernés par [tutorial-writer](../tutorial-writer/SKILL.md).

# 2. Déclenchement & Limites
- **Activer :** Rédaction, audit ou adaptation de tutoriels du domaine UML (diagrammes de contexte, cas d'utilisation, classes, séquences).
- **Ne PAS activer :** Autres domaines ➔ Skill correspondant | Architecture globale/ADR ➔ `tutorial-architecture-writer` | Gouvernance transversale ➔ `tutorial-writer`.

# 3. Stack Technique & Outils du Domaine
- **Moteur de rendu :** Mermaid.js natif dans Markdown (`mermaid`).
- **Diagrammes types :** `graph TD` (contexte/flux), `sequenceDiagram` (interactions), `classDiagram` (classes/entités).
- **Fichiers sources :** Fichiers `.mmd` ou blocs Mermaid encapsulés dans les fiches `.md`.
- **Zéro capture d'écran :** Tout schéma est impérativement sous format déclaratif textuel éditable.

# 4. Règles Spécifiques de Rédaction UML
1. **Diagramme de Contexte Délimité :** Tout tutoriel de cadrage/modélisation doit débuter par un diagramme de contexte délimitant les acteurs externes et les frontières du système cible.
2. **Traçabilité avec le Product Backlog :** Tout cas d'utilisation modélisé doit être explicitement relié à une User Story issue du Product Backlog du sprint.
3. **Syntaxe Déclarative Standardisée :** Noms des participants explicites, messages orientés action, messages de retour en pointillés (`-->>`).
4. **Omission des Notions Déjà Acquises :** Aucune réintroduction théorique des bases UML validées en N1/N2 (définitions d'acteurs, flèches basiques). Aller droit à la modélisation métier.

# 5. Formats de Livrables & Validation
- **Fiches didactiques :** `tutoriels/uml/[slug-ua]/[slug-tuto]/[slug-tuto].md`
- **Schémas sources :** `tutoriels/uml/[slug-ua]/[slug-tuto]/[slug-tuto].mmd` (ou intégrés dans le `.md`)
- **Critères de validation :**
  - Rendu Mermaid valide sans erreur de parsing.
  - Correspondance stricte 1:1 entre acteurs du diagramme et rôles de la session.
  - Respect de l'isolation colonne 0 pour les blocs de code.
