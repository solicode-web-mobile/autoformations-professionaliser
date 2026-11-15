# Guide Opérationnel : Comment Utiliser `tutorial-lab-writer`

## 1. Rôle du Skill
Le skill `tutorial-lab-writer` est le rédacteur technique et pédagogique dédié aux Unités d'Apprentissage relevant du niveau de maturité **`UA-Lab`** (ateliers pratiques guidés de modélisation, de cadrage agile, d'architecture et d'outillage IA).

---

## 2. Cas d'Usage Principaux
- Rédaction des 3 fiches de tutoriels (Théorie, Pratique sur projet d'imitation, Prompts RIO fil rouge) pour une Unité d'Apprentissage `UA-Lab`.
- Alignement et mise à jour d'un atelier pratique guidé à partir de la source de vérité (`_plan-tuto-D.XXX.Y.md`).
- Formalisation des critères d'évaluation et de validation d'un atelier pratique UML, Scrum ou Architecture.

---

## 3. Prompts Types pour Invoquer le Skill
- *« Rédige les fiches de tutoriels pour l'UA-Lab UA.311.21 à partir du plan _tutos/_plan-tuto-D.311.2.md. »*
- *« Mets à jour la tâche 2 (Pratique) de l'UA-Lab UA.311.22 avec les jalons de réalisation Mermaid. »*
- *« Rédige le prompt RIO de la tâche 3 de l'UA-Lab UA.312.11 pour le projet fil rouge. »*

---

## 4. Prérequis
Avant d'activer le skill, s'assurer que :
1. L'Unité d'Apprentissage est explicitement qualifiée avec `maturite: "UA-Lab"`.
2. Le plan de tutoriels associé (`_tutos/_plan-tuto-D.XXX.Y.md`) et le cadrage de session (`_tutos/_S0X.md`) sont disponibles comme sources de vérité.
3. Les emplacements cibles de livrables (`livrables/uml/`, `livrables/ia/prompts/`, etc.) sont identifiés.

---

## 5. Déroulement Pas-à-Pas

### Étape 1 : Chargement des Sources de Vérité
- Charger la description de l'UA dans `_uas/` et dans le plan du domaine `_tutos/_plan-tuto-D.XXX.Y.md`.
- Extraire les 3 tâches associées : Tâche 1 (Théorie), Tâche 2 (Pratique), Tâche 3 (Prompts & Skills).

### Étape 2 : Rédaction de la Fiche Théorie (`T.XXX.YY1`)
- Renseigner la section 1 : Positionnement dans le Flux & la Stack.
- Définir le Travail à faire pour l'apprenant (recherche documentaire, mémo de synthèse).
- Formaliser les Notions Clés et les questions d'auto-évaluation.

### Étape 3 : Rédaction de la Fiche Pratique (`T.XXX.YY2`)
- Définir le chemin exact du livrable physique attendu.
- Découper la réalisation en 3 jalons chronologiques clairs.
- Ajouter les points de vigilance et les critères de validation sous forme de cases à cocher `[ ]`.

### Étape 4 : Rédaction de la Fiche Prompts & Skills (`T.XXX.YY3`)
- Structurer le prompt selon la méthode RIO (Rôle, Instruction, Output, Contraintes Négatives).
- Spécifier les critères de test du prompt avec un agent IA.

### Étape 5 : Encodage et Validation
- Sauvegarder impérativement les fichiers en UTF-8 sans BOM.
- Vérifier la présence du champ `maturite: "UA-Lab"` et de l'état `en_construction: true`.

---

## 6. Méthode de Vérification des Livrables
- **Absence de BOM :** Exécuter le test de validation PowerShell sur les fichiers `.md`.
- **Rendu Jekyll :** Vérifier que les pages s'affichent correctement sous `_layouts/tuto.html`.
- **Zéro Capture d'Écran :** Contrôler que tous les livrables exigés sont des fichiers de code ou de texte (`.mmd`, `.md`, `.prompt.md`).
