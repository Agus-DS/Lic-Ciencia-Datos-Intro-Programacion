-- SISTEMA DE STOCK

-- Ejercicio 1


conteoProducto :: (Eq t) => t -> [t] -> Integer 
conteoProducto _ [] = 0
conteoProducto p (x:xs) | p /= x = 0
                        | otherwise = 1 + conteoProducto p xs
