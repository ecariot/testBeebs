import mysql.connector
# connexion à la base de données 
connection = mysql.connector.connect(
    host="localhost",   
    user="admin",       
    password="admin",   
    database="admin_db"  
)

cursor = connection.cursor() # Objet crée lors de la connection à la db avec la méthode cursor qui me permet d'executer les requêtes SQL

# requête SQL pour obtenir les combinaisons catégorie-marque en ne gardant que celles qui ont au moins 100 products
query = """
    SELECT category, brand, COUNT(id) AS product_count, GROUP_CONCAT(id) AS product_ids
    FROM Product
    GROUP BY category, brand
    HAVING product_count >= 100; 
"""
cursor.execute(query) # execution de la requête SQL avec la methode execute

# récupération des résultats
results = cursor.fetchall()

# création d'un dictionnaire pour stocker les titres de pages et les IDs de produits associés
pages = {}
for (category, brand, product_count, product_ids) in results:
    page_title = f"{category} {brand}"  # génération du titre de la page sous forme de string ("Bodies Jacadi")
    product_id_list = product_ids.split(',')  # conversion des IDs de produits en liste
    pages[page_title] = product_id_list

# fermeture de la connexion
cursor.close()
connection.close()

print(pages) # affichage final du dictionnaire
