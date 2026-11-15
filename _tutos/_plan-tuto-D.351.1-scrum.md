# Plan des Tutoriels : D.351.1 — Gouvernance Agile Scrum

> **Domaine :** `D.351.1` | **Compétence :** `C.351` — Piloter un projet avec Scrum | **Session :** S01  
> **Niveau de Maturité :** UA-Lab (Atelier pratique guidé)  
> **Branche Git de Travail :** `sprint1`  
> **Référentiels Liés :** [`../../3.sprints/flux-travail-n3.md`](../../3.sprints/flux-travail-n3.md) | [`../../3.sprints/stack-technique-n3.md`](../../3.sprints/stack-technique-n3.md)

---

## 1. Description des Unités d'Apprentissage du Domaine

### UA.351.11 — Introduction à Scrum

- **Code :** `UA.351.11`
- **Maturité :** `UA-Lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 02
- **Positionnement Flux de Travail :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 1.2 — Gouvernance d'Équipe Scrum
- **Briques Stack Technique :** Cadre Scrum, Rôles, Cérémonies, Artéfacts, Charte d'équipe
- **Compétence :** `C.351` — Piloter un projet avec Scrum
- **Domaine :** `D.351.1` — Gouvernance agile Scrum
- **Durée estimée :** 4 heures
- **Objectif :** Installer la gouvernance agile de la promotion en formation active par projets en s'appropriant les 3 piliers empiriques, les rôles et cérémonies Scrum pour contractualiser une charte d'équipe engageante.
- **Description :** Installer la gouvernance agile de l'équipe. L'apprenant s'approprie les 3 piliers empiriques, les 3 rôles, les 5 événements/cérémonies Scrum et co-rédige la charte d'équipe définissant les responsabilités partagées et les règles de vie collaborative.
- **Notions Clés Utilisées dans le Sprint :**
  - Les 3 Piliers Empiriques (Transparence, inspection, adaptation).
  - Les 3 Rôles Scrum (Product Owner, Scrum Master, Développeurs).
  - Les 5 Événements/Cérémonies Scrum (Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective).
  - Les 3 Artéfacts Scrum (Product Backlog, Sprint Backlog, Incrément déployable).
  - Charte d'équipe agile (Horaires du Daily, protocole d'entraide peer coaching, rotation du rôle de Scrum Master).
- **Livrable :** Charte d'équipe de la promotion (`scrum/charte-equipe.md`) sur la branche `sprint1`.
- **Travail à Faire :** Co-rédiger la charte d'équipe sur le Projet d'imitation, formaliser les règles de fonctionnement collectif et le calendrier des cérémonies.

---

### UA.351.12 — Product Backlog et User Stories

- **Code :** `UA.351.12`
- **Maturité :** `UA-Lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 05
- **Positionnement Flux de Travail :** Phase B — Analyse, Conception & Planification / Étape 2.2 — Découpage User Stories & Product Backlog
- **Briques Stack Technique :** Product Backlog, User Stories INVEST, Priorisation MoSCoW, Story Points
- **Compétence :** `C.351` — Piloter un projet avec Scrum
- **Domaine :** `D.351.1` — Gouvernance agile Scrum
- **Durée estimée :** 6 heures
- **Objectif :** Découper les fonctionnalités globales du blog en User Stories indépendantes selon le standard INVEST pour formaliser le Product Backlog ordonné et priorisé selon la méthode MoSCoW.
- **Description :** Structurer et prioriser le carnet de produit Scrum pour le Projet d'imitation. L'apprenant s'approprie la définition formelle du Product Backlog, rédige les User Stories avec critères d'acceptation, applique la grille INVEST et ordonnance le carnet selon MoSCoW.
- **Notions Clés Utilisées dans le Sprint :**
  - Définition formelle du Product Backlog : source unique, vivante et ordonnancée par la valeur sous la responsabilité du PO.
  - Format canonique User Story (« En tant que... je veux... afin de... »).
  - Critères de qualité INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable).
  - Priorisation MoSCoW (Must, Should, Could, Won't) et critères d'acceptation Gherkin.
- **Livrables :** Product Backlog initial priorisé (`livrables/scrum/product-backlog.md`) et prompt réutilisable (`livrables/ia/prompts/prompt-product-backlog.prompt.md`) sur la branche `sprint1`.
- **Travail à Faire :** Construire le Product Backlog du Blog des Lauréats, formaliser les critères d'acceptation et concevoir le prompt `prompt-product-backlog`.

---

## 2. Plan des Tutoriels : UA.351.11

### T.351.111 — Théorie : Cadre Scrum, Rôles & Cérémonies
*(Tâche 1 — Présentation Théorique & Exercices d'Assimilation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 1.2 — Gouvernance d'Équipe Scrum.
- **Stack mobilisée :** Méthodologie agile Scrum, gouvernance d'équipe produit.

#### 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches nécessaires et formaliser une fiche de synthèse expliquant le fonctionnement du cadre empirique Scrum, les rôles et le déroulement des cérémonies.

#### 3. Répartition Didactique (Règle des 20/80)
- **Les 20% fournis directement au tutoriel :**
  - *Les 3 Rôles Scrum :* Product Owner (porteur de valeur et des priorités), Scrum Master (garant du cadre et facilitateur), Développeurs (responsables de l'incrément et de la qualité technique).
  - *Les 5 Événements/Cérémonies :* Le Sprint, le Sprint Planning, le Daily Scrum, la Sprint Review et la Sprint Retrospective.
  - *Les 3 Artéfacts & les 3 Piliers :* Product Backlog, Sprint Backlog, Incrément conforme à la DoD ; Transparence, Inspection, Adaptation.
- **Les 80% recherchés par l'apprenant :**
  - Déroulement opérationnel et timebox de chaque cérémonie (les 3 questions clés du Daily Scrum, la règle des 15 minutes, l'escalade des blocages).
  - Les 5 valeurs Scrum (Engagement, Courage, Focus, Ouverture, Respect).

#### 4. Livrable Attendu
- Fiche de synthèse des rôles et cérémonies intégrée dans le journal d'apprentissage.

---

### T.351.112 — Pratique : Charte d'équipe & Organisation
*(Tâche 2 — Réalisation Pratique sur le Projet d'Imitation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 1.2 — Charte d'Équipe.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `scrum/charte-equipe.md`

#### 2. Travail à Faire (Projet d'Imitation)
L'apprenant applique les notions de rôles et de cérémonies pour co-rédiger avec le formateur la Charte d'équipe de la promotion pour le *Blog des Lauréats* :
1. **Rôles & Rotation :** Calendrier de rotation du Scrum Master.
2. **Règles de Vie :** Horaire fixe du Daily Scrum (9h00, 15 min max) et canaux officiels d'échange.
3. **Protocole de Peer Coaching :** Règle des 15 min de recherche individuelle avant sollicitation d'un pair, puis escalade au Scrum Master après 30 min de blocage.

#### 3. Critères de Validation
- [ ] Le fichier `scrum/charte-equipe.md` existe et est versionné sur la branche `sprint1`.
- [ ] Le protocole d'escalade des difficultés et la rotation du Scrum Master y sont explicitement rédigés.

---

## 3. Plan des Tutoriels : UA.351.12

### T.351.121 — Théorie : Product Backlog et User Stories
*(Tâche 1 — Présentation Théorique & Exercices d'Assimilation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase B — Analyse, Conception & Planification / Étape 2.2 — Découpage User Stories & Product Backlog.
- **Stack mobilisée :** Méthodologie agile Scrum, Product Backlog, User Stories, INVEST, MoSCoW.

#### 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches nécessaires et concevoir un support synthétique expliquant la structure d'un carnet de produit Scrum et le découpage en User Stories selon les critères INVEST.

#### 3. Répartition Didactique (Règle des 20/80)
- **Les 20% fournis directement au tutoriel :**
  - **Définition primordiale du Product Backlog :** La source unique, centralisée et vivante de tout ce qui est nécessaire dans le produit. C'est un carnet ordonnancé selon la valeur métier sous l'autorité exclusive du Product Owner.
  - **Structure canonique de la User Story :** « En tant que [rôle], je veux [action] afin de [valeur métier / bénéfice] ».
  - **Les critères INVEST** (Independent, Negotiable, Valuable, Estimable, Small, Testable) et les 4 priorités MoSCoW (Must, Should, Could, Won't).
- **Les 80% recherchés par l'apprenant :**
  - Techniques de rédaction de critères d'acceptation exploitables (formulation Gherkin / Given-When-Then).

#### 4. Livrable Attendu
- Grille d'évaluation INVEST complétée.

---

### T.351.122 — Pratique : Construction du Product Backlog initial
*(Tâche 2 — Réalisation Pratique sur le Projet d'Imitation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase B — Analyse, Conception & Planification / Étape 2.2 — Carnet Produit Initial.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/scrum/product-backlog.md`

#### 2. Travail à Faire (Projet d'Imitation)
Bâtir le carnet de produit du *Blog des Lauréats* :
1. **Recensement des Exigences :** Identifier les besoins fonctionnels à partir des cas d'utilisation macro.
2. **Rédaction des User Stories :** Rédiger les PBIs au format standard avec critères d'acceptation.
3. **Priorisation MoSCoW :** Définir les items Must Have pour le premier sprint (consultation publique d'article).

#### 3. Critères de Validation
- [ ] Le fichier `livrables/scrum/product-backlog.md` est présent et structuré en tableau Markdown sur la branche `sprint1`.
- [ ] 100% des PBIs respectent le format User Story et les critères INVEST.

---

### T.351.123 — Création du prompt-product-backlog
*(Tâche 3 — Transposition IA)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase B — Analyse, Conception & Planification / Étape 2.2 — Automatisation du Backlog.
- **Branche Git de travail :** `sprint1`
- **Fichiers modifiés ou créés :** `livrables/ia/prompts/prompt-product-backlog.prompt.md`

#### 2. Travail à Faire
Concevoir et tester dans `livrables/ia/prompts/prompt-product-backlog.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de produire le Product Backlog complet et ordonné pour l'application métier.

#### 3. Missions Concrètes Réalisées par le Prompt
1. Analyser les besoins fonctionnels d'une application métier et les découper en User Stories INVEST complètes.
2. Rédiger pour chaque User Story des critères d'acceptation testables selon le formalisme Given-When-Then.
3. Ordonnancer et prioriser les User Stories selon MoSCoW en isolant le périmètre fonctionnel du premier Sprint.

#### 4. Critères de Validation
- [ ] Le fichier `livrables/ia/prompts/prompt-product-backlog.prompt.md` est présent et testé sur la branche `sprint1`.
- [ ] Le backlog généré couvre l'ensemble des parcours utilisateurs avec une priorisation cohérente.
