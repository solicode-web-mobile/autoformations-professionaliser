# Mission : Génération de l'Artéfact Interactif de Révision (`generer-artefact-revision.md`)

## 1. Objectif
Rédiger un artéfact interactif standardisé (`plan-revision-[cible].md`) permettant au concepteur de relire le document révisé **tel quel**, de commenter et de valider (via le bouton *Proceed*) l'ensemble des ajustements sans pollution d'annotations de lignes, ainsi que la matrice des skills à adapter.

---

## 2. Structure Obligatoire de l'Artéfact

L'artéfact interactif doit comporter obligatoirement :
- **Métadonnées de l'artéfact :**
  - `UserFacing: true`
  - `RequestFeedback: true`
  - `Summary`: Résumé clair des modifications proposées et des skills impactés.
- **Section 1 : User Review Required (Arbitrages et Points Validés)** :
  - Mettre en évidence les décisions de conception, choix d'architecture ou évolutions pédagogiques arbitrées avec le concepteur.
- **Section 2 : Document Révisé Intégral (Affiché tel quel)** :
  - Restituer l'intégralité du document cible avec les ajustements intégrés.
  - **Interdiction formelle des mentions de numéros de lignes** (ex : ne jamais écrire "Lignes 1 à 7", "Lignes 28 à 41", etc.). Le document doit être propre, lisible et utilisable directement.
- **Section 3 : Matrice des Skills Impactés** :
  - Pour chaque skill concerné, préciser le fichier cible (`SKILL.md` ou `missions/<mission>.md`) et la nature de la mise à jour à apporter.
- **Section 4 : Plan d'Exécution et Vérification** :
  - Découpage séquentiel des opérations de modification et tests automatisés.

---

## 3. Règles de Formatage
- **Affichage 'tel quel' du document :** Le texte doit être restitué sous sa forme finale sans balises parasites de repérage de lignes.
- **Zéro tableau Markdown (`| ... |` interdit) :** Structurer exclusivement sous forme de listes à puces directes (`- `).
- **Zéro code numérique `UA.*` :** Désignations descriptives et sémantiques.
- Liens relatifs vers les fichiers modifiés.
