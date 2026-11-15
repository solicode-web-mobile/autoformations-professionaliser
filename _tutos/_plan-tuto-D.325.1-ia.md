# Plan des Tutoriels : D.325.1 — Ingénierie de Prompt et Agents IA

> **Domaine :** `D.325.1` | **Compétence :** `C.325` — Développer des solutions logicielles avec l'assistance de l'IA | **Session :** S01  
> **Niveau de Maturité :** UA-Lab (Atelier pratique guidé)  
> **Référentiels Liés :** [`../../3.sprints/flux-travail-n3.md`](../../3.sprints/flux-travail-n3.md) | [`../../3.sprints/stack-technique-n3.md`](../../3.sprints/stack-technique-n3.md)

---

## 1. Description des Unités d'Apprentissage du Domaine

### UA.325.11 — Prompt Engineering

- **Code :** `UA.325.11`
- **Maturité :** `UA-lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 03
- **Positionnement Flux de Travail :** Phase 1 — Cadrage & Gouvernance Agile / Étape 1.3 — Outillage Prompt Engineering
- **Briques Stack Technique :** LLMs (Claude, Gemini), Méthode RIO, Context Engineering, Méta-prompting
- **Compétence :** `C.325` — Développer des solutions logicielles avec l'assistance de l'IA
- **Domaine :** `D.325.1` — Ingénierie de prompt et agents IA
- **Durée estimée :** 8 heures
- **Objectif :** Maîtriser le dialogue déterministe avec les modèles de langage et le Context Engineering pour outiller l'équipe d'un méta-prompt réutilisable capable de générer tous les prompts du flux de travail sans hallucination.
- **Description :** Outiller le développeur augmenté par l'ingénierie de prompt structurée. L'apprenant formalise le guide méthodologique RIO et conçoit le méta-prompt réutilisable pour automatiser la transposition des étapes sur le projet Fil Rouge.
- **Notions Clés Utilisées dans le Sprint :**
  - Méthode directrice RIO : Rôle précis (persona d'expert), Instructions contextualisées sans ambiguïté, Output au format strict (Markdown, code pur).
  - Context Engineering : Injection du contexte métier et des règles de développement, réduction drastique des hallucinations.
  - Contraintes négatives explicites : Suppression du bavardage de politesse, interdiction formelle de dévier du périmètre fonctionnel.
  - Méta-Prompting : Conception d'un prompt générateur de prompts (`prompt-creator.prompt.md`) paramétré par variables `[VARIABLE]`.
- **Livrables :** Guide opératoire d'ingénierie de prompt (`livrables/ia/README.md`) et générateur de prompts (`livrables/ia/prompt-creator.prompt.md`).
- **Travail à Faire :** Rédiger le guide RIO d'équipe, concevoir le méta-prompt prompt-creator et tester sa pertinence sur un cas d'usage réel.

---

## 2. Plan des Tutoriels : UA.325.11

### T.325.111 — Théorie : Prompt Engineering
*(Tâche 1 — Présentation Théorique & Exercices d'Assimilation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase 1 — Cadrage & Gouvernance Agile / Étape 1.3 — Outillage Prompt Engineering.
- **Stack mobilisée :** Chaîne d'outillage IA, LLMs (Gemini, Claude), architecture de contextes.

#### 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches documentaires nécessaires et concevoir une présentation synthétique (support visuel ou mémo écrit) expliquant les mécanismes de traitement des LLMs, la structure d'un prompt directif selon la méthode RIO et l'intérêt du Context Engineering par rapport au prompting naïf.

#### 3. Notions Clés du Sprint à Ne Pas Oublier
*(L'apprenant doit obligatoirement couvrir ces notions et les enrichir par sa propre recherche) :*
- Le principe de complétion statistique d'un LLM et la sensibilité au contexte initial.
- Le triptyque RIO (Rôle, Instruction, Output).
- Le rôle des contraintes négatives pour fiabiliser la conformité des sorties.
- La notion de méta-prompting et la réutilisabilité des gabarits.

#### 4. Points de Réflexion & Auto-Évaluation
- *Pourquoi un prompt demandant simplement « Écris-moi une page Laravel » donne-t-il un résultat inexploitable en production ?*
- *En quoi l'exigence d'un format de sortie strict (Markdown/code brut) protège-t-elle l'intégration dans un pipeline de développement ?*

---

### T.325.112 — Pratique : Guide de prompt
*(Tâche 2 — Réalisation Pratique sur le Projet d'Imitation)*

#### 1. Livrable Attendu
- `livrables/ia/README.md` : Guide opératoire de référence de l'équipe pour l'ingénierie de prompts.

#### 2. Consignes & Jalons de Réalisation
Bâtir le guide opératoire en respectant ces 3 jalons :
1. **Formalisation de la Méthode RIO :** Documenter les trois volets canoniques avec exemples concrets appliqués au développement web.
2. **Standardisation des Règles de Sortie :** Définir la liste des contraintes négatives obligatoires (zéro texte d'accompagnement, code complet sans omission `// TODO`, chemins relatifs stricts).
3. **Banque d'Exemples Annotés :** Fournir au moins 2 exemples types annotés (un prompt de modélisation et un prompt de génération de code).

#### 3. Points de Vigilance
- ⚠️ Le guide ne doit pas être un traité théorique généraliste sur l'IA, mais un guide de travail immédiatement exploitable par la promotion.
- ⚠️ Veiller à la portabilité des exemples.

#### 4. Critères de Validation
- [ ] Le fichier `livrables/ia/README.md` est présent et versionné sous Git.
- [ ] Les règles RIO et les contraintes négatives y sont clairement formalisées.
- [ ] Le guide sert de standard d'équipe pour toutes les étapes suivantes du sprint.

---

### T.325.113 — Prompts & Skills : Méta-prompt Fil Rouge
*(Tâche 3 — Conception Prompts & Skills Projet Fil Rouge)*

#### 1. Positionnement dans le Flux Fil Rouge
- Transposition de l'Étape 1.3 (Outillage Prompt Engineering) vers la chaîne d'outillage transverse du Projet Fil Rouge.

#### 2. Travail à Faire
Concevoir et tester dans `livrables/ia/prompt-creator.prompt.md` le méta-prompt officiel permettant à l'agent IA de générer, sur simple description d'un besoin, le prompt RIO complet et contextualisé pour chaque étape future du Projet Fil Rouge.

#### 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Expert senior en Prompt Engineering et architecture logicielle pour développeurs augmentés.
- **Instruction :** Prendre en entrée la description d'une tâche d'ingénierie logicielle et produire un prompt directif structuré en Rôle / Contexte / Instructions pas-à-pas / Contraintes négatives / Format de sortie.
- **Output :** Bloc Markdown contenant le prompt prêt à être enregistré dans un fichier `*.prompt.md`.
- **Contraintes Négatives :** Le méta-prompt ne doit pas exécuter la tâche lui-même ; il doit **produire le prompt** qui permettra d'exécuter la tâche.

#### 4. Critères de Validation
- [ ] Le fichier `livrables/ia/prompt-creator.prompt.md` est présent et testé.
- [ ] Soumis à une tâche test (ex: « Générer un diagramme de séquence »), il produit un prompt RIO complet, testable et conforme aux standards de la promotion.
