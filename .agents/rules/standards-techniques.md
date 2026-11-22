---
trigger: always_on
---

# Standards Techniques & Comportementaux du Projet

## 1. Encodage Strict (UTF-8 Sans BOM) & Prévention Anti-Mojibake
- **Encodage Universel :** Tous les fichiers créés ou modifiés (`.md`, `.html`, `.css`, `.js`, `.yml`, `.csv`) doivent impérativement être encodés en **UTF-8 sans BOM**.
- **Lecture Sécurisée sous PowerShell Windows :**
  - **Interdiction formelle de `Get-Content` brut sans `-Encoding utf8` :** Sous Windows PowerShell 5.1, `Get-Content` sans paramètre d'encodage lit le fichier en Windows-1252 (ANSI). Réécrire une chaîne ainsi lue entraîne irrémédiablement un **double encodage UTF-8 (*mojibake*)**.
  - Toujours spécifier explicitement l'encodage UTF-8 à la lecture :
    ```bash
    # Méthode .NET recommandée (100% fiable) :
    $contenu = [System.IO.File]::ReadAllText($chemin, [System.Text.Encoding]::UTF8)

    # Ou commande PowerShell explicite :
    $contenu = Get-Content -Path $chemin -Encoding utf8 -Raw
    ```
- **Écriture Sécurisée sous PowerShell Windows :**
  - Éviter `Set-Content -Encoding UTF8` (qui écrit souvent un BOM sous Windows PowerShell 5.1).
  - Utiliser impérativement l'objet .NET avec `$False` pour le BOM :
    ```bash
    $utf8NoBom = New-Object System.Text.UTF8Encoding $False
    [System.IO.File]::WriteAllText($chemin, $contenu, $utf8NoBom)
    ```
- **Interdiction Formelle du Double Encodage (Mojibake) et des Caractères Corrompus :**
  - Interdiction absolue d'enregistrer ou de commiter tout fichier comportant des séquences de double encodage UTF-8 (*mojibake* résultant d'une re-conversion ANSI/UTF-8) ou le caractère de remplacement Unicode `\uFFFD` (``).
  - Avant tout commit ou fin d'intervention, l'Agent IA doit vérifier l'absence totale de ces motifs sur l'ensemble des fichiers modifiés.

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
- **Consultation et Séparation des Espaces de Livrables (`ua-lab/` vs `tutoriels/`) :**
  - **Sur la plateforme d'autoformation Jekyll (`autoformations-professionaliser`) :** Les livrables de référence des ateliers d'apprentissage sont réalisés et hébergés dans **`ua-lab/[slug-domaine]/[slug-ua]/[slug-tuto]/`** par l'Agent Rédacteur d'Autoformation (via le skill `tuto-livrable-atelier-writer`) **toujours sur l'application modèle TodoList**. Ils sont consultables par les apprenants directement depuis les tutoriels enrichis (`tuto-atelier-notions`).
  - **Sur le poste apprenant (dépôt du projet cible) :** L'apprenant ancre ses illustrations et cas pratiques d'ateliers **toujours sur son Projet Technique individuel** et range ses fiches sous `tutoriels/`. Pour le code applicatif (`tuto-code`), il opère **toujours sur le Projet d'Imitation (Blog)** pour livrer le code sous `src/`.
  - **Décharge formelle :** L'Agent Réalisation de Sprint est formellement déchargé de la production des ateliers d'autoformation (`ua-lab`).
  - **Exclusion de la Navigation Just the Docs (`nav_exclude: true`) :** Tous les livrables de référence publiés sous `ua-lab/` (fiches Markdown et diaporamas Marp) doivent obligatoirement porter `nav_exclude: true` dans leur Front Matter YAML afin de ne pas apparaître dans le menu de navigation latéral du site.

## 4. Transparence de l'Agent IA & Traçabilité des Actions
- **Affichage Obligatoire des Skills Utilisés :** À la fin de chaque échange / discussion, l'Agent IA doit obligatoirement afficher la liste exacte des **Skills locaux utilisés** lors de la réponse (format : `Skills utilisés : [skill-1], [skill-2]`).
- **Plans d'action & Artéfacts `/plan` :** Dans tout artéfact de plan d'implémentation (`plan-*.md`), l'Agent IA doit obligatoirement et systématiquement déterminer et lister de manière exhaustive les **Skills locaux mobilisés** pour l'ensemble du plan ainsi que pour chaque étape/composant. Chaque étape du plan doit explicitement mentionner le ou les skills responsables de sa réalisation.

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

