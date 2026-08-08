import re

# Liste des balises HTML autorisées dans ce problème
BALISES_AUTORISEES = {"b", "i", "em", "div", "p"}

# Expression régulière qui capture une balise HTML :
#   groupe 1 : le "/" optionnel (présent si c'est une balise fermante)
#   groupe 2 : le nom de la balise (b, i, em, div, p)
# Exemple : "<div>"  -> ("", "div")
#           "</div>" -> ("/", "div")
PATTERN_BALISE = re.compile(r"<(/?)(\w+)>")


def checkDOmm(strParam: str) -> str:
    """
    Analyse une chaîne 'strParam' contenant du texte et des balises HTML
    (b, i, em, div, p) et détermine si l'imbrication des balises est :

      1. Correcte                                  -> renvoie "true"
      2. Presque correcte (un seul nom à changer)   -> renvoie le nom de
                                                        la première balise
                                                        à corriger
      3. Incorrecte (il faudrait changer plus
         d'une balise, ou ajouter/enlever une
         balise)                                    -> renvoie "false"
    """

    # --------------------------------------------------------------
    # ÉTAPE 1 : Extraire toutes les balises de la chaîne
    # --------------------------------------------------------------
    # On parcourt strParam avec finditer pour récupérer, pour CHAQUE
    # balise trouvée :
    #   - sa position de départ dans la chaîne (pour savoir laquelle
    #     apparaît "en premier" plus tard)
    #   - si elle est ouvrante ou fermante
    #   - son nom (div, b, i, em, p)
    #
    # Le texte brut (hello, world, etc.) est simplement ignoré : il
    # n'a aucune influence sur la structure d'imbrication.
    balises = []
    for match in PATTERN_BALISE.finditer(strParam):
        est_fermante = (match.group(1) == "/")
        nom = match.group(2)
        position = match.start()
        balises.append({
            "position": position,
            "fermante": est_fermante,
            "nom": nom,
        })

    # --------------------------------------------------------------
    # ÉTAPE 2 : Vérifier la STRUCTURE (imbrication) avec une pile
    # --------------------------------------------------------------
    # On ignore volontairement les NOMS des balises à cette étape :
    # on veut juste savoir si la forme générale (ouverture/fermeture)
    # est cohérente, indépendamment de quel nom est utilisé.
    #
    # Principe de la pile :
    #   - balise ouvrante  -> on l'empile
    #   - balise fermante  -> elle doit "fermer" la dernière balise
    #                         ouverte (sommet de la pile) ; on dépile
    #                         et on enregistre la PAIRE (ouvrante, fermante)
    #
    # Si on essaie de fermer alors que la pile est vide, ou s'il reste
    # des balises ouvertes non fermées à la fin du parcours, cela
    # signifie qu'il manque une balise ou qu'il y en a une de trop.
    # Ce genre de problème ne peut PAS être réparé en changeant
    # seulement le NOM d'une balise -> on retourne directement "false".
    pile = []
    paires = []  # liste de tuples (balise_ouvrante, balise_fermante)

    for balise in balises:
        if not balise["fermante"]:
            # Balise ouvrante : on l'empile
            pile.append(balise)
        else:
            # Balise fermante : elle doit correspondre au sommet de la pile
            if not pile:
                # Fermeture "orpheline" : aucune balise ouverte à fermer
                # -> structure cassée, pas réparable avec un seul changement
                return "false"
            ouvrante = pile.pop()
            paires.append((ouvrante, balise))

    if pile:
        # Il reste des balises ouvertes jamais fermées
        # -> structure cassée, pas réparable avec un seul changement
        return "false"

    # --------------------------------------------------------------
    # ÉTAPE 3 : Vérifier les NOMS des balises dans chaque paire
    # --------------------------------------------------------------
    # Maintenant que la structure (l'imbrication) est valide, on
    # regarde si le nom de chaque balise ouvrante correspond bien au
    # nom de sa balise fermante associée.
    #
    # On collecte toutes les paires où les noms NE correspondent PAS.
    paires_incorrectes = [
        (ouvrante, fermante)
        for (ouvrante, fermante) in paires
        if ouvrante["nom"] != fermante["nom"]
    ]

    # Cas 1 : aucune incohérence de nom -> tout est parfaitement correct
    if len(paires_incorrectes) == 0:
        return "true"

    # Cas 3 : deux incohérences ou plus -> impossible de réparer en
    # changeant une seule balise -> "false"
    if len(paires_incorrectes) > 1:
        return "false"

    # Cas 2 : exactement une incohérence -> on peut tout réparer en
    # changeant le nom d'une seule balise (soit l'ouvrante, soit la
    # fermante de cette paire). On doit renvoyer le nom de celle qui
    # apparaît EN PREMIER dans la chaîne d'origine.
    ouvrante, fermante = paires_incorrectes[0]
    premiere_balise = min(ouvrante, fermante, key=lambda b: b["position"])
    return premiere_balise["nom"]


# --------------------------------------------------------------
# Programme principal : lit l'entrée utilisateur et affiche le résultat
# --------------------------------------------------------------
if __name__ == "__main__":
    print(checkDOmm(input()))