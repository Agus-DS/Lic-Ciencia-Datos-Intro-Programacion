doubleMe x = x + x
doubleUs x y = doubleMe x + doubleMe y

doubleSmallNumber x = if x > 100 then x else x*2

--listas de números
let lostNumbers = [4,8,15,16,23,42]