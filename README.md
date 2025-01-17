# ![](media/logo.png)

# Sistema de Bolsas de Estudo

Este projeto foi desenvolvido como parte da disciplina INF1039 da PUC-Rio. Trata-se de um site construído com o framework Django, HTML, CSS e JavaScript, com o objetivo de auxiliar calouros e veteranos na busca por bolsas de estudo em suas respectivas universidades.

O site oferece uma plataforma intuitiva tanto para as organizações quanto para os discentes. As organizações podem divulgar as bolsas de estudo disponíveis, enquanto os discentes têm uma experiência de navegação simples e eficiente para encontrar a bolsa ideal.

---

## Como Configurar e Executar o Projeto Localmente

### Pré-requisitos
Certifique-se de que possui os seguintes programas instalados em sua máquina:
- **Python 3.8 ou superior**
- **Pip (gerenciador de pacotes do Python)**
- **Virtualenv (opcional, mas recomendado)**

### Passo a Passo

1. **Clone este repositório**  
   Abra o terminal e execute:  
   ```bash
   git clone https://github.com/usuario/projeto-bolsas.git
   cd projeto-bolsas
2. **Crie e ative um ambiente virtual**
    ```bash
    python -m venv venv
    # Ativação no Windows
    venv\Scripts\activate
    # Ativação no Linux/Mac
    source venv/bin/activate
3. **Inicie o servidor local**
    ```bash
    python manage.py runserver
O servidor estará disponível em http://127.0.0.1:8000.


### Como Utilizar o Site
1. **Acesse o site local:**
- Abra o navegador e vá até http://127.0.0.1:8000.
2. **Explorar bolsas de estudo:**
- Calouros e veteranos podem procurar por bolsas disponíveis através do seu nome e pelo perfil das Instituições.
- Organizações podem fazer login para gerenciar e divulgar novas bolsas de estudo.
3. **Cadastro e Login:**
- Discentes e organizações podem se cadastrar e acessar o sistema para usufruir de funcionalidades personalizadas.

### Demonstração em Vídeo

