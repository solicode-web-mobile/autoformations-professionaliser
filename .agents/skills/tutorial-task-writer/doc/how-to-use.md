# Guide Opérationnel : Comment Utiliser `tutorial-task-writer`

## 1. Rôle du Skill
Le skill `tutorial-task-writer` rédige et met à jour les fiches de tutoriels opérationnels rattachées aux Unités d'Apprentissage de maturité **`UA-Tâche`** (cadrage de périmètre, rituels et cérémonies de sprint Scrum, outillage IA des cérémonies, bilans de progression).

---

## 2. Cas d'Usage Principaux
- Rédaction d'un tutoriel de cérémonie agile (Sprint Planning, Sprint Review, Sprint Retrospective, Backlog Refinement).
- Rédaction du tutoriel de cadrage opérationnel du périmètre d'un sprint (`cadrage/cadrage-projet.md`).
- Rédaction des tutoriels d'outillage IA des cérémonies agiles (conception des prompts de clôture et de planification).
- Cadrage des bilans individuels et collectifs d'acquisition de compétences.

---

## 3. Prompts Types pour Invoquer le Skill
- *« Rédige la fiche opérationnelle de cadrage de projet (T.351.211) pour l'UA-Tâche UA.351.21. »*
- *« Formalise le tutoriel de rituel de Sprint Planning (T.351.221) pour l'UA-Tâche UA.351.22 sans aucune théorie et sur la branche sprint1. »*
- *« Rédige le tutoriel d'outillage IA T.351.235 créant les 4 prompts de clôture de sprint selon la méthode RIO. »*

---

## 4. Prérequis
1. L'Unité d'Apprentissage parente doit porter la mention `maturite: "UA-Tâche"`.
2. Le plan de développement du domaine (`_plan-tuto-D.351.2-realisation-projet.md`) et le cadrage de session (`_sessions/S[X].md`) sont disponibles.
3. Les artefacts attendus (cadrage, procès-verbaux, grilles DoD, rapports de rétrospective, prompts de cérémonie) sont clairement délimités.
4. La branche Git de travail (ex: `sprint1`) est identifiée.

---

## 5. Déroulement Pas-à-Pas
1. **Étape 1 — Définition des Prérequis (Sans cours) :**  
   Lister sous forme de points clés la base théorique et pratique requise (commandes CLI, branches, concepts) et les prérequis de projet sur la branche `sprintX`, sans dispenser de cours théorique passif.
2. **Étape 2 — Synthèse du Travail à Faire :**  
   Formuler clairement les tâches concrètes et opérationnelles à réaliser dans ce tutoriel.
3. **Étape 3 — Découpage des Étapes de Réalisation (Zéro Théorie) :**  
   Structurer le déroulement en étapes d'action directes rédigées à l'impératif direct (*« Exécutez »*, *« Créez »*, *« Validez »*).
4. **Étape 4 — Définition des Livrables & Critères de Validation :**  
   Spécifier l'emplacement exact des fichiers produits sur la branche de sprint (`sprintX`) hors dossier `labs/` et formuler des critères de validation binaires `[ ]`.
5. **Étape 5 — Sauvegarde & Contrôle :**  
   Enregistrer le fichier en **UTF-8 sans BOM** sous `_tutos/[Domaine]/[UA]/[Code-Tuto]/[slug].md` avec `maturite: "UA-Tâche"` et `en_construction: false` dès validation.