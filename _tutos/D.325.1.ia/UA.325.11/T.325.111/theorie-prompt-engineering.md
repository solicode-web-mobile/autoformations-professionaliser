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
maturite: "UA-Lab"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Travail à faire
Effectuer les recherches documentaires nécessaires et concevoir une fiche de synthèse expliquant le fonctionnement d'un LLM, la structure d'un prompt directif selon la méthode RIO et l'intérêt du Context Engineering dans le développement logiciel.

## 2. Notions fondamentales
- **Fenêtre de contexte et injection chirurgicale :** Un modèle de langage ne conserve aucune mémoire implicite entre sessions distinctes. L'agent doit recevoir explicitement les règles, le périmètre et les fichiers cibles.
- **Méthode RIO :**
  - **Rôle :** Persona technique de haut niveau (ex. *« Expert Senior Laravel 12 »*).
  - **Intention / Instructions :** Objectif fonctionnel unique et séquence d'actions sans ambiguïté.
  - **Output :** Délimitation stricte du format attendu (Markdown brut, bloc de code sans bavardage).
- **Contraintes négatives bloquantes :** Supprimer tout bavardage introductif ou de politesse, interdire le code partiel (`// TODO`) et forcer des chemins relatifs stricts.

## 3. Recherches à effectuer
- Analyser le phénomène d'hallucination des LLMs et comment la complétion probabiliste influence la génération de code source.
- Comparer l'approche *Zero-Shot prompting* et *Few-Shot prompting* sur des cas d'usage de développement web.
- Expérimenter l'impact de consignes négatives strictes sur la reproductibilité des sorties.

## 4. Livrable attendu
- **Fichier de synthèse :** `tutoriels/ia/agent-skills/prompt-engineering/prompt-engineering.md` sur la branche `sprint1`.
- **Contenu attendu :** Synthèse personnelle structurée reprenant les notions fondamentales (LLMs, méthode RIO, Context Engineering) et les réponses documentées aux recherches à effectuer.
