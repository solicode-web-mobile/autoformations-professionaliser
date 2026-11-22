---
name: tuto-writer
description: Master Skill et chef d'orchestre de la rédaction, de la gouvernance didactique et de la synchronisation des tutoriels avec les livrables du projet cible. Opère de façon générique sur les niveaux N1, N2 et N3 pour l'EFP. Centralise les règles transversales (UTF-8, colonne 0, organisation des livrables, typologie tuto-*, journalisation CLI ciblée, style A1-A2), route vers tutorial-*-writer et pilote le contrat .sync/rules-sync.md.
version: 4.4.0
---

# 1. Mission & Responsabilités
Master Skill et chef d'orchestre didactique de l'**EFP (Établissement de Formation Professionnelle)**, opérant de manière **générique et indépendante du niveau** (N1 Découvrir, N2 Prototyper, N3 Développer / Réaliser selon `.agents/rules/` et `.agents/resources/[niveau]/`).

```mermaid
flowchart LR
    Rules[".agents/rules/<br/>(Niveau & Persona)"] --> Master["tuto-writer (Master)"]
    Refs[".agents/references/<br/>(Livrables, Typologie, Maturation, Gitflow)"] --> Master
    Master --> RulesShared["Socle Transversal Partagé (12 Règles)"]
    Master --> Format["Typologie tuto-*"]
    Format --> Code["tuto-code-writer<br/>(tuto-notion / tuto-code)"]
    Format --> Lab["tuto-atelier-writer<br/>(tuto-atelier dans _tutos/)"]
    Lab --> LabReal["tuto-livrable-atelier-writer<br/>(Réalisation dans ua-lab/)"]
    Format --> Task["tuto-tache-writer<br/>(tuto-tache)"]
    Master --> Domain["Domaine Technique"]
    Domain --> TDomain["tuto-writer-[slug]"]
```

Il assure une quadruple responsabilité cardinale :
1. **Gouvernance Transversale :** Fait respecter le socle commun invariable (encodage, formatage Markdown, organisation des livrables selon `.agents/references/organisation-livrables.md`, journalisation CLI ciblée selon `.agents/references/maturation-et-typologie-ua-tuto.md`, style A1-A2).
2. **Aiguillage Didactique :** Route vers le sous-skill spécialisé de l'écosystème `tutorial-*-writer` selon la maturité (`veille`, `lab`, `ua-lab`, `tutoriel`, `projet`) et le type (`tuto-atelier`, `tuto-notion`, `tuto-code`, `tuto-tache`).
3. **Règles Spécifiques par Domaine :** Combine la structure avec le skill dédié du domaine `tuto-writer-[slug]` (`uml`, `architecture`, `laravel`, `ia`, `scrum`, `realisation-projet`, etc.).
4. **Synchronisation Inter-Agents :** Pilote de façon exclusive les échanges, la validation des livrables et le passage de `maturite: "lab"` à `maturite: "ua-lab"` selon le contrat `<projet-cible>/.sync/rules-sync.md`.

---

# 2. Déclenchement & Limites
- **Activer :** Création/refonte de tutoriels (tous niveaux) ; audit de conformité didactique ; routage vers `tutorial-*-writer` ; synchronisation des versions avec le projet cible selon `.sync/rules-sync.md`.
- **Ne PAS activer :** Planification globale de session/stubs ➔ `didactique-tuto-planner` | Alignement session/flux opérationnel ➔ `didactique-session-planner` | Layouts/CSS Jekyll ➔ `dev-jekyll` | Synchronisation Core Theme ➔ `sync-theme`.

---

# 3. Entrées & Ressources à Charger
- **Normes Centralisées des Livrables & Typologie :** `.agents/references/organisation-livrables.md` et `.agents/references/maturation-et-typologie-ua-tuto.md`.
- **Cycle de Maturation des Ateliers :** `.agents/references/maturation-et-typologie-ua-tuto.md`.
- **Stratégie Git & Identité de l'Agent :** `.agents/references/gitflow.md` et `.agents/rules/persona.md`.
- **Contrat Inter-Agents :** `<projet-cible>/.sync/rules-sync.md` (consultation obligatoire avant tout échange/synchronisation).
- **Configuration Dynamique :** Directives du niveau actif dans `.agents/rules/` et standards techniques dans `.agents/rules/standards-techniques.md`.
- **Référentiel Cible :** Dépôt physique du projet cible, arborescence miroir des versions `<projet-cible>/.sync/` et livrables sous `tutoriels/` ou racine (`src/`, `docs/`, `sprints/`).

---

