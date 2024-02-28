# django-back-youtube

<details>
<summary>REST API</summary>

<details>
<summary>(1) 모델 구조</summary>


1. Users (Custom)

- email
- password
- nickname
- is_business(boolean): personal, business

2. Videos

- title
- link
- description
- category
- views_count
- thumbnail
- video_uploaded_url (S3)
- video_file(FileField)
- User:FK

3. Like/Dislike

- User:FK
- Video:FK
  Video:Like/Dislike (1:N)

4. Comments

- User:FK
- Video:FK
- like
- dislike
- content

5. Subcriptions (채널 구독)

- User:FK => subscriber (구독한) -> 내가 구독한 사람
- User:FK => subscribed_to (구독을 당한) -> 나를 구독한 사람

6. Notifications

- User:FK
- message
- is_read

7. Common

- created_at
- updated_at

8. Chatting (예정)

- User:FK (nickname)

</details>

</details>

## problem

- ### git hub actions
    - #### lint
        Error: Process completed with exit code 127.

## Solved

- [lint](#lint)
    - ./Dockersfile line 19  
    [$DEV="true"] => [ $DEV="true" ]  
    add whitespace