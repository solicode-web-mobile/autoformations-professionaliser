---
name: tuto-notion-writer
description: Conçoit et rédige les fiches de tutoriels théoriques et syntaxiques isolées hors imitation pour l'EFP (type: tuto-notion).
version: 1.0.0
---

# 1. Mission
Ce skill est spécialisé dans la conception et la rédaction des tutoriels de notions théoriques, syntaxiques ou conceptuelles isolées (**`type: "tuto-notion"`**) pour l'EFP. Il enseigne un concept ciblé (syntaxe de framework, kata, structure de données) en bac à sable sans modification directe du code du projet d'imitation.

# 2. Déclenchement & Limites
- **Quand l'activer :**
  - Rédaction d'un tutoriel de concept théorique ou d'apprentissage syntaxique (`type: "tuto-notion"`).
  - Exercices d'application isolés hors `src/`.
- **Quand NE PAS l'activer :**
  - Ateliers pratiques guidés (utiliser `tuto-atelier-writer`).
  - Tâches de projet opérationnelles et rituels Scrum (utiliser `tuto-tache-writer`).
  - Progression incrémentale de code sous `src/` (utiliser `tuto-code-writer`).

# 3. Règles Normatives du Format `tuto-notion`
- **Typologie & Rattachement :**
  - `type: "tuto-notion"`.
  - Appartient à une UA d'apprentissage théorique/syntaxique.
- **Règles d'Exigence :**
  - **Zéro Diaporama Marp :** `presentation-[slug].md` est formellement proscrit (réservé aux ateliers).
  - **Journal des commandes CLI :** Requis uniquement si le tutoriel implique des manipulations terminal (`[slug].command.md`).
  - **Livrables :** Logés dans `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/`.
- **Référence Gouvernante :** [`.agents/references/maturation-et-typologie-ua-tuto.md`](file:///d:/solicode-web-mobile/autoformations-professionaliser/.agents/references/maturation-et-typologie-ua-tuto.md).

# 4. Procédure Pas-à-Pas
1. **Étape 1 :** Définir le concept clé à isoler et l'objectif pédagogique (*Ce que vous devez apprendre*).
2. **Étape 2 :** Présenter les 20% de notions fondamentales débloquant la compréhension.
3. **Étape 3 :** Fournir l'exercice d'application ou de manipulation.
4. **Étape 4 :** Documenter les commandes CLI associées dans `[slug].command.md` si exécutées.
