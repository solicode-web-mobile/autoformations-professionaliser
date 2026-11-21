# Mission : Synchronisation Document et Skills (`synchroniser-skills.md`)

## 1. Objectif
Appliquer de manière synchrone et atomique les modifications validées par le concepteur sur le document cible (ex: fichier de session) et propager les évolutions méthodologiques sur les skills et règles impactés.

---

## 2. Démarche d'Exécution Post-Validation

1. **Mise à jour du document cible :**
   - Appliquer les modifications validées sur les lignes cibles du document source (ex: `flux-travail-s0.md`).
   - Conserver les conventions strictes : noms génériques exacts des étapes, un seul livrable principal par étape, typologie `UA-Lab` vs `UA-Tâche`.

2. **Mise à jour des skills impactés :**
   - Modifier les fichiers `SKILL.md` ou les missions des skills répertoriés dans la matrice de l'artéfact.
   - S'assurer que chaque `SKILL.md` modifié conserve sa taille compacte canonique ($\le 75$ lignes).

3. **Mise à jour des règles si nécessaire :**
   - Reporter toute nouvelle règle permanente dans `.agents/rules/`.

4. **Contrôle Qualité Automatisé :**
   - Exécuter la vérification de conformité :
     - 0 tableau Markdown (`^\s*\|`).
     - 0 code numérique `UA.*`.
     - 0 terme obsolète : MySQL et Laravel 13 obligatoires.
     - Statut Git sans commit ni push automatique.
