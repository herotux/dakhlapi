from fastapi import FastAPI
from app.api import (
    users, persons, incomes, expenses, tags, budgets, categories, accounts, debts, credits, installments, auth
)
from app.database import engine, Base

# ایجاد جداول دیتابیس
Base.metadata.create_all(bind=engine)

app = FastAPI()

# اضافه کردن مسیرها
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(persons.router)
app.include_router(incomes.router)
app.include_router(expenses.router)
app.include_router(tags.router)
app.include_router(budgets.router)
app.include_router(categories.router)
app.include_router(accounts.router)
app.include_router(debts.router)
app.include_router(credits.router)
app.include_router(installments.router)
