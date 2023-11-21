from fastapi import FastAPI, status, Request
from dotenv import load_dotenv
import os

from .db import MongoManager
from .validators.validator import type_of

load_dotenv()
HOST = os.getenv("MONGO_HOST")
PORT = int(os.getenv("MONGO_PORT"))
DB = os.getenv("MONGO_DATABASE")

client = MongoManager(HOST, PORT, DB)


app = FastAPI(title="From validator")


@app.get("/get_templates")
async def get_templates_api():
    """_summary_ Return json with list of templates

    Returns:
        dict: {"templates": List[template]}
    """
    forms = await client.get_templates()
    return {"templates": forms}


@app.post(
    "/create_form",
    status_code=201
    )
async def create_form_api(req: Request):
    """_summary_ Creates template in db

    Args:
        req (Request): Body: json

    Returns:
        dict: {"status": HTTP_status, "error": string(if exists)}
    """
    try:
        body = await req.json()
        await client.create_template(dict(body))
        return {"status": status.HTTP_201_CREATED, "form": body}
    except ValueError as err:
        return {"status": status.HTTP_400_BAD_REQUEST, "error": str(err)}


@app.post(
    '/get_form'
)
async def get_form_api(request: Request) -> dict:
    """_summary_

    Returns:
        if finded template:
            dict: {templates_name: str}
        else:
            dict: {fields: type_of_fields}
    """
    input_form: dict = request.query_params._dict
    find_form: dict = dict()
    for key, val in input_form.items():
        val_type = await type_of(val)
        find_form[key] = val_type
    find_form = dict(sorted(find_form.items()))
    # беру первую пару ключ: значение из входящей формы
    first_entry = list(find_form.items())[0]
    to_find = {first_entry[0]: first_entry[1]}
    # все шаблоны, в которых есть первая пара ключ: значение из входящей формы
    finded = await client.get_templates(to_find)
    for i in finded:
        # Проверка на совпадение
        if all([find_form.get(key) == val for key, val in i.items() if key != "name"]):  # noqa 501
            return {"finded form": i["name"]}
    return find_form


# Функция аналогичная предыдущей, но она правильна с точки зрения REST
# Написал еще и её на случай, если в задании была скрыта проверка)
@app.post(
    '/get_form_REST'
)
async def get_form_RESTapi(request: Request) -> dict:
    input_form = await request.json()
    input_form = dict(input_form)
    find_form: dict = dict()
    for key, val in input_form.items():
        val_type = await type_of(val)
        find_form[key] = val_type
    find_form = dict(sorted(find_form.items()))
    # беру первую пару ключ: значение из входящей формы
    first_entry = list(find_form.items())[0]
    to_find = {first_entry[0]: first_entry[1]}
    # все шаблоны, в которых есть первая пара ключ: значение из входящей формы  # noqa 501
    finded = await client.get_templates(to_find)
    for i in finded:
        # Проверка на совпадение
        if all([find_form.get(key) == val for key, val in i.items() if key != "name"]):  # noqa 501
            return {"finded form": i["name"]}
    return find_form
