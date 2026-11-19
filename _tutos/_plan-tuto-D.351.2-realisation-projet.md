# Plan des Tutoriels : D.351.2 — Réalisation de Projet & Rituels Agiles

> **Domaine :** `D.351.2` | **Compétence :** `C.351` — Piloter un projet avec Scrum et gouverner les cérémonies | **Session :** S01  
> **Niveau de Maturité :** UA-Tâche (Niveau 0 — Cadrage, cérémonies et phases opérationnelles de projet)  
> **Branche Git de Travail :** `sprint1`  
> **Projet Référence :** Projet d'imitation (*Blog des Lauréats*)  
> **Référentiels Liés :** [`../../3.sprints/flux-travail-n3.md`](../../3.sprints/flux-travail-n3.md) | [`../../3.sprints/stack-technique-n3.md`](../../3.sprints/stack-technique-n3.md)

---

## 1. Description des Unités d'Apprentissage du Domaine

### UA.351.21 — Cadrage du périmètre du projet (Sprint 1)

- **Code :** `UA.351.21`
- **Maturité :** `UA-tâche` (Cadrage de périmètre de projet)
- **Ordre en Session :** Étape 04
- **Positionnement Flux de Travail :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 4 — Cadrage du Projet
- **Briques Stack Technique :** Cadrage agile, Matrice de périmètre, Vision produit
- **Compétence :** `C.351` — Piloter un projet avec Scrum et gouverner les cérémonies
- **Domaine :** `D.351.2` — Réalisation de projet et rituels agiles
- **Durée estimée :** 2 heures
- **Objectif :** Définir et formaliser le périmètre d'intervention du projet pour le Sprint 1 en contractualisant les frontières fonctionnelles (In-Scope / Out-of-Scope) et la feuille de route dans sprints/sprints.md.
- **Description :** Poser les frontières opérationnelles du projet sur le Blog des Lauréats. L'apprenant explicite la vision produit, identifie les acteurs clés (Lauréat et Apprenant/Visiteur), délimite les exigences In-Scope vs Out-of-Scope du premier sprint et contractualise le suivi dans sprints/sprints.md et sprints/README.md.
- **Notions Clés Utilisées dans le Sprint :**
  - Vision produit et personas cibles : Lauréat et Apprenant/Visiteur.
  - Délimitation du périmètre In-Scope (consultation publique sous Laravel) vs Out-of-Scope (zéro authentification, zéro MySQL).
  - Gouvernance de sprint et source unique de vérité (`sprints/sprints.md`).
- **Livrable :** Dossier `sprints/` (`sprints/sprints.md`, `sprints/README.md`) et journal des commandes `tutoriels/realisation-projet/cadrage/perimetre-produit/perimetre-produit.command.md` sur la branche `sprint1`.
- **Travail à Faire :** Rédiger `sprints/README.md`, formaliser `sprints/sprints.md` en déclarant le Sprint 1 en statut Actif pour le Projet d'imitation (*Blog des Lauréats*) et consigner les commandes.

---

### UA.351.22 — Planification de sprint et carnet de tâches (Sprint 1)

