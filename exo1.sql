SELECT o.seller_id, COUNT(p.id) AS total_sold /*Sélectionne l'Id du vendeur depuis la table Order*/
FROM Order o /*Fait la jointure entre Order et Order_has_product*/
JOIN Order_has_product ohp ON o.id = ohp.order_id 
JOIN Product p ON ohp.product_id = p.id /*Fait la jointure entre Product et Order_has_product*/
WHERE p.brand = 'Jacadi' /*Filtre les produits pour ne garder que ceux de la marque Jacadi*/
GROUP BY o.seller_id /*Groupe les resultats par ID du vendeur*/
ORDER BY total_sold DESC /*Donne un ordre decroissant des vendeurs ayant des commandes Jacadi*/
LIMIT 1; /*Renvoie la premiere ligne c'est a dire le vendeur ayant le plus de commandes Jacadi*/
