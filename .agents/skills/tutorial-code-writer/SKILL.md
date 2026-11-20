---
name: tutorial-code-writer
description: Conçoit et rédige les tutoriels techniques d'apprentissage de code incrémental pas-à-pas (UA-Tuto, progression E_{n-1} -> E_n vers un code final d'arrivée) nativement simplifiés, avec injecteur window.pageData pour l'éditeur interactif. Opère de manière générique sur tous les niveaux selon les règles configurées dans .agents/rules/. Membre de l'écosystème tutorial-*-writer sous la gouvernance de tutorial-writer.
version: 1.1.0
---

# 1. Mission
Ce skill est le **rédacteur technique spécialisé dans l'apprentissage de code incrémental pas-à-pas** (`UA-Tuto`).
Il opère de façon générique et indépendante du niveau d'apprentissage (N1, N2, N3), s'adaptant aux technologies et directives configurées dans `.agents/rules/`.
Il fait partie intégrante de l'écosystème **`tutorial-*-writer`** et applique les règles transversales et le protocole de synchronisation gouvernés par le Master Skill **[tutorial-writer](../tutorial-writer/SKILL.md)**.

Sa vocation didactique est de découper un code source final en paliers élémentaires et digestes :
chaque tutoriel transforme l'état d'entrée $E_{n-1}$ vers l'état de sortie $E_n$ avec le strict minimum de code nécessaire pour comprendre la notion.

### Trajectoire Pédagogique Globale
$$\text{Tutoriel (Comprendre avec le minimum de code)} \longrightarrow \text{Prototype (Pratiquer \& consolider)} \longrightarrow \text{Projet (Développer la compétence métier)}$$

Le skill prend en charge deux dynamiques de code :
1. **Le Tutoriel Unitaire Autonome :** Apprentissage ciblé d'une fonction ou brique isolée avec son micro-livrable.
2. **La Série de Tutoriels en Progression Incrémentale :** Découpe méthodique d'un **code source final d'arrivée** en étapes successives ($E_0 \to E_1 \to \dots \to E_n$), chaque tutoriel apportant une brique cumulée.

---

# 2. Déclenchement & Limites
- **Quand l'activer :**
  - Rédaction d'une **série de tutoriels de code en progression** à partir d'un code source final cible (*« Rédige la série de tutoriels pour construire la maquette de la page d'accueil »*).
  - Rédaction d'un **tutoriel unitaire de code** (*« Rédige un tutoriel pour créer un composant interactif »*).
  - Modernisation ou allègement d'un ancien tutoriel de programmation trop dense pour respecter le principe de charge cognitive minimale.
  - Configuration de composants interactifs utilisant `data_*` et `window.pageData`.
- **Quand NE PAS l'activer :**
  - Ateliers pratiques guidés d'assimilation, modélisation ou outillage IA (`UA-Lab`) ➔ Utiliser [tutorial-lab-writer](../tutorial-lab-writer/SKILL.md).
  - Tâches opérationnelles de sprint et rituels agiles (`UA-Tâche`) ➔ Utiliser [tutorial-task-writer](../tutorial-task-writer/SKILL.md).
  - Planification globale et ordonnancement de session ➔ Utiliser [tutorial-planer](../tutorial-planer/SKILL.md).
  - Gouvernance globale, routage et synchronisation physique ➔ Utiliser [tutorial-writer](../tutorial-writer/SKILL.md).

---

# 3. Entrées & Ressources à Charger
- **Règles Transversales Partagées :** Chargement obligatoire du socle défini dans le Master Skill [tutorial-writer](../tutorial-writer/SKILL.md).
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
1. **Respect du Socle Transversal de `tutorial-writer` :** Encodage strict UTF-8 sans BOM, blocs colonne 0 avec saut de ligne, arborescence canonique `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/`, français A1-A2, respect des règles de versionnement du niveau actif.
2. **Principe de Continuité Absolue ($E_{n-1} \to E_n$) :** Dans une série, le code de départ du tutoriel $N$ doit être rigoureusement identique au livrable final validé du tutoriel $N-1$.
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
1. **Étape 1 — Analyse du Code Final & Découpage :** Identifier le code source cible et isoler les incréments successifs.
2. **Étape 2 — Préparation des États $E_{n-1}$ et $E_n$ :** Définir le delta technique exact à coder par l'apprenant.
3. **Étape 3 — Rédaction du Corps Pédagogique :**
   - Contexte & Objectif opérationnel (une seule phrase d'impact).
   - Données de départ (fichiers d'entrée).
   - Notions essentielles (explications courtes avec extraits autonomes).
   - Pratique guidée (tableau d'action didactique pas-à-pas).
   - Livrable attendu (chemin relatif canonique sous `tutoriels/`).
   - Glossaire concis d'une ligne par terme nouveau.
4. **Étape 4 — Transmission au Master Skill :** Signaler à `tutorial-writer` le livrable produit pour synchronisation miroir avec le projet cible.

---

# 6. Gestion des Ambiguïtés & Décisions
- **Surcharge cognitive :** Si le code final nécessite trop de modifications intermédiaires, scinder le tutoriel en deux sous-étapes ou déléguer la complexité conceptuelle à un `UA-Lab` préalable via `tutorial-writer`.
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
- Emplacement : `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/` sur la branche de travail active.
- Fichier : `[slug-tuto].md` (et code source sous `src/` ou dossier de projet).

## 6. Glossaire
- **[Terme] :** [Définition courte d'une ligne].
```

---

# 8. Contrôle Qualité (Checklist Binaire)
- [ ] Le tutoriel démarre colonne 0 sans indentation pour chaque bloc de code.
- [ ] Le code de départ reprend exactement la fin du tutoriel précédent ($E_{n-1} \to E_n$).
- [ ] Le livrable est spécifié avec son chemin relatif canonique sous `tutoriels/`.
- [ ] Le versionnement Git respecte les règles du niveau actif définies dans `.agents/rules/`.
- [ ] Le script `window.pageData` est injecté si des champs `data_*` sont renseignés.
- [ ] Les règles transversales de `tutorial-writer` sont scrupuleusement respectées.

---

# 9. Gestion des Erreurs Fréquentes
| Erreur Typique | Cause | Solution Immédiate |
| :--- | :--- | :--- |
| Rupture de continuité dans une série | Tutoriel N déconnecté de N-1 | Vérifier que l'état initial de N reprend rigoureusement le code final de N-1 |
| Blocs de code indentés sous des puces | Formatage Markdown incorrect | Aligner strictement à la colonne 0 avec saut de ligne |
| Multiples exercices d'entraînement | Confusion avec le projet | Réduire au strict minimum de code (1 seul cas d'application concis) |

---

# 10. Exemples Concrets (Few-Shot)
> **Tutoriel T.XXX.111 :** Déclarer la route ou le squelette d'entrée renvoyant un texte simple.  
> **Tutoriel T.XXX.112 :** Modifier l'entrée pour retourner le template de vue associé.  
> **Tutoriel T.XXX.113 :** Intégrer la boucle ou le binding dynamique pour afficher la liste de données.
