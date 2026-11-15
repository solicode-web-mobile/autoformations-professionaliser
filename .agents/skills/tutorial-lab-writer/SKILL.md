---
name: tutorial-lab-writer
description: Conçoit, structure et rédige les tutoriels d'ateliers pratiques guidés pour les Unités d'Apprentissage à maturité UA-Lab (Théorie d'assimilation, Pratique guidée sur projet d'imitation, Prompts et Skills RIO sur projet fil rouge).
version: 1.0.0
inspiration:
  source: "solicode-pedagogy"
  plugin: "pedagogy-referential"
  pattern: "ua-lab-triad, guided-practice & prompt-engineering"
---

# 1. Mission
Ce skill est l'**artisan pédagogique et technique** chargé de concevoir et rédiger les fiches d'ateliers pratiques guidés pour les Unités d'Apprentissage à maturité **`UA-Lab`**.

Alors que `tutorial-writer` est dédié aux tutoriels pas-à-pas d'apprentissage de code pur (`UA-Tuto`, progression $E_{n-1} \to E_n$), `tutorial-lab-writer` encadre les disciplines de cadrage, de modélisation, d'outillage IA, de gouvernance agile Scrum et d'architecture logicielle.

### La Triade Canonique d'une UA-Lab
Chaque Unité d'Apprentissage de maturité `UA-Lab` se décompose obligatoirement en trois tâches / tutoriels complémentaires :

$$\text{Tâche 1 (Théorie)} \longrightarrow \text{Tâche 2 (Pratique Imitation)} \longrightarrow \text{Tâche 3 (Prompts \& Skills Fil Rouge)}$$

1. **Tâche 1 — Présentation Théorique & Exercices d'Assimilation (`T.XXX.YY1`) :**  
   Comprendre les fondations conceptuelles, la frontière du système, les rôles ou les patrons d'architecture. Évaluation par questions réflexives et mémos de synthèse.
2. **Tâche 2 — Réalisation Pratique sur le Projet d'Imitation (`T.XXX.YY2`) :**  
   Mise en pratique guidée sur le projet de référence (*ex: Blog des Lauréats*). Production d'un livrable physique versionnable (`livrables/uml/*.mmd`, `livrables/scrum/*.md`, `livrables/architecture/*.md`).
3. **Tâche 3 — Conception Prompts & Skills Projet Fil Rouge (`T.XXX.YY3`) :**  
   Transposition opérationnelle vers le projet fil rouge (*ex: Plateforme Cinéma*) via l'ingénierie de prompt formalisée selon la méthode **RIO** (Rôle, Instruction, Output délimité, Contraintes négatives).

---

# 2. Déclenchement & Limites

- **Quand l'activer :**
  - Rédaction ou enrichissement des fiches de tutoriels associées à une Unité d'Apprentissage de maturité **`UA-Lab`**.
  - Structuration des consignes et jalons de modélisation UML (Mermaid.js).
  - Rédaction des guides de gouvernance agile Scrum (charte d'équipe, Product Backlog, User Stories).
  - Formalisation des dossiers d'architecture logicielle (ADR, diagrammes de séquence).
  - Élaboration de prompts directifs et skills d'assistance IA selon la méthode RIO.
- **Quand NE PAS l'activer :**
  - Rédaction de tutoriels pas-à-pas d'apprentissage de code pur (`UA-Tuto`) ➔ Utiliser [tutorial-writer](../tutorial-writer/SKILL.md).
  - Planification globale, ordonnancement de sessions et arbitrage d'UAs ➔ Utiliser [tutorial-planer](../tutorial-planer/SKILL.md).
  - Évolution des layouts Jekyll Just the Docs ou styles CSS ➔ Utiliser [dev-jekyll](../dev-jekyll/SKILL.md).

---

# 3. Structure Normée des 3 Fiches d'une UA-Lab

### Format Fiche Tâche 1 : Théorie & Assimilation
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
en_construction: true
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** [Phase et étape du sprint]
- **Stack mobilisée :** [Outils et technologies mobilisés]

## 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
[Description concrète de la recherche ou du livrable de synthèse]

## 3. Notions Clés du Sprint à Ne Pas Oublier
- [Notion 1]
- [Notion 2]

## 4. Points de Réflexion & Auto-Évaluation
- *[Question réflexive 1]*
- *[Question réflexive 2]*
```

### Format Fiche Tâche 2 : Pratique sur Projet d'Imitation
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
en_construction: true
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Livrable Attendu
- `livrables/[domaine]/[fichier.ext]` : [Description précise du livrable]

## 2. Consignes & Jalons de Réalisation
Bâtir le livrable en respectant ces 3 jalons :
1. **[Jalon 1] :** [Description opérationnelle]
2. **[Jalon 2] :** [Description opérationnelle]
3. **[Jalon 3] :** [Description opérationnelle]

## 3. Points de Vigilance
- ⚠️ [Avertissement sur un piège ou une mauvaise pratique fréquente]

## 4. Critères de Validation
- [ ] [Critère vérifiable 1]
- [ ] [Critère vérifiable 2]
```

### Format Fiche Tâche 3 : Prompts & Skills Projet Fil Rouge
```markdown
---
layout: tuto
title: "Prompts & Skills : [Nom de l'Action Fil Rouge]"
sous_titre: "[Sous-titre logique explicitant la transposition]"
slug: "[slug-kebab-case]"
permalink: /tutos/[slug-kebab-case]/
tuto_id: "T.XXX.YY3"
version: "normal"
ua: "UA.XXX.YY"
maturite: "UA-Lab"
nav_order: 3
simplified: true
en_construction: true
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux Fil Rouge
- Transposition de l'[Étape X] vers le Projet Fil Rouge.

## 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/[nom-du-prompt].prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de produire le livrable pour n'importe quelle application métier.

## 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** [Persona d'expert précis]
- **Instruction :** [Consigne directrice sans ambiguïté]
- **Output :** [Format strict de sortie, sans bavardage]
- **Contraintes Négatives :** [Interdictions formelles d'exclusion]

## 4. Critères de Validation
- [ ] [Critère d'évaluation du prompt testé avec l'IA]
```

---

# 4. Règles Inviolables
1. **Zéro Capture d'Écran comme Livrable :** Le livrable est obligatoirement un fichier versionnable commité sous Git (`.mmd`, `.md`, `.prompt.md`).
2. **Encodage Strict UTF-8 sans BOM :** Tous les fichiers générés doivent respecter la règle 1 de `standards-techniques.md`.
3. **Maturité Explicite :** La mention `maturite: "UA-Lab"` figure obligatoirement dans le frontmatter YAML. Le terme « type » est banni.
4. **Schémas Déclaratifs Mermaid.js :** Tous les diagrammes de contexte, cas d'utilisation ou flux doivent être modélisés en syntaxe déclarative Mermaid native intégrable directement en Markdown.
