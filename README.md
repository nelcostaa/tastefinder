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

tastefinder/ ├── README.md ├── environment.yml ├── data/ │ ├── raw/ │ └── processed/ ├── notebooks/ │ ├── 01_eda.ipynb │ └── 02_modeling.ipynb ├── src/ │ ├── data/ │ ├── features/ │ ├── models/ │ └── visualization/ ├── app/ │ ├── main.py │ ├── model/ │ └── static/ ├── docker/ │ ├── docker-compose.yml │ └── Dockerfile ├── .gitignore └── LICENSE-

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
- [ ] Configuração do ambiente Conda
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
