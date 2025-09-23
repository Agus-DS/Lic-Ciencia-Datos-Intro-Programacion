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
-- ejercicio 8
sumaDigitos :: Integer -> Integer 
sumaDigitos x | x == 0 = x
              | otherwise = mod x 10 + sumaDigitos (div x 10)

-- ejercicio 9 
esCapicua :: Integer -> Bool
esCapicua x | x >= 0 && x < 10 = True
            | ultimo  /=  primero = False 
            | otherwise = esCapicua (div x 10 - primero * 10 ^ (cantDigitos x-2))
             where ultimo =  mod x 10
                   primero = iesimoDigito x 1

-- ejercicio 11
eAprox :: Int -> Float
eAprox 0 = 1
eAprox x =  eAprox(x-1) + (1 / fromIntegral (factorial x))

factorial :: Int -> Int
factorial 0 = 1
factorial x = x*factorial(x-1)

e :: Float
e = eAprox 10

-- ejercicio 12
raizDe2Aprox :: Int -> Float
raizDe2Aprox 0 = 2
raizDe2Aprox x =  (2 + (1 / fromIntegral x-1)) + raizDe2Aprox(x-1)

-- ejercicio 14
sumaPotencias :: Int -> Int -> Int -> Int
sumaPotencias x 1 z = x ^ 1+z
sumaPotencias x y z = sumaPotencias x (y-1) z + sumaPotencia x y z

sumaPotencia :: Int -> Int -> Int -> Int
sumaPotencia x y 1 = x ^ (y+1)
sumaPotencia x y z = sumaPotencia x y (z-1) + x ^ y+z 

--ejercicio 19
esSumaInicialDePrimos :: Int -> Bool 
esSumaInicialDePrimos x = x

kEsimoPrimo :: Int -> Int !!


--- se resuelve sumaKprimos usando nEsimoPrimo que suma la 

nEsimoPrimo :: Int -> Int
nEsimoPrimo 1 = 2
nEsimoPrimo 2 = 3
nEsimoPrimo x =  2 + nEsimoPrimo(x-1)
