# import fitz  # import the bindings
#
#
# def parce_pdf():
#     fname = "Exampl.pdf"  # get filename from command line
#     doc = fitz.open(fname)  # open document
#     pixel = doc[0] #page pdf
#     pix = pixel.get_pixmap()  # render page to an image
#     pix.save("images/page.png")  # store image as a PNG
#     print(doc.metadata)
