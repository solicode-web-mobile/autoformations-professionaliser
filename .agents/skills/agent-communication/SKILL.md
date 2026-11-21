---
name: agent-communication
description: Pilote la communication formelle inter-agents (redacteur-autoformation et realisation-sprint) via des canaux physiques d'échange symlinkés et des templates standardisés.
version: 1.0.0
---

# 1. Mission
Ce skill gouverne et formalise la communication inter-agents entre l'**Agent Rédacteur d'Autoformation** (`redacteur-autoformation`) et l'**Agent Réalisation de Sprint** (`realisation-sprint`). Il standardise les canaux d'échanges, les templates de requêtes et garantit la synchronisation bidirectionnelle instantanée par lien symbolique (symlink).

# 2. Déclenchement & Limites
- **Quand l'activer :**
  - Émission d'une consigne de cadrage, d'alignement ou de découpage vers l'Agent Réalisation.
  - Demande de clarification ou d'arbitrage sur un flux opérationnel reçu.
  - Notification de livraison, promotion de statut de tutoriel ou demande d'audit de livrables.
  - Initialisation ou réparation des canaux de communication physiques et de leurs liens symboliques.
- **Quand NE PAS l'activer :**
  - Rédaction interne d'un tutoriel ou d'une UA (utiliser `tuto-writer` ou `didactique-session-planner`).
  - Échange direct en langage naturel avec l'utilisateur humain.

# 3. Architecture des Canaux & Règles Inviolables
1. **Nommage Standardisé :**
   Format obligatoire : `[agent-emetteur]-to-[agent-recepteur].md`
   Exemple canonique : `redacteur-autoformation-to-realisation-sprint.md`.
2. **Localisation Physique du Fichier :**
   - Le fichier réel réside **exclusivement dans le dépôt de l'agent émetteur** sous `.agents/communication-agents/`.
3. **Lien Symbolique (Symlink) chez le Récepteur :**
   - Le dépôt du récepteur contient un lien symbolique pointant directement vers le fichier de l'émetteur :
     ```powershell
     New-Item -ItemType SymbolicLink -Path "<recepteur>\.agents\communication-agents\<nom-canal>.md" -Target "<emetteur>\.agents\communication-agents\<nom-canal>.md" -Force
     ```
   - Toute mise à jour de l'émetteur est immédiatement accessible au récepteur sans duplication de données.
4. **Encodage Strict :** UTF-8 sans BOM sur tous les messages.
5. **Archivage Systématique :** Dès qu'un échange est `RESOLU`, il doit être archivé sous `.agents/communication-agents/archive/YYYY-MM-DD-[slug].md` avant d'émettre un nouveau message `A_TRAITER`.

# 4. Structure Normative d'un Message Inter-Agents
Tout message transmis via le canal adopte la structure suivante :
```markdown
# Communication Inter-Agents : [Objet Concret]

- **Émetteur :** `[agent-emetteur]`
- **Destinataire :** `[agent-recepteur]`
- **Date :** `YYYY-MM-DD`
- **Statut :** `A_TRAITER` | `EN_COURS` | `RESOLU`

## 1. Contexte & Déclencheur
Explication concise du besoin ou de l'événement déclencheur.

## 2. Directives ou Demandes Opérationnelles
Points précis, exigences de conformité, règles d'ingénierie ou questions d'arbitrage.

## 3. Livrables ou Réponses Attendus
Ce que l'agent destinataire doit produire ou confirmer dans son dépôt.

## 4. Accusé de Réception & Historique des Échanges
Section complétée par l'agent destinataire lors de la prise en compte.
```

# 5. Procédure Pas-à-Pas
1. **Étape 1 — Création ou Sélection du Canal :** Identifier l'émetteur et le récepteur. Vérifier la présence du fichier physique et du symlink.
2. **Étape 2 — Rédaction du Message :** Rédiger la demande en appliquant le gabarit normatif.
3. **Étape 3 — Mise à Jour du Statut :** Positionner le statut sur `A_TRAITER`.
4. **Étape 4 — Notification :** Informer l'utilisateur de la consigne transmise pour exécution par l'agent cible.
