# -*- coding: utf-8 -*-
import streamlit as st
import time
import random
import urllib.parse

# Inicializa o log do diagrama
plantuml_log = [
    "@startuml",
    "' Diagrama de Atividades - Campanha com Influenciadores",
    "start"
]

def registrar(atividade, tipo="acao"):
    if tipo == "acao":
        plantuml_log.append(f":{atividade};")
    elif tipo == "decisao_ini":
        plantuml_log.append(f"if ({atividade}?) then (sim)")
    elif tipo == "decisao_senao":
        plantuml_log.append("else (não)")
    elif tipo == "decisao_fim":
        plantuml_log.append("endif")
    elif tipo == "fork_ini":
        plantuml_log.append("fork")
    elif tipo == "fork_meio":
        plantuml_log.append("fork again")
    elif tipo == "fork_fim":
        plantuml_log.append("end fork")
    elif tipo == "fim":
        plantuml_log.append("stop")
        plantuml_log.append("@enduml")

class Campanha:
    def __init__(self, nome):
        self.nome = nome
        self.kpis = []
        self.influenciadores = []
        self.status = "Inicio"

class Conteudo:
    def __init__(self):
        self.aprovado = False
        self.publicado = False
        self.metricas = {}

def definir_objetivos(c):
    c.kpis = ["Alcance", "Engajamento"]
    c.status = "Objetivos definidos"
    registrar("Definir Objetivos")

def identificar_influencers(c):
    c.influenciadores = random.sample(["A", "B", "C"], 2)
    c.status = "Influencers identificados"
    registrar("Selecionar Influencers")

def negociar(c):
    c.status = "Contrato definido"
    registrar("Negociar Contrato")

def desenvolver():
    registrar("Desenvolver Conteúdo")
    return Conteudo()

def decisao_aprovar(conteudo, aprovou):
    registrar("Conteúdo Aprovado?", "decisao_ini")
    if aprovou:
        conteudo.aprovado = True
        return True
    else:
        registrar("", "decisao_senao")
        return False

def revisar(conteudo):
    registrar("Revisar Conteúdo")
    conteudo.aprovado = True

def publicar(conteudo):
    conteudo.publicado = True
    registrar("Publicar Conteúdo")

def metricas(conteudo):
    registrar("", "fork_ini")
    registrar("Monitorar Alcance")
    conteudo.metricas['alcance'] = random.randint(10000, 50000)
    registrar("", "fork_meio")
    registrar("Gerenciar Comentários")
    conteudo.metricas['comentarios'] = random.randint(100, 1000)
    registrar("", "fork_fim")

def consolidar():
    registrar("Analisar Resultados")

def relatorio():
    registrar("Gerar Relatório")
    registrar("", "fim")

# --- INTERFACE STREAMLIT ---

st.title("📊 Diagrama de Atividades UML - Campanha de Marketing")

if st.button("Executar Processo"):
    campanha = Campanha("Campanha 2025")
    definir_objetivos(campanha)
    identificar_influencers(campanha)
    negociar(campanha)
    conteudo = desenvolver()

    aprovou = st.radio("O influenciador aprovou o conteúdo?", ("Sim", "Não"))
    aprovado_bool = aprovou == "Sim"

    if decisao_aprovar(conteudo, aprovado_bool):
        registrar("", "decisao_fim")
        publicar(conteudo)
        metricas(conteudo)
        consolidar()
        relatorio()
    else:
        revisar(conteudo)
        registrar("", "decisao_fim")
        publicar(conteudo)
        metricas(conteudo)
        consolidar()
        relatorio()

    plantuml_code = "\n".join(plantuml_log)
    encoded = urllib.parse.quote(plantuml_code.encode("utf-8"))
    plantuml_url = f"https://www.plantuml.com/plantuml/png/~h{encoded}"

    st.subheader("📈 Diagrama Gerado")
    st.image(plantuml_url, caption="Diagrama de Atividades Gerado", use_container_width=True)
    st.download_button("📥 Baixar código PlantUML", plantuml_code, file_name="diagrama.puml")

    st.code(plantuml_code, language='text')
