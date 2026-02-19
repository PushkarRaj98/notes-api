from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from database import conn, cursor


app = FastAPI()

# for HTML
templates = Jinja2Templates(directory="templates")

# for CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# temporary storage
notes = []
notes_id =1

@app.get("/")
def home(request: Request):
    cursor.execute("SELECT * FROM notes")
    data = cursor.fetchall()

    return templates.TemplateResponse("index.html", {
        "request": request,
        "notes": data
    })


@app.post("/add")
def add_note(note: str = Form(...)):
    cursor.execute("INSERT INTO notes (text) VALUES (?)", (note,))
    conn.commit()

    return RedirectResponse(url="/", status_code=303)



@app.post("/delete/{id}")
def delete_note(id: int):
    cursor.execute("DELETE FROM notes WHERE id = ?", (id,))
    conn.commit()

    return RedirectResponse(url="/", status_code=303)
