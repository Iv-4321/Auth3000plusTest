




# import fitz
# from django.http import HttpResponse
#
#
# def parserPdf(request):
#     pdf_document = request
#     doc = fitz.open(pdf_document)
#     print("Исходный документ", doc)
#     print(doc.metadata)
#     page_count = 0
#     parsedMessages = doc.metadata
#     for parsedMessage in parsedMessages:
#         newRecord = metadata(
#             name=parsedMessage['title'],
#             author=parsedMessage['author']
#         )
#         newRecord.save()
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
#     return HttpResponse("Done")
