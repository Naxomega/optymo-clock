import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# --- CONFIGURATION ---
URL_CIBLE = "https://www.optymo.fr/bus/horaires-et-plans/"
IMAGE_PICTO_L20 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L20.png"
IMAGE_PICTO_L21 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L21.png"
IMAGE_PICTO_L23 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L23.png"
IMAGE_PICTO_L24 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L24.png"
IMAGE_PICTO_L25 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L25.png"
IMAGE_PICTO_L26 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L26.png"
IMAGE_PICTO_L30 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L30.png"
IMAGE_PICTO_L31 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L31.png"
IMAGE_PICTO_L32 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L32.png"
IMAGE_PICTO_L33 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L33.png"
IMAGE_PICTO_L34 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L34.png"
IMAGE_PICTO_L35 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L35.png"
IMAGE_PICTO_L36 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L36.png"
IMAGE_PICTO_L37 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L37.png"
IMAGE_PICTO_L38 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L38.png"
IMAGE_PICTO_L39 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L39.png"
IMAGE_PICTO_L40 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L40.png"
IMAGE_PICTO_L90 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L90.png"
IMAGE_PICTO_L91 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L91.png"
IMAGE_PICTO_L92 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L92.png"
IMAGE_PICTO_L93 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L93.png"
IMAGE_PICTO_LX = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-LX.png"
IMAGE_PICTO_L9 = "https://www.optymo.fr/wp-content/uploads/2021/08/SMTC-Picto-L9.png"
import os

# Configuration des cibles
# Format : "numéro_ligne": ("nom_du_fichier", "classe_css_specifique")
CONFIG_LIGNES = {
    # Fichier Secondaire.html
    "20": ("Secondaire.html", "line-20"),
    "21": ("Secondaire.html", "line-21"),
    "22": ("Secondaire.html", "line-22"),
    "23": ("Secondaire.html", "line-23"),
    "24": ("Secondaire.html", "line-24"),
    "25": ("Secondaire.html", "line-25"),
    "26": ("Secondaire.html", "line-26"),
    "X":  ("Secondaire.html", "line-x"),
    
    # Fichier Suburbain.html
    "30": ("Suburbain.html", "subline-even"),
    "31": ("Suburbain.html", "subline-odd"),
    "32": ("Suburbain.html", "subline-even"),
    "33": ("Suburbain.html", "subline-odd"),
    "34": ("Suburbain.html", "subline-even"),
    "35": ("Suburbain.html", "subline-odd"),
    "36": ("Suburbain.html", "subline-even"),
    "37": ("Suburbain.html", "subline-odd"),
    "38": ("Suburbain.html", "subline-even"),
    "39": ("Suburbain.html", "subline-odd"),
    "40": ("Suburbain.html", "subline-even"),
    "90": ("Suburbain.html", "line-90"),
    "91": ("Suburbain.html", "line-91"),
    "92": ("Suburbain.html", "line-92"),
    "93": ("Suburbain.html", "line-93"),
    "9": ("index.html", "line-9"),
}

