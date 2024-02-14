from database_util import DatabaseUtil
from repository.base_respository import (
    UserStatusRepository, 
    WorkTimeRepository, 
    OperationRateRepository, 
    ProductionRateRepository, 
    ProductionContextRepository, 
    ErrorContextRepository, 
    SaleContextRepository
)

def main():
    # 데이터베이스 초기화
    DatabaseUtil.initialize('sqlite:///example.db', echo=True)
    
    # 각 모델별로 리포지토리 인스턴스 생성
    userStatusRepository = UserStatusRepository()
    work_time_repo = WorkTimeRepository()
    
    # 데이터 추가 예제
    user_status = userStatusRepository.save(first="Yes", second="No", midnight="No", absent="Yes", training="No", etc="Yes", rest="No", early="Yes")
    work_time = work_time_repo.save(unit_number=123, normal="8 hours", overtime="2 hours")
    # 나머지 모델에 대해서도 비슷한 방식으로 데이터를 추가할 수 있습니다.
    
    # 데이터 조회 예제
    # 오늘 날짜에 해당하는 UserStatus 데이터 조회
    user_statuses_today = userStatusRepository.findByDate()
    print("Today's User Statuses:")
    for status in user_statuses_today:
        print(status)
    
    # WorkTime 데이터 조회
    work_times_today = work_time_repo.findByDate()
    print("Today's Work Times:")
    for work_time in work_times_today:
        print(work_time)
    
    # 나머지 모델에 대해서도 비슷한 방식으로 데이터를 조회할 수 있습니다.

if __name__ == "__main__":
    main()
