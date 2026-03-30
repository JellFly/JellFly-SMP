# Vote ServeurPrivé GitHub Pages

Ce projet est conçu pour fonctionner comme un site statique sur GitHub Pages.
Le frontend est dans `index.html` et utilise Firebase pour l'authentification et le stockage des votes.

## Pourquoi GitHub Pages
- GitHub Pages sert des fichiers HTML/CSS/JS statiques.
- Le site ne nécessite pas de backend Python pour être publié.
- Firebase gère l'authentification et la base de données côté client.

## Déploiement GitHub Pages
1. Crée un dépôt GitHub et pousse le contenu du dossier `vote-site`.
2. Dans les paramètres du dépôt, va dans `Pages`.
3. Choisis la branche `main` (ou `master`) et le dossier `/ (root)` comme source.
4. Enregistre. GitHub Pages publiera le site à l'URL fournie.

## Pré-requis Firebase
1. Crée un projet Firebase dans la console Firebase.
2. Active l'authentification Email/Mot de passe (`Authentication > Sign-in method`).
3. Crée une base Firestore en mode `production` ou `test` selon ton besoin.
4. Vérifie que `index.html` contient la bonne configuration `firebaseConfig`.

## Test local
Tu peux prévisualiser le site localement en utilisant un serveur statique simple.

Avec Python installé :
```powershell
python -m http.server 8000
```
Puis ouvre `http://localhost:8000` dans ton navigateur.

## Statistiques officielles ServeurPrivé
L'interface peut charger directement les statistiques publiques du serveur depuis l'API de serveur-prive.net.

## Notes
- Le site fonctionne en mode statique sur GitHub Pages.
- L'application utilise Firebase pour l'authentification et le stockage des votes.
- La liste des top voteurs n'est pas exposée publiquement par l'API serveur-prive.net.
- Remplace `SERVER_TOKEN` dans `index.html` par ton token API ServeurPrivé pour activer la vérification des votes par IP.
