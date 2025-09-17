import System.Win32 (xBUTTON1)
-- Ejercicio 1
h x | x == 1 = 8
    | x == 4 = 131
    | x == 16 = 16

o x | x == 8 = 16
    | x == 16 = 4
    | x == 131 = 1

z x = h (o x)

k x = o (h x)

-- Ejercicio 2
--a)
absoluto x = if x <0 then (-x) else x

--b)
maximoAbsoluto x y = if absoluto(x) > absoluto (y) then absoluto(x) else absoluto(y)

--c)
maximo x y = if x > y then x else  y
           

maximo3 x y z = if (maximo x y) > z then (maximo x y) else z

--e)
ambosSonCero :: Int -> Int -> Int
ambosSonCero x y | (x == 0) && (y == 0) = x
                 | otherwise = undefined

--f)
enMismoIntervalo :: Float -> Float -> Bool 
enMismoIntervalo x y | (x <= 3) && (y <= 3) = True
                     | ((x > 3) && (x <= 7)) && ((y > 3) && (y <= 7)) = True
                     | (x > 7) && (y > 7) = True
                     | otherwise = False

--g)
sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | (x /= y) && (x /= z) && (y /= z) = x + y + z
                    | ((y /= z) && (z /= x)) || ((y /= z) && (x /= y)) = z + y
                    | (x /= y) && (x /= z) = x + y
                    | otherwise = x

--h)
esMultiploDe :: Int -> Int -> Int
esMultiploDe x y | mod x y == 0 = 1
                 | y == 0 = undefined
                 | otherwise = 0

--J) 
digitoDecenas :: Int -> Int
digitoDecenas x | x > 9 = mod (div x 10) 10 
                | otherwise = undefined


-- Ejercicio 3

estanRelacionados :: Int -> Int -> Bool
estanRelacionados x y | (x == 0) && (y == 0) = undefined
                      | (x*x) + y*x*div x (-y) == 0 = True
                      | otherwise = False

-- Ejercicio 4

--a) 
productoInterno :: (Float, Float) -> (Float, Float) -> Float
productoInterno (vx,vy) (wx,wy) = (vx * wx) + (vy * wy)

--b)
esParMenor :: (Float, Float) -> (Float, Float) -> Bool
esParMenor (x1,x2) (y1,y2) | (fst(x1,x2) < fst(y1,y2)) && (snd(x1, x2) < snd(y1,y2)) = True
                           | otherwise = False

--c)
distancia :: (Float, Float) -> (Float, Float) -> Float
distancia (x1, x2) (y1, y2) = sqrt(((x1-y1)**2) + ((x2-y2)**2) )

--d) 
sumaTerna :: (Int, Int, Int) -> Int
sumaTerna (x1,x2,x3) = x1+x2+x3

--e)

sumarSoloMultiplos :: (Int, Int, Int) -> Int -> Int
sumarSoloMultiplos (x1,x2,x3) y | (mod x1 y == 0) && (mod x2 y == 0) && (mod x3 y == 0) = x1 + x2 + x3
                                | (mod x2 y == 0) && (mod x3 y == 0) = x2 + x3
                                | (mod x1 y == 0) && (mod x3 y == 0) = x1 + x3
                                | (mod x1 y == 0) && (mod x2 y == 0) = x1 + x2 
                                | otherwise = 0

--f)
posPrimerPar :: (Int, Int, Int) -> Int
posPrimerPar (x1,x2,x3) | mod x1 2 == 0 = 0
                        | mod x2 2 == 0 = 1
                        | mod x3 2 == 0 = 2
                        | otherwise =  4

--g)
crearPar :: a ->  b-> (a, b)
crearPar a b = (a,b)


-- ej 5

todosMenores :: (Int, Int, Int) -> Bool
todosMenores (x,y,z) = (f x > g x) && (f y > g y) && (f z > g z)


f :: Int -> Int
f x | x <= 7 = x*x 
    | otherwise = 2*x - 1

g :: Int -> Int
g x | mod x 2 == 0 = div x 2
    | otherwise = 3*x + 1

--ejercicio 6
bisiesto :: Integer -> Bool
bisiesto x = (mod x 4 == 0) || ((mod x 100 == 0) && (mod x 400 /= 0))

--ejercicio 7
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (x1,x2,x3) (y1,y2,y3) | (x1-y1) + (x2-y2) + (x3-y3) < 0 = - ((x1-y1) + (x2-y2) + (x3-y3))
                                         | otherwise = (x1-y1) + (x2-y2) + (x3-y3)

--ejercicio 8

comparar :: Int -> Int -> Int
comparar x y| sumaUltimosDosDigitos x < sumaUltimosDosDigitos y = 1
            | sumaUltimosDosDigitos x > sumaUltimosDosDigitos y = -1
            | otherwise = 0

sumaUltimosDosDigitos :: Int -> Int
sumaUltimosDosDigitos x = mod x 10 + mod (div x 10) 10