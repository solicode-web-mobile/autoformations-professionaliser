---
name: tutorial-lab-writer
description: Conçoit, structure et rédige les tutoriels d'ateliers pratiques guidés pour les Unités d'Apprentissage à maturité UA-Lab (Notions fondamentales, Recherche active, Pratique guidée sur projet cible, Prompts et Skills RIO ciblés).
version: 2.1.0
---

# 1. Mission & Structure Flexible
Rédacteur technique et pédagogique de l'écosystème `tutorial-*-writer`, dédié aux **`UA-Lab`** (assimilation conceptuelle, modélisation UML/schémas, architecture, frameworks, outillage IA).
Applique le socle transversal et la synchronisation gouvernés par [tutorial-writer](../tutorial-writer/SKILL.md).

Une `UA-Lab` comporte **entre 2 et 4 tâches modulaires** selon les acquis :
$$\text{[Théorie essentielle (Optionnelle)]} \longrightarrow \text{Pratique Cible (Obligatoire)} \longrightarrow \text{[Création de Prompt(s) (Si flux récurrent)]}$$
- **Omission Théorie :** Omettre si les notions sont déjà acquises aux étapes/niveaux antérieurs.
- **Omission Prompt :** Réserver les prompts aux étapes récurrentes produisant un livrable reproductible (banni pour découverte conceptuelle pure, ADR unique ou Hello World initial).
- **Tranches Framework Complètes :** Scinder l'outillage IA en `prompt-back-end` et `prompt-front-end` (avec entraînement au Live Coding).

---

# 2. Déclenchement & Limites
- **Activer :** Ateliers `UA-Lab` ; modélisation UML (Mermaid) ; ateliers agiles Scrum (User Stories INVEST, Product Backlog) ; dossiers d'architecture (ADR) ; prompts directifs RIO.
- **Ne PAS activer :** Code incrémental pas-à-pas ➔ `tutorial-code-writer` | Tâches de projet / cérémonies sans théorie ➔ `tutorial-task-writer` | Planification globale ➔ `tutorial-planer` | Gouvernance & synchronisation ➔ `tutorial-writer`.

---

# 3. Structures Normées des Fiches `UA-Lab`

Frontmatter commun : `layout: tuto`, `title:`, `sous_titre:`, `slug:`, `permalink:`, `tuto_id:`, `ua:`, `maturite: "UA-Lab"`, `nav_order:`, `simplified: true`, `en_construction: false`, `branche: "sprintX"`.

### A. Fiche Théorie & Assimilation
```markdown
## 1. Travail à faire
- [Consignes claires d'assimilation et d'investigation]
## 2. Notions fondamentales
- **[Concept 1] :** [Définition discriminante et exemples essentiels]
## 3. Recherches à effectuer
- [Points d'approfondissement et questions d'investigation active de l'apprenant]
## 4. Livrable attendu
- Emplacement : `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].md` sur la branche active.
```

### B. Fiche Pratique sur Projet Cible (Zéro Solution Clé en Main)
```markdown
## 1. Positionnement dans le Flux & la Stack
- **Contexte :** [Étape du flux de travail et composants impactés]
## 2. Travail à Faire (Projet Cible)
1. **Étape 1 — [Nom] :** [Cahier des charges technique et étapes directives sans solution copier-coller]
2. **Étape 2 — [Nom] :** [Cahier des charges technique et étapes directives]
## 3. Critères de Validation
- [ ] [Critère vérifiable opposable 1] | [ ] [Critère vérifiable opposable 2]
```

### C. Fiche Création de Prompt IA (Méthode RIO)
```markdown
## 1. Positionnement dans le Flux & la Stack
## 2. Travail à Faire
## 3. Missions Concrètes Réalisées par le Prompt
1. [Mission 1] | 2. [Mission 2]
## 4. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** [Persona d'expert] | **Instruction :** [Consigne sans ambiguïté]
- **Output :** [Format strict de sortie] | **Contraintes Négatives :** [Interdictions formelles]
## 5. Critères de Validation
- [ ] Prompt consigné dans `livrables/ia/prompts/prompt-[nom].prompt.md` sur la branche active.
```

---

# 4. Règles Inviolables
1. **Ciblage du Projet Cible :** Pratique exécutée sur le projet cible et la branche (`sprintX`) définis dans `.agents/rules/`.
2. **Autonomie de la Pratique (Zéro Solution Clé en Main) :** Fournir spécifications rigoureuses, cahier des charges RIO et étapes directives, mais **interdiction formelle de fournir la solution rédigée complète prête à copier-coller** (réservée à `UA-Tuto` et `UA-Tâche`).
3. **Zéro Fuite Didactique :** Interdiction des termes « 20/80 », « Règle des 20/80 » ou « Ce que l'apprenant doit produire ». Utiliser « Notions fondamentales » et « Recherches à effectuer ».
4. **Zéro Durée Affichée & Zéro Jalon :** Aucune mention de temps (`(2h)`) aux apprenants. Terme direct « Étape » obligatoire (« Jalon » proscrit).
5. **Formatage Colonne 0 & UTF-8 :** Tout bloc de code débute strictement colonne 0 (zéro indentation), précédé et suivi d'une ligne vide. UTF-8 sans BOM.
6. **Chemins Canoniques :** `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/`. Proscrire les dossiers orphelins (`labs/`), les `README.md` unitaires et les captures d'écran.
7. **Versionnement Git :** Respecter l'autonomie Git du niveau actif (aucun `commit`/`push` imposé aux apprenants si autonomie prescrite).
8. **Gouvernance :** Réfère au Master Skill [tutorial-writer](../tutorial-writer/SKILL.md) pour les règles partagées et la synchronisation avec le projet cible via `.sync/rules.md`.
