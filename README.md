# TasteFinder

**Your Intelligent Restaurant Recommender.**  
Um projeto completo de ciência de dados, utilizando técnicas modernas de coleta, análise, modelagem e deploy de dados relacionados a restaurantes.

---

## 🚀 Visão Geral

TasteFinder é um sistema de recomendação de restaurantes baseado em:
- Avaliações de usuários
- Tipo de cozinha
- Localização
- Faixa de preço
- Análise de sentimentos (futuro)

### Pipeline do Projeto
- Extração de dados via Web Scraping
- Armazenamento em banco de dados PostgreSQL
- Processos de ETL (Extração, Transformação e Carga)
- Análise Exploratória de Dados (EDA)
- Treinamento de modelo de Machine Learning
- Deploy do modelo por meio de API
- Interface web via GitHub PagesO sistema inclui coleta de dados, armazenamento em banco de dados SQL, processo ETL, análise exploratória, machine learning, API REST e Frontend.

---

## 🏗️ Estrutura do Projeto
* `README.md`: Este arquivo contém a descrição geral do seu projeto, instruções de uso, etc.
* `environment.yml`: Arquivo que lista as dependências do seu projeto para criar um ambiente Conda.
* `data/`: Diretório para armazenar os dados.
    * `raw/`: Contém os dados brutos, sem processamento.
    * `processed/`: Armazena os dados após o processamento e preparação.
* `notebooks/`: Contém notebooks Jupyter para exploração de dados (EDA) e modelagem.
    * `01_eda.ipynb`: Notebook para realizar a análise exploratória dos dados.
    * `02_modeling.ipynb`: Notebook para desenvolver e avaliar modelos.
* `src/`: Código fonte do seu projeto, organizado por funcionalidades.
    * `data/`: Módulos relacionados à manipulação de dados.
    * `features/`: Módulos para engenharia de features.
    * `models/`: Módulos para definir e treinar modelos de machine learning.
    * `visualization/`: Módulos para gerar visualizações.
* `app/`: Código da sua aplicação web ou interface de usuário.
    * `main.py`: Ponto de entrada da aplicação.
    * `model/`: Arquivos relacionados ao modelo utilizado na aplicação.
    * `static/`: Arquivos estáticos como CSS, JavaScript e imagens.
* `docker/`: Arquivos relacionados à configuração do Docker para conteinerização.
    * `docker-compose.yml`: Arquivo para definir e gerenciar múltiplos containers Docker.
    * `Dockerfile`: Arquivo com as instruções para construir a imagem Docker.
* `.gitignore`: Especifica arquivos e diretórios que o Git deve ignorar.
* `LICENSE`: Arquivo contendo a licença do seu projeto.

---

## 📚 Tecnologias Utilizadas

- Python 3.10
- Conda
- PostgreSQL
- SQLAlchemy
- Flask
- HTML5, CSS3, JavaScript
- BeautifulSoup / Selenium
- scikit-learn
- pandas, numpy, matplotlib, seaborn
- Docker
- GitHub Pages

---

## ⚙️ Configuração do Ambiente

Clone o repositório e configure o ambiente:

```bash
git clone https://github.com/seu-usuario/tastefinder.git
cd tastefinder
conda env create -f environment.yml
conda activate tastefinder
```

---

## 📈 Status do Projeto

- [x] Estrutura de diretórios criada
- [x] Configuração do ambiente Conda
- [ ] Banco de dados PostgreSQL inicializado via Docker
- [ ] Script de web scraping implementado
- [ ] Processo ETL estruturado
- [ ] Análise Exploratória de Dados (EDA) realizada
- [ ] Modelo de Machine Learning treinado
- [ ] API de recomendação criada (Flask ou FastAPI)
- [ ] Frontend (GitHub Pages) conectado ao backend
- [ ] Documentação finalizada

---

## 📄 Licença

Este projeto está licenciado sob a MIT License.

---

## 🤝 Como Contribuir

Contribuições são bem-vindas!  
Para mudanças significativas, abra uma *Issue* para discussão antes de abrir o *Pull Request*.

### Passos para contribuir:

1. Faça um Fork do projeto

2. Crie uma Branch  
   ```bash
   git checkout -b feature/NovaFuncionalidade
   ```

3. Commit suas mudanças
   ```bash
    git commit -m 'feature: Adiciona NovaFuncionalidade'
   ```

4. Push para a Branch
    ```bash
    git push origin feature/NovaFuncionalidade
    ```
