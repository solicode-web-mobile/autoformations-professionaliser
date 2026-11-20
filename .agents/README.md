# Écosystème des Compétences IA (`.agents/`) — Plateforme Autoformations

Ce répertoire centralise l'intelligence, les règles didactiques, les références normatives et les **Skills modulaires** qui pilotent le fonctionnement de l'**Agent IA Autoformation** sur la plateforme Solicode.

---

## 1. Cartographie des Compétences IA

L'écosystème s'articule autour de 5 grandes familles fonctionnelles :

```mermaid
flowchart TD
    subgraph Cadrage ["1. Cadrage & Ingénierie Didactique"]
        Adapter["session-flux-travail-adapter"]
        Scrum["scrum-pedagogical-plan-adapter"]
        Planer["tutorial-planer"]
    end

    subgraph Redaction ["2. Rédaction des Tutoriels (Écosystème tutorial-*-writer)"]
        Master["tutorial-writer (Master Skill)"]
        subgraph Formats ["Maturités Pédagogiques"]
            Code["tutorial-code-writer (UA-Tuto)"]
            Lab["tutorial-lab-writer (UA-Lab)"]
            Task["tutorial-task-writer (UA-Tâche)"]
        end
        subgraph Domaines ["Règles Spécifiques par Domaine"]
            DomUml["tutorial-writer-uml"]
            DomArch["tutorial-writer-architecture"]
            DomLar["tutorial-writer-laravel"]
            DomIA["tutorial-writer-ia"]
            DomScrum["tutorial-writer-scrum"]
            DomProj["tutorial-writer-realisation-projet"]
        end
    end

    subgraph Synchronisation ["3. Synchronisation Inter-Agents"]
        SyncRules[".sync/rules.md (Dépôt Projet Cible)"]
    end

    subgraph Socle ["4. Plateforme & Thème"]
        Jekyll["dev-jekyll"]
        Theme["sync-theme"]
    end

    subgraph Gouvernance ["5. Méta-Gouvernance IA"]
        PluginDev["skills-dev"]
    end

    Adapter --> Planer
    Planer --> Master
    Master --> Formats
    Master --> Domaines
    Master <--> SyncRules
```

