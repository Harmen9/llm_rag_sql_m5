import os
import json
from pathlib import Path

from dotenv import load_dotenv
from langchain_openai import OpenAI

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

load_dotenv()

OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
API_ENDPOINT: str  = os.getenv("API_ENDPOINT ")

base_path: Path = Path(__file__).parent
config_path: Path = base_path / 'config.json'

with open(config_path, encoding="utf-8") as f:
    config: dict = json.load(f)
    conf_db: dict = config['db']

conn_str: str = f"postgresql+psycopg2://{conf_db['username']}:{conf_db['password']}@{conf_db['host']}/{conf_db['database']}"
db = SQLDatabase.from_uri(
    conn_str,
    schema=conf_db['schema'],
    include_tables=[
        "calendar",
        "sales",
        "sell_price"

    ],  # we include only one table to save tokens in the prompt :)
    sample_rows_in_table_info=3
    )


llm = OpenAI(
    openai_api_key=OPENAI_API_KEY,
    model=config['model']['name'],
    temperature=config['model']['temperature']
    )

db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

db_chain.run("How many locations are there with more than 20 distinct products?")
