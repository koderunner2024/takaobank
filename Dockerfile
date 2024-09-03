# 베이스 이미지로 Python 3.9 사용
FROM python:3.9-slim

# 컨테이너 내 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 업데이트 및 필요한 의존성 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 파이썬 패키지 관리자(pip) 최신 버전으로 업그레이드
RUN pip install --upgrade pip

# 로컬의 requirements.txt 파일을 컨테이너로 복사
COPY requirements.txt .

# 필요한 파이썬 패키지 설치
RUN pip install -r requirements.txt

# 로컬의 모든 소스 코드 파일을 컨테이너로 복사
COPY . .

# Django 관리 명령어를 실행하여 마이그레이션 적용
RUN python manage.py migrate

# Django 개발 서버 실행 (포트 8000에서)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
