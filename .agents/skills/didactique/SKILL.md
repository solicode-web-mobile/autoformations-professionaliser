---
name: didactique
description: Master Skill et chef d'orchestre de l'ingénierie pédagogique EFP générique pour tous les niveaux (N1 Découvrir, N2 Prototyper, N3 Développer). Gouverne le cadrage des sessions Scrum de 80h, la pédagogie des 3 projets, l'apprentissage actif sans redondance de prérequis, et route vers didactique-session-planner et didactique-tuto-planner.
version: 1.2.0
---

# Master Skill : didactique

## 1. Rôle et Mission
Ce Master Skill est le **chef d'orchestre de l'ingénierie didactique** pour l'ensemble des formations de l'EFP sur les 3 niveaux de cursus : **N1 (Découvrir)**, **N2 (Prototyper)** et **N3 (Développer / Réaliser)**. Il garantit la cohérence pédagogique amont avant toute rédaction de tutoriels :
1. **Gouvernance du socle didactique** : application des principes d'apprentissage actif adaptés au niveau cible résolu dans `.agents/rules/`.
2. **Orchestration des compétences de conception** : aiguillage ciblé vers le niveau Macro (Session & Sprint) ou le niveau Micro (Tutoriels & Stubs).

## 2. Principes Directeurs Inviolables (Socle Tous Niveaux)
1. **Calibrage Temporel Indicatif :** La durée globale d'une session (standard indicatif de 80 heures / 10 jours ouvrés pour un Sprint Scrum) est fournie à **titre purement indicatif** pour les formateurs et concepteurs pédagogiques. Elle sert de repère de cadrage macro et ne doit jamais être affichée ni fragmentée en durées unitaires dans les consignes destinées aux apprenants.
2. **Pédagogie des 3 Projets :**
   - **Projet 1 — Imitation :** Référence commune guidée pas-à-pas avec le formateur. Les tutoriels rédigés s'appliquent exclusivement à ce projet.
   - **Projet 2 — Technique :** Réalisation autonome par l'apprenant pour reproduire la technique sur son projet individuel (après le sprint).
   - **Projet 3 — Fil Rouge :** Transposition vers une application métier (autonome ou avec Agent IA selon le niveau, après le sprint).
3. **Cycle d'Apprentissage Actif :** $\text{Comprendre} \longrightarrow \text{Reproduire} \longrightarrow \text{Expérimenter} \longrightarrow \text{Réaliser} \longrightarrow \text{Réutiliser}$.
4. **Non-Régression & Zéro Répétition des Prérequis :** Ne jamais introduire de cours théorique sur les notions déjà acquises aux niveaux antérieurs (en N2 : prérequis N1 acquis ; en N3 : prérequis N1 et N2 acquis ; en N1 : apprentissage direct des fondamentaux).
5. **Typologie et Maturation Didactique Stricte :**
   - **Maturité `projet` / `type: "tuto-tache"` :** Action opérationnelle, cadrage, initialisation outillée, rituels Scrum. **0% théorie.**
   - **Maturité `lab` & `ua-lab` / `type: "tuto-atelier"` :** Découverte active d'un paradigme. En phase `lab` : recherche active sans notions fondamentales détaillées. En phase `ua-lab` : lab validé sur le terrain avec plan d'UA spécifié et notions fondamentales détaillées (20% fondamentaux, 80% approfondissement).
6. **Discrétion Pédagogique :** Interdiction formelle d'exposer la cuisine interne aux apprenants (ne jamais mentionner « 20/80 » ou des durées unitaires dans les fiches destinées aux apprenants).

## 3. Matrice d'Aiguillage Opérationnel
Selon la mission demandée, invoquer immédiatement le sous-skill spécialisé :

```mermaid
flowchart TD
    Demande["Demande d'Ingénierie Didactique (N1 / N2 / N3)"] --> Routeur{"Nature du besoin ?"}
    Routeur -- "Macro : Session, Flux réel, Élagage, Décomposition UAs" --> SP["didactique-session-planner"]
    Routeur -- "Micro : Séquençage pas-à-pas, Titrage technique, Stubs Jekyll" --> TP["didactique-tuto-planner"]
    Routeur -- "Aval : Rédaction et synchronisation des fiches tutos" --> TW["tuto-writer (Master Aval)"]
```

- **Besoin Niveau Session / Sprint :** Cadrer la session, aligner avec le flux de travail réel (`_flux-travail.md`), auditer et élaguer les tâches selon Scrum (10 questions), qualifier les UAs (`UA-Tâche` vs `UA-Lab`), mettre à jour `_sessions/S[X].md` ➔ Invoquer **`didactique-session-planner`**.
- **Besoin Niveau Progression / Tutoriels :** Découper la réalisation pas-à-pas sans rupture ($E_{n-1} \to E_n$), formuler des titres équilibrés sans entité métier, insérer le sas « Bien démarrer », matérialiser les entités Jekyll et générer les stubs sous `_tutos/` (`en_construction: true`) ➔ Invoquer **`didactique-tuto-planner`**.
- **Besoin Rédactionnel Aval :** Rédiger le corps complet des fiches, injecter `window.pageData` et synchroniser avec les livrables du projet cible ➔ Déléguer à **`tuto-writer`**.

## 4. Contrôle Qualité de l'Orchestrateur
- [ ] La durée de session (indicative : 80 heures) sert de repère macro pour les formateurs sans être affichée aux apprenants.
- [ ] Le projet d'imitation du niveau actif est la cible exclusive des travaux guidés.
- [ ] Aucun cours théorique n'est réintroduit pour les prérequis validés aux niveaux antérieurs.
- [ ] L'aiguillage respecte la frontière étanche : Macro (`session-planner`) vs Micro (`tutorial-planner`).