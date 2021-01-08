# school_api


CRUD
- Student;
- Teacher;
- School;
- Book image;
---

Rules:
- One student has one teacher and one school;
- One student can have many book images;
- One teacher belongs to one school;
---

_*:
- [FastAPI](https://fastapi.tiangolo.com/);
- [Docker](https://docs.docker.com/);
- [Pyrebase4](https://github.com/nhorvath/Pyrebase4);
- [Firebase](https://firebase.google.com/docs);
---

## Instructions

Build image and run the tests:

```
$ docker-compose up -d --build
$ docker-compose exec web pytest
```
---

Test out the following routes:

1. http://localhost:8002/students
2. http://localhost:8002/teachers
3. http://localhost:8002/schools
4. http://localhost:8002/docs