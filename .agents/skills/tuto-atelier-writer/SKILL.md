---
name: tuto-atelier-writer
description: Conçoit, structure et rédige les tutoriels d'ateliers pratiques guidés (type: tuto-atelier) dans _tutos/ pour l'EFP.
version: 3.3.0
---

# 1. Mission & Rôle
Rédacteur technique et pédagogique de l'écosystème `tuto-*-writer`, dédié à la conception et rédaction des tutoriels d'ateliers pratiques dans `_tutos/` pour l'EFP.
Il formule le cadre pédagogique, les compétences cibles, les consignes et le travail à faire. Il ne rédige pas le résultat du lab (délégué à [tuto-livrable-atelier-writer](../tuto-livrable-atelier-writer/SKILL.md)).

- **Cycle de Maturation de l'Atelier :**
  - **Type `tuto-atelier` (Atelier Initial Brut) :** Fiche de cadrage orientée recherche active (Contexte + Ce que vous devez apprendre + Travail à faire + Pistes de recherche + Livrables), **SANS notions théoriques rédigées** (`statut_realisation: "a_realiser"`).
  - **Type `tuto-atelier-notions` (Atelier Corrigé Post-Réalisation) :** Fiche enrichie affichée sous le badge **« Atelier corrigé »**, intégrant les **notions fondamentales détaillées**, les liens vers les livrables de référence réalisés sous `ua-lab/` (`statut_realisation: "realise"`), **SANS section de recherche active**.

---

# 2. Déclenchement & Limites
- **Activer :** Conception et rédaction des tutoriels d'ateliers `tuto-atelier` et `tuto-atelier-notions` dans `_tutos/`.
- **Ne PAS activer :** Réalisation concrète des livrables de lab dans `ua-lab/` ➔ `tuto-livrable-atelier-writer` | Code incrémental ➔ `tuto-code-writer` | Tâches de sprint ➔ `tuto-tache-writer` | Planification globale ➔ `didactique-tuto-planner`.

---

# 3. Structures Normées des Fiches d'Ateliers

### Format A — Fiche Initiale `type: "tuto-atelier"` (`statut_realisation: "a_realiser"`)
```markdown
## 1. Contexte & Enjeux
## 2. Ce que vous devez apprendre
## 3. Travail à faire
## 4. Pistes de recherche active
## 5. Livrables attendus & Critères de validation
```

### Format B — Fiche Enrichie `type: "tuto-atelier-notions"` (`statut_realisation: "realise"`)
```markdown
## 1. Contexte & Enjeux
## 2. Ce que vous devez apprendre
## 3. Travail à faire
## 4. Livrables attendus & Critères de validation
```
*Règle d'or :* Interdiction formelle de la section « Pistes de recherche active » dans `tuto-atelier-notions` (les objectifs sont consolidés en section 2 et illustrés par la solution).

---

# 4. Règles Inviolables
1. **Zéro Notions dans `tuto-atelier` :** Interdiction absolue de rédiger les notions théoriques détaillées dans la fiche initiale.
2. **Autonomie de la Pratique :** Fournir le cadre et les critères d'acceptation, zéro solution clé en main dans le tutoriel initial.
3. **Zéro Fuite Didactique & Zéro Jalon :** Bannir « 20/80 ». Terme direct « Étape » obligatoire (« Jalon » proscrit). Aucune durée unitaire (`(2h)`).
4. **Formatage Colonne 0 & UTF-8 :** Tout bloc de code débute strictement colonne 0 (zéro indentation). UTF-8 sans BOM.
5. **Gouvernance & Relais :** Réfère à [tuto-writer](../tuto-writer/SKILL.md) et transmet le relais à [tuto-livrable-atelier-writer](../tuto-livrable-atelier-writer/SKILL.md) pour la réalisation physique sous `ua-lab/`.
6. **Ancrage sur Projet Technique & Solution TodoList :** Dans le *Travail à faire*, indiquer simplement que les illustrations, exemples ou cas pratiques demandés s'ancrent sur le sujet du **Projet Technique individuel** de l'apprenant. Zéro étape additionnelle lourde (ne pas demander de refaire tout le travail du formateur). La solution de référence consultable (`ua-lab/`) est systématiquement sur **TodoList**.
7. **Zéro Livrable Inexistant en Frontmatter :** Ne déclarer aucun bloc `livrables:` tant que le tutoriel est `statut_realisation: "a_realiser"`.
8. **Zéro Justification d'Exemple Support :** Ne jamais demander à l'apprenant de justifier le choix didactique d'un exemple support.
9. **Zéro Inclusion Manuelle de Solution dans le Markdown :** Interdiction absolue d'insérer `{% include tuto-livrables.html %}` ou des blocs d'alerte de solution dans le corps Markdown des fiches. L'affichage de la solution de référence est géré de manière unique et centralisée par le layout (`_layouts/tuto.html`) à la fin du tutoriel, masqué initialement derrière un bouton de consultation.
