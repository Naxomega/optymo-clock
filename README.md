# Optymo' Clock (Work In Progress)
Optymo' Clock est un projet visant à réunir un maximum de pages d'horaires en temps réel fournies par Optymo\
Bien évidemment, Optymo' Clock est uniquement un moyen d'accès aux pages d'horaires, qui sont faites par Optymo\
Donc je ne serai responable de tout coutenu qui y apparait (même si, a part voir votre bus partir sous votre nez, y'a pas de gros risque, mais quand même...)\
Optymo' Clock est EN AUCUN CAS afflié à Optymo.\
(Pourquoi Optymo' Clock ? C'est un jeu de mot avec Optymo et O' Clock, qui signifie une heure pile en anglais)


# NEWS
(4 Mai 2025) Wouah ca fait longtemps que je ne suis pas passé par ici, mais j'ai plein de nouvelles idées afin de rendre ce site encore meilleur ! Cepandant, j'année prochaine, je vais (je l'espère) partir dans une autre ville pour mes études, ce qui me contraindra de stopper le projet. (Cependant je vais voir, une fois installé dans la ville de mon choix, si il est possible et utile de faire un site comme celui-là) En attendant, je vais essayer de l'améliorer en utilisant des connaisances toutes fraîches (PHP notamment) et avec de nouvelles idées que voici : 
- Une page par arrêt : c'est la que PHP me sera utile, car grâce à lui je n'aurais pas besoin de faire une page par arrêt mais une seule page contenant tout les arrêts (même si, je vais tester lequel est le plus pratique pour moi)
- Informations supplémentaires : dans ces nouvelles pages, je compte inclure un iframe (une sorte de fenêtre) vers le site d'Optymo, et donner des informations supplémentaires sur la page (de mon côté) tel que : les correspondances (y compris les correspondances indirectes comme les arrêts Fg de Lyon et Dubail, qui sont à coté mais en aucun cas réferencés en tant que corrrespondances du côté d'Optymo), les lieux notables à proximité (par exemple le lycée Follerau aux arrêts Liberté Madrid et Follerau, la gare aux arrêts Gare (hé oui vous ne l'avez pas vue venir celle la :D ) etc...)\

(20 Juin 25) Chose promise, chose dûe, a l'heure actuelle, les deux pages de la ligne 1 sont fonctionelles, mais j'ai rencontré un problême : je n'ai pas réussi à trouver l'identifiant de certains arrêts,  mais cela n'empêche pas leur apparition sur le site, car j'ai utilisé l'iframe qui est intégré sur la carte "en temps réelle" d'Optymo, mais le problême, c'est que les bus des 2 sens apparaissent, c'est pas trop dérangeant selon moi, mais j'aimerais quand même avoir les vrais liens d'arrêts. Aussi, j'ai trouvé des arrêts qui n'existent juste pas (même sur la carte en temps réelle, les  iframes donnent une page d'erreur). J'ai répertorié tout ca dans un fichier Word qui est dans Optymo-Clock\Autres\Arrets.docx, tout ce qui est surligné en jaune est un arrêt oû il me manque son lien, ou un arrêt qui n'existe pas. \
J'ai aussi ajouté une page Contribuer et une page à propos.\
(18 Juin 25) Bon, je dois avouer que j'ai pas trop touché à ce projet depuis un bout de temps, mais je vous promet que je vais continuer le développement d'ici une à deux semaines\
(12 Mai 25) C'est bon, toutes les pages de toutes les lignes ont été crées (1, 2, 3, 4, 5 et 8), donc je vais pouvoir attaquer les pages des directions (1 -> Résidences, 1 -> Valdoie...) et y inclure les arrêts.\
Voici ma roadmap pour le restant de ce qu'il y a à faire : Pages dédiés aux Lignes (Ordre : 1, 2, 5, 3, 4), Page tous arrêts ainsi que les sous divisions par lignes, la page contribuer et la ligne 8 (Je la fais passer dernière car je n'ai pas l'impression que beaucoup de gens l'utilisent, mais je me trompe peut être...)\
(7 Mai 25) J'ai ajouté des pages pour les lignes 1 et 2, ainsi que leur liens et thèmes respectifs, en l'état, leur liens mènent à une page vide,
mais je souhaite faire les pages des lignes pour toutes les lignes et ensuite afficher les différents arrêts.\
(5 Mai 25) En l'état, le site n'est pas encore crée, seule la repo l'est, mais je m'y metterais quand je pourrais
J'ai une assez pauvre bibliothèque de liens d'arrêts, certains viennent de QR Codes que j'ai scannés moi-même
Et d'autres sont ceux que j'ai réussi à "Déduire" (Sur certains liens d'arrêts, ce qui caractérise une page d'une autre est "l'identifiant" de l'arrêt,
et on peut déduire l'ID de certains arrêts en mettant comme ID les 3 premières lettres de l'arrêt (L'ID de l'arrêt Gare c'est "Gar"), suivi d'un numéro
qui correspond au sens des bus qui y circulent (Par exemple, l'arrêt Gare ou passe la ligne 1, l'ID sera "Gar01" que le bus est en direction des résidences, et "Gar02"
si il va vers Valdoie, pour les arrêts ou il y a plein de bus qui y passent (comme l'arrêt Gare par exemple), les arrêts des autres bus seront dans la continuité,
"Gar03" et "Gar04" pour la ligne 2, "Gar05" et "Gar06" pour la ligne 3.
Si vous souhaitez contribuer (aux arrêts), envoyez-moi une demande sur Discord (@naxomegaenpersonne] et donnez moi le lien et je l'ajouterai à mon document
Voila, c'est tout pour cette fois-ci, bon journée/soirée !\
EDIT 1h plus tard : Le site est en ligne, non-fonctionnel mais en ligne quand même !
Si vous souhaitez contribuer côté code, faites un pull request
et je verrais si je l'approuverais ou pas...

