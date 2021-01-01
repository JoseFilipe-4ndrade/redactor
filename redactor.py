#Bibliotecas
import streamlit as st
#import os

#NLP, em português spacy.load('pt_core_news_sm') PER, ORG, LOC
import spacy
from spacy import displacy
nlp = spacy.load('pt_core_news_sm')

#Templates
HTML_WRAPPER = """<div style="overflow-x: auto; border: lpx solid #e6e9ef; border-radius: 0.25rem; padding: lrem">{}</div>"""

# Função para filtrar e redigir
def sanitize_nomes(text):
    docx = nlp(text)
    redacted_sentences = []
    for ent in docx.ents:
        ent.merge()
    for token in docx:
        if token.ent_type_ == 'PER':
            redacted_sentences.append("[NOME] ")
        else:
            redacted_sentences.append(token.string)
    return "".join(redacted_sentences)

# Função para filtrar e redigir
def sanitize_locais(text):
    docx = nlp(text)
    redacted_sentences = []
    for ent in docx.ents:
        ent.merge()
    for token in docx:
        if token.ent_type_ == 'LOC':
            redacted_sentences.append("[LUGAR] ")
        else:
            redacted_sentences.append(token.string)
    return "".join(redacted_sentences)

# Função para filtrar e redigir
def sanitize_org(text):
    docx = nlp(text)
    redacted_sentences = []
    for ent in docx.ents:
        ent.merge()
    for token in docx:
        if token.ent_type_ == 'ORG':
            redacted_sentences.append("[ORGANIZAÇÃO] ")
        else:
            redacted_sentences.append(token.string)
    return "".join(redacted_sentences)

#Função para destacar as entidades

def render_entities(rawtext):
    docx = nlp(rawtext)
    html = displacy.render(docx, style = "ent")
    html = html.replace("\n\n","\n")
    result = HTML_WRAPPER.format(html)
    return result
                 

def main():
    """ App de edição de documentos"""
    st.title("Identificando Entidades")
    st.markdown("Aplicativo que utiliza _Machine Learning_ supervisionada para identificar entidades da língua portuguesa. Construído em python com o uso das bibliotecas: *Streamlit* e *Spacy*. ")
    
    
    st.sidebar.header("Menu")

    activities = ["Aplicativo","Sobre"]

    choice = st.sidebar.selectbox("Select a opção",activities)

    if choice == "Aplicativo":
        st.subheader("Escrita dos termos")
        st.markdown("Abaixo tente adicionar texto com nome de pessoas, lugares e organizações.")
        rawtext = st.text_area("Insira o Texto:","Digite Aqui")
        redaction_item = ["Nomes","Lugares","Organizações"]
        redaction_choice = st.selectbox("Selecione o termo para destacar", redaction_item)
        
        if st.button("Enviar"):
            if redaction_choice == "Nomes":
                result = sanitize_nomes(rawtext)
            elif redaction_choice == "Lugares":
                result = sanitize_locais(rawtext)
            elif redaction_choice == "Organizações":
                result = sanitize_org(rawtext)

            st.subheader("Análise Geral")
            st.write(render_entities(rawtext), unsafe_allow_html=True)
            st.text("Legenda: PER: Nome; LOC: Lugar; ORG: Organização.")

            
            st.subheader("Análise Selecionada")
            st.write(result)
            

    elif choice == "Sobre":
        st.subheader("Sobre")
        st.markdown("**Autor:** José Filipe S de Andrade")
        st.markdown("**Aplicativo baseado em:**"'[ Canal J-sec](https://www.youtube.com/watch?v=y1UNZZwB5FA&list=PLJ39kWiJXSixyRMcn3lrbv8xI8ZZoYNZU&index=12)',False)
        st.markdown("**Repositório: **""[Github](https://github.com/JoseFilipe-4ndrade/redactor)",False)
    
if __name__ == '__main__':
    main()