- **Code :** `UA.351.22`
- **Maturité :** `UA-tâche` (Planification Scrum de sprint)
- **Ordre en Session :** Étape 07
- **Positionnement Flux de Travail :** Phase B — Analyse, Conception & Planification / Étape 2.4 — Planification & Sprint Backlog
- **Briques Stack Technique :** Sprint Backlog, Décomposition en tâches, Definition of Done, dossier issues/
- **Compétence :** `C.351` — Piloter un projet avec Scrum et gouverner les cérémonies
- **Domaine :** `D.351.2` — Réalisation de projet et rituels agiles
- **Durée estimée :** 4 heures
- **Objectif :** Bâtir le Sprint Backlog du premier incrément à partir du cas d'usage de consultation, initialiser l'espace de suivi issues/ (README.md et issues-open.md) et contractualiser la Definition of Done en 7 critères bloquants face au Sprint Goal.
- **Description :** Cérémonie opérationnelle de planification du sprint. L'équipe sélectionne la User Story prioritaire déduite des cas d'utilisation, la découpe en tâches d'ingénierie concrètes, active les tâches dans issues/issues-open.md, s'engage sur le Sprint Goal et conçoit le prompt réutilisable `prompt-sprint-planning`.
- **Notions Clés Utilisées dans le Sprint :**
  - Rituel du Sprint Planning en 2 parties (Quoi et Comment).
  - Organisation de l'espace de suivi des tâches `issues/` (`README.md`, `issues-open.md`, `issues-à-valider.md`, `issues-closes.md`).
  - Décomposition de la User Story en tâches d'ingénierie concrètes.
  - Contractualisation de la Definition of Done (DoD) en 7 critères bloquants face au Sprint Goal.
- **Livrables :** Espace de suivi `issues/` (`issues/README.md`, `issues/issues-open.md`), Sprint Backlog S1 (`scrum/sprint-backlog-s1.md`) et prompt d'ingénierie (`livrables/ia/prompts/prompt-sprint-planning.prompt.md`) sur la branche `sprint1`.
- **Travail à Faire :** Animer la planification du sprint, initialiser `issues/README.md`, activer les tâches dans `issues/issues-open.md` et concevoir le prompt `prompt-sprint-planning`.

---

### UA.351.23 — Clôture de sprint, démonstration et rétrospective (Sprint 1)

- **Code :** `UA.351.23`
- **Maturité :** `UA-tâche` (Cérémonies de clôture et amélioration continue)
- **Ordre en Session :** Étape 12
- **Positionnement Flux de Travail :** Phase D — Clôture de Sprint, Rétrospective & Bilan
- **Briques Stack Technique :** Sprint Review, Sprint Retrospective, Backlog Refinement, Bilan de compétences
- **Compétence :** `C.351` — Piloter un projet avec Scrum et gouverner les cérémonies
- **Domaine :** `D.351.2` — Réalisation de projet et rituels agiles
- **Durée estimée :** 4 heures
- **Objectif :** Valider l'incrément déployable en démonstration live face aux critères de la DoD, animer une rétrospective réflexive identifiant la dette d'empathie, raffiner le carnet produit et concevoir le skill modulaire d'automatisation de clôture de sprint.
- **Description :** Clôture rigoureuse et amélioration continue du sprint. L'équipe démontre l'incrément fonctionnel, conduit la rétrospective réflexive révélant le manque de Design Thinking (justifiant le Sprint S02), affine le Product Backlog, clôture le bilan individuel et produit le skill modulaire cloture-sprint orchestrant les 4 missions automatisant ces rituels récurrents.
- **Notions Clés Utilisées dans le Sprint :**
  - Démonstration fonctionnelle live de l'incrément déployable (Sprint Review).
  - Validation critère par critère de la Definition of Done (DoD).
  - Rétrospective réflexive et détection de la dette d'empathie utilisateur.
  - Backlog Refinement pour le sprint suivant.
  - Architecture modulaire d'un Skill Agent IA (orchestrateur SKILL.md et missions spécialisées).
- **Livrables :** Revue de sprint (`scrum/revue-s1.md`), rétrospective (`scrum/retrospective-s1.md`), backlog affiné (`scrum/product-backlog.md`), bilan individuel (`scrum/bilan-s1.md`) et skill modulaire de clôture (`.agents/skills/cloture-sprint/` et documentation `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/`) sur la branche `sprint1`.
- **Travail à Faire :** Réaliser les rituels de clôture et concevoir le skill modulaire de clôture de sprint orchestrant les 4 missions.

---

## 2. Plan des Tutoriels : UA.351.21

### T.351.211 — Cadrage du périmètre du projet (Sprint 1)

