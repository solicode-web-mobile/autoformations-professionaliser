# Guide Opérationnel : Comment Utiliser le Master Skill `tutorial-writer`

## 1. Rôle et Responsabilités du Master Skill
`tutorial-writer` est le **Master Skill et chef d'orchestre** gouvernant la création, la révision et la synchronisation de l'ensemble des tutoriels du cursus Solicode.
Il fonctionne de façon **générique et indépendante du niveau**, adaptant son comportement selon les directives définies dans `.agents/rules/` (N1 Découvrir, N2 Prototyper, N3 Développer / Réaliser).

Il assure deux rôles stratégiques :
1. **Gouvernance Transversale :** Il fait respecter le socle invariable commun (encodage UTF-8 sans BOM, mise en page colonne 0, chemin canonique `tutoriels/`, journalisation CLI sans commande d'administration git, style direct A1-A2, terminal configuré dans les rules, interdiction des termes internes comme 20/80 et Jalons).
2. **Autorité Unique de Synchronisation Inter-Agents :** Il consulte obligatoirement `<projet-cible>/.sync/rules.md` pour savoir comment interagir avec l'Agent Réalisation (Agent Projet), compare les versions déclarées dans le front-matter de `_tutos/` avec celles de `.sync/.../version.yml`, synchronise le contenu réel et met à jour les statuts (`synchronise`, `a_adapter`).

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
*Action de l'Agent :* Détecte la nature de l'UA, active le sous-skill adapté (`tutorial-code-writer`, `tutorial-lab-writer` ou `tutorial-task-writer`), applique le socle commun et initialise le bloc `livrables` dans le front-matter.

### B. Synchronisation Inter-Agents selon `.sync/rules.md`
```markdown
@[.agents/skills/tutorial-writer/SKILL.md] Synchronise les tutoriels avec le projet cible selon .sync/rules.md.
```
*Action de l'Agent :*
1. Lit `<projet-cible>/.sync/rules.md`.
2. Parcourt `.sync/` pour extraire les versions actuelles (`version.yml`).
3. Compare avec le front-matter des tutoriels sources dans `_tutos/`.
4. Si la version `.sync/` > version front-matter, actualise le contenu, met à jour la version et passe le statut à `synchronise`.
5. Si un livrable est incomplet ou défaillant, passe le statut à `a_adapter`.

### C. Audit de Traçabilité des Livrables
```markdown
@[.agents/skills/tutorial-writer/SKILL.md] Audite l'état de synchronisation du tutoriel _tutos/D.351.1.scrum/UA.351.11/T.351.111/comprendre-scrum.md avec .sync/.
```

---

## 4. Format du Front-Matter pour la Traçabilité
Le Master Skill s'assure que chaque tutoriel source dans `_tutos/` comporte le bloc standardisé :

```yaml
sprint: "sprint1"
statut_realisation: "realise" # ou "synchronise", "a_adapter"
livrables:
  - chemin: "tutoriels/scrum/initiation-scrum/comprendre-scrum/comprendre-scrum.md"
    version: "1.0.0"
  - chemin: "tutoriels/scrum/initiation-scrum/comprendre-scrum/presentation-comprendre-scrum.md"
    version: "1.0.0"
```
