-- Ejercicio 1

fibonacci :: Int -> Int
fibonacci x | x < 0 = undefined
            | x == 0 = 0
            | x == 1 = 1
            | otherwise = fibonacci (x-1) + fibonacci (x-2)

-- Ejercicio 2 
parteEntera :: Float -> Integer
parteEntera  x | x <= 1 = 0
               |  otherwise = 1 + parteEntera(x-1)         

-- Ejercicio 3
esDivisible :: Integer -> Integer -> Bool
esDivisible x y = resto x y == 0 
  
resto :: Integer -> Integer -> Integer
resto x y | x < y = x
          | otherwise = resto (x-y) y 

-- ejercicio 4
sumaImpares :: Integer -> Integer
sumaImpares x | x == 1 = 1
              | otherwise = (2 * x) - 1 + sumaImpares(x-1)

-- ejercicio 5 (preguntar por el requiere con el caso de negativos)

medioFact :: Integer -> Integer
medioFact x | x == 0 = 1
            | x < 0 = 1
            | otherwise = x * medioFact(x-2)

-- ejercicio 6
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales x | x < 10 && x >= 0 = True
                      | mod x 10 /= mod (div x 10) 10  = False
                      | otherwise = todosDigitosIguales (div x 10)

-- ejercicio 7
iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito x z | z > cantDigitos x || z < 0 = undefined
                 | z == cantDigitos x = mod x 10
                 | otherwise = iesimoDigito (div x 10) z

cantDigitos :: Integer -> Integer
cantDigitos x | x >=0 && x < 10 = 1
              | otherwise =  1 + cantDigitos (div x 10)                                                                                                                                                       

