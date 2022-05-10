#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

city = str(input('Digite uma cidade: ')).strip() #tirando espaços
print(city[:5].upper() == 'SANTO') #pegando do início até a 4 letra da palavra
