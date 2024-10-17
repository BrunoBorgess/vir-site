import streamlit as st
from PIL import Image
import base64

# Configurações iniciais da página
st.set_page_config(page_title="Virset - Engenharia de Dados", page_icon=":rocket:", layout="wide")

# Carrega a imagem da logo
logo = Image.open("vir.png")

# Função para converter a imagem para base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Converte a logo para base64
logo_base64 = get_base64_of_image("vir.png")

# CSS para um design moderno e estilizado
st.markdown(
    f"""
    <link href='https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap' rel='stylesheet'>
    <link href='https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap' rel='stylesheet'>
    <style>
        body {{
            background-color: #181818; /* Preto profundo */
            font-family: 'Montserrat', sans-serif;  
            color: #E0E0E0; /* Cinza claro */
            margin: 0;
            padding: 0;
        }}

        .top-bar {{
            background-color: rgba(36, 36, 36, 0.9); /* Cinza escuro com transparência */
            padding: 15px 30px; /* Aumentado para mais espaço */
            color: #FFFFFF;
            font-size: 20px;
            font-weight: bold;
            width: 100%;
            position: fixed;
            top: 0;
            left: 0;
            z-index: 1000;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
            display: flex;
            justify-content: space-between;
            align-items: center;
            transition: top 0.3s ease;
        }}

        .menu {{
            display: flex;
            gap: 30px; /* Aumentado o espaço entre os itens do menu */
        }}

        .menu a {{
            color: #76c7c0; /* Verde água */
            text-decoration: none;
            padding: 10px 20px; /* Aumentado para maior área clicável */
            border-radius: 5px;
            transition: background-color 0.3s, color 0.3s;
            font-weight: 600; /* Tornar o texto mais proeminente */
        }}

        .menu a:hover {{
            background-color: rgba(118, 199, 192, 0.2);
            color: #4FC3F7; /* Azul claro */
        }}

        .content {{
            margin-top: 100px; /* Aumentado para evitar sobreposição com a barra fixa */
            text-align: center;
            padding: 20px;
            background: linear-gradient(180deg, rgba(24, 24, 24, 0.8), rgba(0, 0, 0, 0.8)), url('https://example.com/background.jpg'); /* Exemplo de imagem de fundo */
            background-size: cover;
            border-radius: 15px;
        }}

        .card {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            border: 2px solid #4FC3F7; /* Azul claro */
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 8px 16px rgba(255, 255, 255, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }}

        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(255, 255, 255, 0.2);
            background: rgba(255, 255, 255, 0.2);
            border-color: #76c7c0; /* Verde água */
        }}

        .btn-whatsapp {{
            background-color: #25D366; /* Verde do WhatsApp */
            color: white;
            padding: 15px 30px;
            border-radius: 25px;
            text-decoration: none;
            font-size: 20px;
            font-weight: bold;
            transition: background-color 0.3s ease, transform 0.3s;
            margin-top: 30px;
            display: inline-block;
        }}

        .btn-whatsapp:hover {{
            background-color: #1EBD5B;
            transform: scale(1.05);
        }}

        .logo {{
            max-width: 50px; /* Diminuindo o tamanho da logo */
            margin-right: 15px;
        }}

        footer {{
            background-color: #242424; /* Cinza escuro */
            color: #E0E0E0; /* Cinza claro */
            padding: 20px 0;
            margin-top: 40px;
            text-align: center;
        }}
        
        /* Estilo para dispositivos móveis */
        @media (max-width: 768px) {{
            .top-bar {{
                flex-direction: column;
                align-items: flex-start;
                padding: 10px; /* Menos espaço no mobile */
            }}
            .menu {{
                flex-direction: column;
                align-items: flex-start;
                margin-top: 10px;
            }}
        }}
    </style>
    <script>
        let lastScrollTop = 0;
        window.onscroll = function() {{
            const topBar = document.querySelector('.top-bar');
            const currentScroll = window.pageYOffset || document.documentElement.scrollTop;

            if (currentScroll > lastScrollTop && currentScroll > 50) {{
                topBar.style.top = '-80px'; // Ajuste este valor para modificar o quanto a barra deve ser movida para cima
            }} else {{
                topBar.style.top = '0';
            }}
            lastScrollTop = currentScroll <= 0 ? 0 : currentScroll; // Para Mobile or negative scrolling
        }};
    </script>
    """,
    unsafe_allow_html=True
)

