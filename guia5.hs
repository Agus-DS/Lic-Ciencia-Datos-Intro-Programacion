-- ejercicio 1)

--1)

longitud :: [t] -> Integer
longitud  [] = 0
longitud (x:xs) = 1 + longitud(xs)

--2)
ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

--3)
principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs

--4)
reverso :: [t] -> [t]
reverso [] = []
reverso (lista) = [ultimo (lista)] ++ reverso(principio (lista)) 


-- ejercicio 2)

-- 1)
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) | e == x = True
                   | otherwise = pertenece e xs

-- 2)
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales (x:xs) | x /= ultimo (x:xs) = False
                    | otherwise = todosIguales (principio (x:xs))
--3)
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [x] = True
todosDistintos (x:xs) | pertenece x xs = False
                      | otherwise = todosDistintos xs
--4)
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [x] = False
hayRepetidos (x:xs) | pertenece x xs = True
                      | otherwise = hayRepetidos xs

--5)
quitar :: (Eq t) =>  t -> [t] -> [t]
quitar e [] = []
quitar e (x:xs) | e == x = xs
              | otherwise = quitar e xs

--6)
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos e (x:xs) | pertenece e (x:xs) = quitarTodos e (quitar e (x:xs))
                     | otherwise = x:xs


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
agregarContacto (n,t) ((n2,t1):lc) | n == n2 = ((n,t):lc)
                                   | otherwise = (n2,t1) : agregarContacto (n,t) lc 
