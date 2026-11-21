# Skill : didactique (Master Orchestrateur Tous Niveaux)

## Présentation
Le skill **`didactique`** est le Master Skill d'ingénierie pédagogique de l'EFP, opérant de façon **générique sur l'ensemble des 3 niveaux du cursus** :
- **N1 (Découvrir) :** Fondamentaux du web, programmation procédurale, SQL relationnel.
- **N2 (Prototyper) :** Programmation Orientée Objet, architecture 3-tiers, modélisation UML.
- **N3 (Développer / Réaliser) :** Frameworks modernes, architecture logicielle, TDD, Scrum, Agent IA.

Il centralise les principes directeurs communs (sprint 80h, règle des 3 projets, cycle actif, zéro répétition de prérequis) et pilote l'architecture de conception pédagogique en amont de `tutorial-writer`.

## Architecture de la Famille Didactique
- **`didactique` (Master) :** Gouverneur général et garant du cadre didactique de l'EFP (N1, N2, N3).
  - **`didactique-session-planner` (Macro) :** Cadrage du Sprint Scrum 80h, alignement avec le flux réel (`_flux-travail.md`), élagage des tâches inutiles et qualification des UAs quel que soit le niveau.
  - **`didactique-tutorial-planner` (Micro) :** Découpage fin pas-à-pas ($E_{n-1} \to E_n$), titrage technique équilibré, sas « Bien démarrer » et génération des stubs Jekyll.

## Découplage du Niveau Actif
Les règles spécifiques à chaque niveau sont résolues dynamiquement dans `.agents/rules/` (ex: `pedagogie-spartel-n3.md`). Les skills de la famille `didactique` appliquent ces règles sans être couplés en dur à un niveau particulier.

## Cas d'Usage & Prompts Types
- **Cadrage d'une session (N1, N2 ou N3) :**
  > « Active le skill didactique pour concevoir la session S2 de Niveau N2 à partir du flux de travail opérationnel. »
- **Audit et élagage d'un sprint Scrum :**
  > « Utilise didactique pour auditer le plan de la session S1, éliminer les redondances et cadrer le sprint sur 80 heures. »
- **Planification de la progression fine d'une UA :**
  > « Active didactique pour planifier l'enchaînement pas-à-pas des tutoriels de l'UA et générer les stubs Jekyll. »

## Vérification
Valider la conformité des compétences avec :
```bash
node .agents/skills/skills-dev/scripts/validate-skills.cjs
```