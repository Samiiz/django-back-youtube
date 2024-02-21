# django-back-youtube

## problem

- ### git hub actions
    - #### lint - Error: Process completed with exit code 127.

## Solved

- [lint](#lint---error-process-completed-with-exit-code-127)
    - ./Dockersfile line 19  
    [$DEV="true"] => [ $DEV="true" ]  
    add whitespace