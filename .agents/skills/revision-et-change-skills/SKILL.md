---
name: revision-et-change-skills
description: >-
  Analyse les remarques et sélections du concepteur sur les sessions ou plans,
  produit un artefact interactif de révision (document révisé tel quel et skills impactés),
  puis applique les ajustements validés sur les documents et les compétences.
version: 1.0.0
---

# Skill Révision et Changement de Skills : /revision-et-change-skills

## 1. Mission
Formaliser et automatiser la boucle de co-conception réactive avec le concepteur :
1. Analyser les remarques, sélections et consignes méthodologiques du concepteur.
2. Générer un artéfact interactif de révision (`plan-revision-*.md` avec `RequestFeedback: true`) affichant le document révisé **tel quel** (sans pollution de numéros de lignes du type "Lignes 1 à 7") et la matrice des skills à adapter (avec rappel du rôle de chaque skill en 2 phrases max).
3. Après validation par le concepteur, appliquer les modifications sur le document cible et synchroniser les règles et comportements des skills associés.

## 2. Déclenchement
- **Quand l'activer** :
  - Sélection de lignes ou remarques critiques formulées par le concepteur sur un fichier de session (`flux-travail-s{N}.md`) ou un document d'ingénierie.
  - Demande explicite de modification de session combinée avec l'adaptation de l'écosystème de skills.
  - Commande `/revision-et-change-skills` ou consigne "fixe le plan et les skills".
- **Quand NE PAS l'activer** :
  - Création initiale d'une session à partir de zéro -> utiliser `conception-session`.
  - Évolution du référentiel universel d'ingénierie -> utiliser `flux-travail`.
  - Cérémonies de fin de sprint -> utiliser `cloture-sprint`.

## 3. Missions disponibles
L'agent identifie le travail demandé par le concepteur et exécute la mission correspondante située dans `missions/` :
- missions/analyser-remarques.md : Extrait les remarques du concepteur, identifie les lignes cibles et cartographie les compétences impactées.
- missions/generer-artefact-revision.md : Rédige l'artéfact interactif de révision avec cartographie ligne par ligne et matrice des skills.
- missions/synchroniser-skills.md : Exécute les modifications sur le document cible et répercute les ajustements sur les skills et règles.

## 4. Règles Obligatoires
- Format d'artéfact interactif systématique : `RequestFeedback: true` et `UserFacing: true`.
- Zéro tableau Markdown (`| ... |` interdit) : listes à puces directes (`- `) exclusives.
- Attribution des codes officiels `UA.*` uniquement lorsque l'unité d'apprentissage ou le tutoriel passe à l'état réalisé.
- Préservation rigoureuse de la stack : Laravel 13, MySQL, Preline UI, Tailwind CSS.
