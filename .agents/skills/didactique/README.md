# Skill : didactique (Master Orchestrateur)

## Présentation
Le skill **`didactique`** est le Master Skill d'ingénierie pédagogique de Solicode N3. Il centralise les principes directeurs communs (sprint 80h, règle des 3 projets, cycle actif, zéro prérequis N1/N2) et pilote l'architecture de conception pédagogique en amont de `tutorial-writer`.

## Architecture de la Famille Didactique
- **`didactique` (Master) :** Gouverneur général et garant du cadre didactique Solicode N3.
  - **`didactique-session-planner` (Macro) :** Cadrage du Sprint Scrum 80h, alignement avec le flux réel (`_flux-travail.md`), élagage des tâches inutiles et qualification des UAs.
  - **`didactique-tutorial-planner` (Micro) :** Découpage fin pas-à-pas ($E_{n-1} \to E_n$), titrage technique équilibré, sas « Bien démarrer » et génération des stubs Jekyll.

## Cas d'Usage & Prompts Types
- **Cadrage complet d'une nouvelle session :**
  > « Active le skill didactique pour concevoir la session S2 à partir du flux de travail opérationnel de notre projet Laravel. »
- **Audit et optimisation d'un plan de sprint :**
  > « Utilise didactique pour auditer le plan de la session S1, éliminer les redondances et cadrer le sprint sur 80 heures. »
- **Planification séquentielle des tutoriels :**
  > « Active didactique pour planifier l'enchaînement pas-à-pas des tutoriels de l'UA.321.10 et générer les stubs Jekyll. »

## Vérification
Valider la conformité des compétences avec :
```bash
node .agents/skills/skills-dev/scripts/validate-skills.cjs
```