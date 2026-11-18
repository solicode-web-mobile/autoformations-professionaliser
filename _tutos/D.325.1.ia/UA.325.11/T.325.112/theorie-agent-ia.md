---
layout: tuto
title: "Théorie : Architecture d'un Agent IA et Règles Always-On"
sous_titre: "Comprendre l'anatomie d'un Agent IA outillé, les règles Always-On et la découvrabilité des skills"
slug: "agent-ia"
slug_domaine: "ia"
slug_ua: "agent-skills"
permalink: /tutos/agent-ia/
tuto_id: "T.325.112"
version: "normal"
ua: "UA.325.11"
maturite: "UA-Lab"
nav_order: 2
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Travail à faire
Effectuer les recherches documentaires nécessaires, rédiger une fiche de synthèse personnelle et concevoir un diaporama de restitution Marp expliquant l'anatomie d'un Agent IA de développement, le cycle Perception-Décision-Action, la séparation entre règles permanentes Always-On et compétences modulaires (Skills), ainsi que les principes d'ingénierie logicielle (SSOT, DRY) appliqués aux agents.

## 2. Notions fondamentales
- **Les Trois Paliers d'Autonomie :**
  - **1. LLM (Moteur brut) :** Modèle probabiliste prédisant les séquences textuelles sans mémoire implicite ni capacité d'interagir avec le système de fichiers.
  - **2. Chatbot (Conversationnel passif) :** Interface conversationnelle maintenant l'historique d'un échange, mais incapable de modifier du code ou d'exécuter des tests.
  - **3. Agent IA de développement :** Entité autonome outillée ancrée dans l'espace de travail. Il perçoit l'arborescence, planifie une séquence de tâches, modifie chirurgicalement les fichiers et exécute des commandes via son terminal.
- **Cycle Perception → Décision → Action :**
  - *Perception :* Lecture de la demande du concepteur, inspection des fichiers et analyse de l'arborescence.
  - *Décision :* Établissement d'un plan d'intervention décomposé en sous-tâches ordonnées.
  - *Action :* Utilisation des outils spécialisés de l'agent :
    - Outil d'exécution CLI (`run_command`) pour compiler, tester et vérifier les statuts.
    - Outils d'inspection (`read_file`, `list_dir`) pour lire le code sans le dénaturer.
    - Outils d'édition (`write_file`, `edit_file`) pour implémenter les modifications ciblées.
- **Architecture d'un Agent : Rules Always-On vs Skills Modulaires :**
  - **Règles Always-On (`.agents/rules/`) :** Directives universelles injectées automatiquement à chaque interaction. Elles définissent le cadre non négociable du projet (français simple A1, zéro tableau Markdown, 100% liens relatifs, interdiction de commit et push par l'IA).
  - **Skills Modulaires (`.agents/skills/`) :** Compétences expertes chargées dynamiquement selon le besoin pour préserver la fenêtre de contexte de l'agent.
  - **Découvrabilité & Compacité :** L'agent découvre les compétences grâce à l'en-tête YAML frontmatter (`name` et `description`). Le fichier orchestrateur `SKILL.md` respecte un plafond strict $\le 75$ lignes et délègue les tâches opératoires à son dossier `missions/`.
- **Principes Cardinaux d'Ingénierie Logicielle :**
  - **SSOT (Single Source of Truth) :** Chaque convention est définie à un emplacement unique (ex. les règles de formatage sont dans `regles-generales.md` et ne sont jamais dupliquées).
  - **DRY (Don't Repeat Yourself) :** Les skills s'appuient sur le socle des règles sans les redéfinir.
  - **Gouvernance Humaine :** L'Agent IA propose, analyse et outille ; seul le concepteur valide, commit et push sur le dépôt.

## 3. Recherches à effectuer
- Comparer les architectures agentiques modernes (boucle ReAct : Raisonnement / Action / Observation, et standard MCP : Model Context Protocol).
- Analyser la gestion des autorisations d'outils et les risques de sécurité (injections indirectes de prompts, exécution non contrôlée de commandes shell).
- Étudier comment les agents IA industriels découpent un problème complexe en sous-tâches coordonnées.

## 4. Livrable attendu
- **Fiche technique de synthèse :** `tutoriels/ia/agent-skills/agent-ia/agent-ia.md` sur la branche `sprint1`.
- **Diaporama Marp de restitution :** `tutoriels/ia/agent-skills/agent-ia/presentation-agent-ia.md` sur la branche `sprint1`.
- **Contenu attendu :** Synthèse personnelle structurée reprenant les notions fondamentales (Paliers d'autonomie, cycle Perception-Décision-Action, Always-On vs Skills, principes SSOT/DRY) et les réponses documentées aux recherches à effectuer.
