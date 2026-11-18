---
layout: tuto
title: "Pratique : Conception d'un skill agentique — Exemple skill-presentation"
sous_titre: "Concevoir un skill outillé avec SKILL.md et sa mission spécialisée missions/marp-slides.md"
slug: "skill-presentation"
slug_domaine: "ia"
slug_ua: "agent-skills"
permalink: /tutos/skill-presentation/
tuto_id: "T.325.113"
version: "normal"
ua: "UA.325.11"
maturite: "UA-Lab"
nav_order: 3
simplified: true
en_construction: false
branche: "sprint1"
data_html: ""
data_css: ""
data_js: ""
data_php: ""
---

## 1. Travail à faire
Concevoir et développer, dans le cadre d'un atelier pratique autonome, un skill agentique modulaire nommé `skill-presentation` selon les standards industriels Solicode N3.

Ce skill sert de modèle d'outillage pour automatiser la génération de diaporamas et supports de présentation technique. Vous devez concevoir :
1. Le manifeste orchestrateur du skill : `SKILL.md`.
2. La mission spécialisée de génération de diaporamas Marp : `missions/marp-slides.md`.
3. Le compte-rendu d'atelier formalisé : `skill-presentation.md`.
4. Le diaporama Marp de restitution de l'atelier : `presentation-skill-presentation.md`.
5. Le journal des commandes exécutées : `skill-presentation.command.md`.

## 2. Consignes & Spécifications de Réalisation

1. **Étape 1 — Préparation de l'arborescence de l'atelier :**  
   Initialisez l'arborescence dédiée à l'atelier pratique sous l'emplacement standardisé de tutoriels :

```bash
mkdir -p tutoriels/ia/agent-skills/skill-presentation/missions
```

2. **Étape 2 — Conception du manifeste orchestrateur `SKILL.md` :**  
   Dans `tutoriels/ia/agent-skills/skill-presentation/SKILL.md`, concevez le manifeste du skill selon les directives suivantes :
   - **Frontmatter YAML :** Définir `name: skill-presentation` et rédiger une `description` orientée action et découvrabilité native par l'Agent IA.
   - **Titre principal :** Identifier clairement le nom du skill et sa commande d'activation conventionnelle (`/skill-presentation`).
   - **Section 1 (Mission) :** Définir en 1 à 2 phrases le rôle d'orchestration de présentations de diapositives.
   - **Section 2 (Déclenchement) :** Énoncer explicitement les conditions d'activation (quand l'activer lors d'une demande de diaporama ou soutenance) et les exclusions (quand ne pas l'activer pour de la documentation textuelle classique).
   - **Section 3 (Missions disponibles) :** Déclarer la mission spécialisée accessible sous `missions/marp-slides.md`.
   - **Garde-fou de compacité :** Respecter rigoureusement le plafond strict de $\le 75$ lignes pour l'orchestrateur.

3. **Étape 3 — Conception de la mission spécialisée `missions/marp-slides.md` :**  
   Dans `tutoriels/ia/agent-skills/skill-presentation/missions/marp-slides.md`, formalisez le cahier des charges de la mission de génération de diapositives :
   - **Titre & Objet :** Définir le périmètre de la mission (génération de diaporamas Marp Markdown).
   - **Tâche 1 (En-tête Marp) :** Exiger le bloc YAML initial (`marp: true`, `theme: default`, `paginate: true`, en-tête et pied de page).
   - **Tâche 2 (Page de garde normalisée) :** Intégrer la structure de la première slide (`<!-- _class: lead -->`) avec les mentions obligatoires Solicode : Apprenant, Encadrant ESSARRAJ Fouad, Établissement Solicode Tanger, Domaine, Compétence et Date.
   - **Tâche 3 (Conception des diapositives) :** Imposer la règle stricte du zéro tableau Markdown (listes à puces `- ` exclusives), une densité maximale de 4 à 6 puces par slide, et une diapositive de conclusion obligatoire.
   - **Livrables attendus :** Fichier `.md` prêt à être prévisualisé ou exporté via Marp.

4. **Étape 4 — Rédaction du compte-rendu d'atelier `skill-presentation.md` :**  
   Dans `tutoriels/ia/agent-skills/skill-presentation/skill-presentation.md`, formalisez la notice complète de votre atelier pratique :
   - Les objectifs de l'atelier et compétences mobilisées.
   - L'anatomie d'un skill modulaire avec un diagramme Mermaid illustrant l'orchestrateur (`SKILL.md`) et le sous-dossier `missions/`.
   - La mise en œuvre détaillée des fichiers conçus (`SKILL.md` et `missions/marp-slides.md`).
   - La comparaison avec l'architecture déployée sur le projet d'imitation (*Blog des lauréats*) : `skills-dev` et `gestion-depot`.

5. **Étape 5 — Conception du diaporama Marp `presentation-skill-presentation.md` :**  
   Dans `tutoriels/ia/agent-skills/skill-presentation/presentation-skill-presentation.md`, préparez le support de présentation orale de l'atelier au format Marp Markdown en appliquant les consignes de la mission conçue.

6. **Étape 6 — Journalisation des commandes dans `skill-presentation.command.md` :**  
   Dans `tutoriels/ia/agent-skills/skill-presentation/skill-presentation.command.md`, consignez la commande de préparation des répertoires :

```bash
mkdir -p tutoriels/ia/agent-skills/skill-presentation/missions
```

## 3. Livrables & Critères de validation
- **Livrables attendus :**
  - Compte-rendu d'atelier : `tutoriels/ia/agent-skills/skill-presentation/skill-presentation.md` sur la branche `sprint1`.
  - Diaporama Marp : `tutoriels/ia/agent-skills/skill-presentation/presentation-skill-presentation.md` sur la branche `sprint1`.
  - Manifeste orchestrateur : `tutoriels/ia/agent-skills/skill-presentation/SKILL.md` sur la branche `sprint1`.
  - Mission spécialisée : `tutoriels/ia/agent-skills/skill-presentation/missions/marp-slides.md` sur la branche `sprint1`.
  - Journal des commandes : `tutoriels/ia/agent-skills/skill-presentation/skill-presentation.command.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le fichier `SKILL.md` contient un Front Matter YAML valide avec `name` et `description`, et ne dépasse pas 75 lignes.
  - [ ] Le fichier `SKILL.md` définit clairement sa mission, ses conditions de déclenchement et référence `missions/marp-slides.md`.
  - [ ] La mission `missions/marp-slides.md` détaille les tâches d'en-tête Marp, la page de garde avec mentions Solicode et la règle du zéro tableau Markdown.
  - [ ] Le compte-rendu `skill-presentation.md` explicite l'architecture du skill et la comparaison avec les skills du projet.
  - [ ] Le journal `skill-presentation.command.md` consigne fidèlement la commande d'initialisation de l'arborescence.
