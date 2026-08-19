> [!WARNING]
> Ce projet n'est en AUCUN CAS affilié ou maintenu de quelconque manière que ca soit, à Optymo, la Régie des Transports du Territoire de Belfort (RTTB) ou le Syndicat Mixte des Transports en Commun (SMTC90).

# Optymo' Clock

Optymo' Clock est un projet visant à réunir un maximum de pages d'horaires en temps réel fournies par Optymo
Bien évidemment, Optymo' Clock est uniquement un moyen d'accès aux pages d'horaires, qui sont faites par Optymo
Donc je ne serai responable de tout coutenu qui y apparait (même si, a part voir votre bus partir sous votre nez, y'a pas de gros risque, mais quand même...)
(Pourquoi Optymo' Clock ? C'est un jeu de mot avec Optymo et O'Clock, qui signifie une heure pile en anglais)

# Fonctionnalités
- Interface claire et soignée
- Léger
- Consomme peu de données
- Mode Sombre (qui s'adapte à celui de votre appareil)
- Aperçu des correspondances et lieux importants à proximité

## Fonctionnement

Les pages web ne contiennent aucune interactivité, elles jouent uniquement le rôle de surcouche par dessus les pages crées par Optymo.
Elles utilisent un iframe, permettant d'inclure les pages d'Optymo, et de pouvoir les personnaliser un peu, et d'ajouter des infos supplémentaires.
La page d'accueil utilise le script JavaScript fourni par Mecatran qui est affiché que la page d'Optymo, afin d'afficher les info trafic du réseau. Evidemment, je l'ai un petit peu remanié pour qu'il colle un peu plus avec l'esthétique du site.

## Pourquoi l'utiliser ?

Le site étant rudimentaire, il est utilisable sur tout les navigateurs prenant en charge la balise iframe, qui à été crée en 1997 donc il y a de très grande chances que le site fonctionne avec votre appareil. (Cependant, le CSS utilise des standards modernes (display flex) qui ne sont pas compactible avec les anciens navigateurs, l'esthetique ne sera pas présente, mais le site reste entièrement fonctionnel).\
Rudimentaire, certes, mais pour peu que vous ayez un appareil et navigateur récents, vous profiterez d'une interface soignée et ergonomique.\
Aussi, si vous avez un forfait limité (les forfait pas cher 5-10Go), l'utilisation d'Optymo' Clock vous permettera d'économiser des précieux Mo de données, alors que les application type Maps ou Transit ne lésigneront pas sur la consommation de données.

## Lignes Disponibles

**Ligne 1** Valdoie ↔ Résidences\
**Ligne 2** Ar./Bav./Cra. ↔ Justice\
**Ligne 3** Valdoie ↔ Gare TGV/Châtenois\
**Ligne 4** Offemont ↔ Pépinière/Froideval (Prochainement)\
**Ligne 5** Essert ↔ Prés d'Aumont/Eloie (Prochainement)\
**Ligne 8** Liberté ↔ Evette (Prochainement)

> [!NOTE]
> Etant donné la manière dont le site est crée, je ne peut pas implémenter la ligne 9, les lignes secondaires (20-26) et suburbaines (30-40, 90-93) de la mème manière que les lignes urbaines (les boutons redirigent vers les PDF des horaires, c'est rudimentaire mais c'est impossible de faire autrement)

# MENTIONS LEGALES

Optymo est une marque déposée par la Régie des Transports du Territoire de Belfort (RTTB) depuis 2007, tout droits réservés.
Comme dit précedemment, je ne serai tenu reponsable du contenu affiché dans les iframes fournies par la RTTB\

## Licence

Ce projet est sous licence **GNU Affero General Public License v3.0 (AGPLv3)**.
Comme dit dans le fichier [LICENSE](LICENCE.MD), ce projet vous est distribué sans la moindre garantie.

### Résumé rapide :

| 🟢 Vos permissions | 🟡 Vos devoirs | 🔴 Vos interdictions |
| --- | --- | --- |
| **Utiliser** le projet gratuitement (perso ou commercial) | **Conserver** le nom de l'auteur (Naxoméga) et la mention de licence | **Fermer le code** source en le rendant propriétaire |
| **Modifier** et adapter le code source | **Ouvrir le code** de vos modifications sous licence AGPLv3 | **Relever la responsabilité** de l'auteur en cas de bug |
| **Redistribuer** ou **héberger** l'application en ligne | **Rendre le code accessible** aux utilisateurs du site/service (lien web) |  |

> _Ce résumé est fourni à titre indicatif. En cas de doute juridique, seul le texte du fichier [LICENSE](LICENSE.MD) fait foi._