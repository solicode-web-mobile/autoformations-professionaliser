---
name: skills-dev
description: Conçoit, crée, audite et affine les compétences locales (.agents/skills/) et les règles (.agents/rules/) de l'agent dans le projet.
version: 2.0.0
---

# 1. Mission
Gouverneur et architecte technique des compétences de l'agent. Assure la conception, la création, le raffinement et l'audit des **Skills** locaux (`.agents/skills/`) et des **Règles** permanentes (`.agents/rules/`).

# 2. Déclenchement & Limites
- **Activer :** Création d'un nouveau skill, raffinement d'un skill existant, création/mise à jour d'une règle dans `.agents/rules/`, audit de conformité.
- **Ne PAS activer :** Rédaction de tutoriels ➔ `tuto-writer` | Layouts/CSS Jekyll ➔ `dev-jekyll` | Planification ➔ `tutorial-planer`.

# 3. Structure Canonique d'un Skill
Chaque compétence réside sous `.agents/skills/<nom-du-skill>/` et comporte :
1. **`SKILL.md` :** Spécification technique directe ($\le 80$ lignes), frontmatter YAML (`name`, `description`, `version`), mission, règles et formats de livrables.
2. **`README.md` :** Documentation opérationnelle colocalisée unique et suffisante (rôle, déclencheurs, prompts d'activation, déroulement pas-à-pas).
3. **`resources/` (optionnel) :** Gabarits ou ressources exclusives à cette compétence.

# 4. Règles Inviolables de Gouvernance
1. **Zéro Mécanisme Global :** Toutes les compétences sont 100% locales au dépôt. Aucune dépendance à un Hub externe, catalogue distant ou registre `skills.json`.
2. **Documentation Unique :** Le fichier `README.md` colocalisé est l'unique documentation requise. Aucun sous-dossier `doc/` n'est autorisé.
3. **Encodage Strict :** Tout fichier texte créé ou modifié doit impérativement être encodé en UTF-8 sans BOM.
4. **Validation Statique :** Tout skill créé ou modifié est vérifié par `node .agents/skills/skills-dev/scripts/validate-skills.cjs`.

# 5. Procédure Pas-à-Pas
1. **Définition du Besoin :** Identifier le périmètre et attribuer le nom canonique en minuscules (ex: `tuto-writer-[slug]`).
2. **Rédaction `SKILL.md` :** Remplir le frontmatter YAML et formaliser les règles techniques spécifiques en $\le 80$ lignes.
3. **Rédaction `README.md` :** Rédiger la documentation synthétique (prompts types et étapes opérationnelles).
4. **Contrôle Qualité :** Exécuter `node .agents/skills/skills-dev/scripts/validate-skills.cjs` (0 erreur).
