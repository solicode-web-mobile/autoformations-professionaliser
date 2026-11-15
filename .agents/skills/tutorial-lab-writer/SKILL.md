---
name: tutorial-lab-writer
description: Conçoit, structure et rédige les tutoriels d'ateliers pratiques guidés pour les Unités d'Apprentissage à maturité UA-Lab (Théorie d'assimilation 20/80, Pratique guidée sur projet d'imitation, Prompts et Skills RIO ciblés).
version: 2.0.0
inspiration:
  source: "solicode-pedagogy"
  plugin: "pedagogy-referential"
  pattern: "ua-lab-flexible, pareto-20-80, single-sprint-branch & recurrent-workflow-prompts"
---

# 1. Mission
Ce skill est l'**artisan pédagogique et technique** chargé de concevoir et rédiger les fiches d'ateliers pratiques guidés pour les Unités d'Apprentissage à maturité **`UA-Lab`**.

Alors que `tutorial-writer` est dédié aux tutoriels pas-à-pas d'apprentissage de code incrémental (`UA-Tuto`, progression $E_{n-1} \to E_n$), `tutorial-lab-writer` encadre les disciplines de cadrage conceptuel, de modélisation (UML Mermaid), d'outillage IA, de gouvernance agile Scrum, d'architecture logicielle et de réalisation applicative avec frameworks.

### Structure Didactique Flexible d'une UA-Lab
Une Unité d'Apprentissage de maturité `UA-Lab` ne suit pas une triade dogmatique rigide. Elle s'adapte dynamiquement aux acquis antérieurs et à la nature du livrable, comportant **entre 2 et 4 tâches** selon les règles suivantes :

$$\text{[Théorie 20/80 (Optionnelle)]} \longrightarrow \text{Pratique Imitation (Obligatoire)} \longrightarrow \text{[Création de Prompt(s) (Si flux récurrent)]}$$

1. **Règle d'Omission de la Théorie (Prérequis N1/N2 déjà validés) :**  
   Ne jamais introduire de tutoriel théorique pour des notions déjà maîtrisées aux niveaux antérieurs (ex : diagramme de contexte UML, diagramme de cas d'utilisation, bases de Tailwind CSS). Dans ce cas, l'UA débute immédiatement par la pratique outillée sur le projet d'imitation.
2. **Règle d'Omission du Prompt (Hors Flux Récurrent) :**  
   Les prompts ne sont créés que pour les étapes récurrentes du flux de travail produisant un livrable de sprint. Ne créer **aucun prompt** pour les labs d'apprentissage conceptuel pur (ex : découverte de Scrum), les décisions architecturales uniques prises une seule fois (ex : ADR-01) ou les tutoriels de prise en main initiale (ex : Hello World Laravel, premier contrôleur).
3. **Cas Particulier du Lab d'Ingénierie de Prompt (Étape 01) :**  
   Dans un lab dédié au prompting, la pratique EST directement la création du méta-prompt générateur (`prompt-creator`).
4. **Scission des Prompts Applicatifs :**  
   Pour les tranches verticales complètes (ex : Laravel), scinder systématiquement l'outillage IA en deux prompts distincts : `prompt-back-end` et `prompt-front-end` (accompagné d'un entraînement au Live Coding).

---

# 2. Déclenchement & Limites

