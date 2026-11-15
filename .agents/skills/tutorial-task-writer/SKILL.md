---
name: tutorial-task-writer
description: Conçoit, structure et rédige les fiches de tutoriels opérationnels de projet et cérémonies de sprint pour les Unités d'Apprentissage à maturité UA-Tâche (Cadrage initial, validation environnement, pitch, Sprint Planning, Sprint Review, Rétrospective réflexive, Backlog Refinement, Débriefing).
version: 1.0.0
inspiration:
  source: "solicode-pedagogy"
  plugin: "pedagogy-referential"
  pattern: "ua-task-operational, sprint-ceremony & agile-governance"
---

# 1. Mission
Ce skill est l'**artisan opérationnel et méthodologique** chargé de concevoir et rédiger les fiches de tutoriels associées aux Unités d'Apprentissage de maturité **`UA-Tâche`**.

### Distinction Clé : `UA-Tâche` vs `UA-Lab` vs `UA-Tuto`
- **`UA-Tuto` (Apprentissage didactique) :** Progression pas-à-pas de code pur ($E_{n-1} \to E_n$), pilotée par `tutorial-writer`.
- **`UA-Lab` (Atelier pratique guidé) :** Assimilation conceptuelle et pratique selon la triade Théorie / Pratique imitation / Prompts RIO fil rouge, pilotée par `tutorial-lab-writer`.
- **`UA-Tâche` (Tâche de réalisation de projet) :** Une `UA-Tâche` n'a **pas** pour finalité d'enseigner une notion théorique ou une syntaxe de code. Elle formalise et guide l'exécution d'une **tâche de projet ou d'un rituel agile du sprint** (ex: cadrage, checklist outillage, pitch, Sprint Planning, Sprint Review, Rétrospective, Débriefing).

---

# 2. Déclenchement & Limites

- **Quand l'activer :**
  - Rédaction et maintenance des fiches de tutoriels associées à une Unité d'Apprentissage de maturité **`UA-Tâche`**.
  - Formalisation des guides opérationnels de cérémonies agiles Scrum (Sprint Planning, Sprint Review, Sprint Retrospective, Daily).
  - Élaboration de protocoles de lancement de projet, checklists de validation d'environnement et supports de pitch.
  - Structuration des bilans d'acquisition de compétences et journaux de progression.
- **Quand NE PAS l'activer :**
  - Rédaction de tutoriels pas-à-pas de code incrémental (`UA-Tuto`) ➔ Utiliser [tutorial-writer](../tutorial-writer/SKILL.md).
  - Rédaction d'ateliers pratiques guidés avec triade RIO (`UA-Lab`) ➔ Utiliser [tutorial-lab-writer](../tutorial-lab-writer/SKILL.md).
  - Cadrage macro et ordonnancement de session ➔ Utiliser [tutorial-planer](../tutorial-planer/SKILL.md).

---

# 3. Structure Normée d'une Fiche `UA-Tâche`

Chaque tutoriel d'une `UA-Tâche` respecte scrupuleusement la structure canonique suivante :

```markdown
---
layout: tuto
title: "[Titre Opérationnel de la Tâche]"
sous_titre: "[Sous-titre explicite décrivant l'action concrète dans le sprint]"
slug: "[slug-kebab-case]"
permalink: /tutos/[slug-kebab-case]/
tuto_id: "T.XXX.YYY"
version: "normal"
ua: "UA.XXX.YY"
maturite: "UA-Tâche"
nav_order: [numéro d'ordre : 1, 2, 3...]
simplified: true
en_construction: true
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Objectif Opérationnel & Prérequis
- **Objectif :** [Action concrète à réaliser dans le sprint et résultat attendu]
- **Durée estimée :** [Durée en heures]
- **Prérequis :** [Artefacts ou validations préalables requises]

## 2. Déroulement Pas-à-Pas de la Tâche
Exécuter la tâche en respectant ces étapes chronologiques :
1. **Étape 1 — [Nom étape 1] :** [Description directe et directive à l'impératif]
2. **Étape 2 — [Nom étape 2] :** [Description directe et directive à l'impératif]
3. **Étape 3 — [Nom étape 3] :** [Description directe et directive à l'impératif]

## 3. Livrables & Critères de Réussite
- **Livrables attendus :**
  - `[chemin/du/livrable.md]` : [Description du fichier produit]
- **Critères de validation :**
  - [ ] [Critère vérifiable et opposable 1]
  - [ ] [Critère vérifiable et opposable 2]
```

---

# 4. Règles Inviolables
1. **Action Opérationnelle Pure :** Bannir les longs développements théoriques ou académiques. La fiche donne des consignes d'action claires (*« Exécutez »*, *« Rédigez »*, *« Validez »*).
2. **Livrables Concrets et Traçables :** Chaque tâche débouche obligatoirement sur un artefact versionné sous Git (`.md`, dépôt initialisé, checklist émargée). Zéro validation verbale sans trace écrite.
3. **Maturité Explicite :** La mention `maturite: "UA-Tâche"` figure obligatoirement dans le frontmatter YAML. Le terme « type » est banni.
4. **Encodage Strict UTF-8 sans BOM :** Tous les fichiers générés respectent la règle 1 de `standards-techniques.md`.
