# Skill : didactique-session-planner

## Présentation
Le skill **`didactique-session-planner`** est l'expert du niveau **Macro (Session & Sprint)**. Il prend en entrée le flux de travail opérationnel réel du projet (`_flux-travail.md` ou livrables de l'équipe) et la session de formation (`_sessions/S[X].md`) pour cadrer un Sprint Scrum rigoureux de 80 heures, élaguer les tâches inutiles et qualifier les Unités d'Apprentissage (`_uas/`).

## Responsabilités Clés
1. **Arbitrage de Véracité :** Le projet réel fait autorité pour les étapes physiques et livrables ; la session fait autorité pour les compétences certifiantes.
2. **Élagage Scrum :** Application des 10 questions de critique didactique pour supprimer le superflu (`CONSERVER`, `SIMPLIFIER`, `FUSIONNER`, `DÉPLACER`, `SUPPRIMER`, `COMPLÉTER`).
3. **Qualification des UAs :** Typologie stricte en `UA-Tâche` (0% théorie) et `UA-Lab` (Pareto 20/80 sans exposition de cuisine interne).
4. **Mise à jour Référentielle :** Actualisation de `_sessions/S[X].md` et production du Plan Artefact d'impact des UAs.

## Prompts Types
- **Aligner une session depuis un flux de travail :**
  > « Exécute didactique-session-planner pour mettre à jour la session S1 à partir de _flux-travail.md, en conservant la durée de 80h et en qualifiant les UAs. »
- **Auditer et élaguer un plan de sprint :**
  > « Utilise didactique-session-planner pour auditer la liste des activités de S2, appliquer la grille des 10 questions d'élagage Scrum et produire la matrice d'impact des UAs. »

## Format de Sortie (Plan Artefact)
Le skill produit un rapport structuré :
1. Synthèse de l'arbitrage (flux réel vs session).
2. Tableau d'élagage des activités (Activité, Décision, Justification).
3. Matrice d'impact des UAs (Action, Code UA, Domaine, Maturité, Titre, Livrable physique).