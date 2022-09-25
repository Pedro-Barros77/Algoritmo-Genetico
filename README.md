# Algoritmo-Genetico

Criado por [Pedro Barros](https://github.com/Pedro-Barros77)
e [Elias Lima](https://github.com/Elias-Lima-code)
para fins de prática e estudos em Inteligência Artificial.
> (UNA - 'Sistemas de Informação' e 'Gestão de Tecnologia da Informação')


_Primeira versão em 24-09-2022_


## Como funciona?

O algorítmo utiliza do modelo evolutivo de _Charles Darwin_, onde os melhores/mais fortes prevalecem e os mais fracos desaparecem do ecossistema.
Através de cruzamento genético e mutações, a IA consegue aprimorar os genes de cada cromossomo até que alcance o valor desejado.

Os parâmetros são customizáveis:
```
TOTAL_POPULATION = 50
TOTAL_GENES = 5
TARGET_PERCENTAGE = 0.98
CHOSEN_PERCENTAGE = 0.3
MUTATION_PERCENTAGE = 0.01
MIN_SUCCEEDED = 1
```
Resultado:

![Resultado obtido no console](https://user-images.githubusercontent.com/85514585/192126530-0ee34ed2-aaad-4e4d-bf4e-e43a11e440a3.png)


A Heurística utilizada foi simplesmente somar todos os valores dos genes, sendo assim quanto maior o valor mais perto do ideal está.
Dentre os nossos planos estão:
- [x] Adicionar personalização do intervalo de valores possíveis para os genes
- [ ] Adicionar personalização da Eurística (soma, subtração, multiplicação, números primos, números ímpares, números pares, divisíveis por X
- [ ] Criar interface gráfica amigável para o usuário e para acompanhamento do processo e de estatísticas

:green_circle: Uso e implementação livre, favor incluir os devidos créditos
