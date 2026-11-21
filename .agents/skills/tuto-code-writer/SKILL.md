---
name: tuto-code-writer
description: Conçoit et rédige les tutoriels techniques d'apprentissage de code pour l'EFP (maturite: tutoriel, type: tuto-notion hors imitation sous tutoriels/ ou type: tuto-code incrémental E_{n-1} -> E_n sur imitation sous src/) nativement simplifiés, avec injecteur window.pageData pour l'éditeur interactif. Opère de manière générique sur tous les niveaux selon les règles configurées dans .agents/rules/. Membre de l'écosystème tutorial-*-writer sous la gouvernance de tuto-writer.
version: 1.3.0
---

# 1. Mission
Ce skill est le **rédacteur technique spécialisé dans l'apprentissage de code** en maturité **`tutoriel`** pour l'EFP.
Il opère de façon générique et indépendante du niveau d'apprentissage (N1, N2, N3), s'adaptant aux technologies et directives configurées dans `.agents/rules/`.
Il fait partie intégrante de l'écosystème **`tutorial-*-writer`** et applique les règles transversales, l'organisation des livrables et le protocole de synchronisation gouvernés par le Master Skill **[tuto-writer](../tuto-writer/SKILL.md)**, [.agents/references/organisation-livrables.md](../../references/organisation-livrables.md) et [.agents/references/maturation-et-typologie-ua-tuto.md](../../references/maturation-et-typologie-ua-tuto.md).

### Trajectoire Pédagogique Globale
$$\text{Tutoriel (Comprendre avec le minimum de code)} \longrightarrow \text{Prototype (Pratiquer \& consolider)} \longrightarrow \text{Projet (Développer la compétence métier)}$$

Selon [.agents/references/maturation-et-typologie-ua-tuto.md](../../references/maturation-et-typologie-ua-tuto.md), l'apprentissage de code se décline en deux types précis :
1. **`tuto-notion` (Tutoriel de Notion / Syntaxe Isolé) :** Apprentissage ciblé d'une fonction, syntaxe ou brique isolée avec son micro-livrable hors du projet d'imitation. Livrable déposé sous `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/` (sans diaporama Marp, avec rapport CLI `[slug-tuto].command.md` si manipulations CLI).
2. **`tuto-code` (Tutoriel de Code Incrémental sur Imitation) :** Découpe méthodique d'un **code source final d'arrivée** en étapes successives ($E_0 \to E_1 \to \dots \to E_n$), chaque tutoriel apportant une brique cumulée dans le projet d'imitation. Code source produit sous `src/` (ou structure standard du framework), sans diaporama Marp, avec rapport CLI `[slug-tuto].command.md` consigné sous `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/` si manipulations CLI.

---

