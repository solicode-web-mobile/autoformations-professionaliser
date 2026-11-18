---
layout: tuto
title: "Création du skill de clôture de sprint"
sous_titre: "Concevoir le skill modulaire d'automatisation orchestrant les 4 missions de Sprint Review, Retrospective, Refinement et Débriefing"
slug: "skill-cloture-sprint"
slug_domaine: "realisation-projet"
slug_ua: "cloture-sprint"
permalink: /tutos/skill-cloture-sprint/
tuto_id: "T.351.235"
version: "normal"
ua: "UA.351.23"
maturite: "UA-Tâche"
nav_order: 5
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Travail à faire

Concevoir, documenter et tester le skill modulaire réutilisable **`cloture-sprint`** pour l'Agent IA. Ce skill active la commande conventionnelle `/cloture-sprint` et orchestre les 4 missions d'ingénierie agile automatisant la production des livrables de clôture de sprint :
1. L'orchestrateur compact du skill : `.agents/skills/cloture-sprint/SKILL.md`.
2. Les 4 missions spécialisées :
   - `missions/sprint-review.md` (Procès-verbal de démonstration et audit binaire de la Definition of Done).
   - `missions/sprint-retrospective.md` (Animation réflexive et identification de la dette d'empathie utilisateur).
   - `missions/backlog-refinement.md` (Archivage dans `issues/issues-closes.md` et réordonnancement du Product Backlog).
   - `missions/debriefing-session.md` (Bilan d'acquisition des compétences et analyse réflexive du Live Coding).
3. Le guide opérationnel : `.agents/skills/cloture-sprint/doc/how-to-use.md`.
4. La notice d'atelier : `skill-cloture-sprint.md`.
5. Le diaporama Marp de restitution : `presentation-skill-cloture-sprint.md`.
6. Le journal des commandes : `skill-cloture-sprint.command.md`.

## 2. Consignes & Spécifications de Réalisation

1. **Étape 1 — Préparation de l'Arborescence du Skill :**  
   Initialisez les dossiers du skill dans `.agents/skills/cloture-sprint/` et l'espace de documentation d'atelier sous `tutoriels/` :

```bash
mkdir -p .agents/skills/cloture-sprint/missions .agents/skills/cloture-sprint/doc
mkdir -p tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint
```

2. **Étape 2 — Conception du Manifeste Orchestrateur `SKILL.md` :**  
   Dans `.agents/skills/cloture-sprint/SKILL.md`, concevez l'orchestrateur selon les standards d'ingénierie des skills :
   - **Frontmatter YAML :** Définir `name: cloture-sprint` et rédiger une `description` explicite pour la sélection sémantique par l'Agent IA.
   - **Titre & Commande :** Déclarer la commande `/cloture-sprint`.
   - **Section Mission :** Définir le rôle d'automatisation des rituels et documents de clôture de sprint Scrum.
   - **Section Déclenchement :** Expliciter quand activer le skill (en fin de sprint, pour conduire la revue, la rétrospective, le raffinement ou le débriefing) et quand ne pas l'activer (en cours de sprint, pour du code applicatif pur ou la planification initiale).
   - **Section Workflow & Missions Disponibles :** Cartographier le déclenchement séquentiel des 4 missions vers les sous-fichiers de `missions/`.
   - **Garde-fou :** Plafond strict de $\le 75$ lignes pour l'orchestrateur.

3. **Étape 3 — Conception des 4 Missions Spécialisées :**  
   Dans `.agents/skills/cloture-sprint/missions/`, formalisez les 4 missions spécialisées :
   - `missions/sprint-review.md` : Prend en entrée les User Stories complétées et la démonstration live. Évalue critère par critère les 7 conditions de la Definition of Done face au Sprint Goal. Génère le PV dans `scrum/revue-s1.md`.
   - `missions/sprint-retrospective.md` : Structure la collecte réflexive (forces, freins, actions concrètes). Identifie le manque d'empathie utilisateur justifiant l'approche Design Thinking en S2. Génère `scrum/retrospective-s1.md`.
   - `missions/backlog-refinement.md` : Déplace la User Story terminée dans `issues/issues-closes.md` et réordonne les priorités du Product Backlog pour le sprint suivant dans `scrum/product-backlog.md`.
   - `missions/debriefing-session.md` : Évalue le niveau d'acquisition sur les 5 compétences du sprint (C.311, C.312, C.321, C.325, C.351) et débriefe l'épreuve de Live Coding (40 min). Génère `scrum/bilan-s1.md`.
   - *Règle d'or de formatage :* Imposer aux 4 missions la génération de documents Markdown sans tableau (listes à puces directes et titres hiérarchisés).

4. **Étape 4 — Rédaction du Guide Opérationnel `doc/how-to-use.md` :**  
   Dans `.agents/skills/cloture-sprint/doc/how-to-use.md`, documentez pour les membres de l'équipe :
   - Le rôle global du skill.
   - Les commandes d'appel : `/cloture-sprint review`, `/cloture-sprint retrospective`, `/cloture-sprint refinement`, `/cloture-sprint debriefing`.
   - Les prérequis d'exécution (branche de sprint active, incrément testé).
   - Le protocole de vérification des fichiers générés sous `scrum/` et `issues/`.

5. **Étape 5 — Rédaction de la Notice d'Atelier & Diaporama Marp :**  
   - `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/skill-cloture-sprint.md` : Synthèse technique de l'architecture du skill, diagramme Mermaid illustrant l'orchestrateur et ses 4 missions, justification du passage des prompts isolés vers un skill unifié.
   - `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/presentation-skill-cloture-sprint.md` : Diaporama Marp (en-tête Marp, page de garde Solicode, zéro tableau, 4 à 6 puces par slide) présentant le fonctionnement du skill à l'équipe.

6. **Étape 6 — Test d'Activation & Journalisation des Commandes :**  
   Testez l'activation du skill et consignez les commandes exécutées dans `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/skill-cloture-sprint.command.md` :

```bash
mkdir -p .agents/skills/cloture-sprint/missions .agents/skills/cloture-sprint/doc
mkdir -p tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint
```

## 3. Livrables & Critères de validation

- **Livrables attendus :**
  - Manifeste orchestrateur : `.agents/skills/cloture-sprint/SKILL.md` sur la branche `sprint1`.
  - Missions spécialisées : `.agents/skills/cloture-sprint/missions/` (`sprint-review.md`, `sprint-retrospective.md`, `backlog-refinement.md`, `debriefing-session.md`) sur la branche `sprint1`.
  - Guide d'utilisation : `.agents/skills/cloture-sprint/doc/how-to-use.md` sur la branche `sprint1`.
  - Notice technique d'atelier : `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/skill-cloture-sprint.md` sur la branche `sprint1`.
  - Diaporama Marp : `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/presentation-skill-cloture-sprint.md` sur la branche `sprint1`.
  - Journal des commandes : `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/skill-cloture-sprint.command.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le fichier `SKILL.md` contient un Front Matter YAML valide avec `name: cloture-sprint` et ne dépasse pas 75 lignes.
  - [ ] Le manifeste `SKILL.md` référence explicitement les 4 missions du dossier `missions/`.
  - [ ] Chaque mission dans `missions/` impose la génération de documents Markdown sans tableau.
  - [ ] Le guide `doc/how-to-use.md` formalise les commandes d'invocation et les prérequis de chaque rituel.
  - [ ] Le journal `skill-cloture-sprint.command.md` consigne fidèlement les commandes sans commande Git.
