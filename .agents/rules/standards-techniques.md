---
trigger: always_on
---

# Standards Techniques & Comportementaux du Projet

## 1. Encodage Strict (UTF-8 Sans BOM)
- Tous les fichiers créés ou modifiés (`.md`, `.html`, `.css`, `.js`, `.yml`) doivent impérativement être encodés en **UTF-8 sans BOM**.
- Sous PowerShell Windows, éviter `Set-Content -Encoding UTF8`. Utiliser l'objet .NET :
  ```powershell
  $utf8NoBom = New-Object System.Text.UTF8Encoding $False
  [System.IO.File]::WriteAllText($chemin, $contenu, $utf8NoBom)
  ```

## 2. Architecture Jekyll & Just the Docs
- **Collections :** Respecter l'organisation (`_missions/`, `_modules/`, `_competences/`, `_domaines/`, `_uas/`, `_sessions/`, `_tutos/`, `_labs/`, `_prototypes/`, `_projets/`). Le code d'accompagnement réside dans `/code`.
- **Zéro CSS Inline :** Interdiction absolue d'ajouter des balises `<style>` ou du CSS en attribut dans les layouts HTML et includes. Les styles vont exclusivement dans `assets/css/`.
- **Filtre Liquid `jsonify` :** Il ajoute automatiquement les guillemets. Ne jamais entourer manuellement de quotes (`"{{ val | jsonify }}"` est une erreur de syntaxe).
- **Règle de Formatage des Blocs de Code Markdown :**
  - Tout bloc de code (```` ``` ```` ou ```` ```` ````) doit impérativement débuter à la marge gauche (**colonne 0, strictement sans espaces d'indentation**), y compris lorsqu'il est situé sous un élément de liste ordonnée.
  - Toujours **laisser une ligne vide** avant d'ouvrir un bloc de code et une ligne vide après sa fermeture.
  - Le contenu textuel ou Markdown inséré dans le bloc doit être calé à la marge gauche (colonne 0), sans indentation artificielle.

## 3. Éditeur de Code & Gouvernance Normative des Livrables
- **Éditeur interactif :** Dès qu'un tutoriel utilise des champs `data_*`, insérer systématiquement le script `window.pageData` sous le Front Matter. Isoler le code de préparation pour que l'onglet de travail de l'apprenant reste vierge.
- **Médias :** Stockage obligatoire dans `images-tutos/[Domaine]/[ID_Tuto]/[nom.ext]`.
- **Livrables :** Le livrable est toujours un **dépôt GitHub** ou un fichier `.md` de commandes. **Interdiction stricte de captures d'écran comme livrable.**
- **Référentiel Central des Livrables & Typologie :**
  L'organisation physique de tous les livrables sur le poste de l'apprenant est gouvernée de manière centralisée et exclusive par les documents de référence normatifs de l'EFP :
  - **Identité de l'Agent Rédacteur :** `.agents/rules/persona.md` (définit l'**Agent de Rédaction de l'Autoformation**, alias `redacteur-autoformation`). L'agent miroir qui réalise les travaux sur le projet cible est l'**Agent Réalisation de Sprint** (`realisation-sprint`).
  - **Arborescence du Poste Apprenant :** `.agents/references/organisation-livrables.md` (cartographie complète pour N1, N2 et N3 : `tutoriels/`, `src/`, `docs/conception/`, `sprints/`, `scrum/`, `rapport/`, `presentations/`).
  - **Maturation des UAs & Typologie des Tutoriels :** `.agents/references/maturation-et-typologie-ua-tuto.md` (dissociation UA = maturité [`ua-lab`, `projet`] vs Tutoriel = type [`tuto-atelier`, `tuto-atelier-notions`, `tuto-tache`, `tuto-notion`, `tuto-code`], et cycle d'enrichissement de l'atelier).
  - **Stratégie Git & Commits :** `.agents/references/gitflow.md` (branches `sprint[N]`, commits atomiques conventionnels, interdiction formelle de commit/push automatique par l'Agent IA).
- **Règles d'Exclusion et de Structuration Formelle :**
  - **Suppression du dossier `issues/` :** Les tâches de développement sont gérées au niveau du Sprint Planning dans `sprints/sprint-[N].md`.
  - **Règle Unique du fichier `README.md` dans `tutoriels/` :** Requis uniquement à la racine `tutoriels/README.md`. Interdiction formelle dans les sous-dossiers de domaines, d'UAs ou de tutoriels unitaires.
  - **Interdiction formelle du dossier racine `labs/`.**
- **Règle du Journal des Commandes CLI (`[slug-tuto].command.md`) :**
  - Le journal des commandes représente le **rapport d'exécution technique du tutoriel**.
  - Requis **uniquement** pour les `tuto-atelier`, `tuto-notion` et `tuto-code` lorsqu'ils comportent des commandes terminal.
  - **Formellement proscrit pour les `tuto-tache`** (dont les livrables d'ingénierie résident directement aux emplacements racine du projet).
  - Interdiction absolue d'y inclure les commandes Git (`git add`, `git commit`, `git push`).
- **Consultation et Synchronisation du Référentiel Physique (`.sync/rules-sync.md`) :**
  Le Master Skill **`tutorial-writer`** détient l'autorité exclusive d'inspection et de synchronisation avec le dépôt réel du projet cible (configuré ci-dessus ou via `.sync/rules-sync.md`).
  Les échanges et le versioning inter-agents sont formellement régis par le contrat **`<projet-cible>/.sync/rules-sync.md`** :
  - **L'Agent Réalisation de Sprint (`realisation-sprint`) :** Développe les livrables, maintient les numéros de version sémantique exclusivement dans les fichiers `version.yml` logés à l'intérieur du dossier `.sync/` (interdiction stricte de créer des `version.yml` dans `tutoriels/`, `src/`, etc.), et notifie la réalisation dans le front-matter du tutoriel source (`_tutos/`) avec `sprint`, `statut_realisation: "realise"` et la liste des `livrables` (chemins et versions).
  - **L'Agent Autoformation (`tutorial-writer`) :** Déclenche l'audit des livrables réels : pour un `tuto-atelier`, il bascule la fiche de `maturite: "lab"` à `maturite: "ua-lab"`, injecte les notions fondamentales en détail, spécifie le plan d'UA-Lab, aligne les versions dans le front-matter et bascule le statut à `synchronise` (ou `a_adapter` si une discordance majeure est détectée).
  - **Adaptation mutuelle :** En cas d'incohérence, si la pratique du projet réel valide une solution plus pertinente, le tutoriel est adapté pour refléter la réalité ; si le livrable est incomplet, l'Agent Projet corrige le livrable dans `tutoriels/`.

## 4. Transparence de l'Agent IA & Traçabilité des Actions
- **Affichage Obligatoire des Skills Utilisés :** À la fin de chaque échange / discussion, l'Agent IA doit obligatoirement afficher la liste exacte des **Skills locaux utilisés** lors de la réponse (format : `Skills utilisés : [skill-1], [skill-2]`).
- **Affichage des Compétences du Cursus :** Indiquer également les compétences certifiantes du référentiel mobilisées (format : `Compétences du cursus : C.xxx, C.yyy`).
- **Plans d'action :** Expliciter obligatoirement les skills et compétences prévus pour réaliser chaque étape d'un plan d'implémentation.

## 5. Gouvernance des Skills & Documentation Colocalisée
- **100% Local au Dépôt :** Toutes les compétences de l'agent résident sous `.agents/skills/`. Aucun mécanisme de Hub distant ou de compétences globales n'est utilisé. La découverte des compétences s'effectue dynamiquement à partir des fichiers `SKILL.md`.
- **Documentation Colocalisée Suffisante (`README.md`) :** Tout skill (`.agents/skills/<nom-du-skill>/`) doit obligatoirement comporter son fichier `README.md` colocalisé à la racine de son dossier. Ce document constitue la documentation opérationnelle unique et suffisante (rôle, cas d'usage, prompts types pour l'invoquer, déroulement pas-à-pas et méthode de vérification). Aucun sous-dossier `doc/` n'est requis.

## 6. Gouvernance des Modules et Compétences
- **Collection `_modules/` :** Les modules de formation officiels du cursus sont stockés sous `_modules/` avec leur `id_bdd`, `code` (`M105`..`M114`), `module_reference` (`DMB-Mxxx`) et `title`.
- **Protocole Obligatoire de Création de Compétence :**
  Lorsqu'une nouvelle compétence (`_competences/C.xxx.md`) est créée ou révisée :
  1. L'agent IA doit obligatoirement analyser les 10 modules officiels du cursus (`_modules/`).
  2. L'agent IA doit obligatoirement formuler une **proposition formelle d'affectation** du module (`module: "Mxxx"`), de sa référence BDD (`module_reference: "DMB-Mxxx"`) et de sa référence canonique (`reference: "DMB-Mxxx-C.xxx"`), argumentée techniquement et didactiquement.
  3. **Validation Obligatoire du Concepteur Pédagogique :** Il est strictement interdit à l'agent d'acter ou de figer unilatéralement l'affectation du module sans avoir obtenu au préalable la validation explicite du concepteur pédagogique (humain).