- **Code :** `T.351.211`
- **Maturité :** `UA-tâche` (Tutoriel opérationnel de cadrage)
- **Unité d'Apprentissage parente :** `UA.351.21`
- **Titre Canonique :** Cadrage du périmètre du projet (Sprint 1)
- **Position dans le Flux :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 4 — Cadrage du Projet.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `sprints/sprints.md`, `sprints/README.md`, `tutoriels/realisation-projet/cadrage/perimetre-produit/perimetre-produit.command.md`
- **Objectif Opérationnel :** Contractualiser le cadrage du périmètre fonctionnel du Projet d'imitation (*Blog des Lauréats*) pour le Sprint 1.
- **Prérequis :** Prise de connaissance du sujet d'imitation et de la méthode Agile Scrum (`UA.351.11`).
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Formaliser la vision du projet : plateforme de publication d'articles techniques pour valoriser les lauréats.
  2. *Étape 2 :* Délimiter le périmètre strict du Sprint 1 (Ce qui est IN : consultation publique d'un article, lecture CSV, 404 ; Ce qui est OUT : authentification, création d'article, base de données relationnelle).
  3. *Étape 3 :* Identifier les deux acteurs clés (Lauréat et Apprenant/Visiteur public) et consigner l'ensemble dans `sprints/sprints.md` et `sprints/README.md`.
- **Critère de Réussite :** Le fichier `sprints/sprints.md` déclare le Sprint 1 en statut Actif sur la branche `sprint1`.

---

## 3. Plan des Tutoriels : UA.351.22

### T.351.221 — Planification de sprint et carnet de tâches

- **Code :** `T.351.221`
- **Maturité :** `UA-tâche` (Tutoriel opérationnel de planification)
- **Unité d'Apprentissage parente :** `UA.351.22`
- **Titre Canonique :** Planification de sprint et carnet de tâches
- **Position dans le Flux :** Phase B — Analyse, Conception & Planification / Étape 2.4 — Planification & Carnet de tâches.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `issues/README.md`, `issues/issues-open.md`, `scrum/sprint-backlog-s1.md`
- **Objectif Opérationnel :** Animer la planification du Sprint 1, initialiser l'espace `issues/`, découper l'incrément en tâches d'ingénierie et contractualiser la Definition of Done.
- **Prérequis :** Diagramme de cas d'utilisation macro (`UA.311.22`) et initiation Scrum (`UA.351.11`).
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Sélectionner la User Story prioritaire issue du cas d'utilisation : *« Consultation détaillée d'un article de blog »*.
  2. *Étape 2 :* Initialiser le dossier `issues/` et rédiger le guide `issues/README.md`.
  3. *Étape 3 :* Découper la Story en tâches d'ingénierie élémentaires et les activer dans `issues/issues-open.md`.
  4. *Étape 4 :* Formaliser la grille Definition of Done (DoD) en 7 critères bloquants face au Sprint Goal.
- **Critère de Réussite :** Le dossier `issues/` est initialisé avec `issues-open.md` activé et le Sprint Backlog est contractualisé sur la branche `sprint1`.

---

### T.351.222 — Création du prompt-sprint-planning

