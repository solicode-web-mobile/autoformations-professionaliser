---
layout: presentation
title: "Présentation : T.351.113 — Estimation et Product Backlog (Cas TodoList)"
marp: true
theme: default
paginate: true
header: "T.351.113 : Estimation et Product Backlog"
footer: "Scrum & Ingénierie Agile"
nav_exclude: true
---

<!-- _class: lead -->
# T.351.113 : Créer, estimer et ordonner le Product Backlog
### Cas d'étude didactique : Application TodoList
**Unité d'Apprentissage : UA.351.11 — Initiation Scrum**

- **Public** : Développeurs Web (Niveau N3)
- **Domaine** : Scrum & Ingénierie Agile (`D.351.1`)
- **Compétence** : `C.351` — Piloter et animer la démarche Scrum

---

## 1. Pourquoi estimer en Story Points relatifs ?

- **Les limites des heures absolues :**
  - Forte subjectivité et sous-estimation systématique des imprévus.
  - Varie considérablement selon l'expérience individuelle du développeur.

- **La force des Story Points relatifs :**
  - Mesure abstraite combinant : **effort**, **complexité**, **incertitude**.
  - Comparaison directe entre éléments connus.
  - Échelle de Fibonacci : **1, 2, 3, 5, 8, 13** (l'incertitude grandit avec la taille).

---

## 2. La Méthode de Priorisation MoSCoW

- **Must Have (Indispensable) :**
  - Cœur vital du MVP, non négociable pour le premier livrable.
- **Should Have (Important) :**
  - Forte valeur ajoutée mais n'empêche pas l'usage immédiat.
- **Could Have (Souhaitable) :**
  - Options de confort réalisées s'il reste du temps.
- **Won't Have (Reporté) :**
  - Exigences écartées pour le sprint en cours.

---

## 3. Le Product Backlog Chiffré de la TodoList

| Réf | Fonctionnalité | Points | MoSCoW | Cible |
| :-: | :--- | :-: | :-: | :-: |
| **US-02** | Affichage liste & compteur | **2 pts** | **Must Have** | Sprint 1 |
| **US-01** | Ajout d'une tâche via formulaire | **3 pts** | **Must Have** | Sprint 1 |
| **US-03** | Cochage et validation de tâche | **3 pts** | **Must Have** | Sprint 1 |
| **US-04** | Filtrage 3 vues (Toutes/En cours/Fait) | 5 pts | Should Have | Sprint 2 |
| **US-05** | Suppression et purge | 3 pts | Should Have | Sprint 2 |
| **US-06** | Sauvegarde LocalStorage | 5 pts | Could Have | Sprint 3 |

> **Périmètre engagé Sprint 1 : 8 Story Points (MVP vital).**

---

## 4. Les Contrats Qualité : DoR vs DoD

### Definition of Ready (DoR) — Filtre d'entrée :
- Story rédigée au gabarit standard (*En tant que...*).
- Critères d'acceptation clairs et testables.
- Complexité votée en Story Points par l'équipe.

### Definition of Done (DoD) — Filtre de sortie :
- HTML5 sémantique et responsive mobile 375px sans débordement.
- Console du navigateur 100% propre (zéro warning, zéro erreur).
- Critères d'acceptation validés manuellement.
- Code versionné proprement sur la branche active.

---

<!-- _class: lead -->
# Conclusion de l'Atelier T.351.113
### Prêt pour la Planification du Sprint

- Le backlog est chiffré, priorisé et encadré par des contrats qualité stricts.
- **Prochaine étape (T.351.114) :** Planifier, découper et piloter un Sprint de développement avec le tableau Kanban et le Daily Scrum.
