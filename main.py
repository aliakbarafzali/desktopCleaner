import os
import shutil

# Récupération du chemin du bureau pour l'utilisateur sous Windows
desktop_path = r"C:\Users\aafzali\OneDrive - EVERIAL\Bureau"



def display_menu():
    print("\nChoose the type of files to clean:")
    print("1. Images")
    print("2. Videos")
    print("3. Documents")
    print("4. Audio")
    print("5. Compressed files")
    print("6. Folders/archives")
    print("7. All file types")
    print("0. Exit")

def clean_files(choice):
    if choice == "1":
        print("Cleaning image files...")
        cleanImages()
    elif choice == "2":
        print("Cleaning video files...")
        cleanVideos()
    elif choice == "3":
        print("Cleaning document files...")
        cleanDocuments()
    elif choice == "4":
        print("Cleaning audio files...")
    elif choice == "5":
        print("Cleaning compressed files...")
        cleanCompressed()
    elif choice == "6":
        print("Cleaning folders...")
        cleanFolders()
    elif choice == "7":
        print("Cleaning all files...")
        cleanAll()
    elif choice == "0":
        print("Exiting...")
    else:
        print("Invalid choice. Please enter a valid option.")

# Dictionnaires d'extensions pour chaque type de fichier
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp', '.tiff', '.ico', '.heic']
video_extensions = ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpeg', '.3gp']
document_extensions = ['.pdf', '.doc', '.docx', '.txt', '.odt', '.rtf', '.xls', '.xlsx', '.ppt', '.pptx']
audio_extensions = ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma', '.aiff', '.alac']
compressed_extensions = ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz']

def move_files_by_extension(extensions, folder_name):
    destination = os.path.join(desktop_path, folder_name)
    
    # Créer le dossier cible s'il n'existe pas
    if not os.path.exists(destination):
        os.mkdir(destination)
        print(f"{folder_name} created.")

    # Parcourir les fichiers du bureau et déplacer ceux avec les extensions correspondantes
    files = [file for file in os.listdir(desktop_path) if os.path.isfile(os.path.join(desktop_path, file))]
    for file in files:
        file_path = os.path.join(desktop_path, file)
        if os.path.splitext(file)[1].lower() in extensions:
            shutil.move(file_path, destination)
            print(f"Moved {file} to {destination}")

# Fonctions spécifiques pour chaque type de fichier
def cleanImages():
    move_files_by_extension(image_extensions, "Images")

def cleanVideos():
    move_files_by_extension(video_extensions, "Videos")

def cleanDocuments():
    move_files_by_extension(document_extensions, "Documents")

def cleanAudios():
    move_files_by_extension(audio_extensions, "Audios")

def cleanCompressed():
    move_files_by_extension(compressed_extensions, "Archives")

def cleanFolders():
    folders_destination = os.path.join(desktop_path, "Folders")
    
    if not os.path.exists(folders_destination):
        os.mkdir(folders_destination)
        print(f"Dossier 'Folders' créé.")

    items = os.listdir(desktop_path)
    for item in items:
        item_path = os.path.join(desktop_path, item)
        if os.path.isdir(item_path) and item not in ["Folders", "Documents", "Images", "Videos", "Compressed", "Audios"]:
            shutil.move(item_path, folders_destination)
            print(f"Dossier {item} déplacé vers {folders_destination}")

def cleanAll():
    print("Complete cleaning...")
    cleanImages()
    cleanVideos()
    cleanDocuments()
    cleanAudios()
    cleanCompressed()
    cleanFolders()
    print("End of complete cleaning")



while True:
    display_menu()
    user_choice = input("Enter the number of your choice: ")
    if user_choice == "0":
        clean_files(user_choice)
        break
    clean_files(user_choice)


