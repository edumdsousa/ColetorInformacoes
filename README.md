# Coletor de Informações do Sistema

O Coletor de Informações do Sistema é uma aplicação em Python desenvolvida para fornecer uma interface simples e intuitiva para obter e registrar informações importantes sobre o sistema operacional em execução. A aplicação permite que o usuário colete dados como tipo de sistema (PC ou notebook), modelo da placa mãe, RAM, SSD, HDD, entre outras informações úteis.

## Funcionalidades

- Interface gráfica amigável que facilita a obtenção e registro de informações do sistema.
- Obtenção automática de dados importantes, como tipo de sistema, modelo da placa mãe, RAM, SSD e HDD.
- Capacidade de preencher manualmente campos adicionais, como responsável, matrícula, usuário, e-mail e localidade.
- Geração de arquivo de texto com as informações coletadas para referência futura.

## Como usar

1. Faça o download do repositório para o seu computador.
2. Certifique-se de ter o Python instalado.
3. Instale as dependências usando `pip install -r requirements.txt`.
4. Execute o programa com `python coletor_informacoes.py`.
5. Preencha os campos restantes conforme necessário e clique em "Obter Informações".
6. Após revisar os dados, clique em "Escrever" para salvá-los em um arquivo de texto.

## Tecnologias Utilizadas

- Python
- Tkinter (para a interface gráfica)
- psutil (para obter informações do sistema)
- wmi (para obter informações específicas do Windows)

## Contribuições

Contribuições são bem-vindas! Se você encontrou um bug ou deseja adicionar uma nova funcionalidade, sinta-se à vontade para enviar uma solicitação de pull request.

## Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.
