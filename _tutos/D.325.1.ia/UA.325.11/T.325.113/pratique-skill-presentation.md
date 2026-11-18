---
layout: tuto
title: "Pratique : Conception d'un skill agentique — Exemple skill-presentation"
sous_titre: "Concevoir un skill outillé avec SKILL.md, doc/how-to-use.md et missions spécialisées Marp et PowerPoint"
slug: "skill-presentation"
slug_domaine: "ia"
slug_ua: "agent-skills"
permalink: /tutos/skill-presentation/
tuto_id: "T.325.113"
version: "normal"
ua: "UA.325.11"
maturite: "UA-Lab"
nav_order: 3
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 2 — Initialisation de l'Agent IA.
- **Branche Git :** `sprint1`
- **Stack mobilisée :** Architecture des skills agentiques, YAML Front Matter, syntaxe RIO.

## 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Concevoir dans le cadre d'un atelier pratique guidé un skill agentique complet nommé `skill-presentation`. Ce skill sert d'exemple concret pour outiller un Agent IA dans la génération automatique de supports de présentation (diaporamas Marp et plans PowerPoint).

L'apprenant doit créer :
1. Le manifeste du skill : `SKILL.md`.
2. Le guide d'utilisation opérationnel : `doc/how-to-use.md`.
3. Deux missions spécialisées au format RIO :
   - `missions/presentation-marp.mission.md`
   - `missions/presentation-powerpoint.mission.md`

## 3. Étapes de Réalisation Pas-à-Pas

1. **Étape 1 — Création de l'arborescence de l'atelier :**  
   Dans votre projet, créez l'arborescence du skill dans le répertoire `labs/ia/skill-presentation/` :
   ```bash
   mkdir -p labs/ia/skill-presentation/doc labs/ia/skill-presentation/missions
   ```

2. **Étape 2 — Rédaction du manifeste `SKILL.md` :**  
   Dans `labs/ia/skill-presentation/`, créez le fichier `SKILL.md` :
````markdown
---
name: skill-presentation
description: Génère, structure et formate des supports de présentation de projets techniques (diaporamas Marp Markdown et plans structurés pour PowerPoint).
version: 1.0.0
---

# Skill : Présentation de Projets Techniques

Ce skill permet à l'Agent IA de transformer des spécifications, un README ou des livrables de sprint en diaporamas percutants pour les soutenances et revues de projet.

## Capacités
- **Marp Markdown** : Diaporamas prêts à projeter avec thèmes, en-têtes et directives visuelles.
- **Plans PowerPoint** : Trame textuelle structurée (titre, bullets, notes d'orateur) importable dans PowerPoint.
````

3. **Étape 3 — Rédaction du guide d'utilisation `doc/how-to-use.md` :**  
   Dans `labs/ia/skill-presentation/doc/`, créez `how-to-use.md` :
````markdown
# Guide d'Utilisation : skill-presentation

## 1. Rôle du skill
Ce skill est activé dès que l'utilisateur souhaite créer un support de présentation pour une revue de sprint ou une soutenance.

## 2. Prompts d'invocation types
- *"Génère un diaporama Marp de 5 slides résumant le Sprint 1 à partir de mon README.md."*
- *"Prépare la trame PowerPoint de ma soutenance technique."*

## 3. Déroulement de l'exécution
1. L'agent analyse le fichier source (`README.md` ou livrables du sprint).
2. L'agent sélectionne la mission appropriée (`presentation-marp` ou `presentation-powerpoint`).
3. L'agent applique le gabarit standardisé Solicode (page de garde, 3 points par slide maximum).
4. Le livrable est écrit dans `presentations/`.
````

4. **Étape 4 — Conception de la mission `missions/presentation-marp.mission.md` :**  
   Dans `labs/ia/skill-presentation/missions/`, créez `presentation-marp.mission.md` selon la méthode RIO :
````markdown
---
mission: presentation-marp
format: rio
---

# Cahier des Charges de la Mission : Génération Marp

- **Rôle :** Expert Designer & Développeur Frontend spécialisé dans les présentations Marp Markdown.
- **Instruction :** À partir des livrables ou du README fourni en paramètre, générer un diaporama complet au format Marp Markdown.
- **Output :** Fichier Markdown débutant impérativement par l'en-tête Marp (`marp: true`, `theme: default`, `paginate: true`), avec page de garde normalisée (Apprenant, Encadrant, Établissement) et séparateurs `---` stricts.
- **Contraintes Négatives :**
  - Pas de texte narratif ou de commentaires hors du bloc Markdown.
  - Jamais plus de 4 puces par diapositive.
  - Zéro code HTML direct non supporté par Marp.
````

5. **Étape 5 — Conception de la mission `missions/presentation-powerpoint.mission.md` :**  
   Dans `labs/ia/skill-presentation/missions/`, créez `presentation-powerpoint.mission.md` :
````markdown
---
mission: presentation-powerpoint
format: rio
---

# Cahier des Charges de la Mission : Génération PowerPoint

- **Rôle :** Consultant en communication technique et conception de présentations professionnelles.
- **Instruction :** Structurer une trame de présentation hiérarchisée prête à être convertie ou importée dans Microsoft PowerPoint.
- **Output :** Document Markdown avec pour chaque slide : Titre (Niveau 2), Messages clés (liste à puces concise), et section dédiée `### Notes de l'orateur` contenant les arguments oraux.
- **Contraintes Négatives :**
  - Pas de diapositives surchargées de texte.
  - Pas d'acronymes techniques sans définition immédiate.
````

## 4. Livrables & Critères de Validation
- **Livrables attendus :**
  - Dossier `labs/ia/skill-presentation/` comprenant :
    - `SKILL.md` (manifeste YAML).
    - `doc/how-to-use.md` (guide opérationnel).
    - `missions/presentation-marp.mission.md` (mission RIO Marp).
    - `missions/presentation-powerpoint.mission.md` (mission RIO PowerPoint).
- **Critères de validation :**
  - [ ] Le manifeste `SKILL.md` respecte les métadonnées (nom, description, version).
  - [ ] Le fichier `doc/how-to-use.md` formalise les cas d'usage et les prompts types.
  - [ ] Les missions respectent scrupuleusement la structure RIO (Rôle, Instruction, Output, Contraintes négatives).