# Faixa de navegação com o título "Virset" e menu de navegação
st.markdown(
    f"""
    <div class='top-bar'>
        <img src='data:image/png;base64,{logo_base64}' class='logo' alt='Virset Logo'/>
        <div class='menu'>
            <a href='#services'>Serviços</a>
            <a href='#contact'>Contato</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Conteúdo principal
st.markdown("<div class='content'>", unsafe_allow_html=True)

# Seção de Introdução
st.markdown("<h1>Bem-vindo à Virset</h1>", unsafe_allow_html=True)
st.markdown(
    "<p>Na Virset, somos especialistas em engenharia de dados e no desenvolvimento de soluções inovadoras para sua empresa. Nossa equipe é dedicada a projetar e implementar sistemas robustos que integram, processam e analisam dados de forma eficiente, incluindo a criação de Data Warehouses e Data Lakes, além de todos os processos envolvendo a manipulação de dados. "
    "Com uma abordagem focada na transformação digital, capacitamos as empresas a utilizarem seus dados como ativos estratégicos, otimizando processos e melhorando a tomada de decisões. Nossa missão é criar soluções que não apenas atendem às necessidades atuais, mas que também preparam sua empresa para os desafios futuros, garantindo agilidade e competitividade no mercado.</p>",
    unsafe_allow_html=True
)

# Seção de Serviços
st.markdown("<h2 id='services'>Nossos Serviços</h2>", unsafe_allow_html=True)

# Exibe os serviços em um layout organizado
services = [
    ("Arquitetura de Dados", "Desenvolvemos estruturas robustas que potencializam o armazenamento e processamento de dados, permitindo decisões mais informadas."),
    ("Integração de Dados", "Conectamos diferentes fontes de dados para otimizar o fluxo de informações e melhorar a análise em tempo real."),
    ("Análises e Insights", "Transformamos dados em insights valiosos, ajudando sua empresa a se antecipar às tendências do mercado."),
    ("Automatização de Processos", "Eliminamos tarefas repetitivas para que sua equipe foque no que realmente importa: resultados."),
    ("Criação de Sistemas CRM", "Desenvolvemos soluções personalizadas de CRM que otimizam a gestão de relacionamento com clientes e centralizam dados essenciais."),
]

# Criar cartões para serviços com ícones (exemplo de ícones como texto, você pode substituir por ícones de imagem se preferir)
icons = ["🔧", "🔗", "📊", "⚙️", "📈"]

for (title, description), icon in zip(services, icons):
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader(f"{icon} {title}")  # Adiciona um ícone antes do título
    st.write(description)
    st.markdown("</div>", unsafe_allow_html=True)

# Seção de Contato
st.markdown("<h2 id='contact'>Contato</h2>", unsafe_allow_html=True)

# Botão de WhatsApp
st.markdown(
    "<a href='https://wa.me/17991237075' class='btn-whatsapp'>Agende uma Reunião</a>",
    unsafe_allow_html=True
)

# Exibir informações de contato
st.write("E-mail: virsetcomercial@gmail.com")
st.write("Telefone: (17) 99123-7075")

# Rodapé
st.markdown("<footer>", unsafe_allow_html=True)
st.markdown("<p>© 2024 Virset. Todos os direitos reservados.</p>", unsafe_allow_html=True)
st.markdown("</footer>", unsafe_allow_html=True)

# Finaliza o conteúdo principal
st.markdown("</div>", unsafe_allow_html=True)
