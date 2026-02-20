"""
How to run the microservices demo:

1) Terminal A:
   uvicorn user_service:app --reload --port 8001

2) Terminal B:
   uvicorn order_service:app --reload --port 8002

3) Terminal C:
   uvicorn gateway:app --reload --port 8000

Test:
- POST http://127.0.0.1:8000/users
  body: {"email":"a@b.com","name":"Tina"}

- POST http://127.0.0.1:8000/orders
  body: {"user_id":"<ID_FROM_CREATE_USER>","item":"book","qty":2}
"""
