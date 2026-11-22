---
layout: tuto
title: "CrÃ©ation du skill de clÃ´ture de sprint"
sous_titre: "Concevoir le skill modulaire d'automatisation orchestrant les 4 missions de Sprint Review, Retrospective, Refinement et DÃ©briefing"
slug: "skill-cloture-sprint"
slug_domaine: "realisation-projet"
slug_ua: "cloture-sprint"
permalink: /tutos/skill-cloture-sprint/
tuto_id: "T.351.255"
version: "normal"
ua: "UA.351.25"
maturite: "projet"
type: "tuto-tache"
nav_order: 5
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
  - chemin: "tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/skill-cloture-sprint.md"
    version: "1.0.0"
  - chemin: "tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/presentation-skill-cloture-sprint.md"
    version: "1.0.0"
  - chemin: "tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/skill-cloture-sprint.command.md"
    version: "1.0.0"
---

## 1. Travail Ã  faire

Concevoir, documenter et tester le skill modulaire rÃ©utilisable **`cloture-sprint`** pour l'Agent IA. Ce skill active la commande conventionnelle `/cloture-sprint` et orchestre les 4 missions d'ingÃ©nierie agile automatisant la production des livrables de clÃ´ture de sprint :
1. L'orchestrateur compact du skill : `.agents/skills/cloture-sprint/SKILL.md`.
2. Les 4 missions spÃ©cialisÃ©es :
   - `missions/sprint-review.md` (ProcÃ¨s-verbal de dÃ©monstration et audit binaire de la Definition of Done).
   - `missions/sprint-retrospective.md` (Animation rÃ©flexive et identification de la dette d'empathie utilisateur).
   - `missions/backlog-refinement.md` (Archivage dans `issues/issues-closes.md` et rÃ©ordonnancement du Product Backlog).
   - `missions/debriefing-session.md` (Bilan d'acquisition des compÃ©tences et analyse rÃ©flexive du Live Coding).
3. Le guide opÃ©rationnel : `.agents/skills/cloture-sprint/doc/how-to-use.md`.
4. La notice d'atelier : `skill-cloture-sprint.md`.
5. Le diaporama Marp de restitution : `presentation-skill-cloture-sprint.md`.
6. Le journal des commandes : `skill-cloture-sprint.command.md`.

## 2. Consignes & SpÃ©cifications de RÃ©alisation

1. **Ã‰tape 1 â€” PrÃ©paration de l'Arborescence du Skill :**  
   Initialisez les dossiers du skill dans `.agents/skills/cloture-sprint/` et l'espace de documentation d'atelier sous `tutoriels/` :

```bash
mkdir .agents/skills/cloture-sprint/missions, .agents/skills/cloture-sprint/doc
mkdir tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint
```

2. **Ã‰tape 2 â€” Conception du Manifeste Orchestrateur `SKILL.md` :**  
   Dans `.agents/skills/cloture-sprint/SKILL.md`, concevez l'orchestrateur selon les standards d'ingÃ©nierie des skills :
   - **Frontmatter YAML :** DÃ©finir `name: cloture-sprint` et rÃ©diger une `description` explicite pour la sÃ©lection sÃ©mantique par l'Agent IA.
   - **Titre & Commande :** DÃ©clarer la commande `/cloture-sprint`.
   - **Section Mission :** DÃ©finir le rÃ´le d'automatisation des rituels et documents de clÃ´ture de sprint Scrum.
   - **Section DÃ©clenchement :** Expliciter quand activer le skill (en fin de sprint, pour conduire la revue, la rÃ©trospective, le raffinement ou le dÃ©briefing) et quand ne pas l'activer (en cours de sprint, pour du code applicatif pur ou la planification initiale).
   - **Section Workflow & Missions Disponibles :** Cartographier le dÃ©clenchement sÃ©quentiel des 4 missions vers les sous-fichiers de `missions/`.
   - **Garde-fou :** Plafond strict de $\le 75$ lignes pour l'orchestrateur.

3. **Ã‰tape 3 â€” Conception des 4 Missions SpÃ©cialisÃ©es :**  
   Dans `.agents/skills/cloture-sprint/missions/`, formalisez les 4 missions spÃ©cialisÃ©es :
   - `missions/sprint-review.md` : Prend en entrÃ©e les User Stories complÃ©tÃ©es et la dÃ©monstration live. Ã‰value critÃ¨re par critÃ¨re les 7 conditions de la Definition of Done face au Sprint Goal. GÃ©nÃ¨re le PV dans `scrum/revue-s1.md`.
   - `missions/sprint-retrospective.md` : Structure la collecte rÃ©flexive (forces, freins, actions concrÃ¨tes). Identifie le manque d'empathie utilisateur justifiant l'approche Design Thinking en S2. GÃ©nÃ¨re `scrum/retrospective-s1.md`.
   - `missions/backlog-refinement.md` : DÃ©place la User Story terminÃ©e dans `issues/issues-closes.md` et rÃ©ordonne les prioritÃ©s du Product Backlog pour le sprint suivant dans `scrum/product-backlog.md`.
   - `missions/debriefing-session.md` : Ã‰value le niveau d'acquisition sur les 5 compÃ©tences du sprint (C.311, C.312, C.321, C.325, C.351) et dÃ©briefe l'Ã©preuve de Live Coding (40 min). GÃ©nÃ¨re `scrum/bilan-s1.md`.
   - *RÃ¨gle d'or de formatage :* Imposer aux 4 missions la gÃ©nÃ©ration de documents Markdown sans tableau (listes Ã  puces directes et titres hiÃ©rarchisÃ©s).

4. **Ã‰tape 4 â€” RÃ©daction du Guide OpÃ©rationnel `doc/how-to-use.md` :**  
   Dans `.agents/skills/cloture-sprint/doc/how-to-use.md`, documentez pour les membres de l'Ã©quipe :
   - Le rÃ´le global du skill.
   - Les commandes d'appel : `/cloture-sprint review`, `/cloture-sprint retrospective`, `/cloture-sprint refinement`, `/cloture-sprint debriefing`.
   - Les prÃ©requis d'exÃ©cution (branche de sprint active, incrÃ©ment testÃ©).
   - Le protocole de vÃ©rification des fichiers gÃ©nÃ©rÃ©s sous `scrum/` et `issues/`.

5. **Ã‰tape 5 â€” RÃ©daction de la Notice d'Atelier & Diaporama Marp :**  
   - `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/skill-cloture-sprint.md` : SynthÃ¨se technique de l'architecture du skill, diagramme Mermaid illustrant l'orchestrateur et ses 4 missions, justification du passage des prompts isolÃ©s vers un skill unifiÃ©.
   - `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/presentation-skill-cloture-sprint.md` : Diaporama Marp (en-tÃªte Marp, page de garde Solicode, zÃ©ro tableau, 4 Ã  6 puces par slide) prÃ©sentant le fonctionnement du skill Ã  l'Ã©quipe.

6. **Ã‰tape 6 â€” Test d'Activation & Journalisation des Commandes :**  
   Testez l'activation du skill et consignez les commandes exÃ©cutÃ©es dans `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/skill-cloture-sprint.command.md` :

```bash
mkdir .agents/skills/cloture-sprint/missions, .agents/skills/cloture-sprint/doc
mkdir tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint
```

## 3. Livrables & CritÃ¨res de validation

- **Livrables attendus :**
  - Manifeste orchestrateur : `.agents/skills/cloture-sprint/SKILL.md` sur la branche `sprint1`.
  - Missions spÃ©cialisÃ©es : `.agents/skills/cloture-sprint/missions/` (`sprint-review.md`, `sprint-retrospective.md`, `backlog-refinement.md`, `debriefing-session.md`) sur la branche `sprint1`.
  - Guide d'utilisation : `.agents/skills/cloture-sprint/doc/how-to-use.md` sur la branche `sprint1`.
  - Notice technique d'atelier : `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/skill-cloture-sprint.md` sur la branche `sprint1`.
  - Diaporama Marp : `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/presentation-skill-cloture-sprint.md` sur la branche `sprint1`.
  - Journal des commandes : `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/skill-cloture-sprint.command.md` sur la branche `sprint1`.
- **CritÃ¨res de validation :**
  - [ ] Le fichier `SKILL.md` contient un Front Matter YAML valide avec `name: cloture-sprint` et ne dÃ©passe pas 75 lignes.
  - [ ] Le manifeste `SKILL.md` rÃ©fÃ©rence explicitement les 4 missions du dossier `missions/`.
  - [ ] Chaque mission dans `missions/` impose la gÃ©nÃ©ration de documents Markdown sans tableau.
  - [ ] Le guide `doc/how-to-use.md` formalise les commandes d'invocation et les prÃ©requis de chaque rituel.
  - [ ] Le journal `skill-cloture-sprint.command.md` consigne fidÃ¨lement les commandes sans commande Git.