- **Quand l'activer :**
  - Rédaction ou mise à jour des fiches de tutoriels associées à une Unité d'Apprentissage de maturité **`UA-Lab`**.
  - Structuration des consignes et jalons de modélisation UML (Mermaid.js).
  - Rédaction des ateliers de gouvernance agile Scrum (charte d'équipe, Product Backlog, User Stories INVEST).
  - Formalisation des dossiers d'architecture logicielle (ADR, diagrammes de séquence).
  - Élaboration de prompts directifs selon la méthode RIO pour les étapes récurrentes du flux de travail.
- **Quand NE PAS l'activer :**
  - Rédaction de tutoriels pas-à-pas de code pur (`UA-Tuto`) ➔ Utiliser [tutorial-writer](../tutorial-writer/SKILL.md).
  - Rédaction de tutoriels de tâches opérationnelles ou cérémonies sans théorie (`UA-Tâche`) ➔ Utiliser [tutorial-task-writer](../tutorial-task-writer/SKILL.md).
  - Planification globale, ordonnancement de sessions et arbitrage d'UAs ➔ Utiliser [tutorial-planer](../tutorial-planer/SKILL.md).

---

# 3. Structures Normées des Fiches d'une UA-Lab

### Format Fiche Théorie & Assimilation (Règle Pareto 20/80)
```markdown
---
layout: tuto
title: "Théorie : [Nom de la Notion]"
sous_titre: "[Sous-titre logique / pédagogique explicitant l'enjeu]"
slug: "[slug-kebab-case]"
permalink: /tutos/[slug-kebab-case]/
tuto_id: "T.XXX.YY1"
version: "normal"
ua: "UA.XXX.YY"
maturite: "UA-Lab"
nav_order: 1
simplified: true
en_construction: false
branche: "sprintX"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** [Phase et étape du sprint]
- **Branche Git :** `sprintX`
- **Stack mobilisée :** [Outils et technologies mobilisés]

## 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
[Description concrète de la recherche ou du livrable de synthèse]

## 3. Répartition Didactique (Règle des 20/80)

### Les 20% fournis directement au tutoriel :
- **[Définition fondamentale 1] :** [Définition rigoureuse et immédiatement actionnable]
- **[Définition fondamentale 2] :** [Définition rigoureuse et immédiatement actionnable]

### Les 80% recherchés par l'apprenant :
- [Question d'approfondissement ou exploration critique 1]
- [Comparaison technique ou recherche active 2]

## 4. Livrable Attendu
- Fiche de synthèse intégrée dans le journal d'apprentissage personnel de l'apprenant.
```

### Format Fiche Pratique sur Projet d'Imitation
```markdown
---
layout: tuto
title: "Pratique : [Nom de l'Action]"
sous_titre: "[Sous-titre logique explicitant la réalisation sur le projet d'imitation]"
slug: "[slug-kebab-case]"
permalink: /tutos/[slug-kebab-case]/
tuto_id: "T.XXX.YY2"
version: "normal"
ua: "UA.XXX.YY"
maturite: "UA-Lab"
nav_order: 2
simplified: true
en_construction: false
branche: "sprintX"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** [Phase et étape du sprint]
- **Branche Git :** `sprintX`
- **Fichiers modifiés ou créés :** `[chemin/du/fichier.ext]`
- **Stack mobilisée :** [Outils et technologies mobilisés]

## 2. Travail à Faire (Projet d'Imitation)
Bâtir le livrable sur le Projet d'imitation en respectant ces jalons :
1. **[Jalon 1] :** [Description opérationnelle directive]
2. **[Jalon 2] :** [Description opérationnelle directive]
3. **[Jalon 3] :** [Description opérationnelle directive]

## 3. Critères de Validation
- [ ] Le fichier `[chemin/du/fichier.ext]` est présent et versionné sur la branche `sprintX`.
- [ ] [Critère technique vérifiable 1]
- [ ] [Critère technique vérifiable 2]
```

### Format Fiche Création de Prompt IA
```markdown
---
layout: tuto
title: "Création du prompt-[nom]"
sous_titre: "Concevoir le prompt prompt-[nom] pour automatiser [action du flux de travail]"
slug: "creation-prompt-[nom]"
permalink: /tutos/creation-prompt-[nom]/
tuto_id: "T.XXX.YY3"
version: "normal"
ua: "UA.XXX.YY"
maturite: "UA-Lab"
nav_order: 3
simplified: true
en_construction: false
branche: "sprintX"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** [Phase et étape du sprint / Automatisation]
- **Branche Git :** `sprintX`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-[nom].prompt.md`

## 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-[nom].prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de produire le livrable pour n'importe quelle application métier.

## 3. Missions Concrètes Réalisées par le Prompt
1. [Mission opérationnelle 1]
2. [Mission opérationnelle 2]
3. [Mission opérationnelle 3]

## 4. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** [Persona d'expert précis]
- **Instruction :** [Consigne directrice sans ambiguïté]
- **Output :** [Format strict de sortie, sans bavardage]
- **Contraintes Négatives :** [Interdictions formelles d'exclusion]

## 5. Critères de Validation
- [ ] Le prompt est testé et consigné dans `livrables/ia/prompts/prompt-[nom].prompt.md` sur la branche `sprintX`.
- [ ] Il génère une sortie conforme aux standards techniques sans hallucination.
```

---

# 4. Règles Inviolables
1. **Ciblage Exclusif du Projet d'Imitation :** Dans toutes les fiches de tutoriels, le travail pratique cible exclusivement le Projet d'imitation (*Blog des Lauréats*). Les deux autres projets (Portfolio Développeur et Fil Rouge) sont réalisés en aval du sprint.
2. **Branche Git Unique :** Tout livrable physique est associé à la branche de travail du sprint (`branche: "sprintX"`).
3. **Zéro Affichage de Durée aux Apprenants :** Interdiction stricte de mentionner des durées de tâche (`(2h)`, `(4h)`) dans les titres canoniques ou le corps des tutoriels.
4. **Zéro Capture d'Écran comme Livrable :** Le livrable est obligatoirement un fichier de code, de configuration ou de modélisation versionné sous Git (`.php`, `.blade.php`, `.mmd`, `.md`, `.prompt.md`).
5. **Encodage Strict UTF-8 sans BOM :** Tous les fichiers créés ou modifiés respectent la règle 1 de `standards-techniques.md`.
6. **Maturité Explicite & Publication :** `maturite: "UA-Lab"`, `version: "normal"`, `simplified: true` et `en_construction: false` dès validation du tutoriel.