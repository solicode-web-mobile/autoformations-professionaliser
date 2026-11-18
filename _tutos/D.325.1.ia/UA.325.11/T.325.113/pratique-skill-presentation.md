---
layout: tuto
title: "Pratique : Conception d'un skill agentique — Exemple skill-presentation"
sous_titre: "Concevoir un skill outillé avec SKILL.md, doc/how-to-use.md et missions spécialisées Marp et PowerPoint"
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
Concevoir et rédiger, dans le cadre d'un atelier pratique autonome, un skill agentique modulaire nommé `skill-presentation`.

Ce skill sert d'exemple concret d'outillage d'un Agent IA pour la production de supports de restitution technique. Vous devez concevoir :
1. Le manifeste déclaratif du skill : `SKILL.md`.
2. Le guide d'utilisation opérationnel : `doc/how-to-use.md`.
3. La mission RIO de génération de diaporamas Marp : `missions/presentation-marp.mission.md`.
4. La mission RIO de génération de trames PowerPoint : `missions/presentation-powerpoint.mission.md`.
5. Le journal des commandes exécutées : `skill-presentation.command.md`.

## 2. Consignes & Spécifications de Réalisation

1. **Jalon 1 — Préparation de l'arborescence :**  
   Initialisez l'arborescence dédiée à l'atelier dans votre dépôt :

```bash
mkdir -p tutoriels/ia/agent-skills/skill-presentation/doc tutoriels/ia/agent-skills/skill-presentation/missions
```

2. **Jalon 2 — Rédaction du manifeste `SKILL.md` :**  
   Dans `tutoriels/ia/agent-skills/skill-presentation/SKILL.md`, concevez le manifeste du skill en respectant les spécifications suivantes :
   - **En-tête YAML :** Définir `name: skill-presentation`, `description` (explicite pour la découvrabilité native par l'agent IA) et `version: 1.0.0`.
   - **Présentation générale :** Exposer l'objectif du skill (transformer des spécifications ou un README en présentations professionnelles).
   - **Capacités :** Décrire les deux modes pris en charge (diaporamas Marp Markdown prêts à projeter et trames textuelles hiérarchisées pour PowerPoint).

3. **Jalon 3 — Rédaction du guide opérationnel `doc/how-to-use.md` :**  
   Dans `tutoriels/ia/agent-skills/skill-presentation/doc/how-to-use.md`, rédigez le guide d'utilisation destiné aux développeurs et à l'Agent IA :
   - **Rôle du skill :** Préciser dans quelles situations concrètes ce skill est activé (revue de sprint, soutenance technique, restitution client).
   - **Prompts types d'invocation :** Formuler au moins deux exemples de requêtes types démontrant comment déclencher le skill à partir d'un fichier source (ex: à partir de `README.md` ou des livrables de sprint).
   - **Déroulement de l'exécution :** Détailler la séquence pas-à-pas suivie par l'agent (analyse de la source, sélection de la mission, application du gabarit, écriture du livrable).

4. **Jalon 4 — Conception de la mission RIO Marp `missions/presentation-marp.mission.md` :**  
   Dans `tutoriels/ia/agent-skills/skill-presentation/missions/presentation-marp.mission.md`, formalisez le cahier des charges de la mission selon la **méthode RIO** :
   - **Front Matter :** Déclarer `mission: presentation-marp` et `format: rio`.
   - **Rôle :** Spécifier un persona d'expert frontend et design technique spécialisé dans Marp Markdown.
   - **Instruction :** Définir la directive précise guidant l'agent pour convertir la source en diaporama Marp.
   - **Output :** Exiger une structure Markdown stricte débutant par l'en-tête Marp (`marp: true`, `theme: default`, pagination), une page de garde normalisée (Apprenant, Encadrant, Établissement) et des séparateurs de slides `---`.
   - **Contraintes négatives :** Interdire tout texte narratif en dehors des diapositives, limiter à 4 puces par slide et bannir tout HTML non interprétable par Marp.

5. **Jalon 5 — Conception de la mission RIO PowerPoint `missions/presentation-powerpoint.mission.md` :**  
   Dans `tutoriels/ia/agent-skills/skill-presentation/missions/presentation-powerpoint.mission.md`, formalisez le cahier des charges pour PowerPoint selon la **méthode RIO** :
   - **Front Matter :** Déclarer `mission: presentation-powerpoint` et `format: rio`.
   - **Rôle :** Définir un persona de consultant en communication technique.
   - **Instruction :** Formuler la directive pour structurer une trame hiérarchisée prête à l'import dans PowerPoint.
   - **Output :** Imposer un formatage par diapositive comprenant Titre (H2), messages clés sous forme de liste à puces, et une section dédiée `### Notes de l'orateur` contenant les arguments oraux.
   - **Contraintes négatives :** Proscrire les diapositives surchargées de texte et interdire les acronymes non explicités.

6. **Jalon 6 — Journalisation des commandes :**  
   Dans le fichier `tutoriels/ia/agent-skills/skill-presentation/skill-presentation.command.md`, consignez la commande de création des répertoires :

```bash
mkdir -p tutoriels/ia/agent-skills/skill-presentation/doc tutoriels/ia/agent-skills/skill-presentation/missions
```

## 3. Livrables & Critères de validation
- **Livrables attendus :**
  - Dossier d'atelier `tutoriels/ia/agent-skills/skill-presentation/` comprenant vos 4 fichiers rédigés :
    - `SKILL.md` (manifeste YAML et capacités).
    - `doc/how-to-use.md` (guide opérationnel avec cas d'usage et prompts).
    - `missions/presentation-marp.mission.md` (cahier des charges RIO Marp).
    - `missions/presentation-powerpoint.mission.md` (cahier des charges RIO PowerPoint).
  - Journal des commandes : `tutoriels/ia/agent-skills/skill-presentation/skill-presentation.command.md` sur la branche `sprint1`.
- **Critères de validation :**
  - [ ] Le fichier `SKILL.md` contient un Front Matter YAML valide avec nom, description et version.
  - [ ] Le guide `doc/how-to-use.md` explicite le rôle, des prompts d'invocation réalistes et le flux d'exécution.
  - [ ] La mission Marp respecte les 4 composantes RIO (Rôle, Instruction, Output Marp avec en-tête, Contraintes négatives).
  - [ ] La mission PowerPoint respecte les 4 composantes RIO avec la section obligatoire `### Notes de l'orateur`.
  - [ ] Le journal `skill-presentation.command.md` consigne la commande de préparation.
