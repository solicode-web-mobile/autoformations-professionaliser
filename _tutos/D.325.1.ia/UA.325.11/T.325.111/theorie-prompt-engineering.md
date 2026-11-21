---
layout: tuto
title: "Théorie : Prompt Engineering & Méthode RIO"
sous_titre: "Comprendre les LLMs, la méthode RIO, le Context Engineering et le prompting directif"
slug: "prompt-engineering"
slug_domaine: "ia"
slug_ua: "agent-skills"
permalink: /tutos/prompt-engineering/
tuto_id: "T.325.111"
version: "normal"
ua: "UA.325.11"
maturite: "ua-lab"
type: "tuto-atelier"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
sprint: "sprint1"
statut_realisation: "realise"
livrables:
  - chemin: "ua-lab/ia/agent-skills/prompt-engineering/prompt-engineering.md"
    version: "1.0.0"
  - chemin: "ua-lab/ia/agent-skills/prompt-engineering/presentation-prompt-engineering.md"
    version: "1.0.0"
---

## 1. Travail à faire
Effectuer les recherches documentaires nécessaires, concevoir une fiche de synthèse personnelle et préparer un diaporama de restitution Marp expliquant le fonctionnement d'un LLM, la structuration d'une consigne selon la méthode RIO, les patterns fondamentaux d'ingénierie de prompt et les principes du Context Engineering appliqué au développement logiciel.

## 2. Notions fondamentales
- **Définition & Rôle du Prompt Engineering :** Discipline d'ingénierie logicielle consistant à concevoir, calibrer et optimiser les instructions transmises à un modèle de langage (LLM). Il agit comme un contrat d'interface rigoureux garantissant un code source prévisible, maintenable et directement exploitable.
- **La Méthode Directrice RIO :**
  - **R — Rôle (Persona) :** Attribue à l'agent une identité technique précise et un niveau d'expertise (ex. *« Architecte senior expert Laravel »*). Il calibre le vocabulaire, la rigueur d'analyse et les choix d'architecture.
  - **I — Instruction (Contexte & Tâche) :** Exprime l'action à réaliser avec des verbes précis, le contexte métier et les dépendances, assortis de **contraintes négatives bloquantes** (garde-fous interdisant explicitement ce que l'agent ne doit pas faire : pas de bavardage, pas de code tronqué, zéro tableau Markdown).
  - **O — Output (Format attendu) :** Impose la structure de restitution, la langue et les contraintes de forme (Markdown brut, listes à puces `- `, 100% de liens relatifs, respect des plafonds de compacité).
- **Patterns Fondamentaux d'Ingénierie de Prompt :**
  - *Persona Pattern* : Cadrer l'expertise technique et la posture d'analyse.
  - *Template / Format Pattern* : Fournir la structure exacte ou le squelette du fichier à générer.
  - *Constraint Pattern* : Définir des limites strictes (ex: interdiction de commit, zéro tableau Markdown).
  - *Chain-of-Thought & Step-by-Step* : Forcer le modèle à décomposer son raisonnement en étapes séquentielles avant d'agir.
  - *Few-Shot Pattern* : Fournir un ou plusieurs exemples concrets de référence pour ancrer la conformité de la réponse.
  - *Reflective Pattern* : Demander à l'agent d'auditer son travail et d'émettre un plan interactif avant d'appliquer les modifications.
- **Context Engineering & Fenêtre de Contexte :**
  - Un modèle de langage ne conserve aucune mémoire implicite entre sessions distinctes.
  - L'ingénierie de contexte consiste à injecter chirurgicalement les règles, conventions et fichiers nécessaires sans saturer la fenêtre de contexte de l'agent.

## 3. Recherches à effectuer
- Analyser le phénomène d'hallucination des LLMs et comment la complétion probabiliste influence la génération de code source.
- Comparer l'approche *Zero-Shot prompting* et *Few-Shot prompting* sur des cas d'usage concrets de développement web.
- Expérimenter l'impact de contraintes négatives strictes sur la reproductibilité des sorties produites par l'agent.

## 4. Livrable attendu
- **Fiche technique de synthèse :** `ua-lab/ia/agent-skills/prompt-engineering/prompt-engineering.md` sur la branche `sprint1`.
- **Diaporama Marp de restitution :** `ua-lab/ia/agent-skills/prompt-engineering/presentation-prompt-engineering.md` sur la branche `sprint1`.
- **Contenu attendu :** Synthèse personnelle structurée reprenant les notions fondamentales (LLMs, méthode RIO, patterns de prompt, Context Engineering) et les réponses documentées aux recherches à effectuer.
