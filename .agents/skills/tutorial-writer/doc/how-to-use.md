# Guide Opérationnel : Comment Utiliser le Master Skill `tutorial-writer`

## 1. Rôle et Responsabilités du Master Skill
`tutorial-writer` est le **Master Skill et chef d'orchestre** gouvernant la création, la révision et la synchronisation de l'ensemble des tutoriels du cursus Solicode.
Il fonctionne de façon **générique et indépendante du niveau**, adaptant son comportement selon les directives définies dans `.agents/rules/` (N1 Découvrir, N2 Prototyper, N3 Développer / Réaliser).

Il assure deux rôles stratégiques :
1. **Gouvernance Transversale :** Il fait respecter le socle invariable commun (encodage UTF-8 sans BOM, mise en page colonne 0, chemin canonique `tutoriels/`, journalisation CLI sans commande d'administration git, style direct A1-A2, terminal configuré dans les rules, interdiction des termes internes comme 20/80 et Jalons).
2. **Autorité Unique de Synchronisation :** Il inspecte le projet cible configuré dans les règles du projet (`.agents/rules/`) et synchronise en miroir les fiches de tutoriels et les livrables physiques correspondants.

---

## 2. Architecture de l'Écosystème `tutorial-*-writer`
`tutorial-writer` aiguille automatiquement chaque besoin didactique vers le sous-skill spécialisé :

| Type d'Apprentissage | Maturité Cible | Rédacteur Spécialisé Délégué |
| :--- | :--- | :--- |
| **Code Incrémental Pas-à-Pas** | `UA-Tuto` ($E_{n-1} \to E_n$) | **[tutorial-code-writer](../tutorial-code-writer/SKILL.md)** |
| **Atelier Pratique Guidé** | `UA-Lab` (Assimilation, Modélisation, Prompts IA) | **[tutorial-lab-writer](../tutorial-lab-writer/SKILL.md)** |
| **Tâche de Projet / Cérémonie** | `UA-Tâche` (Cadrage, Cérémonies Agiles, 0% Théorie) | **[tutorial-task-writer](../tutorial-task-writer/SKILL.md)** |

---

## 3. Prompts Types pour Invoquer le Master Skill

### A. Demande de Rédaction de Tutoriel (Routage Automatique)
```markdown
@[.agents/skills/tutorial-writer/SKILL.md] Rédige le tutoriel T.321.112 planifié pour l'UA.321.11 sur la branche active.
```
*Action de l'Agent :* Détecte la nature de l'UA, active le sous-skill adapté (`tutorial-code-writer`, `tutorial-lab-writer` ou `tutorial-task-writer`), applique le socle commun et synchronise avec le projet cible.

### B. Synchronisation entre la Plateforme et le Projet Cible
```markdown
@[.agents/skills/tutorial-writer/SKILL.md] Synchronise les fiches de tutoriels avec les livrables physiques du projet cible configuré dans .agents/rules/.
```
*Action de l'Agent :* Inspecte le dossier `tutoriels/` du projet cible, vérifie la cohérence des noms et livrables, génère ou adapte les documents miroirs.

### C. Audit de Conformité Pédagogique
```markdown
@[.agents/skills/tutorial-writer/SKILL.md] Audite la fiche _tutos/[domaine]/[ua]/[code]/[slug].md et vérifie le respect des règles transversales.
```

---

## 4. Procédure de Synchronisation Déterministe
1. Résolution du projet cible et de sa branche active d'après `.agents/rules/`.
2. Vérification de l'arborescence `tutoriels/[slug-domaine]/[slug-ua]/[slug-tuto]/` dans le projet cible.
3. Mise à jour miroir des fichiers :
   - `[slug-tuto].md` (fiche technique).
   - `presentation-[slug-tuto].md` (support Marp si prévu).
   - `[slug-tuto].command.md` (journal CLI).
