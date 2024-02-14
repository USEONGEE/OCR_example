from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from models import Base  # 모델 파일에서 Base 임포트

class DatabaseUtil:
  _engine = None
  _session_factory = None
  _scoped_session = None

  @classmethod
  def initialize(cls, db_url, echo=False):
    if cls._engine is None:
      cls._engine = create_engine(db_url, echo=echo)
      cls._session_factory = sessionmaker(bind=cls._engine)
      cls._scoped_session = scoped_session(cls._session_factory)
      
      # 모든 테이블을 데이터베이스에 생성합니다.
      Base.metadata.create_all(cls._engine)

  @classmethod
  def get_session(cls):
    return cls._scoped_session()

  @classmethod
  def close_session(cls):
    cls._scoped_session.remove()
    
  @classmethod
  def clear_all_data(cls):
    """데이터베이스의 모든 테이블에서 모든 데이터를 삭제합니다."""
    session = cls.get_session()
    for table in reversed(Base.metadata.sorted_tables):
      session.execute(table.delete())
    session.commit()
