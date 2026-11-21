---
name: tuto-writer-scrum
description: Règles de rédaction didactiques et méthodologiques spécifiques au domaine Scrum (D.351.1, Compétence C.351). Membre de l'écosystème tuto-writer sous la gouvernance de tuto-writer.
version: 1.0.0
---

# 1. Mission & Périmètre
Expert de domaine au sein de l'écosystème `tuto-writer`, chargé de prescrire les standards didactiques et exigences méthodologiques propres au domaine **Scrum** (D.351.1, Compétence C.351).
Applique le socle transversal et la synchronisation gouvernés par [tuto-writer](../tuto-writer/SKILL.md).

# 2. Déclenchement & Limites
- **Activer :** Rédaction, audit ou adaptation de tutoriels du domaine Scrum (piliers, rôles, artefacts, DoD, User Stories, rituels théoriques).
- **Ne PAS activer :** Conduite opérationnelle des cérémonies de sprint ➔ `tuto-writer-realisation-projet` | Modélisation UML ➔ `tuto-writer-uml` | Gouvernance transversale ➔ `tuto-writer`.

# 3. Référentiel Méthodologique & Outils
- **Fondations Scrum :** 3 piliers (Transparence, Inspection, Adaptation), 3 rôles (PO, Scrum Master, Développeurs), 5 événements.
- **Standards de backlog :** User Stories selon le critère INVEST, priorisation MoSCoW.
- **Engagements de qualité :** Definition of Done (DoD) opposable, Definition of Ready (DoR).
- **Didactique 20/80 :** Notions fondamentales fournies (20%) + Recherches actives ciblées (80%).

# 4. Règles Spécifiques de Rédaction Scrum
1. **Équilibre Notions Fondamentales / Recherche Active :** Fournir directement les concepts discriminants dans « Notions fondamentales » et guider l'apprenant dans « Recherches à effectuer ». Bannir toute mention interne des « 20/80 ».
2. **Critère INVEST & Priorisation MoSCoW :** Tout tutoriel portant sur le Product Backlog doit imposer la rédaction de User Stories au standard INVEST et la catégorisation MoSCoW (Must, Should, Could, Won't).
3. **Definition of Done (DoD) Explicite :** Exiger des critères vérifiables et mesurables (tests passants, conformité de style, revue de code, branche active).
4. **Zéro Prompt pour l'Assimilation Conceptuelle :** Interdiction d'outiller par un prompt IA l'apprentissage de notions théoriques Scrum pures.

# 5. Formats de Livrables & Validation
- **Fiches didactiques :** `tutoriels/scrum/[slug-ua]/[slug-tuto]/[slug-tuto].md`
- **Critères de validation :**
  - Section « Notions fondamentales » concise et percutante.
  - Section « Recherches à effectuer » orientée action avec questions précises.
  - Respect scrupuleux de l'interdiction de divulguer la cuisine interne (« 20/80 »).
