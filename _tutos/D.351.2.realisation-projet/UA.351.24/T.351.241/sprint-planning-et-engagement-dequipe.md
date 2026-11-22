---
layout: tuto
title: "Planification de sprint et carnet de tÃ¢ches (Sprint 1)"
sous_titre: "BÃ¢tir le Sprint Backlog du premier incrÃ©ment, initialiser l'espace issues/ et contractualiser la Definition of Done"
slug: "sprint-backlog"
slug_domaine: "realisation-projet"
slug_ua: "planification"
permalink: /tutos/sprint-backlog/
tuto_id: "T.351.241"
version: "normal"
ua: "UA.351.24"
maturite: "projet"
type: "tuto-tache"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Objectif OpÃ©rationnel & PrÃ©requis
- **Position dans le flux :** Phase B â€” Analyse Fonctionnelle, Backlog & Planification de Sprint / Ã‰tape 7 â€” Planification de sprint et carnet de tÃ¢ches.
- **Branche Git :** `sprint1`
- **Fichiers modifiÃ©s ou crÃ©Ã©s :** `issues/README.md`, `issues/issues-open.md`, `scrum/sprint-backlog-s1.md`.
- **Objectif :** Animer la planification du Sprint 1 Ã  partir du cas d'usage isolÃ©, initialiser l'espace `issues/` (`issues/README.md` et `issues/issues-open.md`), dÃ©couper l'incrÃ©ment en tÃ¢ches d'ingÃ©nierie et contractualiser la Definition of Done face au Sprint Goal.
- **PrÃ©requis :** Diagramme de cas d'utilisation macro (`UA.311.22`), initiation Ã  la mÃ©thode Agile Scrum (`UA.351.11`) et cadrage du projet (`UA.351.21`).

## 2. DÃ©roulement Pas-Ã -Pas de la TÃ¢che

1. **Ã‰tape 1 â€” SÃ©lection de la User Story Prioritaire :**  
   Retenez la User Story prioritaire dÃ©duite des cas d'utilisation : *Â« En tant qu'apprenant ou recruteur, je veux consulter la page dÃ©taillÃ©e d'un article de blog, afin de dÃ©couvrir la rÃ©alisation d'un laurÃ©at. Â»*

2. **Ã‰tape 2 â€” Initialisation de l'espace de suivi des tÃ¢ches (`issues/`) :**  
   CrÃ©ez le dossier `issues/` pour accueillir le suivi des tÃ¢ches :

```bash
mkdir issues
```

   RÃ©digez le guide `issues/README.md` :

```markdown
# Dossier de Gestion des Issues (`issues/`)

Ce dossier permet de tracer et planifier les tÃ¢ches qui ne sont pas suivies directement par l'application LMS, ou les tÃ¢ches supplÃ©mentaires demandÃ©es par le chef de projet ou proposÃ©es par l'apprenant.

---

## 1. RÃ´le du dossier

- Centraliser les tÃ¢ches techniques de dÃ©veloppement sous format Markdown.
- Les issues crÃ©Ã©es doivent Ãªtre validÃ©es avant d'Ãªtre archivÃ©es.

---

## 2. Contenu attendu dans ce dossier

- `issues-open.md` : Les tÃ¢ches et issues en cours de traitement pour le sprint actif.
- `issues-Ã -valider.md` : Les propositions d'issues en attente de validation.
- `issues-closes.md` : Les tÃ¢ches et issues terminÃ©es et archivÃ©es.
```

3. **Ã‰tape 3 â€” DÃ©coupage en TÃ¢ches d'IngÃ©nierie & Activation dans `issues/issues-open.md` :**  
   DÃ©composez la User Story en micro-tÃ¢ches techniques (Architecture 2 couches & ADR-01, Route et vue Blade d'accueil, ContrÃ´leur et vue de liste, Tranche verticale complÃ¨te avec `ArticleService` CSV et gestion 404). Activez ces tÃ¢ches dans `issues/issues-open.md`.

4. **Ã‰tape 4 â€” Definition of Done (DoD) & Sprint Backlog :**  
   Contractualisez la grille des 7 critÃ¨res bloquants (code versionnÃ© sous Git sur la branche `sprint1`, PSR-12, zÃ©ro warning, tests nominaux et cas 404 validÃ©s, layout responsive). Renseignez le document `scrum/sprint-backlog-s1.md` et engagez l'Ã©quipe sur le Sprint Goal.

5. **Ã‰tape 5 â€” Journalisation des commandes exÃ©cutÃ©es :**  
   Dans `tutoriels/realisation-projet/planification/sprint-backlog/sprint-backlog.command.md`, consignez la commande :

```bash
mkdir issues
```

## 3. Livrables & CritÃ¨res de RÃ©ussite
- **Livrables attendus :**
  - Guide du dossier : `issues/README.md`.
  - Carnet de tÃ¢ches activÃ©es : `issues/issues-open.md`.
  - Sprint Backlog S1 : `scrum/sprint-backlog-s1.md` sur la branche `sprint1`.
  - Journal des commandes : `tutoriels/realisation-projet/planification/sprint-backlog/sprint-backlog.command.md`.
- **CritÃ¨res de validation :**
  - [ ] Le dossier `issues/` est crÃ©Ã© avec son guide `issues/README.md`.
  - [ ] Les micro-tÃ¢ches de rÃ©alisation de la Story sont recensÃ©es dans `issues/issues-open.md`.
  - [ ] Les 7 critÃ¨res de la DoD sont formellement contractualisÃ©s face au Sprint Goal.
  - [ ] Le document `scrum/sprint-backlog-s1.md` est finalisÃ© et versionnÃ© sur la branche `sprint1`.
  - [ ] Le journal `sprint-backlog.command.md` consigne la commande `mkdir issues`.
