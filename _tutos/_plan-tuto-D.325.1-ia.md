# Plan des Tutoriels : D.325.1 — Ingénierie de Prompt et Agents IA

> **Domaine :** `D.325.1` | **Compétence :** `C.325` — Concevoir des Agents IA et développer des Skills | **Session :** S1  
> **Niveau de Maturité :** UA-Lab (Atelier pratique guidé)  
> **Branche Git de Travail :** `sprint1`  
> **Mentor de Domaine :** `.agents/skills/domaine-ia/SKILL.md`

---

## 1. Description des Unités d'Apprentissage du Domaine

### UA.325.11 — Initialisation de l'Agent IA & Architecture des Skills

- **Code :** `UA.325.11`
- **Maturité :** `UA-Lab` (Atelier pratique guidé)
- **Ordre en Session :** Étape 02
- **Positionnement Flux de Travail :** Phase A — Outillage IA, Gouvernance & Cadrage / Étape 2 — Initialisation de l'Agent IA
- **Compétence :** `C.325` — Concevoir des Agents IA et développer des Skills
- **Domaine :** `D.325.1` — Ingénierie de prompt et agents IA
- **Durée estimée :** 6 heures
- **Objectif :** Maîtriser le dialogue déterministe avec les modèles de langage (méthode RIO, patterns de prompt), comprendre l'architecture d'un Agent IA (règles Always-On vs compétences modulaires), concevoir en atelier le skill modulaire `skill-presentation` avec sa mission Marp, puis outiller le projet d'imitation avec les règles permanentes et le skill de démarrage `gestion-depot`.
- **Description :** Accompagné par le skill mentor `domaine-ia`, l'apprenant franchit les étapes de découverte, formalisation et pratique agentique. Il produit les synthèses techniques et diaporamas de soutenance pour chaque étape, et déploie les règles et compétences réelles sur le projet *Blog des Lauréats*.
- **Notions Clés :**
  - Méthode directrice RIO : Rôle précis (persona d'expert), Instructions fermées avec contraintes négatives, Output strict sans tableau.
  - Patterns fondamentaux : Persona, Template, Constraint, Step-by-Step, Reflective.
  - Paliers d'autonomie et architecture de l'agent : LLM brut vs Chatbot passif vs Agent IA autonome outillé.
  - Rules Always-On (`.agents/rules/`) vs Skills modulaires (`.agents/skills/`).
  - Découvrabilité native d'un skill (frontmatter YAML, plafond $\le 75$ lignes, missions spécialisées).
  - Outillage de l'étape d'initialisation de dépôt (`skills-dev`, `gestion-depot`).
- **Livrables :**
  - Livrables d'apprentissage sous `tutoriels/ia/agent-skills/` :
    - `prompt-engineering/` : `prompt-engineering.md`, `presentation-prompt-engineering.md`
    - `agent-ia/` : `agent-ia.md`, `presentation-agent-ia.md`
    - `skill-presentation/` : `skill-presentation.md`, `presentation-skill-presentation.md`, `SKILL.md`, `missions/marp-slides.md`, `skill-presentation.command.md`
  - Livrables d'outillage projet sous le *Blog des Lauréats* :
    - Règles Always-On : `.agents/rules/contexte-projet.md`, `.agents/rules/regles-generales.md`
    - Skills : `.agents/skills/skills-dev/`, `.agents/skills/gestion-depot/` (`missions/init-depot.md`, `missions/init-projet.md`)
    - Journal CLI : `tutoriels/ia/agent-skills/skill-gestion-depot/skill-gestion-depot.command.md`
- **Travail à Faire :** Assimiler le Prompt Engineering et la méthode RIO, explorer l'architecture d'un Agent IA, concevoir en atelier le skill d'exemple `skill-presentation` avec sa mission Marp, puis outiller le projet d'imitation avec les règles Always-On et le skill de démarrage `gestion-depot`.

---

## 2. Plan des Tutoriels : UA.325.11

### T.325.111 — Théorie : Prompt Engineering & Méthode RIO
*(Tâche 1 — Présentation Théorique & Notions Fondamentales)*

- **Slug :** `prompt-engineering` | **Maturité :** `UA-Lab` | **Nav Order :** 1
- **Travail à faire :** Rédiger la fiche technique et le diaporama Marp formalisant le fonctionnement d'un LLM, la méthode RIO, l'injection chirurgicale de contexte et les patterns fondamentaux.
- **Livrables attendus :**
  - Fiche technique : `tutoriels/ia/agent-skills/prompt-engineering/prompt-engineering.md`
  - Diaporama Marp : `tutoriels/ia/agent-skills/prompt-engineering/presentation-prompt-engineering.md`

---

### T.325.112 — Théorie : Architecture d'un Agent IA et Règles Always-On
*(Tâche 2 — Présentation Théorique & Notions Fondamentales)*

- **Slug :** `agent-ia` | **Maturité :** `UA-Lab` | **Nav Order :** 2
- **Travail à faire :** Rédiger la fiche technique et le diaporama Marp explicitant les 3 paliers d'autonomie (LLM vs Chatbot vs Agent), le cycle Perception/Action, l'architecture Rules Always-On vs Skills modulaires, et la découvrabilité native.
- **Livrables attendus :**
  - Fiche technique : `tutoriels/ia/agent-skills/agent-ia/agent-ia.md`
  - Diaporama Marp : `tutoriels/ia/agent-skills/agent-ia/presentation-agent-ia.md`

---

### T.325.113 — Pratique : Conception d'un skill agentique — Exemple skill-presentation
*(Tâche 3 — Atelier Pratique Guidé Autonome)*

- **Slug :** `skill-presentation` | **Maturité :** `UA-Lab` | **Nav Order :** 3
- **Travail à faire :** Concevoir et tester en autonomie le skill modulaire d'exemple `skill-presentation` avec son orchestrateur `SKILL.md` ($\le 75$ lignes), sa mission opératoire `missions/marp-slides.md`, son compte-rendu technique et son diaporama Marp.
- **Livrables attendus :**
  - Compte-rendu technique : `tutoriels/ia/agent-skills/skill-presentation/skill-presentation.md`
  - Diaporama Marp : `tutoriels/ia/agent-skills/skill-presentation/presentation-skill-presentation.md`
  - Skill fonctionnel : `tutoriels/ia/agent-skills/skill-presentation/SKILL.md` et `missions/marp-slides.md`
  - Journal CLI : `tutoriels/ia/agent-skills/skill-presentation/skill-presentation.command.md`

---

### T.325.114 — Application : Outiller l'étape d'initialisation avec le skill gestion-depot
*(Tâche 4 — Déploiement Réel sur le Blog des Lauréats)*

- **Slug :** `skill-gestion-depot` | **Maturité :** `UA-Tâche` | **Nav Order :** 4
- **Travail à faire :** Déployer sur le projet d'imitation le socle de règles permanentes `.agents/rules/` (`contexte-projet.md`, `regles-generales.md`), le skill méta-gouvernance `skills-dev` et le skill opérationnel `gestion-depot` avec ses deux missions (`init-depot.md` et `init-projet.md`).
- **Livrables attendus :**
  - Règles permanentes : `.agents/rules/contexte-projet.md`, `.agents/rules/regles-generales.md`
  - Skills projet : `.agents/skills/skills-dev/SKILL.md`, `.agents/skills/gestion-depot/SKILL.md` (avec `missions/init-depot.md` et `missions/init-projet.md`)
  - Journal CLI : `tutoriels/ia/agent-skills/skill-gestion-depot/skill-gestion-depot.command.md`
