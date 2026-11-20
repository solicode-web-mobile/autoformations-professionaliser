# Guide Opérationnel : Comment Utiliser le Master Skill `tutorial-writer`

## 1. Rôle et Responsabilités du Master Skill
`tutorial-writer` est le **Master Skill et chef d'orchestre** gouvernant la création, la révision et la synchronisation de l'ensemble des tutoriels du cursus Solicode (Niveau N3).

Il est l'unique détenteur de deux rôles stratégiques :
1. **Gouvernance Transversale :** Il impose les règles inviolables communes (encodage UTF-8 sans BOM, mise en page colonne 0, arborescence `tutoriels/`, journalisation CLI sans commande git, français A1-A2, terminal PowerShell Windows, interdiction des termes internes comme 20/80 et Jalons).
2. **Autorité Unique de Synchronisation :** Il inspecte le dépôt réel physique du projet d'imitation (`D:\labs-web\projet-imiation-n3` ou `E:\labs-web\projet-imiation-n3`) et synchronise en miroir les fiches de tutoriels et les livrables physiques correspondants.

---

## 2. Architecture de l'Écosystème `tutorial-*-writer`
`tutorial-writer` aiguille automatiquement chaque besoin didactique vers le sous-skill spécialisé :

| Type d'Apprentissage | Maturité Cible | Rédacteur Spécialisé Délégué |
| :--- | :--- | :--- |
| **Code Incrémental Pas-à-Pas** | `UA-Tuto` ($E_{n-1} \to E_n$) | **[tutorial-code-writer](../tutorial-code-writer/SKILL.md)** |
| **Atelier Pratique Guidé** | `UA-Lab` (20/80, Modélisation, Prompts IA) | **[tutorial-lab-writer](../tutorial-lab-writer/SKILL.md)** |
| **Tâche de Projet / Cérémonie Agile** | `UA-Tâche` (Cadrage, Sprint Review, 0% Théorie) | **[tutorial-task-writer](../tutorial-task-writer/SKILL.md)** |

---

## 3. Prompts Types pour Invoquer le Master Skill

### A. Demande de Rédaction de Tutoriel (Routage Automatique)
```markdown
@[.agents/skills/tutorial-writer/SKILL.md] Rédige le tutoriel T.321.112 de l'UA.321.11 planifié dans le domaine Laravel sur la branche sprint1.
```
*Action de l'Agent :* Détecte la nature de l'UA, active le sous-skill adapté (`tutorial-code-writer`, `tutorial-lab-writer` ou `tutorial-task-writer`), applique le socle commun et synchronise ensuite avec `D:\labs-web\projet-imiation-n3`.

### B. Synchronisation entre le Site et le Projet d'Imitation
```markdown
@[.agents/skills/tutorial-writer/SKILL.md] Synchronise les fiches de tutoriels du sprint 1 avec les livrables physiques du projet d'imitation sous D:\labs-web\projet-imiation-n3.
```
*Action de l'Agent :* Inspecte `D:\labs-web\projet-imiation-n3\tutoriels\`, vérifie la cohérence des noms et livrables, génère ou adapte les documents miroirs.

### C. Audit de Conformité Pédagogique
```markdown
@[.agents/skills/tutorial-writer/SKILL.md] Audite la fiche _tutos/D.311.2.uml/UA.311.21/T.311.211/diagramme-classes.md et vérifie le respect des règles transversales.
```

---

## 4. Procédure de Synchronisation Déterministe
1. Vérification de la présence de `D:\labs-web\projet-imiation-n3` (ou `E:\labs-web\projet-imiation-n3`).
2. Vérification de la branche courante Git (ex: `sprint1`).
3. Vérification de l'arborescence `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/`.
4. Mise à jour miroir des fichiers :
   - `[slug-tuto].md` (fiche technique).
   - `presentation-[slug-tuto].md` (support Marp).
   - `[slug-tuto].command.md` (journal CLI).
