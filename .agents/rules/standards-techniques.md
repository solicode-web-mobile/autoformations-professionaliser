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

## 3. Éditeur de Code & Livrables
- **Éditeur interactif :** Dès qu'un tutoriel utilise des champs `data_*`, insérer systématiquement le script `window.pageData` sous le Front Matter. Isoler le code de préparation pour que l'onglet de travail de l'apprenant reste vierge.
- **Médias :** Stockage obligatoire dans `images-tutos/[Domaine]/[ID_Tuto]/[nom.ext]`.
- **Livrables :** Le livrable est toujours un **dépôt GitHub** ou un fichier `.md` de commandes. **Interdiction stricte de captures d'écran comme livrable.**
- **Règle de Journalisation des Commandes :** Dès qu'un tutoriel implique la saisie de commandes en ligne de commande (CLI / Shell), l'apprenant doit obligatoirement consigner ses commandes dans le fichier standardisé `[slug-tuto].command.md` déposé dans le dossier `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/` sur la branche de sprint active.
- **Consultation et Synchronisation du Référentiel Physique (`D:\labs-web\projet-imiation-n3`) :** L'Agent IA inspecte obligatoirement le dépôt de référence réel situé sous `D:\labs-web\projet-imiation-n3` pour en extraire fidèlement l'arborescence, les scripts, les configurations et les règles. Si une modification demandée par l'utilisateur contredit le contenu actuel de ce référentiel, l'Agent IA doit impérativement corriger et synchroniser les livrables physiques correspondants dans `D:\labs-web\projet-imiation-n3` en même temps que les tutoriels.

## 4. Transparence de l'Agent IA
- **Affichage des compétences :** Indiquer les compétences mobilisées à la fin de chaque réponse.
- **Plans d'action :** Expliciter obligatoirement les compétences prévues pour réaliser chaque étape d'un plan d'implémentation.

## 5. Gouvernance des Skills & Documentation Obligatoire
- Tout skill (`.agents/skills/<nom-du-skill>/`) doit obligatoirement inclure un sous-dossier `doc/` contenant son guide d'utilisation opérationnel (`doc/how-to-use.md`).
- Ce document formalise : le rôle du skill, les cas d'usage, les prompts types pour l'invoquer, les prérequis, le déroulement pas-à-pas et la méthode de vérification des livrables.

## 6. Gouvernance des Modules et Compétences
- **Collection `_modules/` :** Les modules de formation officiels du cursus sont stockés sous `_modules/` avec leur `id_bdd`, `code` (`M105`..`M114`), `module_reference` (`DMB-Mxxx`) et `title`.
- **Protocole Obligatoire de Création de Compétence :**
  Lorsqu'une nouvelle compétence (`_competences/C.xxx.md`) est créée ou révisée :
  1. L'agent IA doit obligatoirement analyser les 10 modules officiels du cursus (`_modules/`).
  2. L'agent IA doit obligatoirement formuler une **proposition formelle d'affectation** du module (`module: "Mxxx"`), de sa référence BDD (`module_reference: "DMB-Mxxx"`) et de sa référence canonique (`reference: "DMB-Mxxx-C.xxx"`), argumentée techniquement et didactiquement.
  3. **Validation Obligatoire du Concepteur Pédagogique :** Il est strictement interdit à l'agent d'acter ou de figer unilatéralement l'affectation du module sans avoir obtenu au préalable la validation explicite du concepteur pédagogique (humain).

