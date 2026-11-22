---
layout: tuto
title: "Raffinement du Product Backlog"
sous_titre: "Actualiser, rÃ©-estimer et rÃ©ordonner le carnet de produit en vue du prochain sprint"
slug: "backlog-refinement"
slug_domaine: "realisation-projet"
slug_ua: "cloture-sprint"
permalink: /tutos/backlog-refinement/
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
---

## 1. Objectif OpÃ©rationnel & PrÃ©requis
- **Position dans le flux :** Phase D â€” ClÃ´ture de Sprint, RÃ©trospective & Bilan / Ã‰tape 12.3 â€” Backlog Grooming.
- **Branche Git :** `sprint1`
- **Fichiers modifiÃ©s ou crÃ©Ã©s :** `scrum/product-backlog.md`, `issues/issues-closes.md`.
- **Objectif :** ClÃ´turer les tÃ¢ches du Sprint 1 et rÃ©ordonner le Product Backlog face aux retours de la revue pour prÃ©parer la planification du Sprint 2.
- **PrÃ©requis :** DÃ©monstration validÃ©e en Sprint Review (`T.351.231`) et analyse rÃ©flexive de rÃ©trospective (`T.351.232`).

## 2. DÃ©roulement Pas-Ã -Pas de la TÃ¢che

1. **Ã‰tape 1 â€” Archivage des TÃ¢ches LivrÃ©es :**  
   Basculez les tÃ¢ches achevÃ©es du Sprint 1 depuis `issues/issues-open.md` vers le registre d'archivage `issues/issues-closes.md` avec mention de la date de clÃ´ture et du commit de validation.

2. **Ã‰tape 2 â€” Actualisation du Statut de la User Story :**  
   Dans `scrum/product-backlog.md`, passez l'Ã©lÃ©ment US-01 (*Â« En tant qu'apprenant ou recruteur, je veux consulter la page dÃ©taillÃ©e d'un article... Â»*) Ã  l'Ã©tat formel `TerminÃ© (Done)`.

3. **Ã‰tape 3 â€” PrÃ©paration et RÃ©ordonnancement du Sprint 2 :**  
   - IntÃ©grez les retours formulÃ©s par le Product Owner lors de la dÃ©monstration.
   - SpÃ©cifiez les critÃ¨res d'acceptation prÃ©liminaires pour les prochaines User Stories prioritaires du Sprint 2 (Phase de Design Thinking, formulaires d'articles et transition vers la base de donnÃ©es relationnelle).
   - RÃ©estimez les Story Points selon l'Ã©chelle de Fibonacci si des incertitudes techniques ont Ã©tÃ© levÃ©es.

## 3. Livrables & CritÃ¨res de RÃ©ussite
- **Livrables attendus :**
  - Carnet de produit actualisÃ© : `scrum/product-backlog.md` sur la branche `sprint1`.
  - Registre des tÃ¢ches archivÃ©es : `issues/issues-closes.md` sur la branche `sprint1`.
- **CritÃ¨res de validation :**
  - [ ] La User Story US-01 est marquÃ©e comme terminÃ©e dans le Product Backlog.
  - [ ] Les tÃ¢ches de rÃ©alisation du Sprint 1 sont archivÃ©es dans `issues/issues-closes.md`.
  - [ ] Les prioritÃ©s pour le Sprint 2 sont clairement ordonnÃ©es.
