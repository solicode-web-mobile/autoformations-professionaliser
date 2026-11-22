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

## 2. Temporalité Indicative & Primauté Normative des Livrables
- **Durée indicative :** La durée temporelle d'une session (standard indicatif : 80 heures / 10 jours ouvrés pour un Sprint Scrum) est fournie à **titre purement indicatif** pour les formateurs et les concepteurs pédagogiques. Elle sert de repère macro pour rythmer les apprentissages sans être un carcan rigide, et ne doit jamais être affichée ni fragmentée en durées unitaires dans les consignes destinées aux apprenants.
- **Primauté Normative des Règles de Livrables :** L'Agent Autoformation est l'autorité normative qui définit l'arborescence et le formatage des livrables (`tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/` pour les tutoriels d'apprentissage, et `docs/`, `sprints/`, `scrum/`, `README.md` pour les livrables de projet). L'Agent Réalisation (`projet-imitation`) adapte obligatoirement ses livrables à cette nomenclature via `.sync/rules-sync.md`.
- **Matrice d'arbitrage de véracité :**
  - **Le Flux Réel fait autorité :** Pour la réalité des étapes franchies, la décomposition des blocs d'apprentissage, les livrables concrets et les commandes CLI réelles.
  - **La Session fait autorité :** Pour les compétences officielles certifiantes (`C.xxx`) et les rituels Scrum.
  - **La Didactique qualifie les UAs :** Les blocs bruts du flux sont critiqués et qualifiés selon la typologie et la maturité (`UA-Lab` / `tuto-atelier` vs `UA-Tâche` / `tuto-tache`).

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

## 4. Typologie des UAs & Respect de la Décomposition du Flux Opérationnel
1. **Qualification didactique :**
   - **`UA-Tâche` (`maturite: "projet"`, `type: "tuto-tache"`) :** Action opérationnelle, cadrage, initialisation outillée, rituels Scrum transversaux ou récurrents sans UA d'apprentissage. **0% théorie.** Livrables situés aux emplacements racine (`docs/`, `sprints/`, `scrum/`, `src/`).
   - **`UA-Lab` (`maturite: "lab"` ou `"ua-lab"`, `type: "tuto-atelier"`) :** Découverte pratique guidée d'un nouveau paradigme. Intègre directement à la suite des ateliers les tâches d'application projet (`tuto-tache`) ancrées sur le sujet d'imitation.
2. **Respect de la décomposition du flux opérationnel :**
   - La session ne s'organise pas en phases abstraites artificielles qui masqueraient ou regrouperaient arbitrairement les UAs.
   - **Chaque bloc opérationnel du flux transmis par l'équipe (`flux-travail-s[X].md`) fait directement l'objet d'une Unité d'Apprentissage dédiée (`UA-Lab` ou `UA-Tâche`)**.
   - Par exemple, dans un flux comportant des blocs successifs intitulés *UA-Lab — Démarche Agile Scrum*, *UA-Lab — Design Thinking : Démarche & Empathie sur Todo List*, *UA-Lab — Design Thinking : Parcours & Prototypage*, *UA-Tâche — Application Projet : Cadrage & Backlog Initial*, et *UA-Tâche — Incrément Maquette & Clôture S0*, **chacun de ces blocs constitue directement une Unité d'Apprentissage dédiée de la session** avec ses tutoriels associés.
   - L'enchaînement de la session dans `_sessions/S[X].md` reflète directement cette séquence ordonnée d'UAs.

## 5. Procédure d'Exécution & Plan Artefact
1. **Lecture & Cartographie :** Charger le flux transmis par le concepteur, `_sessions/S[X].md` et inventorier `_uas/`.
2. **Arbitrage & Élagage :** Appliquer la matrice de véracité et les 10 questions Scrum.
3. **Mise à Jour de la Session (`_sessions/S[X].md`) :** Frontmatter `uas:` ordonné reflétant directement la séquence des UAs du flux, `duree: 80` (indicatif), description centrée sur l'incrément.
4. **Production du Plan Artefact :** Documenter l'arbitrage retenu, la matrice d'impact des UAs et la liste des stubs à initialiser.

## 6. Contrôle Qualité
- [ ] La durée (ex: `duree: 80`) est fournie à titre indicatif sans être affichée aux apprenants.
- [ ] Le document de flux est reçu dynamiquement du concepteur sans présupposer de chemin figé.
- [ ] Les normes de livrables de l'Agent Autoformation s'imposent à l'Agent Projet (`rules-sync.md`).
- [ ] Chaque bloc opérationnel du flux constitue directement une UA qualifiée (`UA-Lab` ou `UA-Tâche`).
- [ ] Le frontmatter `uas:` de `_sessions/S[X].md` est complet et ordonné.