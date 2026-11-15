# Plan des Tutoriels : D.351.1 — Gouvernance Agile Scrum

> **Domaine :** `D.351.1` | **Compétence :** `C.351` — Piloter un projet avec Scrum | **Session :** S01  
> **Niveau de Maturité :** UA-Lab (Atelier pratique guidé)

---

## 1. Description des Unités d'Apprentissage du Domaine

### UA.351.11 [UA-Lab] — Introduction à Scrum

- **Code :** `UA.351.11`
- **Niveau de Maturité :** `UA-Lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 04
- **Positionnement Flux de Travail :** Phase 1 — Cadrage & Gouvernance / Étape 1.2 — Gouvernance d'Équipe Scrum
- **Briques Stack Technique :** Cadre Scrum, Rôles, DoD, Git conventions
- **Compétence :** `C.351` — Piloter un projet avec Scrum
- **Domaine :** `D.351.1` — Gouvernance agile Scrum
- **Durée estimée :** 10 heures
- **Objectif :** Installer la gouvernance agile de la promotion en formation active par projets, s'approprier les 3 piliers empiriques, les 5 valeurs Scrum, les 3 rôles de l'équipe et co-rédiger la charte d'équipe.
- **Description :** Installer la gouvernance agile de la promotion en formation active par projets. L'apprenant s'approprie les 3 piliers empiriques, les 5 valeurs Scrum, les 3 rôles de l'équipe et co-rédige la charte d'équipe définissant les responsabilités partagées et les règles de vie collaborative.
- **Notions Clés Utilisées dans le Sprint :**
  - Les 3 Piliers Empiriques (Transparence, inspection, adaptation).
  - Les 5 Valeurs Scrum (Engagement, courage, focus, ouverture, respect).
  - Les 3 Rôles Scrum adaptés à la pédagogie active (Formateur PO, Scrum Master tournant, Développeurs autonomes).
  - Charte d'équipe agile (Règles d'assiduité, protocole de peer coaching 15/30 min, escalade des difficultés).
  - Definition of Done (DoD) initiale en 7 critères bloquants.
- **Livrables :** Charte d'équipe officielle (`livrables/scrum/charte-equipe.md`) et guide opératoire du Scrum Master (`docs/guide-scrum-pratique.md`).
- **Travail à Faire :** Co-rédiger la charte d'équipe officielle, définir la rotation du rôle de Scrum Master et formaliser le protocole d'entraide active.

---

### UA.351.12 [UA-Lab] — Product Backlog et User Stories

- **Code :** `UA.351.12`
- **Niveau de Maturité :** `UA-Lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 07
- **Positionnement Flux de Travail :** Phase 2 — Analyse des Exigences & Modélisation / Étape 2.2 — Découpage User Stories & Product Backlog
- **Briques Stack Technique :** Product Backlog, User Stories INVEST, Priorisation MoSCoW, Story Points
- **Compétence :** `C.351` — Piloter un projet avec Scrum
- **Domaine :** `D.351.1` — Gouvernance agile Scrum
- **Durée estimée :** 8 heures
- **Objectif :** Décomposer les besoins fonctionnels en User Stories conformes aux critères INVEST et construire le Product Backlog initial priorisé selon MoSCoW.
- **Description :** Structurer et prioriser le carnet de produit Scrum. L'apprenant rédige les User Stories avec critères d'acceptation clairs, applique la grille INVEST et classe les éléments selon la méthode MoSCoW.
- **Notions Clés Utilisées dans le Sprint :**
  - Format canonique User Story (« En tant que... je veux... afin de... »).
  - Critères de qualité INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable).
  - Priorisation MoSCoW (Must, Should, Could, Won't).
  - Estimation relative en Story Points (suite de Fibonacci).
  - Découpage en tranches verticales complètes (pas de saucissonnage horizontal frontend/backend).
- **Livrables :** Product Backlog initial priorisé (`livrables/scrum/product-backlog.md`) et prompt réutilisable (`livrables/ia/prompts/prompt-product-backlog.prompt.md`).
- **Travail à Faire :** Rédiger les User Stories du premier incrément, formaliser les critères d'acceptation, ordonner le backlog et concevoir le prompt d'ingénierie.

---

## 2. Plan des Tutoriels : UA.351.11 [UA-Lab]

### T.351.111 — Théorie : Cadre Scrum
*(Tâche 1 — Présentation Théorique & Exercices d'Assimilation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase 1 — Cadrage & Gouvernance Agile / Étape 1.2 — Gouvernance d'Équipe Scrum.
- **Stack mobilisée :** Méthodologie agile Scrum, gouvernance d'équipe produit.

#### 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches documentaires nécessaires et concevoir une présentation synthétique (support visuel ou mémo écrit) expliquant le fonctionnement du cadre empirique Scrum et justifiant son application dans notre promotion active.

#### 3. Notions Clés du Sprint à Ne Pas Oublier
*(L'apprenant doit obligatoirement couvrir ces notions et les enrichir par sa propre recherche) :*
- Les 3 piliers de l'empirisme (Transparence, Inspection, Adaptation).
- Les 5 valeurs Scrum et leur impact sur le fonctionnement de l'équipe.
- Les 3 rôles officiels (PO, SM, Développeurs) et l'absence de hiérarchie interne.
- Les notions d'auto-organisation, d'engagement et de rotation de rôle.

#### 4. Points de Réflexion & Auto-Évaluation
- *Comment le cadre Scrum permet-il de réagir rapidement face à l'imprévu par rapport à un cycle en cascade ?*
- *Pourquoi le Scrum Master ne doit-il pas agir comme un chef de projet traditionnel ?*

---

### T.351.112 — Pratique : Charte d'équipe
*(Tâche 2 — Réalisation Pratique sur le Projet d'Imitation)*

#### 1. Livrable Attendu
- `livrables/scrum/charte-equipe.md` (ou `scrum/README.md`) : Charte collective de gouvernance signée.

#### 2. Consignes & Jalons de Réalisation
Ne pas recopier de modèle générique ; bâtir la charte en respectant ces 4 jalons :
1. **Rôles & Rotation :** Identifier les membres et fixer le calendrier de rotation hebdomadaire du Scrum Master.
2. **Règles de Vie :** Fixer l'heure précise du Daily (15 min max) et les canaux officiels d'échange.
3. **Protocole de Peer Coaching :** Règle des 15 min de recherche individuelle avant sollicitation d'un pair, puis escalade au SM après 30 min de blocage.
4. **DoD Initiale :** Rédiger 5 à 7 critères d'acceptation minimaux pour l'incrément de sprint.

#### 3. Points de Vigilance
- ⚠️ Éviter les déclarations d'intention vagues ; chaque règle doit être mesurable et opposable.
- ⚠️ La DoD doit être immédiatement testable dès le premier sprint.

#### 4. Critères de Validation
- [ ] Le fichier `livrables/scrum/charte-equipe.md` existe et est versionné sous Git.
- [ ] Le protocole d'escalade des difficultés est explicitement rédigé.
- [ ] La DoD contient au moins 5 critères concrets et vérifiables.

---

### T.351.113 — Prompts & Skills : Gouvernance Scrum Fil Rouge
*(Tâche 3 — Conception Prompts & Skills Projet Fil Rouge)*

#### 1. Positionnement dans le Flux Fil Rouge
- Transposition de l'Étape 1.2 (Gouvernance d'Équipe Scrum) vers l'application métier Fil Rouge (ex : Plateforme Cinéma).

#### 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-gouvernance-scrum.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de générer une charte d'équipe adaptée au contexte spécifique du Projet Fil Rouge.

#### 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Scrum Master senior & coach agile spécialisé dans les équipes produit autonomes.
- **Instruction :** Générer les rôles, les règles de collaboration et la DoD adaptés au thème du Projet Fil Rouge à partir des variables `[THEME_PROJET]` et `[TAILLE_EQUIPE]`.
- **Output :** Document Markdown prêt à être intégré dans le dépôt Fil Rouge.
- **Contraintes Négatives :** Pas de rôles fantaisistes hors Scrum, pas de DoD invérifiable.

#### 4. Critères de Validation
- [ ] Le prompt est testé avec l'agent IA sur le contexte de l'application Fil Rouge.
- [ ] Le résultat généré est cohérent et exploitable sans retouche manuelle majeure.

---

## 3. Plan des Tutoriels : UA.351.12 [UA-Lab]

### T.351.121 — Théorie : Product Backlog
*(Tâche 1 — Présentation Théorique & Exercices d'Assimilation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase 2 — Analyse des Exigences & Modélisation / Étape 2.2 — Découpage User Stories & Product Backlog.
- **Stack mobilisée :** Méthodologie agile Scrum, Product Backlog, User Stories, INVEST, MoSCoW.

#### 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches documentaires nécessaires et formaliser une présentation synthétique (support visuel ou mémo écrit) expliquant la structure d'un carnet de produit Scrum, la décomposition en User Stories selon INVEST et la méthode de priorisation MoSCoW.

#### 3. Notions Clés du Sprint à Ne Pas Oublier
*(L'apprenant doit obligatoirement couvrir ces notions et les enrichir par sa propre recherche) :*
- Le Product Backlog comme artéfact vivant ordonné par valeur métier.
- La structure standard d'une User Story (« En tant que... je veux... afin de... »).
- Les 6 critères de qualité INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable).
- La méthode de priorisation MoSCoW (Must, Should, Could, Won't).
- L'estimation relative en Story Points (suite de Fibonacci) et la règle de non-saucissonnage horizontal.

#### 4. Points de Réflexion & Auto-Évaluation
- *Pourquoi une User Story doit-elle obligatoirement représenter une tranche verticale de valeur et non une tâche technique horizontale ?*
- *Que faire si une exigence est estimée trop volumineuse pour tenir dans un seul sprint ?*

---

### T.351.122 — Pratique : Construction du Product Backlog
*(Tâche 2 — Réalisation Pratique sur le Projet d'Imitation)*

#### 1. Livrable Attendu
- `livrables/scrum/product-backlog.md` : Product Backlog initial priorisé, estimé et documenté.

#### 2. Consignes & Jalons de Réalisation
Bâtir le carnet de produit en respectant ces 4 jalons :
1. **Recensement des Exigences :** Identifier l'ensemble des besoins fonctionnels du *Blog des Lauréats* à partir des cas d'utilisation macro.
2. **Rédaction des User Stories :** Rédiger 8 à 12 PBIs au format standard avec au moins 2 critères d'acceptation par story.
3. **Estimation en Story Points :** Attribuer à chaque PBI une estimation relative (1, 2, 3, 5, 8). Découper tout item supérieur à 8.
4. **Priorisation MoSCoW :** Définir les items Must Have pour le premier sprint (consultation publique d'article) et planifier les suivants.

#### 3. Points de Vigilance
- ⚠️ Interdiction formelle de créer des PBIs techniques purs (« Configurer Apache » ou « Faire le CSS »).
- ⚠️ Chaque PBI doit apporter une valeur observable pour l'utilisateur final.

#### 4. Critères de Validation
- [ ] Le fichier `livrables/scrum/product-backlog.md` est présent et structuré en tableau Markdown.
- [ ] 100% des PBIs respectent le format User Story et les critères INVEST.
- [ ] La sélection des PBIs retenus pour le Sprint 1 est clairement délimitée.

---

### T.351.123 — Prompts & Skills : Product Backlog Fil Rouge
*(Tâche 3 — Conception Prompts & Skills Projet Fil Rouge)*

#### 1. Positionnement dans le Flux Fil Rouge
- Transposition de l'Étape 2.2 (Découpage User Stories & Product Backlog) vers l'application métier Fil Rouge (ex : Plateforme Cinéma).

#### 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-product-backlog.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de produire le Product Backlog complet et ordonné pour le Projet Fil Rouge.

#### 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Product Owner senior expert en analyse de la valeur et backlog grooming agile.
- **Instruction :** Prendre en entrée le thème du Projet Fil Rouge `[THEME_PROJET]` et la liste des acteurs identifiés pour générer un Product Backlog tabulaire complet (10 à 15 User Stories, critères d'acceptation, points Fibonacci et priorité MoSCoW).
- **Output :** Tableau Markdown directement intégrable dans le carnet agile du projet Fil Rouge.
- **Contraintes Négatives :** Pas de saucissonnage horizontal, pas de formulations techniques hors User Story.

#### 4. Critères de Validation
- [ ] Le prompt est testé avec l'agent IA sur le contexte de l'application Fil Rouge.
- [ ] Le backlog généré couvre l'ensemble des parcours utilisateurs du projet avec une priorisation cohérente.
