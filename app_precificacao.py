import streamlit as st
import time

# 1. Configuração inicial da página
st.set_page_config(page_title="Calculadora Otto", page_icon="🛒", layout="centered")

# --- INJEÇÃO DE CSS (MOTION DESIGN E GLASSMORPHISM) ---
st.markdown("""
<style>
    /* Fundo escuro premium */
    .stApp {
        background-color: #0A0A0B;
    }
    
    /* Efeito de Gradiente no Título (Cores quentes puxando para e-commerce/Shopee) */
    .titulo-glow {
        font-size: 3.2rem;
        font-weight: 900;
        background: linear-gradient(90deg, #F58529 0%, #FEDA75 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        animation: fadeInDown 0.8s ease-out;
        margin-bottom: 5px;
    }
    
    .subtitulo {
        text-align: center;
        color: #A0AEC0;
        font-size: 1.1rem;
        margin-bottom: 40px;
        animation: fadeInDown 1s ease-out;
    }

    /* Cards de Vidro (Glassmorphism) para os resultados */
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

    /* Estilos de Tipografia dos Preços */
    .label-margin { font-size: 1rem; color: #A0AEC0; margin-bottom: 10px; font-weight: 600; }
    
    .price-agressivo { background: linear-gradient(90deg, #FF416C 0%, #FF4B2B 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.2rem; font-weight: 800; }
    .price-intermediario { background: linear-gradient(90deg, #00C9FF 0%, #92FE9D 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.2rem; font-weight: 800; }
    .price-premium { background: linear-gradient(90deg, #8A2387 0%, #E94057 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 2.2rem; font-weight: 800; }

    /* Animações de entrada */
    @keyframes fadeInDown { from { opacity: 0; transform: translateY(-30px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }
    
    /* Ocultar menus do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
# --- FIM DO CSS ---

# Interface Visual (Cabeçalho)
st.markdown('<p class="titulo-glow">Calculadora Otto 🛒</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">Preços blindados para máxima lucratividade.</p>', unsafe_allow_html=True)

# Campo de digitação customizado
custo = st.number_input("Custo Total do Produto - R$", min_value=0.0, step=1.0, format="%.2f")

# Botão de ação
if st.button("Gerar Preços Inteligentes 🚀", use_container_width=True):
    if custo > 0:
        with st.spinner("Calculando taxas, impostos e margens cruzadas..."):
            time.sleep(0.6) # Adiciona um pequeno delay de meio segundo apenas para a barra de carregamento ser vista (dá sensação de processamento complexo)
            
            preco_teste = custo
            preco_18 = 0
            preco_25 = 0
            preco_30 = 0

            # O seu motor matemático original (intacto e super rápido)
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

            st.divider()
            st.markdown('<p style="text-align: center; color: #E2E8F0; font-size: 1.3rem; font-weight: 600; margin-bottom: 25px;">Sugestões de Preço Final</p>', unsafe_allow_html=True)
            
            # Divide a tela em 3 colunas e injeta os Cards de Vidro customizados em cada uma
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
