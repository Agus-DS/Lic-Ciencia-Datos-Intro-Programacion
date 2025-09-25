quitar :: (Eq t) =>  t -> [t] -> [t]
quitar e [] = []
quitar e (x:xs) | e == x = xs
              | otherwise = quitar e xs

maximo :: (Ord t) => [t] -> t
maximo [x] = x
maximo (x:xs) | x > (maximo xs) = x
              | otherwise = maximo xs

ordenar :: (Ord t) => [t] -> [t]
ordenar [] = [] 
ordenar (x:xs) = (ordenar (quitar (maximo (x:xs)) (x:xs))) ++ [maximo(x:xs)]


type Texto = [Char]
type Nombre = Texto
type Telefono = Texto
type Contacto = (Nombre, Telefono)
type ContactosTel = [Contacto]

enLosContactos :: Nombre -> ContactosTel -> Bool
enLosContactos _ [] =  False
enLosContactos n ((m,t):lc) | n == m = True
                            | otherwise = enLosContactos n lc

agregarContacto :: Contacto -> ContactosTel -> ContactosTel
agregarContacto c [] = [c]
agregarContacto (n,t) ((n2,t1):lc) | n == n1 = ((n,t):lc)
                                   | otherwise = (n2,t1) : agregarContacto (n,t) lc 



multiplicarFilas :: [[Integer]] -> [Integer]