# Escopo e objetivo



# Iniciando ....

## Faça o clone do repositório atual

* ``` https://github.com/samuelreboucas07/Sistemas-distribu-dos.git ```

## Abra o terminal e execute o seguinte comando:


* ``` cd Sistemas-distribu-dos/Practical\ work\ 1 ```


# Pré-requisitos

Você deverá ter instalado em seu computador a versão 3 da linguagem de programação Python. 

# Protocolo

O socket provê a comunicação entre duas partes. A representação é dada por ```ip:porta```, de modo que o socket para realizar a transferência de informações entre o cliente e servidor utiliza o conjunto de protocolos TCP/IP .

De acordo com o modelo OSI os sockets estão entre a camada de aplicação e de transporte.

![protocolo de comunicação](https://github.com/samuelreboucas07/Sistemas-distribu-dos/blob/Atividade-pratica-1/imgs/protocol.png)

Para iniciar a comunicação entre cliente e servidor é necessário que o cliente conheça o endereço (IP) e a porta do servidor, caso contrário não será possível realizar a comunicação entre as partes, uma vez que este tipo de conexão é sempre iniciada pelo cliente.

# Executando a aplicação

O presente trabalho é caracterizado pela troca de informações entre cliente e servidor, deste modo a execução deste projeto é definida em duas etapas básicas, inicialização do servidor e solicitação do cliente.

## Inicialização do servidor

Para inicializar o servidor o comando deve respeitar o seguinte padrão:

* ``` python3 server_main.py porta repositorio_de_arquivos ```

O valor referente ao campo **porta** representa o ponto de comunicação entre o servidor e o cliente (desde que combinado com o endereço de IP correto). Já o campo **repositorio_de_arquivos** representa a pasta a qual o servidor terá "controle" sobre os arquivos, podendo transferi-los mediante solicitação do cliente.

## Requisição do cliente

### Solicitação de arquivo ao servidor

Para realizar uma requisição ao servidor é necessário seguir o seguinte comando:

* ``` python3 client.py endereco porta nome_arquivo diretorio_destino ```

Baseado no endereço em que o presente servidor está em execução, o campo **endereco** deverá ser substituido por **localhost**, de modo que o comando para execução do cliente fique da seguinte forma:

* ``` python3 client.py localhost porta nome_arquivo diretorio_destino ```

O campo **nome_arquivo** se refere ao arquivo que vai ser solicitado ao servidor, o qual será salvo no diretório informado através do campo **diretorio_destino**.

### Solicitação de informação sobre estado da memóra cache

Além da solicitação de arquivos do servidor o cliente pode solicitar ao servidor que o mesmo envie o estado atual da sua memória cache, informando quais arquivos estão alocados no presente momento. Para tal, execute o seguinte comando. 

* ``` python3 client.py localhost porta list_files_cache ```

**Observação:** O campo **porta** deve ser igual tanto no servidor, quanto no cliente, caso contrário não será possível realizar a comunicação entre as partes.

# Modelagem

## Organização dos arquivos

O presente trabalho foi modularizado de modo a garantir que possíveis refatorações futuras e novas funcionalidades sejam realizadas de modo facilitado, deste modo o servidor foi divido em 3 arquivos e o cliente apenas 1 arquivo.

* ```server_main.py: ``` Arquivo de inicialização do servidor, o mesmo é responsável por habilizar o socket e garnatir que a porta definida no presente endereço seja escutado pelo socket, de modo que a partir do momento que novos clientes tentarem conectar ao servidor, o mesmo tenha ciência da solicitação.
Neste mesmo arquivo é realizado a instanciação da Thread, a qual será explanada nas próximas seções.

* ```server.py: ``` Este arquivo é caracterizado como o principal arquivo do servidor, nele estão desenvolvidas todas as rotinas de leitura de arquivo, comunicação com cliente (recebimento de mensagem e envio de resultado), assim como a intereação com a memória cache, entre outros.
  
* ```cache.py: ``` Dada a configuração da memória cache e os métodos a ela empregada, julgou-se necessário a modularização da mesma, de modo que todas as interações tivessem um contexto bem definido, desde a sua instanciação até o retorno do resultado de seu processamento.

Os arquivos acima representam o servidor da aplicação, desde a camada de interação com o cliente até o armazenamento dos arquivos em memória.

* ```client.py: ``` Este arquivo compreende o tratamento das informações dada pelo cliente ao executar o presente arquivo, assim como a solicitação ao servidor para a transação de dados ou listagem dos items contidos na memória cache.

## Fluxo de execução

O presente projeto apresenta diferentes cenários decorrentes da solicitação do cliente ao servidor, os quais estão descritos abaixo.

1. Solicitação de arquivo presente na memória cache:
   
   Este cenário é o mais indicado no que diz respeito economia de recursos, a cache do servidor é projetada para armazenar arquivos recorrentemente requeridos por um tempo limitado, de modo que o custo de ler o mesmo arquivo a cada requisição seja reduzido.

    Observe na figura abaixo o fluxo de execução neste cenário:

   ![fluxo de execução, arquivo na cache](https://github.com/samuelreboucas07/Sistemas-distribu-dos/blob/Atividade-pratica-1/imgs/req_file_1.png)

   O cliente realiza a requisição de um arquivo ao servidor, em sequência o servidor vai verificar se o arquivo solicitado está na memória cache, caso o resultado seja positivo o arquivo é retornado para o servidor e serializado para enviar ao cliente solicitante. Caso contrário o servidor recebe a informação referente a ausência do arquivo na memória cache, e parte para o pŕoximo caso.

2. Solicitação de arquivo ausente na memória cache:
   
   Partindo da situação anterior, onde o servidor recebe a informação da memória cache que o arquivo solicitado não está presente, temos o seguinte fluxo:

    ![fluxo de execução, arquivo fora da cache](https://github.com/samuelreboucas07/Sistemas-distribu-dos/blob/Atividade-pratica-1/imgs/req_file_2.png)

    Observe que a partir do momento que o servidor tem ciência da falta deste arquivo na memória cache o mesmo vai diretamente ao diretório de conhecimento para ler o arquivo e trazer ao servidor.

    Sequencialmente a memória cache é acessada, e verificado se o arquivo solicitado para transferência tem tamanho menor ou igual ao limite da memória, caso o resultado seja positivo a memória vai liberar espaço ocupado (caso seja necessário) e assim será realizado o armazenamento do arquivo na cache. Após esse processo o arquivo é enviado para o servidor, para assim ser enviado ao cliente.

    Caso o arquivo lido do sistema do diretório tenha tamanho maior que o limite permitido pela memória cache, o mesmo é enviado diretamento para o cliente e não será armazenado na memória cache.

3. Solicitação de lista de arquivos presentes na memória cache:
   
   Este processo representa o menor fluxo de execução entre cliente e servidor. O cliente realiza a solicitação de listagem, o servidor recebe essa requisição, acessa a memória cache, percorre todos os dados armazenados e retorna para o servidor a lista com o nome de cada arquivo, em sequência o servidor retornará esta informação para o cliente.

   ![fluxo de execução, listagem de arquivo](https://github.com/samuelreboucas07/Sistemas-distribu-dos/blob/Atividade-pratica-1/imgs/list_files.png)


## Observações

Dada a topologia de um sistema de requisição entre cliente servidor, toda a informação transferida entre as partes é serializada,  para tal foi utilizado o módulo [Pickle](https://docs.python.org/3/library/pickle.html), o qual transforma as informações em fluxo de bytes para assim serem transferidas, posteriormente a mesma informação é desserializada para assim o requerinte ter conhecimento da mesma.

# Memória Cache

A memória cache deve ter uma estrutura que garanta velocidade de acesso e eficiência no armazenamento temporário, para tal a mesma foi simulada usando uma estrutura de dados baseada em chave e valor, denominada dicionário.

Desta forma a memória cache possui uma estrutura cuja a chave de cada elemento é caracterizada pelo nome do arquivo armazenado, e seu valor é descrito por conter as informações binárias do arquivo lido, assim como o tamanho em Megabytes. Observe no esquema abaixo:

```
{
   "nome_arquivo" : {
                        "conteúdo": '[b'', .... ]',
                        "tamanho": 10,0 
                    }
}
```

# Multiprocessamento

Dada as particularidades de sistemas similares ao presente projeto, o multiprocessamento é uma caracteristica geralmente encontrada devido a necessidade de diferentes clientes realizarem solicitações ao servidor no mesmo período de tempo sem que a solicitação de um cliente onere a experiência de outro devido a impossibilidade de acesso no referido momento.

Deste modo, foi necessário aplicar o conceito de Threads, as quais possibilitam que o sistema operacional execute várias solicitações simultaneamente, sem que uma interefira na outra compartilhando os recursos do processo, mas executando de forma independente.

# Exemplo de funcionamento