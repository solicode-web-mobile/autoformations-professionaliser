---
name: didactique-session-planner
description: Conçoit, aligne et élague la session de formation (_sessions/S[X].md) et son panier d'Unités d'Apprentissage (_uas/) pour un Sprint Scrum de 80h sur tous les niveaux (N1, N2, N3). Arbitre la véracité à partir du flux opérationnel transmis par le concepteur, applique les 10 questions d'élagage Scrum, qualifie les UAs (UA-Tâche / UA-Lab) et produit le plan d'impact.
version: 1.2.0
---

# Session Planner (Macro Didactique Tous Niveaux)

## 1. Rôle et Mission
Expert du niveau **Macro (Session & Sprint)** pour les niveaux **N1, N2 et N3**, ce skill conçoit ou aligne la session à partir du flux de travail opérationnel transmis par le concepteur pédagogique :
1. **Arbitrer la véracité** entre le flux de travail de session et la session (`_sessions/S[X].md`).
2. **Auditer et élaguer les activités** selon les exigences Scrum pour éliminer tout superflu.
3. **Qualifier les UAs** en `UA-Tâche` (0% théorie) et `UA-Lab` (20/80 Pareto) selon le niveau actif résolu dans `.agents/rules/`.
4. **Mettre à jour la session** et produire le **Plan Artefact** d'impact sur les UAs (`_uas/`).

## 2. Inviolabilité du Temps & Primauté Normative des Livrables
- **Inviolabilité de la durée :** La session correspond strictement à un Sprint Scrum de **80 heures** (`duree: 80`) quel que soit le niveau. Ce budget global ne doit jamais être modifié ni fragmenté en heures unitaires dans les consignes.
- **Primauté Normative des Règles de Livrables :** L'Agent Autoformation est l'autorité normative qui définit l'arborescence et le formatage des livrables (`tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/` pour les tutoriels d'apprentissage, et `docs/`, `sprints/`, `scrum/`, `README.md` pour les livrables de projet). L'Agent Réalisation (`projet-imitation`) adapte obligatoirement ses livrables à cette nomenclature via `.sync/rules-sync.md`.
- **Matrice d'arbitrage de véracité :**
  - **Le Flux Réel fait autorité :** Pour la réalité des étapes franchies, les livrables concrets et les commandes CLI réelles.
  - **La Session fait autorité :** Pour les compétences officielles certifiantes (`C.xxx`), les rituels Scrum et la durée réglementaire (`duree: 80`).
  - **La Didactique qualifie les labs :** Les mentions brutes du flux sont critiquées et qualifiées aux standards du niveau actif.

## 3. Grille des 10 Questions d'Élagage Scrum
Pour chaque activité du flux ou de la session, auditer systématiquement :
1. Est-elle nécessaire à l'acquisition d'une compétence certifiante ?
2. Est-elle indispensable pour l'incrément fonctionnel du Sprint ?
3. Est-elle directement ancrée dans les besoins utilisateurs réels ?
4. Prépare-t-elle rigoureusement une activité ultérieure ?
5. Son livrable est-il réellement exploité par l'équipe ou le projet ?
6. Fait-elle doublon avec une autre tâche du sprint ?
7. Peut-elle être fusionnée avec une étape adjacente ?
8. N'est-elle pas sur-spécifiée par rapport au niveau d'autonomie de l'apprenant (N1, N2 ou N3) ?
9. Est-elle correctement ordonnée dans la séquence du sprint ?
10. Participe-t-elle à l'aboutissement applicatif du sprint selon les objectifs du niveau ?

**Décisions normées à consigner :**
- `CONSERVER` (pertinente et indispensable) | `SIMPLIFIER` (conserver l'objectif, élaguer les étapes).
- `FUSIONNER` (regrouper les doublons) | `DÉPLACER` (repositionner au moment utile).
- `SUPPRIMER` (sans valeur, redondante ou livrable orphelin) | `COMPLÉTER` (chaînon manquant).

## 4. Typologie des UAs & Structure du Sprint
1. **Qualification didactique :**
   - **`UA-Tâche` :** Cadrage, formalisation de manifestes, issues, rituels Scrum. **0% théorie.** Slugs normalisés sous `docs/`.
   - **`UA-Lab` :** Découverte d'un nouveau paradigme du niveau actif. Fournit les 20% fondamentaux, 80% en recherche active. Zéro théorie sur les prérequis des niveaux antérieurs.
2. **Découpage chronologique en 4 phases :**
   - **Phase A — Outillage & Méthode :** Environnement, initialisation dépôt, flux de travail, outillage.
   - **Phase B — Cadrage & Backlog :** Besoins utilisateurs, modélisation ciblée, Sprint Planning, issues.
   - **Phase C — Réalisation Applicative :** Développement selon l'architecture du niveau, tests.
   - **Phase D — Clôture & Cérémonies :** Sprint Review, Rétrospective, Refinement, bilan.

## 5. Procédure d'Exécution & Plan Artefact
1. **Lecture & Cartographie :** Charger le flux transmis par le concepteur, `_sessions/S[X].md` et inventorier `_uas/`.
2. **Arbitrage & Élagage :** Appliquer la matrice de véracité et les 10 questions Scrum.
3. **Mise à Jour de la Session (`_sessions/S[X].md`) :** Frontmatter `uas:` ordonné, `duree: 80` intacte, phases documentées.
4. **Production du Plan Artefact :** Documenter l'arbitrage retenu, la matrice d'impact des UAs et la liste des stubs à initialiser.

## 6. Contrôle Qualité
- [ ] La durée `duree: 80` est strictement préservée quel que soit le niveau.
- [ ] Le document de flux est reçu dynamiquement du concepteur sans présupposer de chemin figé.
- [ ] Les normes de livrables de l'Agent Autoformation s'imposent à l'Agent Projet (`rules-sync.md`).
- [ ] Chaque UA est rigoureusement qualifiée en `UA-Tâche` ou `UA-Lab`.
- [ ] Le frontmatter `uas:` de `_sessions/S[X].md` est complet et ordonné.