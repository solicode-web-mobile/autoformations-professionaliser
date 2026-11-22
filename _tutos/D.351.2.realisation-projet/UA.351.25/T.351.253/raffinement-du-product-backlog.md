---
layout: tuto
title: "Raffinement du Product Backlog"
sous_titre: "Actualiser, ré-estimer et réordonner le carnet de produit en vue du prochain sprint"
slug: "backlog-refinement"
slug_domaine: "realisation-projet"
slug_ua: "UA.351.25"
permalink: "/tutos/raffinement-du-product-backlog/"
tuto_id: "T.351.253"
version: "normal"
ua: "UA.351.25"
maturite: "projet"
type: "tuto-tache"
nav_order: 3
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
etape: 1006
---

## 1. Objectif Opérationnel & Prérequis
- **Position dans le flux :** Phase D — Clôture de Sprint, Rétrospective & Bilan / Étape 12.3 — Backlog Grooming.
- **Branche Git :** `sprint1`
- **Fichiers modifiés ou créés :** `scrum/product-backlog.md`, `issues/issues-closes.md`.
- **Objectif :** Clôturer les tâches du Sprint 1 et réordonner le Product Backlog face aux retours de la revue pour préparer la planification du Sprint 2.
- **Prérequis :** Démonstration validée en Sprint Review (`T.351.231`) et analyse réflexive de rétrospective (`T.351.232`).

## 2. Déroulement Pas-à-Pas de la Tâche

1. **Étape 1 — Archivage des Tâches Livrées :**  
   Basculez les tâches achevées du Sprint 1 depuis `issues/issues-open.md` vers le registre d'archivage `issues/issues-closes.md` avec mention de la date de clôture et du commit de validation.

2. **Étape 2 — Actualisation du Statut de la User Story :**  
   Dans `scrum/product-backlog.md`, passez l'élément US-01 (*« En tant qu'apprenant ou recruteur, je veux consulter la page détaillée d'un article... »*) à l'état formel `Terminé (Done)`.

3. **Étape 3 — Préparation et Réordonnancement du Sprint 2 :**  
   - Intégrez les retours formulés par le Product Owner lors de la démonstration.
   - Spécifiez les critères d'acceptation préliminaires pour les prochaines User Stories prioritaires du Sprint 2 (Phase de Design Thinking, formulaires d'articles et transition vers la base de données relationnelle).
   - Réestimez les Story Points selon l'échelle de Fibonacci si des incertitudes techniques ont été levées.

## 3. Livrables & Critères de Réussite
- **Livrables attendus :**
  - Carnet de produit actualisé : `scrum/product-backlog.md` sur la branche `sprint1`.
  - Registre des tâches archivées : `issues/issues-closes.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] La User Story US-01 est marquée comme terminée dans le Product Backlog.
  - [ ] Les tâches de réalisation du Sprint 1 sont archivées dans `issues/issues-closes.md`.
  - [ ] Les priorités pour le Sprint 2 sont clairement ordonnées.
