from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.forms.models import model_to_dict
from ninja import NinjaAPI, ModelSchema, UploadedFile
from ninja.parser import Parser
from .models import Book
import orjson

class OrJsonParser(Parser):
    def parse_body(self, request: HttpRequest):
        return orjson.loads(request.body)

api = NinjaAPI(parser=OrJsonParser())

@api.get(path='book/')
def listar(request: HttpRequest):
    book = Book.objects.all()
    response = [{'id': i.id,'title': i.title,'description': i.description,'author': i.author} for i in book]
    return response

@api.get(path='book/{id}')
def listBooks(request: HttpRequest, id: int):
    book = get_object_or_404(Book, id=id)
    return model_to_dict(book)

@api.get(path='consultation_book/')
def consultationList(request: HttpRequest, id: int = 1):
    book = get_object_or_404(Book, id=id)
    return model_to_dict(book)

class BookSchema(ModelSchema):
    class Config:
        model = Book
        model_fields = '__all__'
    
# from typing import List
# book: List[BookSchema]

@api.post(path='book', response=BookSchema)
def createBook(request: HttpRequest, book: BookSchema):
    b = book.dict()
    book = Book(**b)
    book.save()
    return book

@api.post(path='/file')
def fileUpload(request: HttpRequest, file: UploadedFile):
    print(file.size)
    return 1

@api.get(path='home/')
def home(request: HttpRequest):
    return render(
        request=request,
        template_name='home.html'
    )