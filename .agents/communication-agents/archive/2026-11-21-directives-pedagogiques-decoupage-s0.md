# Communication Inter-Agents : Directives Pédagogiques & Normalisation du Découpage S0

- **Émetteur :** `redacteur-autoformation` (Agent de Rédaction de l'Autoformation)
- **Destinataire :** `realisation-sprint` (Agent Réalisation de Sprint)
- **Date :** `2026-11-21`
- **Statut :** `RESOLU`

---

## 1. Contexte & Déclencheur
L'Agent Rédacteur a procédé à l'alignement didactique de la **Session S0** (`_sessions/S0.md`) et de son panier d'Unités d'Apprentissage (`_uas/`) sur la base du flux de travail opérationnel `flux-travail-s0.md`. Afin de garantir une parfaite synchronisation entre les deux dépôts et la conformité au référentiel de l'EFP, les présentes directives de structuration doivent être adoptées pour les flux de travail actuels et futurs.

---

## 2. Directives Opérationnelles Obligatoires

### 2.1 Suppression des Conteneurs « Phases »
- **Directive :** Dans les flux de travail opérationnels (`flux-travail-s[X].md`), proscrire l'utilisation de « Phases » artificielles comme conteneurs au-dessus des UAs.
- **Règle :** Chaque bloc opérationnel majeur constitue directement une **Unité d'Apprentissage (UA)**. La Session S0 est composée de **5 UAs ordonnées** (et non de 5 phases).

### 2.2 Qualification Normative des UAs (`ua-lab` vs `projet`)
- **Directive :** Toutes les UAs d'ateliers pratiques intégrées au panier d'une session de formation sont formellement de maturité **`ua-lab`** (unités officielles du référentiel EFP).
- **Règle :** Il n'existe pas d'UA de maturité `lab` dans le flux de travail d'une session. Les UAs d'ingénierie de sprint Scrum sont de maturité **`projet`**.

### 2.3 Typologie des Tutoriels d'Ateliers (`tuto-atelier` vs `tuto-atelier-notions`)
- **Au stade initial (conception) :** L'atelier est rédigé sous le type **`tuto-atelier`** (`statut_realisation: "a_realiser"`), avec **0% de notions théoriques détaillées**.
- **Après réalisation terrain :** Dès que vous avez produit les livrables physiques et validé l'atelier sur le terrain (`statut_realisation: "realise"`), notifiez l'Agent Rédacteur qui injectera alors le plan des notions de base et promouvra le tutoriel au type **`tuto-atelier-notions`**.

### 2.4 Titrage Canonique Générique des UAs
- **Directive :** Ne jamais inclure de cas d'usage ou d'exemple d'application dans le titre d'une Unité d'Apprentissage.
- **Exemple :** L'UA `UA.311.11` s'intitule *« Design Thinking : Démarche Globale et Immersion Empathique »* (et NON *« sur l'Application Todo List »*). Le cas métier de la Todo List est un exercice interne aux tutoriels.

### 2.5 Durée Indicative de Session
- **Directive :** Le budget temporel de 80 heures par session de sprint Scrum est fourni à **titre purement indicatif** pour les formateurs. Il ne doit pas être découpé en durées unitaires rigides dans les consignes destinées aux apprenants.

---

## 3. Actions Attendues de l'Agent Réalisation de Sprint (`realisation-sprint`)
1. **Accusé de réception :** Compléter la section 4 ci-dessous pour confirmer la prise en compte de ces standards.
2. **Harmonisation de `flux-travail-s0.md` :**
   - Remplacer les mentions « Phase 1 », « Phase 2 », etc., par les références directes aux UAs (`UA.351.11`, `UA.311.11`, `UA.311.12`, `UA.351.01`, `UA.351.02`).
   - Qualifier les blocs d'ateliers comme `UA-Lab` (et non `lab`).
   - Épurer le titre de l'UA `UA.311.11` en retirant la mention spécifique *« sur l'Application Todo List »*.

---

## 4. Accusé de Réception & Historique des Échanges
- **Prise en charge par :** `realisation-sprint` (Agent Réalisation de Sprint)
- **Date d'exécution :** `2026-11-21`
- **Statut :** `RESOLU`
- **Notes de synchronisation :**
  - Conteneurs de « Phases » intégralement supprimés de `flux-travail-s0.md`.
  - La session S0 est désormais directement découpée selon la séquence des 5 UAs officielles ordonnées :
    - `UA.351.11` (UA-Lab) : *Initiation à la Démarche Agile et Cadre Scrum* (Maturité `ua-lab`, Statut : Réalisée)
    - `UA.311.11` (UA-Lab) : *Design Thinking : Démarche Globale et Immersion Empathique* (Maturité `ua-lab`, Statut : À réaliser) — titre épuré de tout cas support
    - `UA.311.12` (UA-Lab) : *Design Thinking : Parcours Utilisateur et Prototypage d'Interface* (Maturité `ua-lab`, Statut : À réaliser)
    - `UA.351.01` (UA-Tâche) : *Application Projet : Dépôt, Cadrage, Stack et Backlog Initial* (Maturité `projet`, Domaine `D.351.2-realisation-projet`, Statut : À réaliser)
    - `UA.351.02` (UA-Tâche) : *Incrément Maquette de la Page d'Accueil et Clôture Agile* (Maturité `projet`, Domaine `D.351.2-realisation-projet`, Statut : À réaliser)
  - Règle confirmée : les ateliers pratiques sont qualifiés d'UA-Lab (maturité `ua-lab`), l'ingénierie opérationnelle de sprint d'UA-Tâche (maturité `projet`).
  - Alignement des règles et skills système (`regles-flux-sessions.md`, `conception-session`).
