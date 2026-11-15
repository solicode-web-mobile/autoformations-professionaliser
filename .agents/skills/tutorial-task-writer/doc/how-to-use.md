# Guide Opérationnel : Comment Utiliser `tutorial-task-writer`

## 1. Rôle du Skill
Le skill `tutorial-task-writer` rédige et met à jour les fiches de tutoriels opérationnels rattachées aux Unités d'Apprentissage de maturité **`UA-Tâche`** (cadrage, cérémonies de sprint Scrum, bilan de projet).

---

## 2. Cas d'Usage Principaux
- Rédaction d'un tutoriel de rituel agile (Sprint Planning, Sprint Review, Sprint Retrospective, Backlog Grooming).
- Formalisation des étapes de démarrage d'un sprint (cadrage, validation de l'environnement, pitch deck).
- Cadrage des bilans individuels et collectifs d'acquisition de compétences.

---

## 3. Prompts Types pour Invoquer le Skill
- *« Rédige les fiches de tutoriels pour l'UA-Tâche UA.351.21 à partir du plan _tutos/_plan-tuto-D.351.2-realisation-projet.md. »*
- *« Formalise le tutoriel opérationnel du rituel de Sprint Planning (T.351.221) pour l'UA-Tâche UA.351.22. »*
- *« Rédige les étapes de la rétrospective et de la dette d'empathie pour la tâche T.351.232. »*

---

## 4. Prérequis
1. L'Unité d'Apprentissage parente doit porter la mention `maturite: "UA-Tâche"`.
2. Le plan de développement du domaine (`_plan-tuto-D.351.2-realisation-projet.md`) et le cadrage de session (`_S01.md`) sont disponibles.
3. Les artefacts attendus (charte, procès-verbaux, grilles DoD, rapports de rétrospective) sont clairement délimités.

---

## 5. Déroulement Pas-à-Pas
1. **Étape 1 — Définition de l'Objectif Opérationnel & Prérequis :**  
   Clarifier ce que l'équipe doit accomplir concrètement dans le sprint et les prérequis nécessaires.
2. **Étape 2 — Découpage en Étapes Directives :**  
   Structurer le déroulement en 3 à 5 étapes claires rédigées à l'impératif direct (*« Exécutez »*, *« Découpez »*, *« Validez »*).
3. **Étape 3 — Définition des Livrables & Critères de Réussite :**  
   Spécifier l'emplacement exact des livrables Markdown et formuler des critères de validation binaires `[ ]`.
4. **Étape 4 — Sauvegarde & Contrôle :**  
   Enregistrer le fichier en UTF-8 sans BOM sous `_tutos/[Domaine]/[UA]/[Code-Tuto]/[slug].md` avec `maturite: "UA-Tâche"` et `en_construction: true`.
