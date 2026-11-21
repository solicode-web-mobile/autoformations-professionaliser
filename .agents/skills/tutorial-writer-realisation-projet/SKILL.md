---
name: tutorial-writer-realisation-projet
description: Règles de rédaction spécifiques au domaine Réalisation de Projet (D.351.2, Compétence C.351). Membre de l'écosystème tutorial-writer sous la gouvernance de tutorial-writer.
version: 1.1.0
---

# 1. Mission & Périmètre
Expert de domaine au sein de l'écosystème `tutorial-writer`, chargé de prescrire les standards d'action, d'organisation de dépôt et de rituels opérationnels propres au domaine **Réalisation de Projet** (D.351.2, Compétence C.351).
Applique le socle transversal, l'organisation des livrables et la synchronisation gouvernés par [tutorial-writer](../tutorial-writer/SKILL.md), [.agents/references/organisation-livrables.md](../../references/organisation-livrables.md) et [.agents/references/typologie-uas-tutoriels.md](../../references/typologie-uas-tutoriels.md).

# 2. Déclenchement & Limites
- **Activer :** Rédaction, audit ou adaptation de tutoriels opérationnels de projet (cadrage, Sprint Planning, Review, Rétrospective, Refinement, gestion de dépôt).
- **Ne PAS activer :** Apports méthodologiques Scrum théoriques ➔ `tutorial-writer-scrum` | Rédaction de code applicatif ➔ `tutorial-writer-laravel` | Gouvernance transversale ➔ `tutorial-writer`.

# 3. Environnement & Organisation du Projet
- **Maturité canonique :** `maturite: "UA-Tâche"` (`tuto-tache`, 100% orienté action opérationnelle, 0% théorie).
- **Organisation standard d'un dépôt :** `README.md`, `missions/`, `sprints/`, `src/`, `docs/`, `.agents/` selon [.agents/references/organisation-livrables.md](../../references/organisation-livrables.md).
- **Gestion de version & CLI :** GitHub CLI (`gh repo create`), branches partagées de sprint (`sprintX`), PowerShell Windows selon [.agents/references/gitflow.md](../../references/gitflow.md).
- **Rituels de sprint :** Cadrage initial, Sprint Planning, Débriefing, Backlog Refinement, Sprint Review, Sprint Retrospective.

# 4. Règles Spécifiques de Rédaction Réalisation de Projet
1. **Zéro Théorie :** Toute fiche de ce domaine va directement à l'action concrète avec étapes directives numérotées (« Étape X — ... »). Proscrire tout exposé théorique.
2. **Livrables de Tâche de Projet & Rapport CLI :** Pour les fiches de ce domaine relevant de `UA-Tâche` (`tuto-tache`), les livrables sont positionnés aux emplacements racine du projet (`docs/cadrage/`, `docs/conception/`, `sprints/`, `src/`) selon [.agents/references/organisation-livrables.md](../../references/organisation-livrables.md). Le journal CLI (`[slug-tuto].command.md`) est **strictement non requis et non autorisé** (la tâche opère directement sur les fichiers du projet). Si la fiche relève exceptionnellement d'un `tuto-lab`, se conformer à [.agents/references/typologie-uas-tutoriels.md](../../references/typologie-uas-tutoriels.md).
3. **Commandes PowerShell Compatibles :** Création de dossiers par `mkdir` et fichiers par `echo "" > <fichier>`. Proscrire `touch` et `New-Item`.
4. **Exclusion des Outils Formateur :** Le dossier `flux-travail/` ne doit jamais figurer dans les étapes de création de structure du projet pour les apprenants.

# 5. Formats de Livrables & Validation
- **Fiches didactiques :** `tutoriels/realisation-projet/[slug-ua]/[slug-tuto]/[slug-tuto].md`
- **Livrables opérationnels :** Positionnés aux emplacements racine du projet (`docs/cadrage/`, `docs/conception/`, `sprints/`, `src/`, etc.) conformément à [.agents/references/organisation-livrables.md](../../references/organisation-livrables.md). Zéro journal CLI pour `tuto-tache`.
- **Critères de validation :**
  - Respect de la maturité `UA-Tâche` (zéro théorie, 100% action).
  - Emplacements de livrables opérationnels conformes à l'arborescence standard (`organisation-livrables.md`).
  - Aucun fichier `[slug-tuto].command.md` ni diaporama Marp pour `tuto-tache`.
