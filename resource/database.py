from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from resource.db_env import user, password, host, db_name


db_url = f"mysql+pymysql://{user}:{password}@{host}:3306/{db_name}"
# engine = create_engine(db_url, connect_args={'check_same_thread': False})
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()