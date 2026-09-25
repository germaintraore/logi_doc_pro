# Frontend React — logi_doc_pro

Ce dossier contient le frontend React/Vite du projet. Il est actuellement au stade de scaffold : l'interface affichée est un statut statique et ne constitue pas encore une application métier.

## Prérequis

- Node.js compatible avec Vite 8, par exemple `^20.19.0` ou `>=22.12.0`.
- npm.

## Commandes

Depuis `frontend/` :

```powershell
npm install
npm run dev
npm run lint
npm run build
npm run preview
```

- `npm run dev` démarre le serveur Vite avec rechargement à chaud.
- `npm run lint` exécute ESLint sur le projet.
- `npm run build` produit le bundle de production dans `dist/`.
- `npm run preview` sert localement le bundle construit.

## État actuel

- React 19, Vite 8 et Tailwind CSS 3 sont configurés.
- `src/App.jsx` ne contient pas encore de Router ni de client API.
- Les appels API devront être centralisés dans `src/services/`, conformément à `frontend/AGENTS.md`.
- Aucun test frontend n'est configuré.
- `src/index.css` contient actuellement une erreur de syntaxe ; le build doit être considéré en échec jusqu'à correction.
- Les assets et styles issus du template Vite doivent être nettoyés au fur et à mesure.

## Structure prévue

```text
src/
├── components/   composants d'affichage réutilisables
├── hooks/        logique React et règles d'état
├── pages/        Login, Dashboard, catalogue, éditeur
├── services/     appels API centralisés
└── styles/       styles globaux et composants
```

Cette structure est une cible d'organisation ; elle ne doit pas créer des répertoires vides avant d'avoir une responsabilité claire.

## Prochaines étapes

1. Corriger `src/index.css` et valider `npm run build`.
2. Définir la stratégie de stockage et de renouvellement des JWT.
3. Ajouter un client API avec gestion des erreurs.
4. Ajouter Router, pages Login/Dashboard et guards d'accès.
5. Ajouter une stratégie de tests frontend avant les parcours métier.