# 2. Déclenchement & Limites
- **Quand l'activer :**
  - Rédaction d'une **série de tutoriels de code en progression** (`type: "tuto-code"`) à partir d'un code source final cible (*« Rédige la série de tutoriels pour construire la maquette de la page d'accueil »*).
  - Rédaction d'un **tutoriel unitaire de notion** (`type: "tuto-notion"`) (*« Rédige un tutoriel pour manipuler les tableaux associatifs »*).
  - Modernisation ou allègement d'un ancien tutoriel de programmation trop dense pour respecter le principe de charge cognitive minimale.
  - Configuration de composants interactifs utilisant `data_*` et `window.pageData`.
- **Quand NE PAS l'activer :**
  - Ateliers pratiques guidés d'assimilation, modélisation ou outillage IA (`type: "tuto-atelier"`) ➔ Utiliser [tuto-atelier-writer](../tuto-atelier-writer/SKILL.md).
  - Tâches opérationnelles de sprint et rituels agiles (`type: "tuto-tache"`) ➔ Utiliser [tuto-tache-writer](../tuto-tache-writer/SKILL.md).
  - Planification globale et ordonnancement de session ➔ Utiliser [didactique-tuto-planner](../didactique-tuto-planner/SKILL.md).
  - Gouvernance globale, routage et synchronisation physique ➔ Utiliser [tuto-writer](../tuto-writer/SKILL.md).

---

# 3. Entrées & Ressources à Charger
- **Normes Centralisées des Livrables & Typologie :** [.agents/references/organisation-livrables.md](../../references/organisation-livrables.md) et [.agents/references/maturation-et-typologie-ua-tuto.md](../../references/maturation-et-typologie-ua-tuto.md).
- **Stratégie Git :** [.agents/references/gitflow.md](../../references/gitflow.md).
- **Règles Transversales Partagées :** Chargement obligatoire du socle défini dans le Master Skill [tuto-writer](../tuto-writer/SKILL.md).
- **Ressources du Niveau & du Domaine :**
  - Directives du niveau actif dans `.agents/rules/`.
  - Standards techniques du projet dans `.agents/rules/standards-techniques.md`.
  - Fiche du domaine technique concerné sous `.agents/resources/[niveau]/domaines/` si existante.
- **Données d'Entrée du Code :**
  1. Le **Plan des tutoriels de l'UA** : Liste ordonnée des étapes avec leurs notions cibles.
  2. Le **Code source final d'arrivée** : Fichier(s) complet(s) représentant le livrable final attendu.
  3. Le **Code de départ ($E_{n-1}$)** : Fichier initial hérité de l'étape précédente.

---

# 4. Contraintes & Règles Inviolables
1. **Respect du Socle Centralisé & Transversal :** Encodage strict UTF-8 sans BOM, blocs colonne 0 avec saut de ligne, arborescence canonique selon [.agents/references/organisation-livrables.md](../../references/organisation-livrables.md), français A1-A2, respect des règles de versionnement de [.agents/references/gitflow.md](../../references/gitflow.md).
2. **Principe de Continuité Absolue ($E_{n-1} \to E_n$) :** Dans une série `tuto-code`, le code de départ du tutoriel $N$ doit être rigoureusement identique au livrable final validé du tutoriel $N-1$.
3. **Isolation de la Difficulté :** Une seule brique de complexité par tutoriel. Ne jamais introduire simultanément deux bibliothèques ou paradigmes nouveaux.
4. **Code 100% Exécutable et Vérifiable :** Tout extrait fourni dans la pratique doit être autonome, sans variable non déclarée ni appel fictif.
5. **Gestion de l'Éditeur Interactif (`window.pageData`) :**
   - Dès qu'un champ `data_*` est présent dans le frontmatter, injecter le bloc JavaScript sous le frontmatter :
     ```html
     <script>
       window.pageData = {
         code_depart: {{ page.data_code_depart | jsonify }},
         code_solution: {{ page.data_code_solution | jsonify }}
       };
     </script>
     ```
   - Si les champs `data_*` sont vides, supprimer la section *Données de départ*.

---

# 5. Procédure Pas-à-Pas
1. **Étape 1 — Qualification de la Typologie :** Identifier s'il s'agit d'un `tuto-notion` (hors imitation) ou d'un `tuto-code` (sur l'imitation).
2. **Étape 2 — Analyse du Code Final & Découpage :** Identifier le code source cible et isoler les incréments successifs.
3. **Étape 3 — Préparation des États $E_{n-1}$ et $E_n$ :** Définir le delta technique exact à coder par l'apprenant.
4. **Étape 4 — Rédaction du Corps Pédagogique :**
   - Contexte & Objectif opérationnel (une seule phrase d'impact).
   - Données de départ (fichiers d'entrée).
   - Notions essentielles (explications courtes avec extraits autonomes).
   - Pratique guidée (tableau d'action didactique pas-à-pas).
   - Livrable attendu (chemin relatif canonique selon la typologie).
   - Glossaire concis d'une ligne par terme nouveau.
5. **Étape 5 — Transmission au Master Skill :** Signaler à `tuto-writer` le livrable produit pour synchronisation miroir avec le projet cible.

---

# 6. Gestion des Ambiguïtés & Décisions
- **Surcharge cognitive :** Si le code final nécessite trop de modifications intermédiaires, scinder le tutoriel en deux sous-étapes ou déléguer la complexité conceptuelle à un `UA-Lab` préalable via `tuto-writer`.
- **Composant interactif :** Si la manipulation se fait directement dans l'éditeur interactif Jekyll, alimenter obligatoirement `data_code_depart` et `data_code_solution`.

---

# 7. Format de Sortie Canonique
```markdown
---
layout: tuto
title: "Titre du Tutoriel"
sous_titre: "Sous-titre technique"
tuto_id: "T.XXX.YYY"
ua: "UA.XXX.YY"
maturite: "tutoriel"
type: "tuto-code" # tuto-code | tuto-notion
nav_order: 10
simplified: true
data_code_depart: ""
data_code_solution: ""
---

## 1. Contexte & Objectif
[Présentation concrète du composant à réaliser]

## 2. Données de départ
[Fichiers d'entrée nécessaires]

## 3. Notions Essentielles
### 3.1 [Concept clé 1]
[Explication courte avec extrait de code autonome]

## 4. Pratique & Réalisation Guidée
| Étape | Action à réaliser | Fichier modifié | Résultat attendu |
| :-: | :--- | :--- | :--- |
| 1 | [Action 1] | `chemin/fichier.ext` | [Effet visible] |
| 2 | [Action 2] | `chemin/fichier.ext` | [Effet visible] |

## 5. Livrable attendu
- Emplacement : selon `.agents/references/organisation-livrables.md` :
  - Si `tuto-notion` : `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].md`
  - Si `tuto-code` : code source sous `src/` (ou arborescence framework) et rapport `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/[slug-tuto].command.md` (si CLI).
  - Pas de diaporama Marp.

## 6. Glossaire
- **[Terme] :** [Définition courte d'une ligne].
```

---

# 8. Contrôle Qualité (Checklist Binaire)
- [ ] Le tutoriel démarre colonne 0 sans indentation pour chaque bloc de code.
- [ ] Le code de départ reprend exactement la fin du tutoriel précédent ($E_{n-1} \to E_n$).
- [ ] Le livrable est spécifié avec son chemin relatif canonique conforme à `organisation-livrables.md`.
- [ ] Le versionnement Git respecte `gitflow.md` (aucun commit/push imposé à l'apprenant).
- [ ] Le script `window.pageData` est injecté si des champs `data_*` sont renseignés.
- [ ] Aucun diaporama Marp n'est demandé pour un tutoriel de code.
- [ ] Les règles transversales de `tuto-writer` sont scrupuleusement respectées.

---

# 9. Gestion des Erreurs Fréquentes
| Erreur Typique | Cause | Solution Immédiate |
| :--- | :--- | :--- |
| Rupture de continuité dans une série | Tutoriel N déconnecté de N-1 | Vérifier que l'état initial de N reprend rigoureusement le code final de N-1 |
| Blocs de code indentés sous des puces | Formatage Markdown incorrect | Aligner strictement à la colonne 0 avec saut de ligne |
| Multiples exercices d'entraînement | Confusion avec le projet | Réduire au strict minimum de code (1 seul cas d'application concis) |
| Diaporama Marp demandé pour un tutoriel de code | Confusion avec `tuto-lab` | Supprimer la demande de Marp (réservé exclusivement à `tuto-lab`) |

---

# 10. Exemples Concrets (Few-Shot)
> **Tutoriel T.XXX.111 :** Déclarer la route ou le squelette d'entrée renvoyant un texte simple.  
> **Tutoriel T.XXX.112 :** Modifier l'entrée pour retourner le template de vue associé.  
> **Tutoriel T.XXX.113 :** Intégrer la boucle ou le binding dynamique pour afficher la liste de données.
