---
name: tutorial-task-writer
description: Conçoit, structure et rédige les fiches de tutoriels opérationnels de projet et cérémonies de sprint pour les Unités d'Apprentissage à maturité UA-Tâche (Cadrage de périmètre, Sprint Planning, Sprint Review, Rétrospective réflexive, Backlog Refinement, Débriefing, Prompts de cérémonies).
version: 2.0.0
inspiration:
  source: "solicode-pedagogy"
  plugin: "pedagogy-referential"
  pattern: "ua-task-operational, sprint-ceremonies, zero-theory & ceremony-prompts"
---

# 1. Mission
Ce skill est l'**artisan opérationnel et méthodologique** chargé de concevoir et rédiger les fiches de tutoriels associées aux Unités d'Apprentissage de maturité **`UA-Tâche`**.

### Distinction Clé : `UA-Tâche` vs `UA-Lab` vs `UA-Tuto`
- **`UA-Tuto` (Apprentissage incrémental) :** Progression pas-à-pas de code pur ($E_{n-1} \to E_n$), pilotée par `tutorial-writer`.
- **`UA-Lab` (Atelier pratique guidé) :** Assimilation conceptuelle et pratique outillée (UML, architecture, frameworks, outillage IA), pilotée par `tutorial-lab-writer`.
- **`UA-Tâche` (Tâche opérationnelle & Cérémonies de projet) :** Une `UA-Tâche` n'a **aucune vocation théorique**. Elle formalise et guide l'exécution d'une **tâche de cadrage ou d'un rituel agile du sprint** (cadrage de périmètre, Sprint Planning, Sprint Review, Rétrospective, Backlog Refinement, Débriefing individuel) ainsi que les prompts réutilisables instrumentant ces cérémonies.

---

# 2. Déclenchement & Limites

- **Quand l'activer :**
  - Rédaction et maintenance des fiches de tutoriels associées à une Unité d'Apprentissage de maturité **`UA-Tâche`**.
  - Formalisation des guides opérationnels de cérémonies agiles Scrum (Sprint Planning, Sprint Review, Sprint Retrospective, Backlog Grooming, Bilan).
  - Élaboration des protocoles de cadrage de périmètre de projet.
  - Conception des prompts d'ingénierie réutilisables dédiés à l'automatisation des cérémonies agiles.
- **Quand NE PAS l'activer :**
  - Rédaction de tutoriels de code incrémental (`UA-Tuto`) ➔ Utiliser [tutorial-writer](../tutorial-writer/SKILL.md).
  - Rédaction d'ateliers pratiques guidés avec théorie ou modélisation (`UA-Lab`) ➔ Utiliser [tutorial-lab-writer](../tutorial-lab-writer/SKILL.md).
  - Planification globale et ordonnancement de sessions ➔ Utiliser [tutorial-planer](../tutorial-planer/SKILL.md).

---

# 3. Structure Normée d'une Fiche `UA-Tâche`

### Format Fiche Opérationnelle de Projet ou Cérémonie Scrum
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
en_construction: false
branche: "sprintX"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Objectif Opérationnel & Prérequis
- **Position dans le flux :** [Phase et étape du sprint]
- **Branche Git :** `sprintX`
- **Fichiers modifiés ou créés :** `[chemin/du/livrable.md]`
- **Objectif :** [Action concrète à réaliser dans le sprint et résultat attendu]
- **Prérequis :** [Artefacts ou validations préalables requises]

## 2. Déroulement Pas-à-Pas de la Tâche
Exécuter la tâche en respectant ces étapes chronologiques :
1. **Étape 1 — [Nom étape 1] :** [Description directe et directive à l'impératif]
2. **Étape 2 — [Nom étape 2] :** [Description directe et directive à l'impératif]
3. **Étape 3 — [Nom étape 3] :** [Description directe et directive à l'impératif]

## 3. Livrables & Critères de Réussite
- **Livrable attendu :** Fichier `[chemin/du/livrable.md]` sur la branche `sprintX`.
- **Critères de validation :**
  - [ ] [Critère vérifiable et opposable 1]
  - [ ] [Critère vérifiable et opposable 2]
```

### Format Fiche Création de Prompts de Cérémonies Scrum
Lorsque la tâche consiste à outiller l'équipe de prompts d'automatisation des rituels agiles (ex : `prompt-sprint-planning`, `prompt-sprint-review`, `prompt-sprint-retrospective`, `prompt-backlog-refinement`, `prompt-bilan-session`) :
```markdown
---
layout: tuto
title: "Création des prompts de clôture de sprint"
sous_titre: "[Sous-titre explicite décrivant l'outillage IA des cérémonies]"
slug: "[slug-kebab-case]"
permalink: /tutos/[slug-kebab-case]/
tuto_id: "T.XXX.YYY"
version: "normal"
ua: "UA.XXX.YY"
maturite: "UA-Tâche"
nav_order: [numéro d'ordre]
simplified: true
en_construction: false
branche: "sprintX"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Objectif Opérationnel & Prérequis
- **Position dans le flux :** [Phase et étape du sprint / Automatisation]
- **Branche Git :** `sprintX`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-[nom].prompt.md`
- **Objectif :** [Automatiser la production des livrables de cérémonie agile]

## 2. Missions Concrètes des Prompts Réalisés
1. **`prompt-[nom-1]` :** [Description de la mission opérationnelle]
2. **`prompt-[nom-2]` :** [Description de la mission opérationnelle]

## 3. Critères de Validation
- [ ] Les fichiers de prompts sont créés dans `livrables/ia/prompts/` et versionnés sur la branche `sprintX`.
- [ ] Chaque prompt adopte la méthode RIO avec contraintes négatives strictes.
```

---

# 4. Règles Inviolables
1. **Règle Absolue « Zéro Théorie » :** Les tutoriels UA-Tâche sont 100% orientés action. Interdiction formelle d'insérer des exposés théoriques ou des synthèses de cours. L'apprenant applique des consignes directes (*« Exécutez »*, *« Découpez »*, *« Validez »*).
2. **Zéro Affichage de Durée aux Apprenants :** Ne jamais insérer de mention de temps unitaire (`(2h)`, `(4h)`) dans le titre ou le corps de la fiche destinée aux apprenants.
3. **Ciblage Exclusif du Projet d'Imitation :** Toutes les tâches opérationnelles s'exécutent sur le Projet d'imitation (*Blog des Lauréats*).
4. **Livrables Concrets et Traçables sur Branche Unique :** Chaque tâche débouche obligatoirement sur un fichier versionné sur la branche du sprint (`sprintX`). Zéro validation verbale sans artefact écrit (`cadrage/cadrage-projet.md`, `scrum/sprint-backlog-s1.md`, etc.).
5. **Suppression des Cérémonies Obsolètes en N3 :** Ne pas créer de tâches artificielles pour l'initialisation de Git/IDE ou les pitch decks de lancement (notions déjà acquises en N2 ou remplacées par la démonstration continue des livrables).
6. **Encodage Strict UTF-8 sans BOM :** Tous les fichiers générés respectent la règle 1 de `standards-techniques.md`.