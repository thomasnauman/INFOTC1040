from Document import Document

doc_list = []

def doc_maker():
    doc_title = input("What is the title of the document?: ")
    doc_body = input("What is in the body of the document?: ")
    doc_author = input("Who is the author of the document?: ")
    doc = Document(doc_title, doc_body, doc_author)
    doc_list.append(doc)
    return doc

def doc_printer():
    print("The following documents were input")
    for doc in doc_list:
        print(f"{doc.get_title()} was written by {doc.get_author()} and said the following: {doc.get_body()}")
    print("All done!")

def main():
    print("Welcome to the Document Maker!")
    write_a_doc = True
    while write_a_doc:
        doc_maker()
        status = input("Would you like to make more documents (y/n)?: ")
        if status != "y":
            write_a_doc = False
            doc_printer()

main()