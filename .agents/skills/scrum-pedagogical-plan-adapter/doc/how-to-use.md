# Guide Opérationnel : Comment Utiliser `scrum-pedagogical-plan-adapter`

## 1. Rôle du Skill
Le skill `scrum-pedagogical-plan-adapter` analyse, audite, simplifie et harmonise les plans pédagogiques des domaines (`_plan-tuto-*.md`), des Unités d'Apprentissage (`_uas/`) et des tutoriels dans une formation organisée en Sprints sous gouvernance Scrum. Il préserve impérativement le cadre quadri-volets (Imitation, Portfolio, Fil Rouge, Live Coding) et la progression vers l'Agent IA tout en éliminant le bruit documentaire et les tâches redondantes ou prématurées.

---

## 2. Cas d'Usage Principaux
- **Audit de cohérence d'un plan de domaine :** Passer au crible un fichier `_plan-tuto-D.xxx.x.md` pour détecter les doublons, sur-spécifications ou discordances de charge horaire.
- **Simplification et recalibrage d'une UA :** Réduire une unité trop dense à son essentiel opératoire sans perte docimologique.
- **Alignement avec la cadence de Sprint Scrum :** Garantir que les activités de cadrage, conception, réalisation et bilan s'enchaînent de manière fluide sans tomber dans un cycle en V rigide.
- **Validation du chaînage Tri-Projets :** S'assurer que le projet d'imitation, le portfolio individuel et le projet fil rouge (prompts RIO) avancent sur la même technique au cours du même sprint.

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
