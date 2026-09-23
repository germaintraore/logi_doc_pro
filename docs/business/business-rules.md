# Règles Métier — Gestion des Modèles et Documents

Ce document formalise les règles de gestion et le cycle de vie des Modèles (`Templates`) et des Documents dans `logi_doc_pro`.

---

## 1. Cycle de Vie d'un Modèle (`Template`)

Un modèle suit une machine à états stricte :

```text
[ DRAFT ] ──(Soumission par l'utilisateur)──> [ PENDING_REVIEW ]
                                                    │
                   ┌────────────────────────────────┴──────────────────┐
                   ▼                                                   ▼
       [ UNDER_REVIEW / MODIFIED ]                             [ REJECTED ]
                   │                                         (Avec motif de refus)
        (Validation finale par Admin)
                   │
                   ▼
             [ PUBLISHED ]
                   │
                   ▼
             [ ARCHIVED ] (Déprécié par Admin)
```

### Règles d'or :
1. **[BR-TMP-01] Confidentialité des brouillons** : Un modèle avec le statut `DRAFT` n'est visible que par son créateur.
2. **[BR-TMP-02] Gel lors de la soumission** : Dès qu'un utilisateur soumet un modèle (`PENDING_REVIEW`), il ne peut plus le modifier sans annuler la soumission, garantissant l'intégrité de ce que l'administrateur examine.
3. **[BR-TMP-03] Droit de retouche de l'administrateur** : L'administrateur a le droit légitime d'adapter l'orthographe, les variables de blocs, ou la structure d'un modèle soumis pour en garantir le standard de qualité avant publication.
4. **[BR-TMP-04] Attribution & Paternité** : Même si l'administrateur retouche et publie le modèle, le champ `created_by` conserve la référence à l'utilisateur d'origine pour valoriser sa contribution communautaire.
5. **[BR-TMP-05] Immuabilité des documents existants** : Si un modèle publié est modifié ou archivé ultérieurement, les documents utilisateurs déjà générés à partir de ce modèle ne sont pas altérés (principe d'instanciation indépendante en JSONB).

---

## 2. Structure d'un Modèle et Blocs de Contenu

1. **[BR-DOC-01] Format JSONB** : La structure d'un document ou d'un modèle est stockée au format JSONB sous PostgreSQL.
2. **[BR-DOC-02] Typologie des blocs** :
   - Bloc Titre / En-tête
   - Bloc Paragraphe / Markdown enrichi
   - Bloc Liste / Puces
   - Bloc Tableau structuré
   - Bloc Méta-données (ex: Coordonnées CV, Références académiques)
3. **[BR-DOC-03] Assistance IA contextuelle** : L'IA intervient au niveau du bloc sélectionné (reformulation, correction de style, génération de contenu selon prompt guidé).
