---
layout: tuto
title: "Théorie : Prompt Engineering & Méthode RIO"
sous_titre: "Comprendre les LLMs, la méthode RIO, le Context Engineering et le méta-prompting"
slug: "theorie-prompt-engineering"
permalink: /tutos/theorie-prompt-engineering/
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

## 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 1.1 — Outillage Prompt Engineering.
- **Branche Git :** `sprint1`
- **Stack mobilisée :** Chaîne d'outillage IA, LLMs (Gemini, Claude), architecture de contextes.

## 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches documentaires nécessaires et concevoir une fiche de synthèse expliquant le fonctionnement d'un LLM, la structure d'un prompt directif selon la méthode RIO et l'intérêt du Context Engineering.

## 3. Répartition Didactique (Règle des 20/80)

### Les 20% fournis directement au tutoriel :
- **Fenêtre de contexte et injection chirurgicale :** Un modèle de langage ne conserve aucune mémoire implicite entre sessions distinctes. L'agent doit recevoir explicitement les règles, le périmètre et les fichiers cibles (`@fichier`).
- **Méthode RIO :**
  - **Rôle :** Persona technique de haut niveau (ex. *« Expert Senior Laravel 12 »*).
  - **Intention / Instructions :** Objectif fonctionnel unique et séquence d'actions sans ambiguïté.
  - **Output :** Délimitation stricte du format attendu (Markdown brut, bloc de code sans fioriture).
- **Contraintes négatives bloquantes :** Supprimer tout bavardage introductif ou de politesse, interdire le code partiel (`// TODO`) et forcer des chemins relatifs stricts.

### Les 80% recherchés par l'apprenant :
- Analyser le phénomène d'hallucination des LLMs et comment la complétion probabiliste influence la génération de code.
- Comparer l'approche *Zero-Shot prompting* et *Few-Shot prompting* sur des cas d'usage de développement web.
- Expérimenter l'impact de consignes négatives strictes sur la reproductibilité des sorties.

## 4. Livrable Attendu
- Fiche de synthèse RIO intégrée dans le journal d'apprentissage personnel de l'apprenant.