| Compétence (Skill) | Vocation Principale | Entités & Fichiers Clés |
| :--- | :--- | :--- |
| **[tutorial-writer](skills/tutorial-writer/SKILL.md)** | **Master Skill & Chef d'orchestre** : gouverne les 12 règles transversales partagées, route vers les rédacteurs spécialisés et pilote la synchronisation inter-agents. | `_tutos/`, `_plan-tuto-*.md`, `.sync/rules.md` |
| **[tutorial-code-writer](skills/tutorial-code-writer/SKILL.md)** | Rédige les tutoriels d'apprentissage de code incrémental pas-à-pas ($E_{n-1} \to E_n$) avec injecteur interactif `window.pageData`. | `_tutos/...` (`UA-Tuto`) |
| **[tutorial-lab-writer](skills/tutorial-lab-writer/SKILL.md)** | Rédige les ateliers pratiques guidés (notions fondamentales, recherche active, modélisation UML/schémas, outillage IA par skills/prompts). | `_tutos/...` (`UA-Lab`) |
| **[tutorial-task-writer](skills/tutorial-task-writer/SKILL.md)** | Rédige les fiches de cadrage opérationnel et cérémonies agiles de sprint sans aucun apport théorique (0% théorie). | `_tutos/...` (`UA-Tâche`) |
| **[tutorial-writer-uml](skills/tutorial-writer-uml/SKILL.md)** | Rédige les tutoriels UML (diagrammes Mermaid déclaratifs `graph TD`, `sequenceDiagram`, traçabilité Backlog, zéro capture d'écran). | `_tutos/` (domaine `uml`) |
| **[tutorial-writer-architecture](skills/tutorial-writer-architecture/SKILL.md)** | Rédige les tutoriels d'architecture (découpage en couches, fiches ADR, flux de données Mermaid, SOLID, contrôleurs minces). | `_tutos/` (domaine `architecture`) |
| **[tutorial-writer-laravel](skills/tutorial-writer-laravel/SKILL.md)** | Rédige les tutoriels Laravel (Live Coding, FormRequest, Blade/Alpine.js, scission prompt back/front, neutralité de version). | `_tutos/` (domaine `laravel`) |
| **[tutorial-writer-ia](skills/tutorial-writer-ia/SKILL.md)** | Rédige les tutoriels IA & Agents (méthode RIO, méta-prompt générateur, skills modulaires réutilisables). | `_tutos/` (domaine `ia`) |
| **[tutorial-writer-scrum](skills/tutorial-writer-scrum/SKILL.md)** | Rédige les tutoriels Scrum conceptuels (INVEST, MoSCoW, DoD mesurable, notions fondamentales vs recherche active sans mention 20/80). | `_tutos/` (domaine `scrum`) |
| **[tutorial-writer-realisation-projet](skills/tutorial-writer-realisation-projet/SKILL.md)** | Rédige les tâches de projet et cérémonies opérationnelles (maturité UA-Tâche, 0% théorie, journal CLI sans commandes Git). | `_tutos/` (domaine `realisation-projet`) |
| **[tutorial-planer](skills/tutorial-planer/SKILL.md)** | Architecte de la progression pédagogique : conçoit les plans de réalisation par session, crée les entités Jekyll manquantes (`_sessions/`, `_domaines/`, `_uas/`) et initialise les stubs (`en_construction: true`). | `_sessions/`, `_uas/`, `_domaines/`, `_plan-réalisation-tutos/` |
| **[session-flux-travail-adapter](skills/session-flux-travail-adapter/SKILL.md)** | Aligne la session pédagogique sur le flux de travail opérationnel réel du projet (`flux-travail.md`), qualifie didactiquement les labs et produit le Plan Artefact d'impact. | `_sessions/S[X].md`, `_flux-travail.md` |
| **[scrum-pedagogical-plan-adapter](skills/scrum-pedagogical-plan-adapter/SKILL.md)** | Analyse, calibre et simplifie l'organisation pédagogique en sprints Scrum de 80h sans surcharge cognitive. | `_sessions/`, `_uas/` |
| **[dev-jekyll](skills/dev-jekyll/SKILL.md)** | Développe et maintient l'architecture frontend Just the Docs (layouts, includes, CSS/JS, composants interactifs, zéro CSS inline). | `_layouts/`, `_includes/`, `assets/` |
| **[sync-theme](skills/sync-theme/SKILL.md)** | Pilote la synchronisation du socle partagé avec `autoformations-core-theme` via `push_theme.ps1` et `pull_theme.ps1`. | `theme-sync.json`, scripts PowerShell |
| **[skills-dev](skills/skills-dev/SKILL.md)** | Méta-compétence de gouvernance : conçoit, audite et raffine les skills (`.agents/skills/`) et les règles permanentes (`.agents/rules/`). | `.agents/skills/`, `.agents/rules/` |

---

## 2. Guide d'Exécution : Comment Réaliser le Travail de l'Agent

Le travail didactique et technique de l'agent suit un cycle structuré en 5 phases successives :

### Phase 1 : Réconciliation Didactique (Flux Réel ➔ Session)
Quand une équipe de développement ou un flux de travail de projet évolue :
1. Invoquer **`session-flux-travail-adapter`** :
   ```markdown
   @[.agents/skills/session-flux-travail-adapter/SKILL.md] Aligne la session _sessions/S1.md avec le flux de travail opérationnel réel.
   ```
2. L'agent arbitre la vérité (les étapes et livrables réels du flux font autorité ; la didactique et les 80h de la session font autorité) et produit un **Plan Artefact d'impact** listant les UAs et tutoriels à créer, adapter ou conserver.

### Phase 2 : Planification & Intégrité Référentielle
Pour structurer et cadencer le parcours pédagogique d'un sprint ou d'une session :
1. Invoquer **`tutorial-planer`** :
   ```markdown
   @[.agents/skills/tutorial-planer/SKILL.md] Conçois et planifie la progression des tutoriels pour la session S1.
   ```
2. `tutorial-planer` :
   - Établit le plan sans rupture cognitive reliant le dossier de départ au livrable final complet.
   - Crée automatiquement les entités Jekyll manquantes (`_sessions/S[X].md`, `_domaines/`, `_uas/`).
   - Initialise les fiches stubs de tutoriels sous `_tutos/` avec l'état `en_construction: true`.

### Phase 3 : Rédaction Didactique (Écosystème `tutorial-*-writer`)
Pour rédiger ou affiner le contenu des fiches de tutoriels :
1. Invoquer le Master Skill **`tutorial-writer`** :
   ```markdown
   @[.agents/skills/tutorial-writer/SKILL.md] Rédige le tutoriel T.321.112 planifié pour l'UA.321.11.
   ```
2. **Double Délégation (Format Didactique & Domaine Technique) :**
   - **Maturité Pédagogique :**
     - Code incrémental pas-à-pas ($E_{n-1} \to E_n$) ➔ **`tutorial-code-writer`** (`UA-Tuto`).
     - Atelier pratique guidé ➔ **`tutorial-lab-writer`** (`UA-Lab`, théorie essentielle, recherche active, modélisation).
     - Tâche opérationnelle ou cérémonie ➔ **`tutorial-task-writer`** (`UA-Tâche`, 0% théorie).
   - **Règles Spécifiques par Domaine :** Injection automatique du skill technique correspondant (`tutorial-writer-uml`, `tutorial-writer-architecture`, `tutorial-writer-laravel`, `tutorial-writer-ia`, `tutorial-writer-scrum`, `tutorial-writer-realisation-projet`).
3. **Application du Socle Transversal (12 Règles Inviolables) :**
   - Encodage strict UTF-8 sans BOM.
   - Blocs de code débutant strictement à la **colonne 0** (zéro espace, saut de ligne avant et après).
   - Chemin relatif canonique `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/` (aucun `README.md` unitaire).
   - Journalisation CLI `[slug-tuto].command.md` sans commandes Git.
   - Respect de l'autonomie Git selon les règles du niveau actif.
   - Zéro fuite de cuisine interne (pas de mention « 20/80 ») et suppression des jalons au profit du terme direct « Étape ».

### Phase 4 : Synchronisation Inter-Agents & Traçabilité (`.sync/rules.md`)
Pour synchroniser les tutoriels avec le projet cible réel :
1. Invoquer **`tutorial-writer`** en mode synchronisation :
   ```markdown
   @[.agents/skills/tutorial-writer/SKILL.md] Synchronise les fiches de tutoriels avec le projet cible selon .sync/rules.md.
   ```
2. **Mécanisme Déterministe :**
   - Consultation obligatoire du contrat `<projet-cible>/.sync/rules.md`.
   - Inspection des fichiers `version.yml` logés **exclusivement dans `.sync/`** du projet cible.
   - Comparaison avec le front-matter du tutoriel source (`_tutos/`) :
     ```yaml
     sprint: "sprint1"
     statut_realisation: "realise" # basculé à "synchronise" ou "a_adapter"
     livrables:
       - chemin: "tutoriels/[domaine]/[ua]/[slug]/[slug].md"
         version: "1.0.0"
       - chemin: "tutoriels/[domaine]/[ua]/[slug]/presentation-[slug].md"
         version: "1.0.0"
     ```
   - Si `.sync` > front-matter : mise à jour du contenu réel, alignement de la version et passage à `statut_realisation: "synchronise"`.
   - Si discordance majeure ou livrable incomplet : passage à `statut_realisation: "a_adapter"`.

### Phase 5 : Maintenance du Site & Évolution des Compétences
- Pour faire évoluer les composants, styles ou layouts Jekyll ➔ Utiliser **`dev-jekyll`**.
- Pour synchroniser le thème partagé avec le dépôt central ➔ Utiliser **`sync-theme`**.
- Pour créer, raffiner ou auditer un skill ou une règle d'agent ➔ Utiliser **`skills-dev`**.

---

## 3. Matrice d'Aiguillage Rapide

| Besoin Exprimé par l'Utilisateur | Compétence à Invoquer |
| :--- | :--- |
| *« Rédige un tutoriel de code pas-à-pas pour créer un composant »* | **`tutorial-writer`** (route vers `tutorial-code-writer` + `tutorial-writer-laravel`) |
| *« Formalise l'atelier pratique d'architecture et de modélisation »* | **`tutorial-writer`** (route vers `tutorial-lab-writer` + `tutorial-writer-architecture`) |
| *« Modélise les cas d'utilisation ou diagramme de classe Mermaid »* | **`tutorial-writer`** (route vers `tutorial-lab-writer` + `tutorial-writer-uml`) |
| *« Rédige un prompt ou un skill avec la méthode RIO »* | **`tutorial-writer`** (route vers `tutorial-lab-writer` + `tutorial-writer-ia`) |
| *« Rédige la fiche théorique sur la DoD ou le Product Backlog »* | **`tutorial-writer`** (route vers `tutorial-lab-writer` + `tutorial-writer-scrum`) |
| *« Rédige la fiche du rituel de Sprint Planning ou de cadrage »* | **`tutorial-writer`** (route vers `tutorial-task-writer` + `tutorial-writer-realisation-projet`) |
| *« Vérifie l'alignement des versions avec le projet cible »* | **`tutorial-writer`** (via `.sync/rules.md`) |
| *« Planifie l'ensemble de la session S2 et crée les stubs »* | **`tutorial-planer`** |
| *« Le projet réel a ajouté de nouvelles étapes, adapte la session »* | **`session-flux-travail-adapter`** |
| *« Améliore l'affichage du layout ou corrige un composant CSS »* | **`dev-jekyll`** |
| *« Synchronise le Core Theme avec le dépôt central »* | **`sync-theme`** |
| *« Crée un nouveau skill ou modifie une règle d'agent »* | **`skills-dev`** |

---

## 4. Règles Transversales Invariables du Workspace

Toute action menée par l'un quelconque de ces skills doit rigoureusement respecter :
1. **Encodage UTF-8 sans BOM :** Obligatoire pour tous les fichiers texte créés ou modifiés.
2. **Documentation Colocalisée (`README.md`) :** Tout skill possède son fichier `README.md` colocalisé unique et suffisant. Aucun sous-dossier `doc/` n'est requis.
3. **Découplage Multi-Niveaux :** Les skills méthodologiques sont agnostiques et résolvent le niveau (N1, N2, N3) et le projet cible à partir de `.agents/rules/`.
4. **Transparence :** Indiquer obligatoirement les compétences mobilisées à la fin de chaque réponse.
