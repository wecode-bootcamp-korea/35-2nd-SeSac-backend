# PROJECT: 싱그러운 우리
## 소개
- [싱그러운 집]([https://www.bang-olufsen.com/ko/kr](https://www.shouse.garden/main/main.html)을 모티브로 한 사이트
- 자연과 식물에 관한 여행지를 포스팅, 공유하는 커뮤니티 사이트

## 팀 인원
- BE(2명): 김동규, 박서윤
- FE(4명): 김영수, 박성은, 손민지, 이금관

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
  - GET
- 여행지 상세

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
<img width="1400px" src="">

## 사이트 시현 영상
<img src="https://user-images.githubusercontent.com/91110192/181877787-b8f6c159-017d-4452-aac7-5b4e364c5f67.gif">

## API 명세서
<img width="797" alt="스크린샷 2022-07-30 오후 3 33 59" src="https://user-images.githubusercontent.com/91110192/181878038-25f4d635-4407-4d84-b4f1-fbe2c041096f.png">
<img width="789" alt="스크린샷 2022-07-30 오후 3 33 51" src="https://user-images.githubusercontent.com/91110192/181878041-6ccdd0d4-9a61-4354-9086-7fa46f2e6cf7.png">
<img width="793" alt="스크린샷 2022-07-30 오후 3 33 35" src="https://user-images.githubusercontent.com/91110192/181878044-bf1f17df-6cf4-42ae-9a1e-25c518bbf126.png">
<img width="796" alt="스크린샷 2022-07-30 오후 3 33 21" src="https://user-images.githubusercontent.com/91110192/181878045-98d8a784-5828-43f7-80f9-a6f403c55fba.png">

* [싱그러운 우리 API](https://pastoral-slice-3c4.notion.site/API-553343a65d5c49c1bdf2024745ce39c9)를 보시면, 자세한 API를 확인 가능합니다.

## 참고
- 이 프로젝트는 [싱그러운 집](https://www.shouse.garden/main/main.html) 사이트를 참조하여 학습 목적으로 만들었습니다.
- 실무수준의 프로젝트이지만 학습용으로 만들었기 때문에 이 코드를 활용하여 이득을 취하거나 무단 배포할 경우 법적으로 문제될 수 있습니다.