# 4. Contraintes & Règles Inviolables Partagées (Socle Commun)
Tous les rédacteurs `tutorial-*-writer` appliquent obligatoirement ces 12 règles :
1. **Encodage Strict :** UTF-8 sans BOM sur tous les fichiers (`.md`, `.command.md`, code).
2. **Formatage Markdown Colonne 0 :** Tout bloc de code débute strictement à la colonne 0 (zéro espace, même sous une liste), précédé et suivi d'une ligne vide.
3. **Organisation des Livrables & Arborescence Canonique :** Régie par `.agents/references/organisation-livrables.md`. Les livrables d'apprentissage (`tuto-atelier`, `tuto-notion`) sont déposés sous `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/`. Le code source de l'imitation (`tuto-code`) est déposé sous `src/` (ou structure standard du framework). Les livrables opérationnels (`tuto-tache`) sont positionnés aux emplacements racine (`docs/`, `sprints/`, `src/`). Interdiction formelle du dossier `labs/`. Le fichier `README.md` est autorisé uniquement au niveau racine `tutoriels/README.md` (aucun `README.md` dans les sous-dossiers).
4. **Rapport d'Exécution CLI (`[slug-tuto].command.md`) :** Régie par `.agents/references/maturation-et-typologie-ua-tuto.md`. Requis **uniquement** pour les tutoriels `tuto-atelier`, `tuto-notion` et `tuto-code` comportant des manipulations en ligne de commande. **Formellement proscrit pour les fiches `tuto-tache`** (la tâche opérationnelle impacte directement les fichiers de projet à la racine). Consigner les commandes utiles en bloc ```` ```bash ```` brut (sans double encapsulation). Interdiction formelle d'y inclure les commandes Git (`add`, `commit`, `push`). Omettre si aucune commande CLI.
5. **Environnement & Commandes :** Terminal dictated par `.agents/rules/`. Commandes universelles compatibles (`mkdir`, redirection standard `echo "" > <fichier>`, proscrire `touch` et `New-Item`).
6. **Versionnement Git & Commits Atomiques :** Régie par `.agents/references/gitflow.md` et `.agents/rules/persona.md`. Les travaux sont versionnés sur la branche unique du sprint (`sprintX`). Interdiction formelle d'ajouter des étapes directives de commit ou push (`git add`, `git commit`, `git push`) à la fin des tutoriels (autonomie de l'apprenant N2/N3).
7. **Ciblage des Projets (Ateliers vs Code) :** Pour les ateliers (`tuto-atelier`, `tuto-atelier-notions`), l'apprenant ancre ses illustrations et pratiques **toujours sur son Projet Technique individuel** (la solution formateur consultable sous `ua-lab/` étant sur **TodoList**). Pour le code incrémental (`tuto-code`), l'apprenant développe **toujours sur le Projet d'Imitation (*Blog des Lauréats*)** pour délivrer les livrables de code sous `src/`.
8. **Zéro Fuite de Cuisine Interne Didactique :** Interdiction d'exposer aux apprenants des termes internes (« 20/80 », « Règle des 20/80 », « Ce que l'apprenant doit produire »). Utiliser « Notions fondamentales » et « Recherches à effectuer ».
9. **Terminologie Directe :** Utiliser exclusivement le terme « Étape » (`1. **Étape 1 — ... :**`). Le terme « Jalon » est proscrit.
10. **Neutralité Technologique :** Désigner les frameworks par leur nom générique (ex: `Laravel`, `Alpine.js`) sans numéro de version éphémère dans le tutoriel (version définie dans le `README.md` du projet).
11. **Exclusion des Outils Formateur :** Le dossier `flux-travail/` ne doit jamais être transmis aux apprenants ni figurer dans les commandes `mkdir`.
12. **Zéro Capture d'Écran :** Tout livrable est du code source ou du markdown versionné.
13. **Zéro Justification d'Exemple Support & Zéro Solution Fictive :**
    - Interdiction formelle de communiquer aux apprenants la justification didactique du choix d'un cas d'usage support (ex: Todo List) ou de leur demander de justifier ce choix.
    - Ne déclarer aucun bloc `livrables:` en frontmatter tant que le tutoriel est `statut_realisation: "a_realiser"` pour éviter des liens brisés. La traçabilité des livrables s'opère via un fichier `version.yml` à la racine de leur dossier lors de la réalisation.

---

