# Plan des Tutoriels : D.325.1 — Ingénierie de Prompt et Agents IA

> **Domaine :** `D.325.1` | **Compétence :** `C.325` — Développer des solutions logicielles avec l'assistance de l'IA | **Session :** S01  
> **Niveau de Maturité :** UA-Lab (Atelier pratique guidé)  
> **Branche Git de Travail :** `sprint1`  
> **Référentiels Liés :** [`../../3.sprints/flux-travail-n3.md`](../../3.sprints/flux-travail-n3.md) | [`../../3.sprints/stack-technique-n3.md`](../../3.sprints/stack-technique-n3.md)

---

## 1. Description des Unités d'Apprentissage du Domaine

### UA.325.11 — Prompt Engineering

- **Code :** `UA.325.11`
- **Maturité :** `UA-Lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 01
- **Positionnement Flux de Travail :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 1.1 — Outillage Prompt Engineering
- **Briques Stack Technique :** LLMs (Claude, Gemini), Méthode RIO, Context Engineering, Méta-prompting
- **Compétence :** `C.325` — Développer des solutions logicielles avec l'assistance de l'IA
- **Domaine :** `D.325.1` — Ingénierie de prompt et agents IA
- **Durée estimée :** 6 heures
- **Objectif :** Maîtriser le dialogue déterministe avec les modèles de langage et le Context Engineering pour outiller l'équipe d'un méta-prompt réutilisable capable de générer tous les prompts du flux de travail sans hallucination.
- **Description :** Outiller le développeur augmenté par l'ingénierie de prompt structurée. L'apprenant s'approprie la méthode RIO et conçoit le méta-prompt réutilisable `prompt-creator` pour automatiser la transposition des étapes du sprint.
- **Notions Clés Utilisées dans le Sprint :**
  - Méthode directrice RIO : Rôle précis (persona d'expert), Instructions contextualisées sans ambiguïté, Output au format strict (Markdown, code pur).
  - Context Engineering : Injection du contexte métier et des règles de développement, réduction drastique des hallucinations.
  - Contraintes négatives explicites : Suppression du bavardage de politesse, interdiction formelle de dévier du périmètre fonctionnel.
  - Méta-Prompting : Conception d'un prompt générateur de prompts (`prompt-creator.prompt.md`).
- **Livrable :** Méta-prompt générateur de prompts au standard RIO (`livrables/ia/prompts/prompt-creator.prompt.md`) sur la branche `sprint1`.
- **Travail à Faire :** Assimiler la méthode RIO, concevoir le méta-prompt `prompt-creator` et tester sa pertinence sur un cas d'usage réel.

---

## 2. Plan des Tutoriels : UA.325.11

### T.325.111 — Théorie : Prompt Engineering & Méthode RIO
*(Tâche 1 — Présentation Théorique & Exercices d'Assimilation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 1.1 — Outillage Prompt Engineering.
- **Stack mobilisée :** Chaîne d'outillage IA, LLMs (Gemini, Claude), architecture de contextes.

#### 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches documentaires nécessaires et concevoir une fiche de synthèse expliquant le fonctionnement d'un LLM, la structure d'un prompt directif selon la méthode RIO et l'intérêt du Context Engineering.

#### 3. Répartition Didactique (Règle des 20/80)
- **Les 20% fournis directement au tutoriel :**
  - Définition formelle de la fenêtre de contexte et du ciblage chirurgical des fichiers (`@fichier`).
  - Définition de la méthode **RIO** : Rôle expert, Intention opérationnelle fermée, Output délimité.
  - Rôle des contraintes négatives bloquantes (zéro explication, code pur, zéro bavardage).
- **Les 80% recherchés par l'apprenant :**
  - Recherche active sur le phénomène d'hallucination des LLMs et la complétion probabiliste.
  - Distinctions entre *Few-Shot prompting* et *Zero-Shot prompting*.

#### 4. Livrable Attendu
- Fiche de synthèse RIO intégrée dans le journal d'apprentissage.

---

### T.325.112 — Création du prompt-creator
*(Tâche 2 — Pratique & Automatisation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 1.1 — Méta-Prompt Générateur.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-creator.prompt.md`

#### 2. Travail à Faire
Concevoir, tester et valider dans `livrables/ia/prompts/prompt-creator.prompt.md` le méta-prompt officiel permettant à l'agent IA de générer, sur simple description d'un besoin de tâche, le prompt RIO complet et contextualisé pour chaque étape future du sprint.

#### 3. Missions Concrètes Réalisées par le Prompt
1. Analyser une consigne brute de tâche ou d'exigence logicielle.
2. Structurer le prompt selon le formalisme RIO (Rôle expert, Intention opérationnelle fermée, Output délimité).
3. Injecter les contraintes négatives bloquantes (zéro bavardage de politesse, code exécutable complet sans omission, chemins relatifs stricts).
4. Produire un fichier `.prompt.md` prêt à l'emploi.

#### 4. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Métaprompt Engineer expert en systèmes multi-agents.
- **Instruction :** Prendre en entrée la description d'une tâche d'ingénierie logicielle et produire un prompt directif structuré en Rôle / Contexte / Instructions pas-à-pas / Contraintes négatives / Format de sortie.
- **Output :** Bloc Markdown contenant le prompt prêt à être enregistré dans un fichier `*.prompt.md`.
- **Contraintes Négatives :** Le méta-prompt ne doit pas exécuter la tâche lui-même ; il doit produire le prompt qui permettra d'exécuter la tâche.

#### 5. Critères de Validation
- [ ] Le fichier `livrables/ia/prompts/prompt-creator.prompt.md` est présent et versionné sur la branche `sprint1`.
- [ ] Soumis à une consigne brute de test, il génère un prompt RIO complet, testable et conforme aux standards de la promotion.
