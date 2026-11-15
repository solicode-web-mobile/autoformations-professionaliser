# Guide Opérationnel : Comment Utiliser `scrum-pedagogical-plan-adapter`

## 1. Rôle du Skill
Le skill `scrum-pedagogical-plan-adapter` analyse, audite, simplifie et harmonise les plans pédagogiques des domaines (`_plan-tuto-*.md`), des Unités d'Apprentissage (`_uas/`) et des tutoriels dans une formation organisée en Sprints sous gouvernance Scrum. Il préserve impérativement le cadre quadri-volets (Imitation, Portfolio, Fil Rouge, Live Coding) et la progression vers l'Agent IA tout en éliminant le bruit documentaire et les tâches redondantes ou prématurées.

---

## 2. Cas d'Usage Principaux
- **Audit de cohérence d'un plan de domaine :** Passer au crible un fichier `_plan-tuto-D.xxx.x.md` pour détecter les doublons, sur-spécifications ou discordances de charge horaire.
- **Simplification et recalibrage d'une UA :** Réduire une unité trop dense à son essentiel opératoire sans perte docimologique.
- **Alignement avec la cadence de Sprint Scrum :** Garantir que les activités de cadrage, conception, réalisation et bilan s'enchaînent de manière fluide sans tomber dans un cycle en V rigide.
- **Ciblage exclusif du Projet d'imitation dans les tutoriels :** Les tutoriels guident l'apprenant pas-à-pas uniquement sur le *Blog des Lauréats*. Le Portfolio individuel et le Projet Fil Rouge (transposition IA) sont réalisés après la complétion du sprint.
- **Format rigoureux des livrables :** Branche Git unique de sprint (`sprint1`) pour l'ensemble des tâches + liste exacte des fichiers modifiés ou créés (zéro durée unitaire affichée aux apprenants, `en_construction: false`).
- **Zéro théorie dans les tutoriels de type Tâche :** Les cérémonies et cadrages (cadrage, Sprint Planning, Sprint Review, Rétrospective) sont 100% axés sur l'action réelle.
- **Découpage des prompts Laravel :** Séparation en `prompt-back-end` (route, contrôleur IoC, service CSV, 404) et `prompt-front-end` (layout Blade, vue détail Tailwind, page 404).
- **Prompts de clôture de sprint :** Tâche dédiée pour concevoir les 4 prompts de clôture (`prompt-sprint-review`, `prompt-sprint-retrospective`, `prompt-backlog-refinement`, `prompt-bilan-session`).
- **Antériorité du Prompt Engineering :** Placer la maîtrise de la méthode RIO et du méta-prompt `prompt-creator` en Étape 01 pour outiller l'apprenant dès l'entame de la formation. Dans ce lab, la pratique est directement la création du prompt générateur (zéro tutoriel documentaire intermédiaire).
- **Condition stricte de création d'un Prompt :** Uniquement pour les étapes récurrentes du flux de travail qui produisent un livrable de sprint/projet (Backlog, Sprint Planning, Use cases macro, Code métier). Zéro prompt pour les labs d'apprentissage conceptuel (Scrum), les décisions uniques d'architecture globale (ADR), ou la prise en main initiale (Hello World Laravel).
- **Titrage épuré des activités IA & Missions explicites :** Format standard `Création du prompt-[nom]`, avec description explicite des missions concrètes que réalise le prompt.
- **Élimination de la théorie redondante N2 :** Ne pas créer de tutoriel théorique pour des notions déjà validées au Niveau N2 (diagramme de contexte UML, diagramme de cas d'utilisation UML, Tailwind/CSS). Passer directement à la pratique outillée (Mermaid.js).
- **Focalisation de la théorie sur les nouveautés N3 :** Définir en priorité ce qu'est le framework (Laravel 12, pattern MVC, cycle de requête HTTP, Artisan) dès sa première apparition.
- **Application du Principe de Pareto Didactique (20/80) dans les Tutoriels 1 (Théorie) :** S'assurer que les tutoriels théoriques fournissent directement les 20% de définitions clés débloquantes (ex: définition primordiale du Product Backlog, User Stories, DoD, IoC) et laissent les 80% restants à la recherche active de l'apprenant.
- **Sanctuarisation des Tutoriels 2 (Pratique) :** Zéro théorie ni redite de définitions dans le tutoriel pratique. L'effort est 100% focalisé sur la production des livrables du sprint pour le projet d'imitation et le projet technique.
- **Élimination des prérequis régressifs et présentations redondantes :** Écarter les tâches basiques (init Git, création de squelette) et les pitchs superflus, les livrables étant présentés au fil de l'eau et lors de la Sprint Review.

---

## 3. Prompts Types pour Invoquer le Skill
- *« Analyse et simplifie le plan de tutoriels `_tutos/_plan-tuto-D.311.2-uml.md` avec `scrum-pedagogical-plan-adapter`. »*
- *« Audite la cohérence Scrum et le niveau de granularité des tutoriels du domaine Laravel pour le Sprint 1. »*
- *« Réduis la complexité théorique de l'UA.312.11 et propose un plan compact et directement exécutable. »*
- *« Vérifie l'alignement des 3 projets et de l'épreuve de Live Coding dans le déroulement de la session. »*

---

## 4. Prérequis
1. Disposer du plan de tutoriels ou de l'UA cible au format Markdown (`_plan-tuto-*.md`, `_uas/*.md`).
2. Connaître le Sprint cible (`Sprint 1`, `Sprint 2`, etc.) et la durée globale allouée.
3. Identifier les technologies et compétences visées par le référentiel de formation.

---

## 5. Déroulement Pas-à-Pas
1. **Étape 1 — Diagnostic Pédagogique & Scrum :**  
   Analyser le plan existant selon la grille des 10 questions critiques (pertinence, valeur utilisateur, réutilisation, sur-segmentation).
2. **Étape 2 — Matrice des Décisions (Conserver / Simplifier / Fusionner / Supprimer / Déplacer) :**  
   Produire le tableau d'arbitrage justifiant chaque ajustement proposé.
3. **Étape 3 — Restitution du Plan Corrigé Compact :**  
   Formuler les UA et tutoriels dans la structure normalisée (Apprendre $\to$ Appliquer $\to$ Transposer/Automatiser).
4. **Étape 4 — Contrôle de Conformité Finale :**  
   Passer en revue la checklist des 14 points de contrôle obligatoires (prérequis respectés, tri-projets synchronisés, livrables concrets, UTF-8 sans BOM).

---

## 6. Méthode de Vérification des Livrables
- [ ] Le plan corrigé n'introduit aucune rupture avec le référentiel de compétences.
- [ ] Les 3 projets (Imitation, Portfolio, Fil Rouge) et le Live Coding travaillent sur la même technique.
- [ ] Aucune tâche théorique n'est redondante ou superflue.
- [ ] Les fichiers produits sont enregistrés en **UTF-8 sans BOM**.
