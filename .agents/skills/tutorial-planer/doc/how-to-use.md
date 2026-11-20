# Guide d'Utilisation du Skill : tutorial-planer

## 1. Présentation & Rôle
`tutorial-planer` est l'**architecte et ingénieur de la progression pédagogique** des tutoriels au sein du cursus Solicode (Niveaux N1, N2 ou N3 selon le dépôt courant).  
Il intervient en amont de `tutorial-writer`, `tutorial-lab-writer` et `tutorial-task-writer` pour concevoir, auditer et ordonnancer les plans de réalisation technique par session ou sprint :
- En N1/N2 : `_plan-réalisation-tutos/S[X]/plan-developpement.md`.
- En N3 : Plans par domaine `_tutos/_plan-tuto-D.XXX.Y-[nom].md` et cadrage de session `_sessions/S[X].md` / `_tutos/D.XXX.Y/_S0X.md`.

Sa mission est d'assurer une progression continue sans rupture cognitive ($E_{n-1} \rightarrow E_n$), de garantir l'intégrité référentielle des entités Jekyll (`_sessions/`, `_domaines/`, `_uas/`), de respecter le calibrage de sprint (80h en N3) et d'initialiser les fichiers de tutoriels.

---

## 2. Cas d'Usage Principaux
- Cadrage et découpage d'un nouveau sprint de 80h en N3 à travers les 4 phases (A: Outillage & Cadrage, B: Analyse & Planification, C: Réalisation, D: Clôture).
- Conception des plans de tutoriels par domaine (`_tutos/_plan-tuto-D.XXX.Y-[nom].md`).
- Audit et simplification de plans de sessions existants pour éliminer redondances et tâches non pertinentes.
- Arbitrage d'outillage IA : planification des prompts uniquement pour les étapes récurrentes du flux de travail produisant des livrables de sprint.
- Alignement des entités Jekyll (`_sessions/S[X].md`, `_domaines/`, `_uas/`).
- Initialisation des fichiers de tutoriels (stubs `en_construction: true`) et bascule vers `en_construction: false` dès validation.

---

## 3. Prompts Types d'Invocation

```markdown
# Cadrage d'une session de sprint N3 (80h)
@[.agents/skills/tutorial-planer/SKILL.md] Conçois la planification de la Session S01 en 80h réparties sur les 4 phases A, B, C et D selon le flux de travail Scrum.
```

```markdown
# Audit et mise en conformité d'un plan de domaine existant
@[_tutos/_plan-tuto-D.321.1-laravel.md] @[.agents/skills/tutorial-planer/SKILL.md] /plan
Audite ce plan selon les standards N3, élimine les théories superflues, réserve les prompts aux flux récurrents et calibre la branche sprint1.
```

```markdown
# Alignement automatique des entités Jekyll et création des stubs
@[.agents/skills/tutorial-planer/SKILL.md] Aligne la liste uas de la fiche session _sessions/S1.md et crée les fichiers stubs de tutoriels sous _tutos/.
```

---

## 4. Prérequis & Données d'Entrée
- **Cadrage de Session :** Durée verrouillée à 80h (10 jours $\times$ 8h/j en N3) et branche Git `sprintX`.
- **Référentiel de Compétences :** Fiches `_modules/`, `_competences/`, `_domaines/` et `_uas/`.
- **Ciblage du Projet :** Tous les tutoriels ciblent le projet d'application ou d'imitation configuré dans les règles du projet (`.agents/rules/`).
- **Règles applicables :**
  - `.agents/rules/pedagogie-spartel-n3.md` (Pareto 20/80, zéro théorie en tâche, pas de durée aux apprenants).
  - `.agents/rules/standards-techniques.md` (UTF-8 sans BOM, livrables de code source et markdown).

---

## 5. Déroulement Pas-à-Pas (Ce que fait l'Agent)
1. **Étape 1 — Analyse du Périmètre & Cadrage Temporel :** Verrouille la durée globale à 80h pour le sprint.
2. **Étape 2 — Structuration en 4 Phases Chronologiques :**
   - Phase A : Outillage IA, Gouvernance & Cadrage.
   - Phase B : Analyse des Exigences, Conception & Planification.
   - Phase C : Réalisation Applicative & Code Cible.
   - Phase D : Clôture de Sprint, Rétrospective & Bilan.
3. **Étape 3 — Découpage Séquentiel Sans Rupture :** Ordonnance les UAs et tutoriels de manière strictement continue ($1 \dots N$).
4. **Étape 4 — Filtrage des Prompts & Théories :**
   - Supprime les théories déjà acquises aux niveaux antérieurs (ex : diagrammes UML déjà maîtrisés en N2).
   - Réserve la création de prompts aux seules étapes récurrentes de flux de travail.
5. **Étape 5 — Synchronisation des Entités Jekyll :** Crée ou aligne `_sessions/S[X].md`, `_domaines/` et `_uas/`.
6. **Étape 6 — Génération des Fichiers de Tutoriels :** Initialise les fichiers sous `_tutos/[Domaine]/[UA]/[Code-Tuto]/[slug].md`.

---

## 6. Livrables Produits & Méthode de Vérification
- **Livrables attendus :**
  - Plans par domaine `_tutos/_plan-tuto-D.XXX.Y-*.md` validés.
  - Fiche de session `_sessions/S[X].md` synchronisée.
  - Fiches d'Unités d'Apprentissage `_uas/[domaine]/UA.XXX.YY.md` alignées (ordre, durée, notions).
  - Fichiers de tutoriels sous `_tutos/` (en `en_construction: false` dès validation).
- **Checklist binaire de contrôle :**
  - [x] Durée totale de la session exactement égale à 80h.
  - [x] Séquence des UAs continue de 1 à $N$.
  - [x] Branche Git unique `sprintX` indiquée.
  - [x] Zéro durée affichée aux apprenants dans les titres et contenus.
  - [x] Tous les tutoriels ciblent exclusivement le Projet d'imitation.
  - [x] Tous les fichiers sont encodés en **UTF-8 sans BOM**.