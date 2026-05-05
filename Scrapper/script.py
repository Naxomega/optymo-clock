import discord
from discord.ext import commands
import requests  # For downloading web pages and PDFs
from bs4 import BeautifulSoup  # For parsing HTML
from urllib.parse import urljoin  # For fixing relative URLs
import os  # For managing the downloaded PDF file
from datetime import date
# Ce script est basé sur mon travail sur GrailleBot,
# son but est de bruteforce toutes les combinaisons possibles
# afin de récupérer les urls valides

# ============================
# STEP 0: CONFIGURATION
# ============================
jour = date.today()
formatted_date = jour.strftime("%d-%m-%Y")
# This is the main URL of your school's website


# We will search for the news item containing this keyword
SEARCH_KEYWORD = "Menu"  #

# This is the name the PDF will be saved as locally
FILENAME = f"Menu_Cantine_{formatted_date}.pdf"

# !!! PASTE YOUR BOT'S SECRET TOKEN HERE !!!


# --- Confirmed CSS Selectors ---

# Selects the container for each news item on the main page
NEWS_ITEM_CONTAINER = "article.fo-card"

# Selects the title link inside the news item
MENU_PAGE_LINK_SELECTOR = "h3.fo-card__title a"

# Selects any link on the sub-page that ends with '.pdf'
PDF_LINK_SELECTOR = "a"


# ============================
# STEP 1: WEB SCRAPING & DOWNLOAD LOGIC
# ============================

def get_menu_pdf_path():
    """
    Finds the menu link, navigates to the page, downloads the PDF,
    and returns the local file path.
    """
    try:
        # --- PART 1: Find the Full Menu Page Link ---
        print(f"1. Fetching main page: {MAIN_URL}")
        # Set a timeout to prevent the bot from hanging indefinitely
        main_response = requests.get(MAIN_URL, timeout=10)
        # Raise an error if the request failed (e.g., 404, 500)
        main_response.raise_for_status()
        
        main_soup = BeautifulSoup(main_response.content, 'html.parser')

        # Find all news items
        all_news_items = main_soup.select(NEWS_ITEM_CONTAINER)
        menu_page_url = None

        # Loop through all news items to find the one with the keyword
        for item in all_news_items:
            # Find the link element within this item
            link_element = item.select_one(MENU_PAGE_LINK_SELECTOR)
            if link_element and SEARCH_KEYWORD in link_element.get_text():
                # We found it! Get the URL from the 'href' attribute
                relative_link = link_element.get('href')
                # Use urljoin to build a full, absolute URL
                menu_page_url = urljoin(MAIN_URL, relative_link)
                break  # Stop searching once we find the first match

        if not menu_page_url:
            return None, f"⚠️ Aucun élément contenant '{SEARCH_KEYWORD}' trouvé sur la page principale."

        print(f"2. Found menu page link: {menu_page_url}")

       # --- PART 2: Navigate to Menu Page and Find the File Link ---
        print("3. Fetching menu page to find file link...")
        menu_response = requests.get(menu_page_url, timeout=10)
        menu_response.raise_for_status()
        
        menu_soup = BeautifulSoup(menu_response.content, 'html.parser')

        pdf_url = None
        
        # AGGRESSIVE SEARCH: Search every single <a> tag on the page
        for element in menu_soup.find_all(PDF_LINK_SELECTOR): 
            # Check the element's 'href' attribute
            href = element.get('href')
            
            # Look for the unique file-serving script in the link
            if href and 'lectureFichiergw.do' in href:
                relative_pdf_link = href
                # Combine the relative link with the base URL
                pdf_url = urljoin(menu_page_url, relative_pdf_link)
                break # Found it, stop searching

        if not pdf_url:
            return None, "❌ Impossible de trouver de lien contenant 'lectureFichiergw.do' sur la page du menu."

        # --- Download the PDF content ---
        print(f"4. Found PDF URL: {pdf_url}")
        print("5. Downloading PDF file...")
        
        # We need the full URL to download the file served by the script
        pdf_response = requests.get(pdf_url, stream=True, timeout=10)
        pdf_response.raise_for_status()

        # Save the PDF content locally
        with open(FILENAME, 'wb') as f:
            for chunk in pdf_response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Return the local file path and a success message
        return os.path.abspath(FILENAME), "✅ Menu téléchargé avec succès !"

    except requests.exceptions.RequestException as e:
        print(f"Error during web request: {e}")
        return None, f"❌ Une erreur réseau est survenue : {e}"
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, f"❌ Une erreur inattendue est survenue : {e}"

# ============================
# STEP 2: DISCORD BOT INTEGRATION
# ============================

# Define intents: This tells Discord what your bot needs permission to "see"
intents = discord.Intents.default()
intents.message_content = True  # Required to read messages and detect commands

# Initialize the bot with a command prefix (e.g., !menu)
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    """Event handler: runs when the bot successfully connects to Discord."""
    print(f'🤖 Bot is online and logged in as {bot.user}')
    print('------')

@bot.command(name='menu')
async def send_menu(ctx):
    """Command: !menu - Downloads and posts the canteen menu PDF."""
    
    # Send an immediate status update so the user knows the bot is working
    status_msg = await ctx.send("⌛ Recherche du dernier menu de la cantine...")

    # Run the scraping and download function
    # This part can take a few seconds
    file_path, status_message = get_menu_pdf_path()
    
    # Check if the download was successful
    if file_path:
        try:
            # Create a discord.File object from the downloaded file
            jour = date.today()
            formatted_date = jour.strftime("%d/%m/%Y")
            menu_file = discord.File(file_path, filename=FILENAME)

            # Send the file along with the success message
            await ctx.send(
                content=f"**{status_message}** Voici le menu :",
                file=menu_file
            )
            # Delete the "Searching..." message
            await status_msg.delete()

        except Exception as e:
            # If sending the file fails
            print(f"Error sending file to Discord: {e}")
            await status_msg.edit(content=f"❌ Erreur lors de l'envoi du fichier sur Discord : {e}")
        finally:
            # Clean up: Delete the local PDF file after sending it
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"6. Cleaned up local file: {file_path}")
            
    else:
        # If file_path is None, it means the download failed.
        # Edit the status message to show the error.
        await status_msg.edit(content=status_message)

# ============================
# STEP 3: RUN THE BOT
# ============================

if __name__ == '__main__':
    try:
        bot.run(BOT_TOKEN)
    except discord.errors.LoginFailure:
        print("LOGIN FAILED: Please check your BOT_TOKEN in STEP 0.")
    except Exception as e:
        print(f"Error running bot: {e}")