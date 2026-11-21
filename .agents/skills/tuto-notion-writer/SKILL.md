---
name: tuto-notion-writer
description: Conçoit et rédige les fiches de tutoriels théoriques et syntaxiques isolées hors imitation pour l'EFP (type: tuto-notion).
version: 1.0.0
---

# 1. Mission
Ce skill est le **rédacteur technique spécialisé dans les tutoriels de notions théoriques, syntaxiques et conceptuelles** (**`type: "tuto-notion"`**) pour l'EFP. Il rédige les tutoriels de notions isolées ainsi que les fiches techniques de restitution de référence produites sous `ua-lab/` pour [tuto-livrable-atelier-writer](../tuto-livrable-atelier-writer/SKILL.md).

# 2. Déclenchement & Limites
- **Quand l'activer :**
  - Rédaction d'un tutoriel de concept théorique ou syntaxique (`type: "tuto-notion"`).
  - Rédaction des fiches techniques de restitution d'atelier sous `ua-lab/` déléguée par `tuto-livrable-atelier-writer`.
  - Exercices d'application conceptuels isolés.
- **Quand NE PAS l'activer :**
  - Cadrage et énoncés des fiches d'ateliers guidés dans `_tutos/` (utiliser `tuto-atelier-writer`).
  - Tâches opérationnelles de sprint et rituels Scrum (utiliser `tuto-tache-writer`).
  - Progression incrémentale de code sous `src/` (utiliser `tuto-code-writer`).

# 3. Règles Normatives & Niveau de Détail Didactique
- **Niveau de Détail Pédagogique Élevé :** Bannir formellement les listes sèches. Chaque notion essentielle doit être expliquée de façon narrative, progressive et concrète, avec des analogies compréhensibles par un débutant.
- **Zéro Mention d'Encadrant ni d'Établissement :** Interdiction stricte de mentionner un encadrant ou un établissement dans les fiches.
- **Structure Canonique Normée :**
  1. `## 1. Contexte & Objectif de l'Atelier`
  2. `## 2. Données de Référence`
  3. `## 3. Notions Essentielles` (développées et expliquées en profondeur)
  4. `## 4. Pratique & Réalisation Guidée` (avec tableau didactique d'action pas-à-pas)
  5. `## 5. Livrables de Référence Produits & Critères`
  6. `## 6. Glossaire Pédagogique`
- **Typologie Frontmatter :** `type: "tuto-notion"`, `layout: default`.
- **Référence Gouvernante :** [`.agents/references/maturation-et-typologie-ua-tuto.md`](file:///d:/solicode-web-mobile/autoformations-professionaliser/.agents/references/maturation-et-typologie-ua-tuto.md).

# 4. Procédure Pas-à-Pas
1. **Étape 1 :** Définir le contexte et l'objectif opérationnel.
2. **Étape 2 :** Développer les notions essentielles avec des explications narratives riches (proscrire les puces isolées).
3. **Étape 3 :** Construire le tableau d'ingénierie et d'actions pas-à-pas.
4. **Étape 4 :** Définir les critères de validation et le glossaire pédagogique.
