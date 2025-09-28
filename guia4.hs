
-- Ejercicio 1

fibonacci :: Integer -> Integer
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

-- ejercicio 9 PREGUNTAR
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
funAux :: Integer -> Float
funAux 1 = 2
funAux x =  2 +  1 / funAux( x-1)

raizDe2Aprox :: Integer -> Float
raizDe2Aprox x = funAux x - 1

--ejercicio 13
sumatoria :: Integer -> Integer -> Integer
sumatoria 0 _  = 0
sumatoria 1 y = y
sumatoria x y =  sumatoria (x-1) y + sumatoria1 x y

sumatoria1 :: Integer -> Integer -> Integer
sumatoria1 _ 0 = 0
sumatoria1 x y = x^y + sumatoria1 x (y-1)


-- ejercicio 15
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales 1 1 = 1
sumaRacionales  x y =  sumaRacionales1 x y + fromIntegral (div 1  y) + sumaRacionales 1 (y-1)

sumaRacionales1 :: Integer -> Integer -> Float
sumaRacionales1 1 y = fromIntegral (div 1 y)
sumaRacionales1 x y  = fromIntegral (div x y)+ sumaRacionales1 (x-1) y


-- ejercicio 16
--a)
menorDivisor :: Integer -> Integer
menorDivisor x = listaARecorrer 2 x

listaARecorrer :: Integer -> Integer -> Integer
listaARecorrer d x | d == x = x
                   | mod x d == 0 = d
                   | otherwise = listaARecorrer (d + 1) x

--b)
esPrimo :: Integer -> Bool
esPrimo x = (menorDivisor x > 1) && (menorDivisor x == x)  

--c) 
sonCoPrimos :: Integer -> Integer -> Bool
sonCoPrimos x y  = menorDivisor x /= menorDivisor y

--d) 
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo x = recorroPrimos 2 x

recorroPrimos :: Integer -> Integer -> Integer 
recorroPrimos x n | esPrimo x && n == 1 = x
                  | esPrimo x  = recorroPrimos (x+1) (n-1)
                  | otherwise = recorroPrimos (x+1) n

-- ejercicio 17
esFibonacci :: Integer -> Bool
esFibonacci x = x == contadorFibonacci 1 x

contadorFibonacci :: Integer -> Integer -> Integer
contadorFibonacci c x | fibonacci c > x = fibonacci c 
                      | fibonacci c == x = x 
                      | otherwise = contadorFibonacci (c+1) x
