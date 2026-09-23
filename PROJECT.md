# PROJECT.md — Vision du Produit

## Nom du projet
`logi_doc_pro`

## Vision
Une application web moderne, épurée et ultra-rapide pour concevoir, personnaliser et générer des documents professionnels structurés (CVs, Cahiers des charges, Rapports de stage, Document de recherche , exposé des étudiant et élèves,Raports d'activité).

## Différenciateurs clés
1. **Plus simple que Word** : Pas de mise en page manuelle chaotique ; tout repose sur des blocs structurés.
2. **Plus focalisé que Canva** : Priorité au contenu rédigé et à la conformité professionnelle plutôt qu'au design graphique pur.
3. **Assistance IA intégrée** : L'IA aide à formuler, corriger, résumer et structurer les sections du document instantanément.

4. **Modèle Collaboratif & Modération** :
   - **Administrateurs** : Créent et publient les modèles officiels. Ils examinent, ajustent et valident les propositions de modèles soumises par les utilisateurs avant publication globale.
   - **Utilisateurs** : Utilisent et personnalisent les modèles disponibles pour leurs propres documents, et peuvent soumettre de nouveaux modèles à l'administrateur.


## Stack Technique
- **Frontend** : React.js (SPA, Tailwind CSS pour le design moderne).
- **Backend** : Django + Django REST Framework (DRF).
- **Base de données** : PostgreSQL.
- **Moteur IA** : Intégration d'API LLM (OpenAI/Anthropic) gérée côté Backend.