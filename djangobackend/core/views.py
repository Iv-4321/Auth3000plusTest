from rest_framework import viewsets, generics
from .serializers import BookSerializer
    # , BookDetailSerializer
from .models import Book
import json
import requests
import fitz
from django.http import JsonResponse


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def post(self, ):
        pass


# class BookCreateView(generics.CreateAPIView):
#     serializer_class = BookDetailSerializer
#     queryset = Book.objects.all()

    # @classmethod
    # def get_extra_actions(cls):
    #     return []

    # def parserPdf(request):
    #     data = json.loads(request.body.decode())
    #     responce = dict(error=0, message="Message send", success=True)
    #     pdf_document = data.get('pdf')
    #     doc = fitz.open(pdf_document)
    #     print("Исходный документ", doc)
    #     print(doc.metadata)
    #     page_count = 0
    #     for i in range(len(doc)):
    #         for img in doc.getPageImageList(i):
    #             xref = img[0]
    #             pix = fitz.Pixmap(doc, xref)
    #             pix1 = fitz.Pixmap(fitz.csRGB, pix)
    #             page_count += 1
    #             pix1.writePNG("media/picture_number_%s_from_page_%s.png" % (page_count, i + 1))
    #             print("Image number ", page_count, " writed...")
    #             pix1 = None
    #
    #             method = "http://127.0.0.1:8000/api/books/"
    #
    #             r = requests.post(method, data={
    #                 "name": doc.metadata[1],
    #                 "author": doc.metadata[2],
    #                 "picture": pix1,
    #                 "pdf": doc
    #             })
    #
    #             if r.status_code != 200:
    #                 responce['error'] = 5
    #                 responce['message'] = "Возникла ошибка"
    #
    #             return JsonResponse(responce)

# from django.shortcuts import render

# from rest_framework.response import Response

# def messagePost(request):
#     data = json.loads(request.body.decode())
#     responce=dict(error=0, message="Message send", success=True)
#
#     token = "TELEGRAM_TOKEN"
#     url = "https://api.telegram.org/bot"
#     channel_id = "CHAT_ID"
#     url += token
#     method = url + "/sendMessage"
#     text="Имя: \n "+str(data.get('name'))+"\n Email: \n "+str(data.get('email'))+"\n Телефон:\n "+str(data.get('phone'))+"\n Сообщение:\n "+str(data.get('message'))
#
#     r = requests.post(method, data={
#         "name": doc.metadata[1] ,
#         "author": doc.metadata[2],
#         "picture": pix1,
#         "pdf": doc
#           })
#
#     if r.status_code != 200:
#         responce['error'] = 5
#         responce['message']="Возникла ошибка"
#
#     return JsonResponse(responce)