# 5. Procédure d'Aiguillage Didactique & Technique
`tuto-writer` orchestre la double délégation structurelle et technique selon `.agents/references/maturation-et-typologie-ua-tuto.md` :
1. **Délégation par Typologie `tuto-*` :**
   - **`type: "tuto-atelier"` ➔ [tuto-atelier-writer](../tuto-atelier-writer/SKILL.md) & [tuto-livrable-atelier-writer](../tuto-livrable-atelier-writer/SKILL.md) :**
     - `tuto-atelier-writer` rédige la fiche de cadrage de l'atelier dans `_tutos/` (sujet, objectifs, consignes).
     - `tuto-livrable-atelier-writer` réalise concrètement le travail prescrit et produit les livrables sous `ua-lab/` (fiche technique `[slug].md`, diaporama Marp `presentation-[slug].md` avec `layout: presentation`, journal CLI).
     - Promotion en `tuto-atelier-notions` avec notions fondamentales consolidées et bloc de solution consultable.
   - **`type: "tuto-notion"` ➔ [tuto-code-writer](../tuto-code-writer/SKILL.md) :**
     - Notion & syntaxe isolée hors imitation (pratique dans `tutoriels/`, pas de Marp, `[slug-tuto].command.md` si CLI).
   - **`type: "tuto-code"` ➔ [tuto-code-writer](../tuto-code-writer/SKILL.md) :**
     - Progression incrémentale pas-à-pas ($E_{n-1} \to E_n$) intégrée à l'imitation (code dans `src/`, pas de Marp, `[slug-tuto].command.md` si CLI).
   - **`type: "tuto-tache"` ➔ [tuto-tache-writer](../tuto-tache-writer/SKILL.md) :**
     - Cadrage opérationnel et cérémonies agiles Scrum (0% théorie, livrables racine, **zéro `.command.md`**, **zéro diaporama Marp**).
2. **Injection des Règles Spécifiques de Domaine (`tuto-writer-[slug]`) :**
   - Applique les exigences, outils et syntaxes du domaine cible (`uml`, `architecture`, `laravel`, `ia`, `scrum`, `realisation-projet`, etc.).

---

# 6. Protocole de Synchronisation Inter-Agents (`.sync/rules-sync.md`)
Les échanges avec le projet cible appliquent rigoureusement le contrat `<projet-cible>/.sync/rules-sync.md` :

| Dimension | Agent Réalisation (Agent Projet Cible) | Agent Autoformation (`tuto-writer`) |
| :--- | :--- | :--- |
| **Rôle Principal** | Réalise les fonctionnalités, fiches d'atelier, diaporamas Marp et code dans le projet cible. | Maintient `_tutos/`, audite et synchronise les parcours pédagogiques dans Jekyll. |
| **Gestion des Versions** | Crée/incrémente les `version.yml` **exclusivement dans `.sync/`** (ex: `fichier.md: "1.0.0"`). Interdiction formelle hors de `.sync/`. | Lit `.sync/.../version.yml` et compare avec les versions déclarées dans le front-matter du tutoriel. |
| **Notification & Bascule de Maturité** | Déclare dans le front-matter de `_tutos/` : `sprint`, `statut_realisation: "realise"` et la liste des `livrables` (chemins + versions). | **Pour un `tuto-atelier` :** audite les livrables réels, bascule la fiche de `maturite: "lab"` à `maturite: "ua-lab"`, injecte les notions fondamentales en détail, spécifie le plan d'UA et passe `statut_realisation: "synchronise"`. |
| **Adaptation Mutuelle** | Si livrable incomplet/décalé : corrige et adapte le livrable dans `tutoriels/` ou racine. | Si le projet valide une solution plus pertinente : met à jour le tutoriel de référence dans `_tutos/`. |

---

# 7. Format de Sortie Canonique
```markdown
---
layout: tuto
title: "Titre du Tutoriel"
sous_titre: "Sous-titre technique"
tuto_id: "T.XXX.YYY"
ua: "UA.XXX.YY"
maturite: "ua-lab" # lab | ua-lab | tutoriel | projet
type: "tuto-atelier" # tuto-atelier | tuto-notion | tuto-code | tuto-tache
nav_order: 10
simplified: true
branche: "sprint1"
sprint: "sprint1"
statut_realisation: "synchronise" # a_realiser | realise | synchronise | a_adapter
livrables:
  - chemin: "tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].md"
    version: "1.0.0"
  - chemin: "tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/presentation-[slug-tuto].md"
    version: "1.0.0"
---
```

---

# 8. Contrôle Qualité (Checklist Binaire)
- [ ] Encodage UTF-8 sans BOM et blocs de code colonne 0 sans indentation.
- [ ] Dissociation stricte `maturite:` (`lab`, `ua-lab`, `tutoriel`, `projet`) et `type:` (`tuto-atelier`, `tuto-notion`, `tuto-code`, `tuto-tache`).
- [ ] Diaporama Marp `presentation-[slug-tuto].md` présent uniquement pour `tuto-atelier`.
- [ ] Rapport CLI `[slug-tuto].command.md` présent pour `tuto-atelier`, `tuto-notion`, `tuto-code` (strictement absent pour `tuto-tache`).
- [ ] Zéro terme interdit (« Solicode » au profit de « EFP », « 20/80 », « Jalon », captures d'écran).
- [ ] **Protocole .sync/ :** Consultation préalable de `.sync/rules-sync.md` ; bascule de `lab` à `ua-lab` avec notions détaillées après validation de l'atelier.