- **Code :** `T.351.222`
- **Maturité :** `UA-tâche` (Tutoriel d'automatisation IA)
- **Unité d'Apprentissage parente :** `UA.351.22`
- **Titre Canonique :** Création du prompt-sprint-planning
- **Position dans le Flux :** Phase B — Analyse, Conception & Planification / Étape 2.3 — Automatisation de la Planification.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-sprint-planning.prompt.md`
- **Objectif Opérationnel :** Concevoir le prompt d'ingénierie réutilisable permettant à un agent IA de générer le Sprint Backlog découpé à partir d'une sélection de User Stories.
- **Missions Concrètes Réalisées par le Prompt :**
  1. Extraire les User Stories sélectionnées pour le sprint depuis le Product Backlog.
  2. Décomposer chaque User Story en tâches techniques concrètes selon la stack du projet.
  3. Rédiger le document `sprint-backlog.md` avec matrice de suivi et checklist DoD.
- **Cahier des Charges du Prompt (Méthode RIO) :**
  - **Rôle :** Scrum Master & Coach Agile senior expert en décomposition de tâches techniques.
  - **Instruction :** Prendre en entrée les User Stories retenues et produire la décomposition technique détaillée avec critères DoD.
  - **Output :** Fichier Markdown structuré directement intégrable dans `scrum/sprint-backlog-[ID].md`.
  - **Contraintes Négatives :** Pas de tâches vagues ou génériques ; chaque tâche doit spécifier les fichiers cibles impactés.
- **Critère de Réussite :** Le fichier `livrables/ia/prompts/prompt-sprint-planning.prompt.md` est testé et versionné sur la branche `sprint1`.

---

## 4. Plan des Tutoriels : UA.351.23

### T.351.231 — Sprint Review et démonstration live

- **Code :** `T.351.231`
- **Maturité :** `UA-tâche` (Tutoriel opérationnel de démonstration)
- **Unité d'Apprentissage parente :** `UA.351.23`
- **Titre Canonique :** Sprint Review et démonstration live
- **Position dans le Flux :** Phase D — Clôture de Sprint, Rétrospective & Bilan / Étape 5.1 — Démonstration Live.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `scrum/revue-s1.md`
- **Objectif Opérationnel :** Conduire la démonstration live de l'incrément face au formateur Product Owner et valider critère par critère la DoD.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Préparer l'environnement de démonstration sur le serveur local (`php artisan serve`).
  2. *Étape 2 :* Jouer les scénarios nominaux (consultation d'articles valides) et d'erreur (URL inexistante $\to$ page 404).
  3. *Étape 3 :* Renseigner la grille de validation DoD dans `scrum/revue-s1.md`.
- **Critère de Réussite :** Le procès-verbal `scrum/revue-s1.md` atteste de la validation des 7 critères de la DoD sur la branche `sprint1`.

---

### T.351.232 — Sprint Retrospective et dette d'empathie

- **Code :** `T.351.232`
- **Maturité :** `UA-tâche` (Tutoriel opérationnel de rétrospective)
- **Unité d'Apprentissage parente :** `UA.351.23`
- **Titre Canonique :** Sprint Retrospective et dette d'empathie
- **Position dans le Flux :** Phase D — Clôture de Sprint, Rétrospective & Bilan / Étape 5.2 — Analyse Réflexive.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `scrum/retrospective-s1.md`
- **Objectif Opérationnel :** Animer la rétrospective réflexive d'équipe et acter formellement la dette d'empathie utilisateur justifiant l'introduction du Design Thinking au Sprint 2.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Collecter les observations de l'équipe (points forts techniques, difficultés rencontrées).
  2. *Étape 2 :* Analyser la question réflexive : l'écran codé répond-il aux besoins réels d'utilisateurs testés ?
  3. *Étape 3 :* Formaliser le constat de dette méthodologique dans `scrum/retrospective-s1.md`.
- **Critère de Réussite :** Le compte-rendu `scrum/retrospective-s1.md` est validé et acte la transition pédagogique vers le Sprint 2.

---

### T.351.233 — Raffinement du Product Backlog

- **Code :** `T.351.233`
- **Maturité :** `UA-tâche` (Tutoriel opérationnel de raffinement)
- **Unité d'Apprentissage parente :** `UA.351.23`
- **Titre Canonique :** Raffinement du Product Backlog
- **Position dans le Flux :** Phase D — Clôture de Sprint, Rétrospective & Bilan / Étape 5.3 — Backlog Grooming.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `scrum/product-backlog.md`
- **Objectif Opérationnel :** Actualiser et réordonner le Product Backlog à la lumière des retours de revue pour préparer le Sprint 2.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Marquer la User Story US-01 comme terminée (`Terminé`).
  2. *Étape 2 :* Intégrer les nouvelles exigences et réordonner les User Stories de la session suivante (Personas, création d'article).
  3. *Étape 3 :* Mettre à jour `scrum/product-backlog.md`.
- **Critère de Réussite :** Le fichier `scrum/product-backlog.md` est actualisé et prêt pour la planification du Sprint 2.

---

### T.351.234 — Débriefing de session et bilan de progression

- **Code :** `T.351.234`
- **Maturité :** `UA-tâche` (Tutoriel opérationnel d'auto-évaluation)
- **Unité d'Apprentissage parente :** `UA.351.23`
- **Titre Canonique :** Débriefing de session et bilan de progression
- **Position dans le Flux :** Phase D — Clôture de Sprint, Rétrospective & Bilan / Étape 5.4 — Débriefing Individuel.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `scrum/bilan-s1.md`
- **Objectif Opérationnel :** Dresser le bilan individuel d'acquisition des compétences sur l'ensemble de la Session S01.
- **Déroulement Pas-à-Pas :**
  1. *Étape 1 :* Évaluer son niveau d'acquisition sur les 5 compétences du sprint ($C.311, C.312, C.321, C.325, C.351$).
  2. *Étape 2 :* Analyser les résultats de l'épreuve de Live Coding de 40 minutes et cibler les axes de consolidation.
  3. *Étape 3 :* Renseigner la fiche de débriefing individuel dans `scrum/bilan-s1.md`.
- **Critère de Réussite :** Le bilan `scrum/bilan-s1.md` est rempli et versé au suivi de compétences de l'apprenant.

---

### T.351.235 — Création du skill de clôture de sprint

- **Code :** `T.351.235`
- **Maturité :** `UA-tâche` (Tutoriel d'outillage IA & architecture de skill)
- **Unité d'Apprentissage parente :** `UA.351.23`
- **Titre Canonique :** Création du skill de clôture de sprint
- **Position dans le Flux :** Phase D — Clôture de Sprint, Rétrospective & Bilan / Étape 5.5 — Automatisation des Rituels de Clôture.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :**
  - `.agents/skills/cloture-sprint/SKILL.md`
  - `.agents/skills/cloture-sprint/missions/sprint-review.md`
  - `.agents/skills/cloture-sprint/missions/sprint-retrospective.md`
  - `.agents/skills/cloture-sprint/missions/backlog-refinement.md`
  - `.agents/skills/cloture-sprint/missions/debriefing-session.md`
  - `.agents/skills/cloture-sprint/doc/how-to-use.md`
  - `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/skill-cloture-sprint.md`
  - `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/presentation-skill-cloture-sprint.md`
  - `tutoriels/realisation-projet/cloture-sprint/skill-cloture-sprint/skill-cloture-sprint.command.md`
- **Objectif Opérationnel :** Concevoir le skill modulaire réutilisable `cloture-sprint` orchestrant les 4 missions d'ingénierie qui automatisent la production des livrables de clôture de sprint.
- **Missions Orchestrées par le Skill :**
  1. **`missions/sprint-review.md` :** Générer le procès-verbal de démonstration et l'audit binaire critère par critère de la DoD face au Sprint Goal.
  2. **`missions/sprint-retrospective.md` :** Guider l'animation de la rétrospective agile, structurer les forces et axes d'amélioration, et acter le constat de dette d'empathie utilisateur vers S2.
  3. **`missions/backlog-refinement.md` :** Archiver les tâches livrées dans `issues/issues-closes.md` et réordonner/estimer les User Stories du Product Backlog pour le sprint suivant.
  4. **`missions/debriefing-session.md` :** Générer le canevas de débriefing individuel réflexif sur les 5 compétences du sprint ($C.311, C.312, C.321, C.325, C.351$) et analyser le Live Coding 40 min.
- **Critère de Réussite :** Le skill `.agents/skills/cloture-sprint/` est opérationnel, documenté et testé avec la commande `/cloture-sprint` sur la branche `sprint1`.