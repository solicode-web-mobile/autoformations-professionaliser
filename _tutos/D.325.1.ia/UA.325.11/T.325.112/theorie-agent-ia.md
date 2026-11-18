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

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 2 — Initialisation de l'Agent IA.
- **Branche Git :** `sprint1`
- **Stack mobilisée :** Environnement agentique, règles persistantes (`.agents/rules/`), catalogue de skills (`.agents/skills/`).

## 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches documentaires nécessaires et concevoir une fiche de synthèse expliquant l'anatomie d'un Agent IA autonome, la distinction entre règles permanentes Always-On et contexte volatil, ainsi que les mécanismes de découverte native des skills.

## 3. Répartition Didactique (Règle des 20/80)

### Les 20% fournis directement au tutoriel :
- **Chatbot vs Agent IA outillé :** Un chatbot se limite à répondre par du texte généré. Un Agent IA perçoit son environnement (fichiers, terminal, arborescence), raisonne sur une séquence d'actions et utilise des outils (tools) pour manipuler le code et le dépôt.
- **Règles Always-On vs contexte volatil :**
  - Les contextes volatils disparaissent à la fermeture de la session.
  - Les règles permanentes (`.agents/rules/*.md`) sont injectées automatiquement à chaque interaction sans intervention humaine, assurant la conformité aux normes (standards de code, conventions de nommage, architecture).
- **Architecture modulaire d'un Skill :**
  - Un skill est un répertoire autonome regroupant un manifeste (`SKILL.md`), sa documentation opérationnelle (`doc/how-to-use.md`) et des missions ou scripts spécialisés.
  - L'agent découvre les compétences disponibles via la description du manifeste et les active à la demande pour préserver sa fenêtre de contexte.

### Les 80% recherchés par l'apprenant :
- Comparer les architectures agentiques modernes (boucle ReAct : Raisonnement / Action / Observation, et standard MCP : Model Context Protocol).
- Analyser la gestion des autorisations d'outils et les risques de sécurité (injections indirectes de prompts, exécution non contrôlée de commandes shell).
- Étudier comment les agents IA industriels découpent un problème complexe en sous-tâches coordonnées.

## 4. Livrable Attendu
- Fiche de synthèse Architecture d'un Agent IA intégrée dans le journal d'apprentissage personnel de l'apprenant.
