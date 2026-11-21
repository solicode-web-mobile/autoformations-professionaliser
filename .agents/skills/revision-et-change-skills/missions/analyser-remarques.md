# Mission : Analyse des Remarques du Concepteur (`analyser-remarques.md`)

## 1. Objectif
Analyser les remarques, sélections de lignes et consignes méthodologiques fournies par le concepteur afin d'extraire les modifications précises à apporter sur le fichier cible et d'identifier l'ensemble des skills concernés.

---

## 2. Procédure d'Analyse

1. **Localiser le fichier et les sections cibles :**
   - Identifier le fichier source visé (ex : `flux-travail/sessions/flux-travail-s1.md`).
   - Repérer les sections et étapes ciblées par le retour du concepteur.
   - Lire le contenu actuel des sections concernées.

2. **Qualifier chaque remarque du concepteur :**
   - Décomposer le retour du concepteur en consignes unitaires.
   - Associer chaque consigne à une section ou étape fonctionnelle précise.
   - Identifier la nature de la modification : stack technique (ex: MySQL direct), rôle agile (ex: chaque apprenant PO), conception préalable, titrage, ou livrable.

3. **Identifier les compétences et skills impactés :**
   - Si la remarque touche à la structure des sessions -> cibler `conception-session`.
   - Si la remarque touche aux 25 étapes universelles -> cibler `flux-travail`.
   - Si la remarque touche aux rôles Scrum ou prérequis de gouvernance -> cibler `domaine-scrum`.
   - Si la remarque définit une nouvelle règle transverse -> cibler `.agents/rules/`.

4. **Transmettre les éléments qualifiés à la mission `generer-artefact-revision.md`.**
