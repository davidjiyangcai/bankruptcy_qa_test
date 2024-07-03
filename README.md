# bankruptcy_qa_test

Exploratory Code in code_explore

More Mature Code in code_dev
01_save_index.ipynb save the vector database for each case

Things to do:
1. setting up a script for index creation seperately - done
2. find a way to make llm outputs to conform to a specific format
        To do this, for each question we set up an output class which is a pydantic model
3. define a evaluation scheme for accuracy


## docs/internal

- [Development Environment Setup]
  - [Virtual environment](docs/internal/development_environment.md#virtual-environment)
    - [Setting up the virtual environment (one-time)](docs/internal/development_environment.md#setting-up-the-virtual-environment-one-time)
    - [Activating the virtual environment](docs/internal/development_environment.md#activating-the-virtual-environment)
    - [Updating the virtual environment](docs/internal/development_environment.md#updating-the-virtual-environment)

## Project Layout

rag-app/
│
├── data/                # For storing PDF documents or any other data files
├── src/                 # Source code
│   ├── __init__.py
│   ├── extract.py       # Script for text and metadata extraction
│   ├── embed.py         # Script for embedding generation
│   ├── index.py         # Script for indexing embeddings
│   ├── query.py         # Script for handling queries
│   └── app.py           # Main application script
├── notebooks/           # Jupyter notebooks for experimentation
├── requirements.txt     # Dependencies
└── README.md


* SmettersToolbox
  * .vscode/
  * .venv/             # The virtual environment, in gitignore, only local
  * docs/              # For external and internal documents
    * help/
    * internal/
  * data/              # The cases, each case folder with 4 PDF files
    * Endo International Plc/
      * Endo International Objection to Confirmation of Amended Plan.pdf
      * Endo International plc, Petition.pdf
      * Endo International Third Amended Disclosure Statement.pdf
      * Endo_International_plc__Docket.pdf
    * . . .
  * src/
    * __init__.py
    * extract.py       # Script for text and metadata extraction
    * embed.py         # Script for embedding generation
    * index.py         # Script for indexing embeddings
    * query.py         # Script for handling queries
    * app.py           # Main application script
  * tests/
  * notebooks/         # Jupyter notebooks for experimentation
  * .gitignore
  * requirements.txt   # Dependencies
  * README.md

