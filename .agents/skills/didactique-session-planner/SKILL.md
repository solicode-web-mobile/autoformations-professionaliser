---
name: didactique-session-planner
description: Conçoit, aligne et élague la session de formation (_sessions/S[X].md) et son panier d'Unités d'Apprentissage (_uas/) pour un Sprint Scrum de 80h. Arbitre la véracité entre flux réel (_flux-travail.md) et référentiel, applique les 10 questions d'élagage Scrum, qualifie les UAs (UA-Tâche / UA-Lab) et produit le plan d'impact.
version: 1.0.0
---

# Session Planner (Macro Didactique)

## 1. Rôle et Mission
Expert du niveau **Macro (Session & Sprint)**, ce skill fusionne l'alignement avec le flux réel de projet et le cadrage Scrum :
1. **Arbitrer la véracité** entre le flux opérationnel réel (`_flux-travail.md`) et la session (`_sessions/S[X].md`).
2. **Auditer et élaguer les activités** selon les exigences Scrum pour éliminer le superflu.
3. **Qualifier les UAs** en `UA-Tâche` (0% théorie) et `UA-Lab` (20/80 Pareto).
4. **Mettre à jour la session** et produire le **Plan Artefact** d'impact sur les UAs (`_uas/`).

## 2. Inviolabilité du Budget Temps & Matrice de Véracité
- **Inviolabilité de la durée :** La session correspond strictement à un Sprint Scrum de **80 heures** (`duree: 80`). Ce budget global ne doit jamais être modifié ni fragmenté en heures unitaires dans les consignes.
- **Matrice d'arbitrage de véracité :**
  - **Le Flux Réel fait autorité :** Pour la réalité des étapes franchies (`git init`, CLI `gh`, Artisan), les arborescences physiques (`missions/`, `flux-travail/`, `issues/`) et les livrables concrets.
  - **La Session fait autorité :** Pour les compétences officielles certifiantes (`C.311`..`C.351`), les rituels Scrum (Planning, Review, Rétro) et la durée réglementaire (`duree: 80`).
  - **La Didactique qualifie les labs :** Les mentions brutes du flux (`lab-github`, etc.) sont critiquées et qualifiées aux standards N3.

## 3. Grille des 10 Questions d'Élagage Scrum
Pour chaque activité du flux ou de la session, auditer systématiquement :
1. Est-elle nécessaire à l'acquisition d'une compétence certifiante ?
2. Est-elle indispensable pour l'incrément fonctionnel du Sprint ?
3. Est-elle directement ancrée dans les besoins utilisateurs réels ?
4. Prépare-t-elle rigoureusement une activité ultérieure ?
5. Son livrable est-il réellement exploité par l'équipe ou le projet ?
6. Fait-elle doublon avec une autre tâche du sprint ?
7. Peut-elle être fusionnée avec une étape adjacente ?
8. N'est-elle pas sur-spécifiée par rapport au niveau d'autonomie N3 ?
9. Est-elle correctement ordonnée dans la séquence du sprint ?
10. Participe-t-elle à la construction de l'Agent IA du sprint ?

**Décisions normées à consigner :**
- `CONSERVER` (pertinente et indispensable) | `SIMPLIFIER` (conserver l'objectif, élaguer les étapes).
- `FUSIONNER` (regrouper les doublons) | `DÉPLACER` (repositionner au moment utile).
- `SUPPRIMER` (sans valeur, redondante ou livrable orphelin) | `COMPLÉTER` (chaînon manquant).

## 4. Typologie des UAs & Structure du Sprint
1. **Qualification didactique :**
   - **`UA-Tâche` :** Cadrage, formalisation de manifestes, issues, rituels Scrum. **0% théorie.**
   - **`UA-Lab` :** Nouveau concept N3 (MVC Laravel, IoC, Prompt RIO). Fournit les 20% fondamentaux, 80% en recherche active. Zéro théorie sur les prérequis N1/N2.
2. **Découpage chronologique en 4 phases :**
   - **Phase A — Outillage & Méthode :** Environnement, initialisation dépôt, flux de travail, Agent IA.
   - **Phase B — Cadrage & Backlog :** User stories, modélisation ciblée, Sprint Planning, issues.
   - **Phase C — Réalisation Applicative :** Développement 2-couches (back/front), tests, TDD.
   - **Phase D — Clôture & Cérémonies :** Sprint Review, Rétrospective, Refinement, bilan.

## 5. Procédure d'Exécution & Plan Artefact
1. **Lecture & Cartographie :** Charger `_flux-travail.md`, `_sessions/S[X].md` et inventorier `_uas/`.
2. **Arbitrage & Élagage :** Appliquer la matrice de véracité et les 10 questions Scrum.
3. **Mise à Jour de la Session (`_sessions/S[X].md`) :** Frontmatter `uas:` ordonné, `duree: 80` intacte, phases A-D documentées avec livrables physiques.
4. **Production du Plan Artefact :** Générer le document de synthèse détaillant l'arbitrage retenu, la matrice d'impact des UAs (`_uas/` créées, adaptées, supprimées avec maturité `UA-Tâche` ou `UA-Lab`) et la liste des stubs à initialiser.

## 6. Contrôle Qualité
- [ ] La durée `duree: 80` est strictement préservée.
- [ ] Le flux réel dicte les étapes concrètes et les livrables physiques (`missions/`, `issues/`).
- [ ] Toutes les activités inutiles ou redondantes ont été élaguées avec justification.
- [ ] Chaque UA est rigoureusement qualifiée en `UA-Tâche` ou `UA-Lab`.
- [ ] Le frontmatter `uas:` de `_sessions/S[X].md` est complet et ordonné.