def recuperer_url_ligne_20():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L20}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L20})

        if image:
            print("✅ Picto Ligne 20 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"

def recuperer_url_ligne_21():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L21}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L21})

        if image:
            print("✅ Picto Ligne 21 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_23():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L23}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L23})

        if image:
            print("✅ Picto Ligne 23 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_24():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L24}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L24})

        if image:
            print("✅ Picto Ligne 24 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_25():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L25}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L25})

        if image:
            print("✅ Picto Ligne 25 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_26():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L26}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L26})

        if image:
            print("✅ Picto Ligne 26 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_30():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L30}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L30})

        if image:
            print("✅ Picto Ligne 30 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_31():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L31}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L31})

        if image:
            print("✅ Picto Ligne 31 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_32():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L32}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L32})

        if image:
            print("✅ Picto Ligne 32 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_33():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L33}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L33})

        if image:
            print("✅ Picto Ligne 33 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_34():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L34}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L34})

        if image:
            print("✅ Picto Ligne 34 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_35():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L35}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L35})

        if image:
            print("✅ Picto Ligne 35 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_36():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L36}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L36})

        if image:
            print("✅ Picto Ligne 36 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_37():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L37}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L37})

        if image:
            print("✅ Picto Ligne 37 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_38():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L38}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L38})

        if image:
            print("✅ Picto Ligne 38 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_39():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L39}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L39})

        if image:
            print("✅ Picto Ligne 39 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_40():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L40}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L40})

        if image:
            print("✅ Picto Ligne 40 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_90():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L90}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L90})

        if image:
            print("✅ Picto Ligne 90 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_91():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L91}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L91})

        if image:
            print("✅ Picto Ligne 91 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_92():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L92}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L92})

        if image:
            print("✅ Picto Ligne 92 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_93():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L93}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L93})

        if image:
            print("✅ Picto Ligne 93 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_X():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_LX}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_LX})

        if image:
            print("✅ Picto Ligne X trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def recuperer_url_ligne_9():
    print(f"🔍 Connexion à {URL_CIBLE}...")
    
    try:
        # 1. On récupère le contenu de la page
        # Le 'headers' simule un vrai navigateur pour éviter d'être bloqué
        headers = {'User-Agent': 'Mozilla/5.0'}
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        reponse.raise_for_status() # Vérifie si la page a chargé correctement

        # 2. On prépare BeautifulSoup
        soup = BeautifulSoup(reponse.text, 'html.parser')

        # 3. On cherche l'image. 
        # On essaie de la trouver via 'src' OU 'data-src' (sécurité lazy-loading)
        image = soup.find("img", attrs={"src": IMAGE_PICTO_L9}) or \
                soup.find("img", attrs={"data-src": IMAGE_PICTO_L9})

        if image:
            print("✅ Picto Ligne 9 trouvé !")
            
            # 4. On remonte à la balise <a> qui contient le lien
            lien_parent = image.find_parent("a")
            
            if lien_parent and lien_parent.has_attr('href'):
                url_pdf = lien_parent['href']
                
                # 5. On s'assure que l'URL est complète (absolue)
                url_complete = urljoin(URL_CIBLE, url_pdf)
                return url_complete
            else:
                return "❌ Image trouvée, mais aucun lien <a> autour."
        else:
            return "❌ Impossible de trouver l'image du picto sur la page."

    except Exception as e:
        return f"❌ Erreur lors du scraping : {e}"
def mettre_a_jour_fichier_groupe(nom_fichier, dict_urls_fraiches):
    chemin_complet = os.path.join("Lignes", nom_fichier)
    
    if not os.path.exists(chemin_complet):
        print(f"❌ Erreur : {chemin_complet} introuvable.")
        return

    with open(chemin_complet, "r", encoding="utf-8") as f:
        lignes = f.readlines()

    modifie = False
    for i in range(len(lignes)):
        if 'class="line-dot' in lignes[i]:
            for num_bus, (fichier_cible, classe_css) in CONFIG_LIGNES.items():
                if fichier_cible == nom_fichier:
                    identifiant_unique = f">{num_bus}</a>"
                    
                    if classe_css in lignes[i] and identifiant_unique in lignes[i]:
                        url = dict_urls_fraiches.get(num_bus)
                        if url and "http" in url:
                            nouvelle_ligne = f'            <a href="{url}" class="line-dot {classe_css}">{num_bus}</a>\n'
                            
                            # On ne modifie et ne passe à True QUE si la ligne change vraiment
                            if lignes[i] != nouvelle_ligne:
                                lignes[i] = nouvelle_ligne
                                modifie = True
                            break 
    
    if modifie:
        with open(chemin_complet, "w", encoding="utf-8") as f:
            f.writelines(lignes)
        print(f"💾 {nom_fichier} mis à jour avec succès.")
    else:
        print(f"✅ {nom_fichier} est déjà à jour (aucun changement).")


def mettre_a_jour_fichier_accueil(nom_fichier, dict_urls_fraiches):
    chemin_complet = os.path.join(nom_fichier)
    
    if not os.path.exists(chemin_complet):
        print(f"❌ Erreur : {chemin_complet} introuvable.")
        return

    with open(chemin_complet, "r", encoding="utf-8") as f:
        lignes = f.readlines()

    modifie2 = False
    for i in range(len(lignes)):
        if 'class="line-dot' in lignes[i]:
            for num_bus, (fichier_cible, classe_css) in CONFIG_LIGNES.items():
                if fichier_cible == nom_fichier:
                    identifiant_unique = f">{num_bus}</a>"
                    
                    if classe_css in lignes[i] and identifiant_unique in lignes[i]:
                        url = dict_urls_fraiches.get(num_bus)
                        if url and "http" in url:
                            nouvelle_ligne = f'            <a href="{url}" class="line-dot {classe_css}">{num_bus}</a>\n'
                            
                            # On ne modifie et ne passe à True QUE si la ligne change vraiment
                            if lignes[i] != nouvelle_ligne:
                                lignes[i] = nouvelle_ligne
                                modifie2 = True
                            break 
    
    if modifie2:
        with open(chemin_complet, "w", encoding="utf-8") as f:
            f.writelines(lignes)
        print(f"💾 {nom_fichier} mis à jour avec succès.")
    else:
        print(f"✅ {nom_fichier} est déjà à jour (aucun changement).")
if __name__ == "__main__":
    urls_extraites = {
        "20": recuperer_url_ligne_20(),
        "21": recuperer_url_ligne_21(),
        "22": recuperer_url_ligne_21(), # Copie auto de la 21
        "23": recuperer_url_ligne_23(),
        "24": recuperer_url_ligne_24(),
        "25": recuperer_url_ligne_25(),
        "26": recuperer_url_ligne_26(),
        "X":  recuperer_url_ligne_X(),
        "30": recuperer_url_ligne_30(),
        "31": recuperer_url_ligne_31(),
        "32": recuperer_url_ligne_32(),
        "33": recuperer_url_ligne_33(),
        "34": recuperer_url_ligne_34(),
        "35": recuperer_url_ligne_35(),
        "36": recuperer_url_ligne_36(),
        "37": recuperer_url_ligne_37(),
        "38": recuperer_url_ligne_38(),
        "39": recuperer_url_ligne_39(),
        "40": recuperer_url_ligne_40(),
        "90": recuperer_url_ligne_90(),
        "91": recuperer_url_ligne_91(),
        "92": recuperer_url_ligne_92(),
        "93": recuperer_url_ligne_93(),
        "9": recuperer_url_ligne_9(),
    }
    print("\n--- Phase d'écriture ---")
    mettre_a_jour_fichier_groupe("Secondaire.html", urls_extraites)
    mettre_a_jour_fichier_groupe("Suburbain.html", urls_extraites)
    mettre_a_jour_fichier_accueil("index.html", urls_extraites)
