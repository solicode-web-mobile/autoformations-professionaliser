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

## 3. Éditeur de Code & Livrables
- **Éditeur interactif :** Dès qu'un tutoriel utilise des champs `data_*`, insérer systématiquement le script `window.pageData` sous le Front Matter. Isoler le code de préparation pour que l'onglet de travail de l'apprenant reste vierge.
- **Médias :** Stockage obligatoire dans `images-tutos/[Domaine]/[ID_Tuto]/[nom.ext]`.
- **Livrables :** Le livrable est toujours un **dépôt GitHub** ou un fichier `.md` de commandes. **Interdiction stricte de captures d'écran comme livrable.**
- **Règle Universelle des Chemins de Livrables (`tutoriels/`) :**
  Tout livrable d'apprentissage doit obligatoirement être spécifié avec son chemin relatif complet sous l'arborescence standardisée :
  `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/`
  - **Fiche théorique :** `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].md` sur la branche active du sprint.
  - **Atelier pratique ou exemple guidé :** Déposé obligatoirement sous `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/` (fichiers de code, manifestes, documentation). **Interdiction formelle d'utiliser un dossier racine `labs/`.**
  - **Tâche de projet opérationnelle :** Livrables positionnés aux emplacements racine officiels (`src/`, `.agents/`, `rapport/`, `presentations/`, etc.) ET journal des commandes dans `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].command.md`.
  - **Interdiction formelle des formulations vagues :** Ne jamais écrire de mentions floues telles que *« journal d'apprentissage personnel »* sans fournir le chemin complet et explicite du fichier à commiter.
  - **Interdiction des fichiers `README.md` au niveau des tutoriels unitaires :** Les dossiers de tutoriels unitaires (`tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/`) ne doivent pas comporter de fichier `README.md`. Le document technique principal est directement `[slug-tuto].md` accompagné de son diaporama Marp `presentation-[slug-tuto].md`. Les fichiers `README.md` sont réservés aux dossiers structurels parents (`tutoriels/`, `[slug-domaine]/`, `[slug-ua]/`).
- **Règle de Journalisation des Commandes :**
  - Dès qu'un tutoriel implique la saisie de commandes en ligne de commande (CLI / Shell), l'apprenant doit obligatoirement consigner ses commandes dans le fichier standardisé `[slug-tuto].command.md` déposé dans `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/` sur la branche de sprint active.
  - Dans la fiche de tutoriel, les commandes du journal sont présentées directement sous la forme d'un bloc ```` ```bash ```` (sans double encapsulation ```` ````markdown ````).
  - Le journal ne consigne que les commandes opérationnelles utiles de la tâche : **interdiction formelle d'y inclure les commandes Git (`git add`, `git commit`, `git push`)**.
  - **S'il n'y a aucune commande CLI à exécuter dans le tutoriel (travail purement rédactionnel ou d'édition dans l'IDE), ne pas citer cette partie** (aucun fichier journal ni étape de journalisation).
  - **Interdiction formelle des étapes de Commit / Push :** Interdiction d'ajouter une étape directive de commit ou push (`git add`, `git commit`, `git push`) à la fin des tutoriels. Les apprenants N3 maîtrisent déjà le cycle de versionnement Git et gèrent leurs commits de manière autonome.
- **Environnement d'Exécution & Commandes CLI en N3 :**
  - L'environnement de travail officiel en Niveau N3 est **Windows (PowerShell)** pour tous les développements (Laravel, Git, GitHub CLI, Artisan, tests).
  - L'environnement **Linux (Bash)** est strictement réservé au domaine de **déploiement** (serveurs distants, conteneurisation).
  - Les commandes CLI fournies aux apprenants doivent fonctionner nativement sous Windows PowerShell tout en adoptant la syntaxe la plus familière et proche possible des standards Linux :
    - Conserver systématiquement **`mkdir`** (`mkdir dossier`, `mkdir chemin/vers/dossier` sans option `-p` inutile sous PowerShell, et `mkdir dossier1, dossier2` pour plusieurs dossiers).
    - Pour créer un fichier vide, utiliser la redirection standard **`echo "" > <fichier>`** (proscrire `touch` non reconnu par PowerShell et proscrire `New-Item`).
- **Consultation et Synchronisation du Référentiel Physique (`.sync/rules-sync.md`) :**
  Le Master Skill **`tutorial-writer`** détient l'autorité exclusive d'inspection et de synchronisation avec le dépôt réel du projet cible (configuré ci-dessus ou via `.sync/rules-sync.md`).
  Les échanges et le versioning inter-agents sont formellement régis par le contrat **`<projet-cible>/.sync/rules-sync.md`** :
  - **L'Agent Réalisation (Agent Projet) :** Développe les livrables, maintient les numéros de version sémantique exclusivement dans les fichiers `version.yml` logés à l'intérieur du dossier `.sync/` (interdiction stricte de créer des `version.yml` dans `tutoriels/`, `src/`, etc.), et notifie la réalisation dans le front-matter du tutoriel source (`_tutos/`) avec `sprint`, `statut_realisation: "realise"` et la liste des `livrables` (chemins et versions).
  - **L'Agent Autoformation (`tutorial-writer`) :** Consulte systématiquement `.sync/rules-sync.md` pour interagir avec l'Agent Réalisation, compare les versions déclarées dans le front-matter du tutoriel source avec celles de `.sync/.../version.yml`. Si une mise à jour est détectée, il actualise le contenu didactique dans Jekyll, aligne les versions dans le front-matter et bascule le statut à `synchronise` (ou `a_adapter` si une discordance majeure est détectée).
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

