import streamlit as st
import time

# 1. Configuração inicial da página (Mantenha sempre no topo)
st.set_page_config(page_title="Calculadora Otto Shopee", page_icon="🛒", layout="centered")

# --- INJEÇÃO DE CSS (MOTION DESIGN E GLASSMORPHISM) ---
# Adicionei novas classes para o card de cabeçalho e o rótulo verde
st.markdown("""
<style>
    /* Fundo escuro premium */
    .stApp {
        background-color: #0A0A0B;
    }
    
    /* NOVO: Card Gigante do Cabeçalho com Cores Temáticas da Shopee */
    .header-card-shopee {
        background-color: #EE4D2D; /* Laranja Shopee */
        border-radius: 20px;
        padding: 40px 20px; /* Grande preenchimento para ser "gigante" */
        text-align: center;
        color: #FFFFFF; /* Texto branco */
        box-shadow: 0 4px 15px rgba(238, 77, 45, 0.4); /* Sombra laranja */
        margin-bottom: 10px; /* Espaço pequeno para o subtítulo */
        animation: fadeInDown 0.8s ease-out; /* Animação de motion design */
    }
    
    /* NOVO: Título Branco dentro do Card */
    .header-title-shopee {
        font-size: 3.2rem;
        font-weight: 900;
        text-transform: uppercase;
        color: #FFFFFF;
        margin: 0; /* Remove margens padrão */
    }
    
    /* ATUALIZADO: Novo Subtítulo em cinza */
    .new-subtitulo {
        text-align: center;
        color: #A0AEC0; /* Cinza */
        font-size: 1.1rem;
        margin-top: 0px;
        margin-bottom: 40px; /* Espaço para o campo de custo */
        animation: fadeInDown 1s ease-out;
    }

    /* Cards de Vidro (Glassmorphism) para os resultados (Mantido) */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 25px 15px;
        text-align: center;
        color: #E2E8F0;
        transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), border 0.4s ease;
        animation: fadeInUp 0.8s ease-out;
        margin-bottom: 20px;
    }
    
    .glass-card:hover {
        transform: translateY(-8px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Estilos de Tipografia dos Preços (Mantido) */
    .label-margin { font-size: 1rem; color: #A0AEC0; margin-bottom: 10px; font-weight: 600; }
    
    .price-agressivo { background: linear-gradient(90deg, #FF416C 0%, #FF4B2B 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.2rem; font-weight: 800; }
    .price-intermediario { background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.2rem; font-weight: 800; }
    .price-premium { background: linear-gradient(90deg, #8A2387 0%, #E94057 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.2rem; font-weight: 800; }

    /* NOVO: Rótulo Verde Dinheiro para o Custo do Produto */
    .green-money-label {
        color: #28a745; /* Verde Dinheiro */
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 10px;
    }

    /* Animações de entrada (Mantido) */
    @keyframes fadeInDown { from { opacity: 0; transform: translateY(-30px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }
    
    /* Ocultar menus do Streamlit (Mantido) */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
# --- FIM DO CSS ---

# 2. Interface Visual (Lançamento do Cabeçalho)

# Renderiza o card gigante laranja Shopee com o título branco
st.markdown(f'''
<div class="header-card-shopee">
    <h1 class="header-title-shopee">CALCULADORA OTTO Shopee</h1>
</div>
''', unsafe_allow_html=True)

# Renderiza o novo subtítulo abaixo
st.markdown('<p class="new-subtitulo">Preços exatos para máximo controle operacional</p>', unsafe_allow_html=True)

# 3. Campo de Entrada de Custo (Estilizado)

# Renderiza o rótulo verde dinheiro acima do campo de entrada
st.markdown('<p class="green-money-label">Custo Total do Produto - R$</p>', unsafe_allow_html=True)
# O campo de entrada em si fica sem rótulo para não repetir
custo = st.number_input(label="", min_value=0.0, step=1.0, format="%.2f")

# Botão de ação (Mantido)
if st.button("Gerar Preços Inteligentes 🚀", use_container_width=True):
    if custo > 0:
        with st.spinner("Calculando taxas, impostos e margens cruzadas..."):
            # Delay para sensação de processamento complexo (Aumentado para 1s para o motion design)
            time.sleep(1.0) 
            
            preco_teste = custo
            preco_18 = 0
            preco_25 = 0
            preco_30 = 0

            # O seu motor matemático original (intacto)
            while preco_30 == 0:
                if preco_teste < 80.00:
                    taxa = (preco_teste * 0.20) + 4.00
                elif preco_teste < 100.00:
                    taxa = (preco_teste * 0.14) + 16.00
                elif preco_teste < 200.00:
                    taxa = (preco_teste * 0.14) + 20.00
                else:
                    taxa = (preco_teste * 0.14) + 26.00
                    
                imposto = preco_teste * 0.06
                lucro = preco_teste - custo - taxa - imposto
                margem_atual = lucro / preco_teste if preco_teste > 0 else 0
                
                if margem_atual >= 0.18 and preco_18 == 0:
                    preco_18 = preco_teste
                if margem_atual >= 0.25 and preco_25 == 0:
                    preco_25 = preco_teste
                if margem_atual >= 0.30 and preco_30 == 0:
                    preco_30 = preco_teste
                    
                preco_teste += 0.10

            # Exibe os resultados (Mantido)
            st.divider()
            st.markdown('<p style="text-align: center; color: #E2E8F0; font-size: 1.3rem; font-weight: 600; margin-bottom: 25px;">Sugestões de Preço Final</p>', unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f'''
                <div class="glass-card" style="box-shadow: 0 10px 30px rgba(255, 75, 43, 0.12);">
                    <div class="label-margin">🔥 Agressivo (18%)</div>
                    <div class="price-agressivo">R$ {preco_18:.2f}</div>
                </div>
                ''', unsafe_allow_html=True)
                
            with col2:
                st.markdown(f'''
                <div class="glass-card" style="box-shadow: 0 10px 30px rgba(0, 201, 255, 0.12);">
                    <div class="label-margin">⚖️ Intermediário (25%)</div>
                    <div class="price-intermediario">R$ {preco_25:.2f}</div>
                </div>
                ''', unsafe_allow_html=True)
                
            with col3:
                st.markdown(f'''
                <div class="glass-card" style="box-shadow: 0 10px 30px rgba(233, 64, 87, 0.12);">
                    <div class="label-margin">💎 Premium (30%)</div>
                    <div class="price-premium">R$ {preco_30:.2f}</div>
                </div>
                ''', unsafe_allow_html=True)
    else:
        st.warning("Por favor, insira um custo da peça válido para calcular.")
