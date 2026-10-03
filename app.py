"""
Guia Turístico Pro - Aplicação de Aprendizagem e Treino Profissional
Trilingue: Português Técnico, English, Español
Baseado no Programa Oficial de Formação para Guias de Turismo
"""

import streamlit as st
import pandas as pd
import json
import random
import os

# Import data modules
from data.syllabus_content import MODULES_SYLLABUS, BIBLIOGRAPHY_DATA
from data.glossary import GLOSSARY_DATA
from data.quizzes import QUIZ_QUESTIONS
from data.scenarios import GUIDING_SCENARIOS
from utils.speech import play_audio_button, get_audio_file

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Guia Turístico Pro | Formação & Aprendizagem Trilingue",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS STYLING ---
st.markdown("""
<style>
    :root {
        --primary: #1e3a8a;
        --secondary: #0284c7;
        --accent: #d97706;
        --bg-light: #f8fafc;
        --card-bg: #ffffff;
        --text-main: #0f172a;
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #0369a1 100%);
        color: white;
        padding: 2.2rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.25);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        margin-bottom: 0.5rem;
        color: #ffffff !important;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        color: #cbd5e1;
        max-width: 900px;
        line-height: 1.6;
    }
    
    .feature-card {
        background-color: var(--card-bg);
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    
    .module-pill {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }
    
    .pill-blue { background-color: #dbeafe; color: #1e40af; }
    .pill-amber { background-color: #fef3c7; color: #92400e; }
    .pill-emerald { background-color: #d1fae5; color: #065f46; }
    
    .lang-badge {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 6px;
    }
    .lang-pt { background-color: #e0f2fe; color: #0369a1; }
    .lang-en { background-color: #fef2f2; color: #b91c1c; }
    .lang-es { background-color: #fefce8; color: #a16207; }
    
    .flashcard {
        background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
        border: 2px solid #3b82f6;
        border-radius: 16px;
        padding: 2rem;
        min-height: 220px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        box-shadow: 0 10px 20px rgba(59, 130, 246, 0.12);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "flashcard_idx" not in st.session_state:
    st.session_state.flashcard_idx = 0
if "flashcard_show_answer" not in st.session_state:
    st.session_state.flashcard_show_answer = False
if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    belem_img_path = os.path.join(os.path.dirname(__file__), "assets", "torre_de_belem.png")
    if os.path.exists(belem_img_path):
        st.image(belem_img_path, caption="Torre de Belém, Lisboa", use_container_width=True)
    else:
        st.image("https://images.unsplash.com/photo-1588614959060-4d144f28b207?w=600&auto=format&fit=crop&q=80", caption="Torre de Belém, Lisboa", use_container_width=True)
    st.title("🧭 Guia Turístico Pro")
    st.caption("Plataforma Trilingue de Formação e Qualificação")
    
    nav_option = st.radio(
        "Navegação Principal:",
        [
            "🏠 Início & Visão Geral",
            "🏰 Monumento em Destaque: Torre de Belém",
            "📖 Módulo 1: General English & Comunicação",
            "🍷 Módulo 2: Gastronomia & Enologia",
            "🏛️ Módulo 3: Arquitetura & Património",
            "🛡️ Módulo 4: Introdução à Heráldica",
            "⏳ Módulo 5: História & Relações UK/Europa",
            "📇 Glossário Técnico Trilingue (Com Áudio)",
            "🃏 Treino com Flashcards",
            "🎯 Quizzes de Avaliação",
            "🎙️ Estúdio de Guiamento & Roleplay",
            "📚 Bibliografia & Referências"
        ]
    )
    
    st.markdown("---")
    st.subheader("🌐 Idiomas de Estudo")
    st.markdown("""
    - 🇵🇹 **PT:** Português Técnico
    - 🇬🇧 **EN:** Professional English
    - 🇪🇸 **ES:** Español Guía Profesional
    """)
    st.info("🔊 **Áudio Nativo:** Todas as frases têm reprodução de áudio integrada com pronúncia em PT, EN e ES.")

# ==========================================
# 1. INÍCIO & VISÃO GERAL
# ==========================================
if nav_option == "🏠 Início & Visão Geral":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">🧭 Guia Turístico Pro — Formação Trilingue</div>
        <div class="hero-subtitle">
            Plataforma pedagógica e prática para formação e qualificação de Guias de Turismo, Intérpretes e Informadores.
            Domine a comunicação profissional, o vocabulário técnico, a gastronomia, a arquitetura, a heráldica e a história em <b>Português</b>, <b>Inglês</b> e <b>Espanhol</b>.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📋 Estrutura Curricular do Programa de Formação")
    st.write("O conteúdo desta aplicação foi desenvolvido em concordância integral com o plano curricular oficial:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container():
            st.markdown("""
            <div class="feature-card">
                <span class="module-pill pill-blue">Módulo 1</span>
                <h3>🗣️ General English & Comunicação</h3>
                <ul>
                    <li><b>1.1 Pronunciation:</b> Projeção vocal, dicção e toponímia comparada com IPA.</li>
                    <li><b>1.2 Grammar:</b> Fórmulas diplomáticas e registo formal de guia.</li>
                    <li><b>1.3 Vocabulary:</b> Gestão de fluxos, segurança e calçada tradicional.</li>
                    <li><b>1.4 Communication Techniques:</b> Storytelling e método L.E.A.R.N.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with st.container():
            st.markdown("""
            <div class="feature-card">
                <span class="module-pill pill-amber">Módulo 2</span>
                <h3>🍷 Gastronomy – Specific Vocabulary</h3>
                <ul>
                    <li><b>2.1 Regional Food & Wine:</b> Vinhos DOC (Douro, Dão, Alentejo, Vinho Verde), fortificados (Ruby vs Tawny).</li>
                    <li><b>2.2 Menu Descriptions:</b> Confeção tradicional (cataplana, bacalhau) e gestão de alergénios.</li>
                    <li><b>2.3 Foreign Influences:</b> Rota das especiarias, Tempura japonês e o chá britânico.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with st.container():
            st.markdown("""
            <div class="feature-card">
                <span class="module-pill pill-emerald">Módulo 3</span>
                <h3>🏛️ Architecture & Areas of Interest</h3>
                <ul>
                    <li><b>3.1 Religious Buildings:</b> Manuelino (Torre de Belém, Jerónimos, Tomar), Gótico e Talha Dourada.</li>
                    <li><b>3.2 Palaces & Public Heritage:</b> Palácio da Pena, Queluz, Mafra e Aquedutos.</li>
                    <li><b>3.3 Museums & Collections:</b> Azulejo, Coches, MNAA e Coleção Gulbenkian.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        with st.container():
            st.markdown("""
            <div class="feature-card">
                <span class="module-pill pill-blue">Módulo 4</span>
                <h3>🛡️ Brief Introduction to Heraldry</h3>
                <ul>
                    <li><b>4.1 Municipal Coats of Arms:</b> Interpretação das Coroas Murais (5 ouro Lisboa, 5 prata Cidades, 4 prata Vilas).</li>
                    <li><b>4.2 Specific Vocabulary:</b> Esmaltes, metais, regra de contraste e as Quinas de Portugal.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
        with st.container():
            st.markdown("""
            <div class="feature-card">
                <span class="module-pill pill-amber">Módulo 5</span>
                <h3>⏳ History of Portugal & European Links</h3>
                <ul>
                    <li><b>5.1 Pre-History to 1128:</b> Fundação de Portugal (1128) vs Conquista Normanda (1066).</li>
                    <li><b>5.2 Monarchy to 1910:</b> Tratado de Windsor (1386), D. Filipa de Lencastre e Wellington.</li>
                    <li><b>5.3 1910 to Present:</b> República, Lisboa na II Guerra Mundial, 25 de Abril e UE.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        with st.container():
            st.markdown("""
            <div class="feature-card">
                <span class="module-pill pill-emerald">Ferramentas de Estudo</span>
                <h3>🧰 Recursos Práticos Integrados</h3>
                <ul>
                    <li>🏰 <b>Especial Torre de Belém:</b> Visita guiada completa, arquitetura e áudio.</li>
                    <li>🔊 <b>Leitor de Áudio Nativo:</b> Ouça a pronúncia de qualquer termo nos 3 idiomas.</li>
                    <li>📇 <b>Glossário Técnico Trilingue:</b> Base de dados pesquisável com frases de aplicação.</li>
                    <li>🃏 <b>Flashcards Interativos:</b> Treino de memorização e tradução no terreno.</li>
                    <li>🎯 <b>Quizzes de Avaliação:</b> Teste com pontuação automática e correções técnicas.</li>
                    <li>🎙️ <b>Estúdio de Guiamento:</b> Roteiros reais prontos com discursos completos.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# MONUMENTO EM DESTAQUE: TORRE DE BELÉM
# ==========================================
elif nav_option == "🏰 Monumento em Destaque: Torre de Belém":
    belem_scen = next(s for s in GUIDING_SCENARIOS if s["id"] == "torre_belem_master")
    
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">🏰 Torre de São Vicente de Belém (UNESCO 1983)</div>
        <div class="hero-subtitle">
            Monumento ícone de Portugal — Visita Guiada Completa, História Militar, Arquitetura Manuelina e Guião de Discurso Trilingue com Áudio.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_img, col_info = st.columns([1, 1])
    with col_img:
        belem_local_img = os.path.join(os.path.dirname(__file__), "assets", "torre_de_belem.png")
        if os.path.exists(belem_local_img):
            st.image(belem_local_img, caption="Torre de Belém (Fotografia Oficial / Estilo Manuelino)", use_container_width=True)
        else:
            st.image("https://images.unsplash.com/photo-1588614959060-4d144f28b207?w=1000&auto=format&fit=crop&q=80", caption="Torre de Belém", use_container_width=True)
    with col_info:
        st.markdown("""
        ### 📋 Ficha Técnica do Monumento
        - **Nome Oficial:** Torre de São Vicente a Par de Belém
        - **Data de Construção:** 1514 – 1519 (Reinado de D. Manuel I)
        - **Arquiteto:** Francisco de Arruda
        - **Classificação:** Património Mundial da Humanidade UNESCO (1983)
        - **Material:** Pedra de Lioz (calcário compacto da região de Lisboa e Sintra)
        - **Função Original:** Fortaleza de artilharia para cruzamento de fogos na foz do Rio Tejo
        - **Elementos Notáveis:** Baluarte com 16 canhoneiras, gárgula do rinoceronte (*Ganda*), guaritas mouriscas, estátua de Nossa Senhora do Bom Sucesso, loggia renascentista e esferas armilares.
        """)
    
    st.markdown("---")
    
    # Historical Context Tabs
    st.subheader("📖 Contexto Histórico e Arquitetónico Trilingue")
    c_tab_pt, c_tab_en, c_tab_es = st.tabs(["🇵🇹 Português Técnico", "🇬🇧 Professional English", "🇪🇸 Español Profesional"])
    
    with c_tab_pt:
        st.markdown(belem_scen["historical_context_pt"])
    with c_tab_en:
        st.markdown(belem_scen["historical_context_en"])
    with c_tab_es:
        st.markdown(belem_scen["historical_context_es"])
        
    st.markdown("---")
    
    # Complete Guided Speech with Audio
    st.subheader("🗣️ Guião de Discurso Profissional de Campo (Com Áudio Integrado)")
    st.write("Pratique a apresentação ao vivo deste monumento diante dos turistas:")
    
    belem_lang_choice = st.radio("Selecione o Idioma do Discurso:", ["🇵🇹 Português Técnico", "🇬🇧 Professional English", "🇪🇸 Español Profesional"], horizontal=True, key="belem_radio")
    belem_lang_key = "pt" if "Português" in belem_lang_choice else ("en" if "English" in belem_lang_choice else "es")
    
    for idx, step in enumerate(belem_scen["scripts"][belem_lang_key]):
        is_guide = "Guia" in step["speaker"] or "Tour Guide" in step["speaker"]
        box_color = "border-left: 5px solid #1e3a8a; background-color: #f8fafc;" if is_guide else "border-left: 5px solid #d97706; background-color: #fffbeb;"
        spk_icon = "🎤" if is_guide else "🙋"
        
        st.markdown(f"""
        <div style="{box_color} padding: 1.2rem; border-radius: 8px; margin-bottom: 0.8rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <b>{spk_icon} {step['speaker']}</b>
                <span style="font-size: 0.8rem; color: #64748b; font-style: italic;">📌 {step['notes']}</span>
            </div>
            <p style="font-size: 1.05rem; margin-top: 8px; line-height: 1.6; color: #1e293b;">
                "{step['text']}"
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        play_audio_button(step['text'], belem_lang_key, f"🔊 Praticar Áudio ({belem_lang_key.upper()})", f"belem_aud_{belem_lang_key}_{idx}")
        st.write("")

# ==========================================
# 2. MÓDULOS TEMÁTICOS (1 a 5)
# ==========================================
elif nav_option.startswith("📖 Módulo") or nav_option.startswith("🍷 Módulo") or nav_option.startswith("🏛️ Módulo") or nav_option.startswith("🛡️ Módulo") or nav_option.startswith("⏳ Módulo"):
    
    import importlib
    import data.syllabus_content
    import data.glossary
    importlib.reload(data.syllabus_content)
    importlib.reload(data.glossary)
    from data.syllabus_content import MODULES_SYLLABUS
    from data.glossary import GLOSSARY_DATA
    
    mod_id = int(nav_option.split("Módulo ")[1][0])
    module_data = MODULES_SYLLABUS[mod_id]
    
    st.markdown(f"""
    <div class="hero-banner">
        <div class="hero-title">{module_data['icon']} {module_data['title_pt']}</div>
        <div class="hero-subtitle">
            <b>🇬🇧 English:</b> {module_data['title_en']}<br>
            <b>🇪🇸 Español:</b> {module_data['title_es']}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    topic_tabs = st.tabs([topic["name_pt"] for topic in module_data["topics"]])
    
    for i, topic in enumerate(module_data["topics"]):
        with topic_tabs[i]:
            # --- LANGUAGE SELECTOR ---
            lang_choice = st.radio(
                "🌐 Selecione o Idioma da Lição / Select Lesson Language / Seleccione el Idioma:",
                ["🇵🇹 Português Técnico", "🇬🇧 Professional English", "🇪🇸 Español Profesional"],
                horizontal=True,
                key=f"lang_radio_{mod_id}_{topic['id']}"
            )
            
            if "English" in lang_choice:
                st.subheader(f"🇬🇧 {topic.get('name_en', topic['name_pt'])}")
                st.info(f"💡 **Learning Objective:** {topic.get('summary_en', '')}")
                st.markdown(topic.get("content_en", ""))
            elif "Español" in lang_choice:
                st.subheader(f"🇪🇸 {topic.get('name_es', topic['name_pt'])}")
                st.info(f"💡 **Objetivo de Aprendizaje:** {topic.get('summary_es', '')}")
                st.markdown(topic.get("content_es", ""))
            else:
                st.subheader(f"🇵🇹 {topic.get('name_pt', '')}")
                st.info(f"💡 **Objetivo:** {topic.get('summary_pt', '')}")
                st.markdown(topic.get("content_pt", ""))
            
            st.markdown("---")
            st.subheader("🔊 Vocabulário & Frases de Exemplo com Áudio")
            
            related_terms = [t for t in GLOSSARY_DATA if t["module"] == mod_id]
            if related_terms:
                for idx, term in enumerate(related_terms):
                    with st.expander(f"🔹 {term['pt']} | {term['en']} | {term['es']}"):
                        c1, c2, c3 = st.columns(3)
                        with c1:
                            st.markdown(f"<span class='lang-badge lang-pt'>🇵🇹 Português Técnico</span>", unsafe_allow_html=True)
                            st.markdown(f"**`{term['pt']}`**")
                            st.caption(f"Fonética: {term.get('phonetic_pt', '')}")
                            st.write(term['context_pt'])
                            st.markdown(f"*Frase:* \"{term['example_pt']}\"")
                            play_audio_button(term['example_pt'], 'pt', '🔊 Ouvir PT', f"mod_{mod_id}_pt_{idx}")
                            
                        with c2:
                            st.markdown(f"<span class='lang-badge lang-en'>🇬🇧 Professional English</span>", unsafe_allow_html=True)
                            st.markdown(f"**`{term['en']}`**")
                            st.caption(f"Phonetics: {term.get('phonetic_en', '')}")
                            st.write(term['context_en'])
                            st.markdown(f"*Example:* \"{term['example_en']}\"")
                            play_audio_button(term['example_en'], 'en', '🔊 Listen EN', f"mod_{mod_id}_en_{idx}")

                        with c3:
                            st.markdown(f"<span class='lang-badge lang-es'>🇪🇸 Español Profesional</span>", unsafe_allow_html=True)
                            st.markdown(f"**`{term['es']}`**")
                            st.caption(f"Fonética: {term.get('phonetic_es', '')}")
                            st.write(term['context_es'])
                            st.markdown(f"*Ejemplo:* \"{term['example_es']}\"")
                            play_audio_button(term['example_es'], 'es', '🔊 Escuchar ES', f"mod_{mod_id}_es_{idx}")

# ==========================================
# 3. GLOSSÁRIO TÉCNICO TRILINGUE
# ==========================================
elif nav_option.startswith("📇 Glossário"):
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">📇 Glossário Técnico Trilingue com Áudio</div>
        <div class="hero-subtitle">
            Vocabulário especializado em Português Técnico, Inglês e Espanhol com leitores de áudio integrados e explicações de terreno.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_search, col_mod = st.columns([3, 2])
    with col_search:
        search_query = st.text_input("🔍 Pesquisar termo ou conceito (PT, EN ou ES):", placeholder="Ex: mural, doc, wine, manuelino, treaty, quinas, crown...")
    with col_mod:
        selected_mod = st.selectbox("Filtrar por Módulo:", ["Todos os Módulos", "Módulo 1: Comunicação & Gestão", "Módulo 2: Gastronomia & Vinhos", "Módulo 3: Arquitetura & Património", "Módulo 4: Heráldica", "Módulo 5: História & Relações UK"])
    
    filtered_data = GLOSSARY_DATA
    if selected_mod != "Todos os Módulos":
        mod_num = int(selected_mod.split("Módulo ")[1][0])
        filtered_data = [t for t in filtered_data if t["module"] == mod_num]
        
    if search_query:
        q = search_query.lower()
        filtered_data = [
            t for t in filtered_data 
            if q in t["pt"].lower() or q in t["en"].lower() or q in t["es"].lower() or q in t["context_pt"].lower() or q in t["example_pt"].lower()
        ]
        
    st.caption(f"Encontrados **{len(filtered_data)}** termos técnicos.")
    
    for idx, term in enumerate(filtered_data):
        with st.container():
            st.markdown(f"""
            <div class="feature-card">
                <span class="module-pill pill-blue">Módulo {term['module']} — {term['category_pt']}</span>
                <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px;">
                    <div>
                        <span class="lang-badge lang-pt">🇵🇹 Português Técnico</span>
                        <h4 style="margin: 6px 0; color: #1e3a8a;">{term['pt']}</h4>
                        <p style="font-size: 0.85rem; color: #64748b;">{term['context_pt']}</p>
                        <p style="font-size: 0.9rem; font-style: italic;">"{term['example_pt']}"</p>
                    </div>
                    <div>
                        <span class="lang-badge lang-en">🇬🇧 Professional English</span>
                        <h4 style="margin: 6px 0; color: #b91c1c;">{term['en']}</h4>
                        <p style="font-size: 0.85rem; color: #64748b;">{term['context_en']}</p>
                        <p style="font-size: 0.9rem; font-style: italic;">"{term['example_en']}"</p>
                    </div>
                    <div>
                        <span class="lang-badge lang-es">🇪🇸 Español Profesional</span>
                        <h4 style="margin: 6px 0; color: #a16207;">{term['es']}</h4>
                        <p style="font-size: 0.85rem; color: #64748b;">{term['context_es']}</p>
                        <p style="font-size: 0.9rem; font-style: italic;">"{term['example_es']}"</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            c_aud1, c_aud2, c_aud3 = st.columns(3)
            with c_aud1:
                st.caption("🇵🇹 Áudio Português:")
                play_audio_button(term['example_pt'], 'pt', '🔊 Ouvir PT', f"gloss_pt_{idx}")
            with c_aud2:
                st.caption("🇬🇧 English Audio:")
                play_audio_button(term['example_en'], 'en', '🔊 Listen EN', f"gloss_en_{idx}")
            with c_aud3:
                st.caption("🇪🇸 Audio Español:")
                play_audio_button(term['example_es'], 'es', '🔊 Escuchar ES', f"gloss_es_{idx}")
            st.markdown("<hr style='margin: 1.5rem 0; border: none; border-top: 1px dashed #cbd5e1;'>", unsafe_allow_html=True)

# ==========================================
# 4. TREINO COM FLASHCARDS
# ==========================================
elif nav_option == "🃏 Treino com Flashcards":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">🃏 Flashcards de Memorização Rápida</div>
        <div class="hero-subtitle">
            Treine a agilidade mental, tradução instantânea e conceitos patrimoniais com suporte de pronúncia áudio.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col_filter, col_mode = st.columns(2)
    with col_filter:
        flash_mod = st.selectbox("Escolha o Módulo para Treino:", ["Todos", "1. Comunicação", "2. Gastronomia", "3. Arquitetura", "4. Heráldica", "5. História"])
    with col_mode:
        flash_target_lang = st.selectbox("Idioma da Pergunta Frontal:", ["Português (Traduza para EN & ES)", "English (Translate to PT & ES)", "Español (Traduzca a PT & EN)"])
        
    flash_items = GLOSSARY_DATA
    if flash_mod != "Todos":
        m_id = int(flash_mod.split(".")[0])
        flash_items = [t for t in flash_items if t["module"] == m_id]
        
    if not flash_items:
        st.warning("Não existem termos disponíveis para este filtro.")
    else:
        if st.session_state.flashcard_idx >= len(flash_items):
            st.session_state.flashcard_idx = 0
            
        current_card = flash_items[st.session_state.flashcard_idx]
        
        st.write(f"Cartão **{st.session_state.flashcard_idx + 1}** de **{len(flash_items)}**")
        
        if not st.session_state.flashcard_show_answer:
            if "Português" in flash_target_lang:
                question_text = current_card['pt']
                q_badge = "🇵🇹 Português Técnico"
                q_context = current_card['context_pt']
                aud_text = current_card['pt']
                aud_lang = 'pt'
            elif "English" in flash_target_lang:
                question_text = current_card['en']
                q_badge = "🇬🇧 Professional English"
                q_context = current_card['context_en']
                aud_text = current_card['en']
                aud_lang = 'en'
            else:
                question_text = current_card['es']
                q_badge = "🇪🇸 Español Profesional"
                q_context = current_card['context_es']
                aud_text = current_card['es']
                aud_lang = 'es'
                
            st.markdown(f"""
            <div class="flashcard">
                <span class="module-pill pill-blue">Módulo {current_card['module']} — {current_card['category_pt']}</span>
                <span class="lang-badge">{q_badge}</span>
                <h2 style="color: #1e3a8a; margin: 15px 0;">{question_text}</h2>
                <p style="color: #64748b; font-size: 1rem; max-width: 600px;">{q_context}</p>
                <p style="color: #94a3b8; font-size: 0.85rem; margin-top: 15px;">👉 Como traduz e apresenta este conceito aos visitantes?</p>
            </div>
            """, unsafe_allow_html=True)
            
            play_audio_button(aud_text, aud_lang, "🔊 Ouvir Termo", f"fc_q_{st.session_state.flashcard_idx}")
            
            if st.button("🔄 Revelar Respostas & Equivalências Trilingues", use_container_width=True, type="primary"):
                st.session_state.flashcard_show_answer = True
                st.rerun()
                
        else:
            st.markdown(f"""
            <div class="flashcard" style="border-color: #16a34a; background: #f0fdf4;">
                <span class="module-pill pill-emerald">Respostas Trilingues & Exemplos</span>
                <div style="text-align: left; width: 100%; margin-top: 15px;">
                    <div style="margin-bottom: 12px;">
                        <span class="lang-badge lang-pt">🇵🇹 PT</span> <b>{current_card['pt']}</b><br>
                        <small style="color: #15803d;">"{current_card['example_pt']}"</small>
                    </div>
                    <div style="margin-bottom: 12px;">
                        <span class="lang-badge lang-en">🇬🇧 EN</span> <b>{current_card['en']}</b><br>
                        <small style="color: #15803d;">"{current_card['example_en']}"</small>
                    </div>
                    <div>
                        <span class="lang-badge lang-es">🇪🇸 ES</span> <b>{current_card['es']}</b><br>
                        <small style="color: #15803d;">"{current_card['example_es']}"</small>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            c_a, c_b, c_c = st.columns(3)
            with c_a:
                st.caption("🇵🇹 Áudio PT:")
                play_audio_button(current_card['example_pt'], 'pt', '🔊 Áudio PT', f"fc_a_pt_{st.session_state.flashcard_idx}")
            with c_b:
                st.caption("🇬🇧 Audio EN:")
                play_audio_button(current_card['example_en'], 'en', '🔊 Audio EN', f"fc_a_en_{st.session_state.flashcard_idx}")
            with c_c:
                st.caption("🇪🇸 Audio ES:")
                play_audio_button(current_card['example_es'], 'es', '🔊 Audio ES', f"fc_a_es_{st.session_state.flashcard_idx}")
                
            col_prev, col_next = st.columns(2)
            with col_prev:
                if st.button("⬅️ Anterior", use_container_width=True):
                    st.session_state.flashcard_idx = (st.session_state.flashcard_idx - 1) % len(flash_items)
                    st.session_state.flashcard_show_answer = False
                    st.rerun()
            with col_next:
                if st.button("➡️ Próximo Cartão", use_container_width=True, type="primary"):
                    st.session_state.flashcard_idx = (st.session_state.flashcard_idx + 1) % len(flash_items)
                    st.session_state.flashcard_show_answer = False
                    st.rerun()

# ==========================================
# 5. QUIZZES DE AVALIAÇÃO
# ==========================================
elif nav_option == "🎯 Quizzes de Avaliação":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">🎯 Teste de Avaliação Oficial de Conhecimentos</div>
        <div class="hero-subtitle">
            Responda às questões técnicas dos 5 módulos do curso de guia turístico. Avalie o seu domínio comunicacional, enológico, arquitetónico, heráldico e histórico.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    quiz_lang = st.radio("Idioma das Perguntas:", ["Português", "English", "Español"], horizontal=True)
    
    with st.form("quiz_form"):
        for q in QUIZ_QUESTIONS:
            st.markdown(f"#### ❓ Questão {q['id']} — Módulo {q['module']} ({q['category']})")
            
            if quiz_lang == "Português":
                q_text = q["question_pt"]
            elif quiz_lang == "English":
                q_text = q["question_en"]
            else:
                q_text = q["question_es"]
                
            st.write(q_text)
            
            selected = st.radio(
                f"Opções para Questão {q['id']}:",
                q["options"],
                key=f"q_{q['id']}",
                index=None
            )
            st.markdown("---")
            
        submitted = st.form_submit_button("🏁 Submeter Exame e Obter Classificação", type="primary", use_container_width=True)
        
    if submitted:
        score = 0
        total = len(QUIZ_QUESTIONS)
        st.session_state.quiz_submitted = True
        
        st.subheader("📊 Resultados do Exame")
        
        for q in QUIZ_QUESTIONS:
            user_choice = st.session_state.get(f"q_{q['id']}")
            correct_opt = q["options"][q["correct_index"]]
            
            if user_choice == correct_opt:
                score += 1
                st.success(f"✅ **Questão {q['id']}: Correto!**")
            else:
                st.error(f"❌ **Questão {q['id']}: Incorreto.** Sua resposta: *{user_choice or 'Sem resposta'}* | Resposta correta: **{correct_opt}**")
                
            if quiz_lang == "Português":
                expl = q["explanation_pt"]
            elif quiz_lang == "English":
                expl = q["explanation_en"]
            else:
                expl = q["explanation_es"]
                
            st.info(f"💡 **Explicação Técnica:** {expl}")
            st.markdown("<br>", unsafe_allow_html=True)
            
        percentage = (score / total) * 100
        st.markdown(f"""
        <div style="background: #1e293b; color: white; padding: 1.5rem; border-radius: 12px; text-align: center; margin-top: 1rem;">
            <h2>Pontuação Final: {score} / {total} ({percentage:.0f}%)</h2>
            <p>{'🏆 Excelente! Está pronto para o exame de certificação profissional de guia turístico.' if percentage >= 80 else '📖 Bom esforço! Reveja os módulos e tente novamente para consolidar.'}</p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# 6. ESTÚDIO DE GUIAMENTO & ROLEPLAY
# ==========================================
elif nav_option == "🎙️ Estúdio de Guiamento & Roleplay":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">🎙️ Estúdio de Guiamento & Roleplay</div>
        <div class="hero-subtitle">
            Simulação de discursos reais em pontos turísticos emblemáticos de Portugal com áudio integrado para treino de pronúncia e ritmo.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    scenario_titles = [s["title_pt"] for s in GUIDING_SCENARIOS]
    selected_scen_title = st.selectbox("Selecione o Roteiro para Simulação:", scenario_titles)
    
    scenario = next(s for s in GUIDING_SCENARIOS if s["title_pt"] == selected_scen_title)
    
    st.markdown(f"**Localização:** 📍 {scenario['location']} | **Conceitos-Chave:** {', '.join(scenario['key_themes'])}")
    
    script_lang = st.radio("Selecione o Idioma do Discurso:", ["🇵🇹 Português Técnico", "🇬🇧 Professional English", "🇪🇸 Español Profesional"], horizontal=True)
    lang_key = "pt" if "Português" in script_lang else ("en" if "English" in script_lang else "es")
    
    st.markdown("---")
    st.subheader("🗣️ Guião de Discurso Profissional Passo a Passo")
    
    for idx, line in enumerate(scenario["scripts"][lang_key]):
        is_guide = "Guia" in line["speaker"] or "Tour Guide" in line["speaker"]
        box_style = "border-left: 5px solid #1e3a8a; background-color: #f8fafc;" if is_guide else "border-left: 5px solid #d97706; background-color: #fffbeb;"
        speaker_icon = "🎤" if is_guide else "🙋"
        
        st.markdown(f"""
        <div style="{box_style} padding: 1.2rem; border-radius: 8px; margin-bottom: 0.8rem;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <b>{speaker_icon} {line['speaker']}</b>
                <span style="font-size: 0.8rem; color: #64748b; font-style: italic;">📌 {line['notes']}</span>
            </div>
            <p style="font-size: 1.05rem; margin-top: 8px; line-height: 1.6; color: #1e293b;">
                "{line['text']}"
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        play_audio_button(line['text'], lang_key, f"🔊 Praticar Áudio ({lang_key.upper()})", f"scen_aud_{lang_key}_{idx}")
        st.write("")

# ==========================================
# 7. BIBLIOGRAFIA & REFERÊNCIAS
# ==========================================
elif nav_option == "📚 Bibliografia & Referências":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">📚 Bibliografia Oficial & Obras de Referência</div>
        <div class="hero-subtitle">
            Fontes historiográficas, guias internacionais e estudos recomendados no plano curricular de formação de guias de turismo.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("📖 Leituras Obrigatórias e Recomendadas")
    
    for book in BIBLIOGRAPHY_DATA:
        st.markdown(f"""
        <div class="feature-card">
            <span class="module-pill pill-amber">{book['category']}</span>
            <h3 style="color: #1e3a8a; margin: 6px 0;">{book['title']}</h3>
            <h5 style="color: #64748b; margin-bottom: 12px;">✍️ Autor(es): <b>{book['author']}</b></h5>
            <p><b>🇵🇹 Resumo:</b> {book['description_pt']}</p>
            <p style="color: #475569;"><b>🇬🇧 Overview:</b> {book['description_en']}</p>
            <p style="color: #64748b;"><b>🇪🇸 Sinopsis:</b> {book['description_es']}</p>
        </div>
        """, unsafe_allow_html=True)
