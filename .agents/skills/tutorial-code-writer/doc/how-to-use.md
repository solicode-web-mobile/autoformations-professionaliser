# Guide Opérationnel : Comment Utiliser `tutorial-code-writer`

## 1. Rôle du Skill
Le skill `tutorial-code-writer` est le rédacteur technique spécialisé dans la production de **tutoriels pas-à-pas d'apprentissage de code incrémental** (`UA-Tuto`).
Il s'applique de manière **générique et transversale à tous les niveaux** (N1, N2, N3), sous la gouvernance du Master Skill **`tutorial-writer`**.

---

## 2. Cas d'Usage Principaux
- Rédaction d'une **série de tutoriels de code en progression** guidant l'apprenant depuis une base vierge ($E_0$) jusqu'au code complet cible ($E_n$).
- Rédaction d'un **tutoriel unitaire de programmation** (apprentissage ciblé d'un module, composant ou contrôleur).
- Allègement didactique de codes sources denses pour respecter le principe de charge cognitive minimale.
- Intégration de l'éditeur interactif Jekyll via les propriétés `data_code_depart` et `data_code_solution`.

---

## 3. Prompts Types pour Invoquer le Skill
- *« Rédige la série de tutoriels de code pour implémenter la vue de détail des articles à partir du code final cible. »*
- *« Rédige le tutoriel de code T.XXX.112 pour la configuration des routes du projet sur la branche active. »*
- *« Écris un tutoriel unitaire d'implémentation d'un composant de formulaire avec validation. »*

---

## 4. Précision Didactique
Ce skill n'est activé que pour l'écriture de code pur incrémental. Pour les ateliers guidés (concepts, modélisation, IA), utiliser `tutorial-lab-writer`. Pour les cérémonies agiles et le cadrage opérationnel, utiliser `tutorial-task-writer`.
