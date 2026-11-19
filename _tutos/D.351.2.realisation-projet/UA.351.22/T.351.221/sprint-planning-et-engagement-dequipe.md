---
layout: tuto
title: "Planification de sprint et carnet de tâches (Sprint 1)"
sous_titre: "Bâtir le Sprint Backlog du premier incrément, initialiser l'espace issues/ et contractualiser la Definition of Done"
slug: "sprint-backlog"
slug_domaine: "realisation-projet"
slug_ua: "planification"
permalink: /tutos/sprint-backlog/
tuto_id: "T.351.221"
version: "normal"
ua: "UA.351.22"
maturite: "UA-Tâche"
nav_order: 1
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Objectif Opérationnel & Prérequis
- **Position dans le flux :** Phase B — Analyse Fonctionnelle, Backlog & Planification de Sprint / Étape 7 — Planification de sprint et carnet de tâches.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `issues/README.md`, `issues/issues-open.md`, `scrum/sprint-backlog-s1.md`.
- **Objectif :** Animer la planification du Sprint 1 à partir du cas d'usage isolé, initialiser l'espace `issues/` (`issues/README.md` et `issues/issues-open.md`), découper l'incrément en tâches d'ingénierie et contractualiser la Definition of Done face au Sprint Goal.
- **Prérequis :** Diagramme de cas d'utilisation macro (`UA.311.22`), initiation à la méthode Agile Scrum (`UA.351.11`) et cadrage du projet (`UA.351.21`).

## 2. Déroulement Pas-à-Pas de la Tâche

1. **Étape 1 — Sélection de la User Story Prioritaire :**  
   Retenez la User Story prioritaire déduite des cas d'utilisation : *« En tant qu'apprenant ou recruteur, je veux consulter la page détaillée d'un article de blog, afin de découvrir la réalisation d'un lauréat. »*

2. **Étape 2 — Initialisation de l'espace de suivi des tâches (`issues/`) :**  
   Créez le dossier `issues/` pour accueillir le suivi des tâches :

```bash
mkdir issues
```

   Rédigez le guide `issues/README.md` :

```markdown
# Dossier de Gestion des Issues (`issues/`)

Ce dossier permet de tracer et planifier les tâches qui ne sont pas suivies directement par l'application LMS, ou les tâches supplémentaires demandées par le chef de projet ou proposées par l'apprenant.

---

## 1. Rôle du dossier

- Centraliser les tâches techniques de développement sous format Markdown.
- Les issues créées doivent être validées avant d'être archivées.

---

## 2. Contenu attendu dans ce dossier

- `issues-open.md` : Les tâches et issues en cours de traitement pour le sprint actif.
- `issues-à-valider.md` : Les propositions d'issues en attente de validation.
- `issues-closes.md` : Les tâches et issues terminées et archivées.
```

3. **Étape 3 — Découpage en Tâches d'Ingénierie & Activation dans `issues/issues-open.md` :**  
   Décomposez la User Story en micro-tâches techniques (Architecture 2 couches & ADR-01, Route et vue Blade d'accueil, Contrôleur et vue de liste, Tranche verticale complète avec `ArticleService` CSV et gestion 404). Activez ces tâches dans `issues/issues-open.md`.

4. **Étape 4 — Definition of Done (DoD) & Sprint Backlog :**  
   Contractualisez la grille des 7 critères bloquants (code versionné sous Git sur la branche `sprint1`, PSR-12, zéro warning, tests nominaux et cas 404 validés, layout responsive). Renseignez le document `scrum/sprint-backlog-s1.md` et engagez l'équipe sur le Sprint Goal.

5. **Étape 5 — Journalisation des commandes exécutées :**  
   Dans `tutoriels/realisation-projet/planification/sprint-backlog/sprint-backlog.command.md`, consignez la commande :

```bash
mkdir issues
```

## 3. Livrables & Critères de Réussite
- **Livrables attendus :**
  - Guide du dossier : `issues/README.md`.
  - Carnet de tâches activées : `issues/issues-open.md`.
  - Sprint Backlog S1 : `scrum/sprint-backlog-s1.md` sur la branche `sprint1`.
  - Journal des commandes : `tutoriels/realisation-projet/planification/sprint-backlog/sprint-backlog.command.md`.
- **Critères de validation :**
  - [ ] Le dossier `issues/` est créé avec son guide `issues/README.md`.
  - [ ] Les micro-tâches de réalisation de la Story sont recensées dans `issues/issues-open.md`.
  - [ ] Les 7 critères de la DoD sont formellement contractualisés face au Sprint Goal.
  - [ ] Le document `scrum/sprint-backlog-s1.md` est finalisé et versionné sur la branche `sprint1`.
  - [ ] Le journal `sprint-backlog.command.md` consigne la commande `mkdir issues`.
