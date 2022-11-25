## SELECT

- SELECT는 데이터베이스에 있는 테이블에서 정보를 검색하는 역할
- 일반적으로 다른 문법과 결합하여 복잡한 쿼리를 수행

#### 기본적인 SELECT문

1. {table_name} 테이블을 참조하여 {column_name} 열을 검토한다.
> SELECT column_name FROM table_name
2. 여러 컬럼을 검색할 땐 쉼표(,)로 구분한다.
> SELECT c1, c2 FROM table_1
3. 모든 컬럼을 검색할 땐 *를 사용한다.
    - 데이터베이스와 애플리케이션 사이의 트래픽이 증가하여, 검색 속도가 느려질 수 있기 때문에 일반적인 경우엔 사용하지 않는다.
> SELECT * FROM table_1
