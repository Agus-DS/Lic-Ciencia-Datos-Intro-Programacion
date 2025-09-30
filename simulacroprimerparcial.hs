module SolucionT2 where

-- Ejercicio 1
cantidadNumerosAbundantes :: Integer -> Integer -> Integer
cantidadNumerosAbundantes  x y | x == y+1 = 0
                               | numeroAbundante x  = 1 + cantidadNumerosAbundantes (x+1) y
                               | otherwise = 0 + cantidadNumerosAbundantes (x+1) y

--numeroAbundante :: Integer -> Bool
numeroAbundante x = sumaDivisores x (x-1) > x

sumaDivisores :: Integer -> Integer -> Integer 
sumaDivisores x y | y == 1 = 1
                  | mod x y /= 0 = 0 + sumaDivisores x (y-1)
                  | otherwise = y + sumaDivisores x (y-1)

-- Ejercicio 2
cursadasVencidas :: [(String, Integer, Integer)] -> [String]
cursadasVencidas [] =  []
cursadasVencidas (x:xs) = cursadaAprobada x : [cursadasVencidas xs]

c (String, Integer, Integer ) -> String
cursadaAprobada (m,a,c) | a < 2021 && c < 
                        | otherwise = m



-- Ejercicio 3
saturarEnUmbralHastaNegativo :: [Integer] -> Integer -> [Integer]
saturarEnUmbralHastaNegativo _ _ = []

-- Ejercicio 4
cantidadParesColumna :: [[Integer]] -> Integer -> Integer
cantidadParesColumna _ _ = 0
