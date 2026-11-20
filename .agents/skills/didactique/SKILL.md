---
name: didactique
description: Master Skill et chef d'orchestre de l'ingénierie pédagogique Solicode N3. Gouverne le cadrage des sessions Scrum de 80h, la pédagogie des 3 projets, l'apprentissage actif sans prérequis N1/N2, et route vers didactique-session-planner et didactique-tutorial-planner.
version: 1.0.0
---

# Master Skill : didactique

## 1. Rôle et Mission
Ce Master Skill est le **chef d'orchestre de l'ingénierie didactique** pour les formations Solicode de Niveau N3 (Développer / Réaliser). Il garantit la cohérence pédagogique amont avant toute rédaction détaillée de tutoriels :
1. **Gouvernance du socle didactique** : respect absolu des standards pédagogiques N3.
2. **Orchestration des compétences de conception** : aiguillage ciblé vers le niveau Macro (Session & Sprint) ou le niveau Micro (Tutoriels & Stubs).

## 2. Principes Directeurs Inviolables (Socle Commun)
1. **Calibrage Temporel Strict :** Chaque session de formation correspond à un Sprint Scrum calibré à **strictement 80 heures** (10 jours à raison de 8h/jour). La métadonnée `duree: 80` est inviolable.
2. **Pédagogie des 3 Projets :**
   - **Projet 1 — Imitation (*Blog des Lauréats*) :** Référence commune guidée pas-à-pas avec le formateur. Les tutoriels rédigés s'appliquent exclusivement à ce projet.
   - **Projet 2 — Technique (*Portfolio Développeur*) :** Réalisation autonome par l'apprenant pour reproduire la technique sur son projet individuel (après le sprint).
   - **Projet 3 — Fil Rouge (*Application Métier*) :** Transposition vers une application métier via les prompts réutilisables créés pour l'Agent IA (après le sprint).
3. **Cycle d'Apprentissage Actif :** $\text{Comprendre} \longrightarrow \text{Reproduire} \longrightarrow \text{Expérimenter} \longrightarrow \text{Réaliser} \longrightarrow \text{Réutiliser}$.
4. **Zéro Réintroduction des Prérequis N1/N2 :** Aucun cours théorique sur les notions déjà acquises aux niveaux antérieurs (HTML/CSS de base, PHP procédural, Git/GitHub de base). Toute manipulation de ce type est traitée en action outillée directe.
5. **Typologie Didactique Stricte :**
   - **`UA-Tâche` :** Action opérationnelle, cadrage, initialisation outillée, rituels Scrum. **0% théorie.**
   - **`UA-Lab` :** Découverte d'un nouveau paradigme N3 (Laravel, Architecture, Prompting RIO). Applique la règle de Pareto 20/80 (fournir les 20% discriminants fondamentaux, 80% en recherche active).
6. **Discrétion Pédagogique :** Interdiction d'exposer la cuisine interne aux apprenants (ne jamais mentionner « 20/80 » ou des durées unitaires dans les fiches destinées aux apprenants).

## 3. Matrice d'Aiguillage Opérationnel
Selon la mission demandée, invoquer immédiatement le sous-skill spécialisé :

```mermaid
flowchart TD
    Demande["Demande d'Ingénierie Didactique"] --> Routeur{"Nature du besoin ?"}
    Routeur -- "Macro : Session, Sprint 80h, Flux réel, Élagage, UAs" --> SP["didactique-session-planner"]
    Routeur -- "Micro : Séquençage pas-à-pas, Titrage technique, Stubs Jekyll" --> TP["didactique-tutorial-planner"]
    Routeur -- "Aval : Rédaction et synchronisation des fiches tutos" --> TW["tutorial-writer (Master Aval)"]
```

- **Besoin Niveau Session / Sprint :** Cadrer la session, aligner avec le flux de travail réel (`_flux-travail.md`), auditer et élaguer les tâches selon Scrum (10 questions), qualifier les UAs (`UA-Tâche` vs `UA-Lab`), mettre à jour `_sessions/S[X].md` ➔ Invoquer **`didactique-session-planner`**.
- **Besoin Niveau Progression / Tutoriels :** Découper la réalisation pas-à-pas sans rupture ($E_{n-1} \to E_n$), formuler des titres équilibrés sans entité métier, insérer le sas « Bien démarrer », matérialiser les entités Jekyll et générer les stubs sous `_tutos/` (`en_construction: true`) ➔ Invoquer **`didactique-tutorial-planner`**.
- **Besoin Rédactionnel Aval :** Rédiger le corps complet des fiches, injecter `window.pageData` et synchroniser avec les livrables du projet cible ➔ Déléguer à **`tutorial-writer`**.

## 4. Contrôle Qualité de l'Orchestrateur
- [ ] Le budget temps de la session est fixé à exactement 80 heures.
- [ ] Le projet d'imitation est la cible exclusive des travaux guidés.
- [ ] Aucun cours théorique n'est réintroduit pour les prérequis N1/N2.
- [ ] L'aiguillage respecte la frontière étanche : Macro (`session-planner`) vs Micro (`tutorial-planner`).