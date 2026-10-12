from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
app = FastAPI()
templates = Jinja2Templates(directory="templates")
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )
@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return RedirectResponse(url="/products", status_code=303)
@app.get("/products")
def products(request: Request):
    product_list = [
        (1, "Laptop", "A powerful laptop for work and study.", 70000, 2),
        (2, "iPhone", "A smartphone with advanced features.", 87000, 2),
        (3, "Smart Watch", "Track your activities and notifications.", 5000, 2),
        (4, "Headphones", "Enjoy clear sound and music.", 2500, 2),
    ]
    return templates.TemplateResponse(
        request=request,
        name="product.html",
        context={"products": product_list}
    )
@app.get("/logout")
def logout():
    return RedirectResponse(url="/", status_code=303)