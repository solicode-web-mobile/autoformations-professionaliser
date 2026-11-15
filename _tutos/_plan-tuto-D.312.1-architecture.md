# Plan des Tutoriels : D.312.1 — Architecture Logicielle en Couches

> **Domaine :** `D.312.1` | **Compétence :** `C.312` — Concevoir et structurer l'architecture logicielle | **Session :** S01  
> **Niveau de Maturité :** UA-Lab (Atelier pratique guidé)  
> **Référentiels Liés :** [`../../3.sprints/flux-travail-n3.md`](../../3.sprints/flux-travail-n3.md) | [`../../3.sprints/stack-technique-n3.md`](../../3.sprints/stack-technique-n3.md)

---

## 1. Description des Unités d'Apprentissage du Domaine

### UA.312.11 — Architecture logicielle en deux couches

- **Code :** `UA.312.11`
- **Maturité :** `UA-lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 08
- **Positionnement Flux de Travail :** Phase 3 — Conception & Architecture Logicielle / Étape 3.1 — Découplage Architectural & Décision ADR
- **Briques Stack Technique :** Architecture 2 couches, Contrôleur mince IoC, Classe Service, ADR, Mermaid séquence
- **Compétence :** `C.312` — Concevoir et structurer l'architecture logicielle
- **Domaine :** `D.312.1` — Architecture logicielle en couches
- **Durée estimée :** 8 heures
- **Objectif :** Concevoir une architecture logicielle découplée isolant le contrôleur mince de la persistance tabulaire via une classe Service dédiée et formaliser ce choix technique stratégique dans un ADR opposable avec diagramme de séquence HTTP.
- **Description :** Isoler la logique de présentation de la logique métier et d'accès aux données. L'apprenant conçoit l'architecture en deux couches, rédige l'ADR-01 justifiant le choix sans base de données relationnelle initiale et modélise la séquence HTTP.
- **Notions Clés Utilisées dans le Sprint :**
  - Principe de séparation des responsabilités (SoC) : découplage strict entre couche de présentation HTTP et logique métier/données.
  - Patron architectural en 2 couches : Contrôleur mince (orchestration HTTP) $\to$ Classe Service (métier et abstraction des données).
  - Décision technique de persistance transitoire : choix délibéré d'une source tabulaire CSV en mémoire (`articles.csv`), zéro SGBD relationnel en amorçage S1.
  - Architecture Decision Record (ADR) : formalisation standardisée de l'ADR-01 (Titre, Statut, Contexte, Décision, Alternatives écartées, Conséquences).
  - Modélisation de flux HTTP en séquence : diagramme Mermaid `sequenceDiagram` illustrant le parcours complet de la requête (cas nominal et cas d'erreur 404).
- **Livrables :** Dossier d'architecture S1 et ADR-01 (`livrables/architecture/architecture-sprint1.md`) et prompt réutilisable (`livrables/ia/prompts/prompt-architecture.prompt.md`).
- **Travail à Faire :** Rédiger l'ADR-01, modéliser le diagramme de séquence en Mermaid.js et concevoir le prompt d'ingénierie d'architecture.

---

## 2. Plan des Tutoriels : UA.312.11

### T.312.111 — Théorie : Architecture 2 couches
*(Tâche 1 — Présentation Théorique & Exercices d'Assimilation)*

#### 1. Positionnement dans le Flux & la Stack
- **Position dans le flux :** Phase 3 — Conception & Architecture Logicielle / Étape 3.1 — Découplage Architectural & Décision ADR.
- **Stack mobilisée :** Principes SOLID (Single Responsibility), patrons d'architecture MVC et Services, formalisme ADR.

#### 2. Travail à Faire (Ce que l'Apprenant Doit Produire)
Effectuer les recherches nécessaires et concevoir une présentation synthétique (support visuel ou mémo écrit) expliquant le principe de séparation des responsabilités, les dangers des « contrôleurs obèses » (*Fat Controllers*), l'intérêt du patron Classe Service pour isoler l'accès aux données et la méthodologie de traçabilité des choix par les ADRs.

#### 3. Notions Clés du Sprint à Ne Pas Oublier
*(L'apprenant doit obligatoirement couvrir ces notions et les enrichir par sa propre recherche) :*
- Le principe SoC (Separation of Concerns).
- Le rôle précis d'un contrôleur mince (recevoir la requête HTTP, appeler le service, retourner la réponse Blade).
- Le rôle d'une classe Service comme frontière métier indépendante du protocole web.
- La structure formelle d'un ADR et les critères d'une décision d'ingénierie traçable.

#### 4. Points de Réflexion & Auto-Évaluation
- *Pourquoi est-il stratégique de démarrer le Sprint 1 avec une classe Service lisant un CSV plutôt que de coder des requêtes SQL directes dans le contrôleur ?*
- *Quand nous remplacerons le CSV par une base relationnelle au Sprint 2, quel composant sera modifié et quel composant restera intact ?*

---

### T.312.112 — Pratique : Décision d'architecture (ADR)
*(Tâche 2 — Réalisation Pratique sur le Projet d'Imitation)*

#### 1. Livrable Attendu
- `livrables/architecture/architecture-sprint1.md` (contenant l'ADR-01 et le diagramme de séquence Mermaid).

#### 2. Consignes & Jalons de Réalisation
Bâtir le livrable d'architecture en respectant ces 3 jalons :
1. **Rédaction de l'ADR-01 :** Documenter le choix de l'architecture 2 couches avec persistance tabulaire CSV (justifier le gain de temps pour l'amorçage et l'absence de configuration SGBD initiale).
2. **Analyse d'Impact & Conséquences :** Lister les bénéfices (rapidité, simplicité, testabilité) et les contraintes acceptées (pas de transactions, volumétrie limitée).
3. **Modélisation de la Séquence HTTP :** Rédiger le diagramme `sequenceDiagram` décrivant l'enchaînement : Navigateur $\to$ Route $\to$ `ArticleController` $\to$ `ArticleService` $\to$ Vue Blade $\to$ Réponse 200 (ainsi que la branche d'exception 404).

#### 3. Points de Vigilance
- ⚠️ L'ADR doit exposer clairement les alternatives qui ont été rejetées (ex: monolithe sans service, ORM direct).
- ⚠️ Le diagramme de séquence doit refléter scrupuleusement les classes et méthodes réelles du code.

#### 4. Critères de Validation
- [ ] Le fichier `livrables/architecture/architecture-sprint1.md` existe et adopte le formalisme canonique ADR.
- [ ] Le diagramme de séquence Mermaid est syntaxiquement valide.
- [ ] L'isolation entre couche de présentation et couche de données est formellement garantie.

---

### T.312.113 — Prompts & Skills : Architecture et ADR Fil Rouge
*(Tâche 3 — Conception Prompts & Skills Projet Fil Rouge)*

#### 1. Positionnement dans le Flux Fil Rouge
- Transposition de l'Étape 3.1 (Découplage Architectural & Décision ADR) vers l'application métier Fil Rouge (ex : Plateforme Cinéma).

#### 2. Travail à Faire
Concevoir dans `livrables/ia/prompts/prompt-architecture.prompt.md` le prompt d'ingénierie réutilisable permettant à un agent IA de produire le dossier d'architecture découplée et l'ADR adapté au Projet Fil Rouge.

#### 3. Cahier des Charges du Prompt (Méthode RIO)
- **Rôle :** Architecte logiciel senior spécialisé en découplage d'applications web et Clean Architecture.
- **Instruction :** Prendre en entrée les contraintes du Projet Fil Rouge `[THEME_PROJET]` et formaliser la décision d'architecture 2 couches avec son ADR complet et le diagramme de séquence Mermaid associé.
- **Output :** Document Markdown prêt pour le dossier d'architecture du projet Fil Rouge.
- **Contraintes Négatives :** Pas de préconisation de micro-services disproportionnés, rester dans le cadre du socle 2 couches défini.

#### 4. Critères de Validation
- [ ] Le prompt est testé sur l'application Fil Rouge.
- [ ] L'ADR généré est pertinent, argumenté et directement intégrable dans le dépôt.
