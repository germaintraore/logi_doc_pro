# COMMANDS_USE.md — Registre Pédagogique des Commandes

Ce document recense toutes les commandes fournies et exécutées dans le projet, accompagnées de leurs explications détaillées pour garantir la maîtrise totale de l'environnement par le développeur.

---

## 1. Nettoyage de l'arborescence

### Commande :
```powershell
Remove-Item -Recurse -Force "-p"
```
- **Justification** : Suppression du dossier vide nommé `-p`, créé accidentellement lors d'une commande `mkdir -p` (syntaxe Bash non compatible par défaut avec CMD Windows).
- **Ce que fait la commande** :
  - `Remove-Item` : Commande PowerShell équivalente à `rm` ou `del` pour supprimer des éléments.
  - `-Recurse` : Supprime récursivement le dossier et tout ce qu'il contient (si applicable).
  - `-Force` : Force la suppression sans demander de confirmation.

---

## 2. Initialisation et Configuration de Git

### Commande 1 :
```powershell
git init
```
- **Justification** : Transformer le dossier local `logi_doc_pro` en un dépôt Git versionné.
- **Ce que fait la commande** : Crée un sous-dossier caché `.git/` qui contiendra l'historique complet des commits, branches et métadonnées du projet.

---

### Commande 2 :
```powershell
git branch -M main
```
- **Justification** : Standardiser le nom de la branche principale sur `main` (la norme actuelle de GitHub et de l'industrie, remplaçant l'ancien nom par défaut `master`).
- **Ce que fait la commande** : Renomme la branche courante en `main`.

---

### Commande 3 :
```powershell
git add .
```
- **Justification** : Placer tous les fichiers du projet (les fichiers `.md` de cadrage et le `.gitignore`) dans la zone de transit (*staging area*).
- **Ce que fait la commande** :
  - `add` : Prépare les fichiers pour le prochain commit.
  - `.` : Désigne l'intégralité du répertoire courant, tout en respectant les exclusions définies dans `.gitignore`.

---

### Commande 4 :
```powershell
git commit -m "docs: cadrage architectural et initialisation du projet"
```
- **Justification** : Créer le tout premier point de sauvegarde (*commit initial*) dans l'historique Git.
- **Ce que fait la commande** :
  - `commit` : Enregistre de manière immuable l'état actuel des fichiers indexés.
  - `-m "..."` : Attache un message clair et descriptif expliquant l'objet de ce commit (convention Conventional Commits `docs:`).

---

### Commande 5 :
```powershell
git remote add origin <URL_DE_TON_DEPOT_GITHUB>
```
- **Justification** : Associer votre dépôt local sur votre machine au dépôt distant hébergé sur GitHub.
- **Ce que fait la commande** :
  - `remote add` : Déclare une nouvelle adresse de serveur distant.
  - `origin` : Nom conventionnel donné au dépôt distant principal.
  - `<URL_DE_TON_DEPOT_GITHUB>` : Adresse HTTPS ou SSH de votre dépôt créé sur GitHub (ex: `https://github.com/votre-nom/logi_doc_pro.git`).

---

### Commande 6 :
```powershell
git push -u origin main
```
- **Justification** : Envoyer vos fichiers et votre historique local vers GitHub.
- **Ce que fait la commande** :
  - `push` : Téléverse les commits locaux vers le dépôt distant.
  - `-u` (ou `--set-upstream`) : Associe durablement la branche locale `main` à la branche distante `origin/main`. Pour les futurs envois, un simple `git push` suffira.
  - `origin main` : Cible la branche `main` du serveur distant `origin`.
