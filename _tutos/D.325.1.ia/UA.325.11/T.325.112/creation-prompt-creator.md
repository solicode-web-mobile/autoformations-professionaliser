---
layout: tuto
title: "Définition du socle de règles et du protocole de l'Agent IA"
sous_titre: "Formaliser les règles, le protocole de fonctionnement et la mission de génération de missions"
slug: "creation-prompt-creator"
permalink: /tutos/creation-prompt-creator/
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
- **Position dans le flux :** Phase A — Initialisation du Projet, Outillage IA & Méthodologie / Étape 02 — Initialisation de l'Agent IA.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `missions/init-ia.mission.md`, `missions/init-agent.mission.md`, `missions/missions-creator.mission.md`

## 2. Travail à Faire
1. Rédiger le socle commun des règles et contexte du projet dans `missions/init-ia.mission.md`.
2. Définir le protocole d'interaction et de fonctionnement opérationnel de l'Agent IA dans `missions/init-agent.mission.md`.
3. Concevoir la mission génératrice de missions d'ingénierie dans `missions/missions-creator.mission.md` en appliquant la méthode RIO.

## 3. Missions Concrètes Réalisées par l'Agent IA
1. Analyser les consignes d'étapes et injecter le contexte projet sans hallucination.
2. Respecter les contraintes négatives bloquantes (zéro bavardage, chemins relatifs stricts, UTF-8 sans BOM).
3. Produire des missions d'ingénierie standardisées et prêtes à l'emploi.

## 4. Critères de Validation
- [ ] Le fichier `missions/init-ia.mission.md` formalise les règles communes du projet.
- [ ] Le fichier `missions/init-agent.mission.md` définit le protocole opérationnel de l'Agent.
- [ ] Le fichier `missions/missions-creator.mission.md` est validé et testé sur un cas d'étape réel.
