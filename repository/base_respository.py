from database_util import DatabaseUtil
from datetime import datetime
from models import UserStatus, WorkTime, OperationRate, ProductionContext, ProductionRate, ErrorContext, SaleContext

class BaseRepository:
  def __init__(self, model):
    self.model = model

  def save(self, **kwargs):
    session = DatabaseUtil.get_session()
    instance = self.model(**kwargs)
    session.add(instance)
    session.commit()
    return instance

  def findByDate(self, date=datetime.utcnow().date()):
    session = DatabaseUtil.get_session()
    return session.query(self.model).filter(self.model.date == date).all()

class UserStatusRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserStatus)

class WorkTimeRepository(BaseRepository):
    def __init__(self):
        super().__init__(WorkTime)

class OperationRateRepository(BaseRepository):
    def __init__(self):
        super().__init__(OperationRate)

class ProductionRateRepository(BaseRepository):
    def __init__(self):
        super().__init__(ProductionRate)

class ProductionContextRepository(BaseRepository):
    def __init__(self):
        super().__init__(ProductionContext)

class ErrorContextRepository(BaseRepository):
    def __init__(self):
        super().__init__(ErrorContext)

class SaleContextRepository(BaseRepository):
    def __init__(self):
        super().__init__(SaleContext)
