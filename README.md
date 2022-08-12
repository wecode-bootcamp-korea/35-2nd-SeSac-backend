# PROJECT: 싱그러운 우리 (by SeSAC)
## 소개
- [싱그러운 집](https://www.shouse.garden/main/main.html)을 모티브로 한 사이트
- 자연과 식물에 관한 여행지를 포스팅, 공유하는 커뮤니티 사이트

## SeSAC 팀 인원
- BE(2명): 김동규, 박서윤
- FE(4명): 김영수, 박성은, 손민지, 이금관
<img width="700px" src="https://user-images.githubusercontent.com/91110192/184283372-ca6c21ff-6cd2-4449-91aa-a40dc203f012.jpg">

## 개발 기간
- 개발 기간 : 2022-08-01 ~ 2022-08-12 (12일)
- 협업 툴 : Slack, Trello, Github, Notion

## 기술 스택
|                                                Language                                                |                                                Framwork                                                |                                               Database                                               |                                                     ENV                                                      |                                                   HTTP                                                   |                                                  Deploy                                                 |
| :----------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------: |:------------------------------------------------------------------------------------------------------: |
| <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> | <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> | <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=black"> | <img src="https://img.shields.io/badge/miniconda3-44A833?style=for-the-badge&logo=anaconda&logoColor=white"> | <img src="https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white"> | <img src="https://img.shields.io/badge/aws-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white"> 


## Backend 역할
**박서윤**
- ERD 모델링
- 여행지 리스트
  - (GET) 여행지 리스트 조회
    - Q객체를 이용한 필터링, 페이지네이션 구현
- 여행지 상세
  - (POST) 여행지 게시물 등록
    - s3를 이용하여 이미지 업로드
  - (GET) 여행지 게시물 상세 조회
  - (DELETE) 여행지 게시물 삭제
    - s3를 이용하여 이미지 삭제

**김동규**
- ERD 모델링
- 소셜 로그인
  - 카카오 API 로그인 구현
- 여행지 상세 댓글
  - (GET) 댓글 조회, 로그인한 이용자의 댓글에 `수정`, `삭제`버튼 활성화
  - (POST) 댓글 작성
  - (PATCH) 댓글 수정
  - (DELETE) 댓글 삭제
 
## 모델링
<img width="1400px" src="https://user-images.githubusercontent.com/91110192/184282825-6ca9b57b-20a5-4a4b-9490-4d6fb9989d07.png">

## 사이트 시현 영상
[싱그러운 집 시현영상](https://www.youtube.com/watch?v=ayGvLwikPxk)

### 메인
<img src="https://user-images.githubusercontent.com/104430030/184285325-a0b7a399-1acd-4291-939e-822bf55ee7c2.GIF">

### 소셜 로그인 및 로그아웃
<img src="https://user-images.githubusercontent.com/104430030/184285340-ee5e048f-7c4b-4b57-9593-2896b547785e.GIF">
<img src="https://user-images.githubusercontent.com/104430030/184287240-f172a994-ea8e-461b-9098-db83d5e843e5.GIF">

### 게시물 리스트
<img src="https://user-images.githubusercontent.com/104430030/184285717-1153760c-cf3e-4077-893f-bd4cbb9aa548.GIF"><img src="https://user-images.githubusercontent.com/104430030/184285725-4c81c58e-d5db-4789-97e5-640f5a461dbc.GIF">

### 게시물 포스팅
<img src="https://user-images.githubusercontent.com/104430030/184286796-d27b30a6-fa53-435b-adb5-8118400a72ef.GIF"><img src="https://user-images.githubusercontent.com/104430030/184286846-0a524f00-b19d-41e9-949c-28c496a108b0.GIF">

### 게시물 상세
<img src="https://user-images.githubusercontent.com/104430030/184287166-e906db31-38ad-4c31-9977-bc0cfc8a0e98.GIF"><img src="https://user-images.githubusercontent.com/104430030/184287193-25fc5f1c-1521-4736-aea3-ae1d14cb6e4c.GIF"><img src="https://user-images.githubusercontent.com/104430030/184287120-328c6e8b-2a82-4413-a752-6daf8a689056.GIF"><img src="https://user-images.githubusercontent.com/104430030/184287124-347473db-a34e-4cd6-af8a-72b9a3a44540.GIF">

## API 명세서
<img width="789" alt="스크린샷 2022-07-30 오후 3 33 59" src="https://user-images.githubusercontent.com/91110192/184284788-c9657496-28e3-4027-bccf-9ebd0ef858ed.png">
<img width="789" alt="스크린샷 2022-07-30 오후 3 33 51" src="https://user-images.githubusercontent.com/91110192/184284793-e3f193f4-8718-47ac-9a0f-00da5e949f10.png">

* [싱그러운 우리 API](https://pastoral-slice-3c4.notion.site/API-553343a65d5c49c1bdf2024745ce39c9)를 보시면, 자세한 API를 확인 가능합니다.

## 참고
- 이 프로젝트는 [싱그러운 집](https://www.shouse.garden/main/main.html) 사이트를 참조하여 학습 목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
