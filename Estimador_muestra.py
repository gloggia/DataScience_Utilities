class estimador(n,z,p,q,d):

 resultado = n * z * z * p * q /(0.05*0.05*(n-1) + 1.645 * 1.645 * 0.5 * 0.5 )
 #return resultado
 print( resultado)

#N: Tamaño de la población. 32,084 personas.

#Z: Coeficiente de confianza. Z = 1.645 para un nivel de confianza del 90%

#p: Probabilidad de éxito. Consideramos el máximo: 0.50

#q: Probabilidad de fracaso. Será 1.00 – 0.50 = 0.50

#d: Error máximo admisible. Consideramos el 5%
