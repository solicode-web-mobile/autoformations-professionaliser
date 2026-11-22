---
name: plan-et-fixe-skills
description: Propose un artéfact de planification d'implémentation (/plan) pour les modifications à apporter sur le projet et formalise l'adaptation conjointe des skills locaux (.agents/skills/) et des règles (.agents/rules/) selon les remarques du concepteur.
version: 1.0.0
---

# Skill : plan-et-fixe-skills

## 1. Mission
Orchestrateur unifié de planification et de maintenance des compétences de l'agent :
1. **Analyse des Remarques :** Examiner les retours critiques, ajustements de stack ou consignes méthodologiques du concepteur.
2. **Production de l'Artéfact de Plan (/plan) :** Générer un artéfact interactif (`plan-*.md` avec `RequestFeedback: true`) cartographiant les modifications de projet (sessions, documents, code) ET l'adaptation des skills/règles.
3. **Exécution & Fixe des Skills :** Après validation explicite (bouton *Proceed*), appliquer les modifications projet et synchroniser les compétences locales sous `.agents/skills/` et règles sous `.agents/rules/`.

## 2. Déclenchement & Limites
- **Activer :**
  - Remarques ou demandes du concepteur impliquant à la fois des changements sur le projet et une évolution des règles ou des skills.
  - Commande `/plan` combinée à un ajustement de comportement agent ou refactorisation de skills.
  - Demandes de type « planifie les modifications et adapte les skills ».
- **Ne PAS activer :**
  - Création/audit isolé d'un skill sans plan de projet global ➔ `skills-dev`.
  - Rédaction directe de tutoriels sans modification de cadrage ➔ `tuto-writer`.
  - Conception initiale de session pure ➔ `didactique-session-planner`.

## 3. Structure Canonique de l'Artéfact de Planification
L'artéfact interactif généré (`<Artifact Directory>/plan-[sujet].md`) doit comporter :
- `User Review Required` : Décisions de conception et choix d'architecture.
- `Open Questions` : Points à clarifier avant exécution.
- `Proposed Changes` : Fichiers cibles groupés par composant avec diffs/snippets (`[NEW]`, `[MODIFY]`, `[DELETE]`).
- `Adaptation des Skills & Règles` : Matrice détaillée des compétences (`.agents/skills/`) et règles (`.agents/rules/`) à ajuster.
- `Skills Mobilisés` : Mention obligatoire des skills locaux mobilisés pour chaque étape.
- `Verification Plan` : Tests automatisés et contrôle manuel.

## 4. Règles Inviolables
1. **Validation Avant Modification :** Aucune modification de code ou de skill n'est appliquée avant l'approbation explicite de l'artéfact.
2. **Conformité Skills :** Tout `SKILL.md` modifié ou créé doit respecter $\le 80$ lignes, frontmatter YAML complet et encodage UTF-8 sans BOM.
3. **Contrôle Qualité :** Exécution systématique de `node .agents/skills/skills-dev/scripts/validate-skills.cjs`.
4. **Walkthrough de Clôture :** Rédaction de `walkthrough.md` après achèvement des travaux.
