# Guide Opérationnel : Comment Utiliser `tutorial-lab-writer`

## 1. Rôle du Skill
Le skill `tutorial-lab-writer` est le rédacteur technique et pédagogique dédié aux Unités d'Apprentissage relevant du niveau de maturité **`UA-Lab`** (ateliers pratiques guidés de modélisation, de cadrage agile, d'architecture, d'outillage IA et de développement avec frameworks).

---

## 2. Cas d'Usage Principaux
- Rédaction des fiches de tutoriels flexibles (Théorie 20/80, Pratique sur projet d'imitation, Création de prompts récurrents) pour une Unité d'Apprentissage `UA-Lab`.
- Arbitrage didactique : omission de théorie superflue (notions N1/N2 déjà validées) ou omission de prompt hors flux récurrent.
- Scission des prompts d'ingénierie applicative (ex: `prompt-back-end` et `prompt-front-end`).
- Alignement et mise à jour des ateliers pratiques à partir des plans de domaine (`_tutos/_plan-tuto-D.XXX.Y-*.md`).

---

## 3. Prompts Types pour Invoquer le Skill
- *« Rédige les fiches de tutoriels pour l'UA-Lab UA.311.21 à partir du plan _tutos/_plan-tuto-D.311.2-uml.md en omettant la théorie déjà acquise en N2. »*
- *« Formalise la fiche théorique 20/80 (T.351.121) de l'UA-Lab UA.351.12 avec les définitions clés de Product Backlog et User Stories. »*
- *« Rédige le tutoriel de création du prompt backend (T.321.133) pour l'UA-Lab UA.321.13 avec le cahier des charges RIO complet. »*

---

## 4. Prérequis
Avant d'activer le skill, s'assurer que :
1. L'Unité d'Apprentissage est explicitement qualifiée avec `maturite: "UA-Lab"`.
2. Le plan de tutoriels associé (`_tutos/_plan-tuto-D.XXX.Y-*.md`) et le cadrage de session (`_sessions/S[X].md`) sont disponibles comme sources de vérité.
3. La branche Git du sprint (ex: `sprint1`) et les fichiers cibles impactés sont clairement identifiés.

---

## 5. Déroulement Pas-à-Pas

### Étape 1 : Chargement des Sources de Vérité
- Charger la description de l'UA dans `_uas/` et dans le plan du domaine `_tutos/_plan-tuto-D.XXX.Y-*.md`.
- Identifier la composition requise (2, 3 ou 4 tâches) selon les règles d'omission de théorie ou d'éviction de prompt.

### Étape 2 : Rédaction de la Fiche Théorie (si requise)
- Appliquer rigoureusement la règle Pareto 20/80 :
  - Fournir 20% de définitions fondamentales incontournables.
  - Formuler les 80% de notions à approfondir par recherche active de l'apprenant.
- Ne jamais afficher d'indication de durée.

### Étape 3 : Rédaction de la Fiche Pratique
- Cibler **exclusivement le Projet d'imitation** (*Blog des Lauréats*).
- Spécifier la branche Git (`branche: "sprintX"`).
- Découper la réalisation en jalons chronologiques clairs et fournir des critères de validation binaires `[ ]`.

### Étape 4 : Rédaction de la Fiche Création de Prompt (si flux récurrent)
- Titrer directement au format `Création du prompt-[nom]`.
- Expliciter les missions concrètes que le prompt exécute pour le projet.
- Structurer le cahier des charges selon la méthode RIO avec contraintes négatives strictes.

### Étape 5 : Encodage et Validation
- Vérifier que le frontmatter porte `en_construction: false` lors de la publication.
- Sauvegarder impérativement en **UTF-8 sans BOM** sous `_tutos/[Domaine]/[UA]/[Code-Tuto]/[slug].md`.