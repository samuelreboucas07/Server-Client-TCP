# Escopo e objetivo



# Iniciando ....

## Faça o clone do repositório atual

* ``` https://github.com/samuelreboucas07/Sistemas-distribu-dos.git ```

## Abra o terminal e execute o seguinte comando:


* ``` cd Sistemas-distribu-dos/Practical\ work\ 1 ```


# Pré-requisitos

Você deverá ter instalado em seu computador a versão 3 da linguagem de programação Python. 

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

1. Solicitação do arquivo presente na cache:
   
   Este cenário é o mais indicado no que diz respeito economia de recursos, a cache do servidor é projetada para armazenar arquivos recorrentemente requeridos por um tempo limitado, de modo que o custo de ler o mesmo arquivo a cada requisição seja reduzido.

    Observe na figura abaixo que 

   ![fluxo de execução](https://github.com/samuelreboucas07/Sistemas-distribu-dos/blob/Atividade-pratica-1/imgs/req_file_1.png)

# Memória Cache

# Multiprocessamento

# Exclusão mútua

# Websocket

# Exemplo de funcionamento