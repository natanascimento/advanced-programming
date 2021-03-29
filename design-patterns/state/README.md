# State - Design Pattern

## Conceito 📃

O State é um padrão de projeto comportamental que permite que um objeto possa alterar o comportamento a partir do momento que seu estado interno for alterado.

O padrão é intimamente relacionado ao conceito matemático de ***Máquina de Estado Finito*** que é basicamente representado como uma máquina abstrata que deve estar em um numero finito de estados. Esta máquina possui um estado por vez, tratando assim como *"o estado atual"*. 

<div align="center">
    <img src="https://refactoring.guru/images/patterns/diagrams/state/problem1.png?id=503968745461a0970d1f"/>
</div>


A ideia principal é que, em qualquer dado momento, há um número finito de estados que um programa possa estar. Dentro de qualquer estado único, o programa se comporta de forma diferente, e o programa pode ser trocado de um estado para outro instantaneamente. Contudo, dependendo do estado atual, o programa pode ou não trocar para outros estados. Essas regras de troca, chamadas transições, também são finitas e pré determinadas.

De forma geral, o state visa delegar o estado de um objeto contexto para uma familia de estados caso o seu objeto de contexto dependa do estado para mudar o seu comportamento. Sendo assim, o padrão encapsula os estados em objetos separados e delega as tarefas para o objeto que representa o estado, os comportamentos mudam assim que seu estado muda. Se um objeto que pode mudar totalmente de comportamento, então terá a impressão que uma nova instância de objeto foi criada a partir de outra classe.

A imagem a seguir reflete muito bem como o padrão State se comporta:

<div align="center">
    <img src="https://refactoring.guru/images/patterns/content/state/state-pt-br.png?id=942966fd4dc52793ca2f"/>
</div>

### Estrutura

1️⃣ - O Contexto armazena uma referência a um dos objetos concretos de estado e delega a eles todos os trabalhos específicos de estado. O contexto se comunica com o objeto estado através da interface do estado. O contexto expõe um setter para passar a ele um novo objeto de estado.

2️⃣ - A interface do Estado declara métodos específicos a estados. Esses métodos devem fazer sentido para todos os estados concretos porque você não quer alguns dos seus estados tendo métodos inúteis que nunca irão ser chamados.

3️⃣ - Os Estados Concretos fornecem suas próprias implementações para os métodos específicos de estados. Para evitar duplicação ou código parecido em múltiplos estados, você pode fornecer classes abstratas intermediárias que encapsulam alguns dos comportamentos comuns.

Objetos de estado podem armazenar referências retroativas para o objeto de contexto. Através dessa referência o estado pode buscar qualquer informação desejada do objeto contexto, assim como iniciar transições de estado.

4️⃣ - Ambos os estados de contexto e concretos podem configurar o próximo estado do contexto e realizar a atual transição de estado ao substituir o objeto estado ligado ao contexto.

<div align="center">
    <img src="https://refactoring.guru/images/patterns/diagrams/state/structure-pt-br.png?id=50efedb80eab6994524b"/>
</div>

### Analogia

Os botões e interruptores de seu smartphone comportam-se de forma diferente dependendo do estado atual do dispositivo:

- Quando o telefone está desbloqueado, apertar os botões leva eles a executar várias funções.
- Quando o telefone está bloqueado, apertar qualquer botão leva a desbloquear a tela.
- Quando a carga da bateria está baixa, apertar qualquer botão mostra a tela de carregamento.


### Vantagens ✅ e Desvantagens ❌

✅ Evita condicionais quando um objeto contexto muda de comportamento dependendo do seu estado atual; 

✅ Desacopla o estado de um objeto contexto e seus métodos em objetos de estado separados;

✅ Facilita a adicao de novos estados sem a necessidade de alterar estados anteriores; 

✅ Princípio de responsabilidade única:

    ✅ Organiza o código relacionado a estados particulares em classes separadas;

✅ Princípio aberto/fechado:

    ✅ Introduz novos estados sem mudar classes de estado ou contexto existentes;

✅ Simplifica o código de contexto ao eliminar condicionais de máquinas de estado pesadas;

❌ Aplicar o padrão pode ser um exagero se a máquina de estado só tem alguns estados ou raramente sofrem alteração;

## Fato Pouco Conhecido

***Os Padrões State e Strategy são irmãos gêmeos que foram separados ao nascer.***

O Padrão Strategy acabou se dando muito bem no négocio dos algoritmos intercambiáveis, já o padrão State, por sua vez, tomou um caminho mais talvez mais nobre de ajudar objetos a controlarem seu comportamento através de mudanças no seu estado interno. 

Essa estrutura pode ser parecida com o padrão Strategy, mas há uma diferença chave. No padrão State, os estados em particular podem estar cientes de cada um e iniciar transições de um estado para outro, enquanto que estratégias quase nunca sabem sobre as outras estratégias.