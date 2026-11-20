# Guide Opérationnel : `tutorial-lab-writer`

## 1. Rôle & Déclenchement
Rédige les tutoriels d'ateliers pratiques guidés pour les Unités d'Apprentissage **`UA-Lab`** (assimilation conceptuelle, modélisation UML/schémas, architecture, frameworks, outillage IA).

## 2. Prompts Types
- *« Rédige les fiches de tutoriels pour l'UA-Lab UA.XXX.YY à partir du plan de domaine en omettant la théorie déjà acquise. »*
- *« Formalise la fiche théorique T.XXX.YY1 de l'UA-Lab avec les notions fondamentales et recherches à effectuer. »*
- *« Rédige le tutoriel de création du prompt backend T.XXX.YY3 selon le cahier des charges RIO complet. »*

## 3. Déroulement Pas-à-Pas
1. **Composition de l'UA-Lab (2 à 4 tâches) :** Identifier si la théorie est requise (omettre si notions déjà acquises) et si un prompt est pertinent (réservé aux flux récurrents reproductibles).
2. **Fiche Théorie & Assimilation :** Rédiger `Notions fondamentales` (socle fourni) et `Recherches à effectuer` (investigation active). Zéro terme interne (« 20/80 » banni). Zéro durée affichée.
3. **Fiche Pratique sur Projet Cible :** Fournir le cadre technique, les étapes directives (`1. **Étape 1 — ... :**`) et les critères `[ ]` binaires. **Zéro solution complète rédigée prête à copier-coller**.
4. **Fiche Création de Prompt IA :** Structurer selon la méthode RIO (Rôle, Instruction, Output, Contraintes Négatives) avec fichier `prompt-[nom].prompt.md`.
5. **Publication :** Enregistrer en UTF-8 sans BOM sous `_tutos/[Domaine]/[UA]/[Code-Tuto]/[slug].md` avec `maturite: "UA-Lab"` et `en_construction: false`.
