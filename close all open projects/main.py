import c4d


def main():
    document = c4d.documents.GetFirstDocument()

    while document:
        closeDocument = document
        document = document.GetNext()

        documentName = closeDocument.GetDocumentName()
        documentPath = c4d.documents.BaseDocument.GetDocumentPath(closeDocument)
        documentSave = documentPath + "\\" + documentName
        overwrite = c4d.SAVEDOCUMENTFLAGS_DONTADDTORECENTLIST
        formatt = c4d.FORMAT_C4DEXPORT
        missingAssets = []
        assets = []

        c4d.documents.SaveDocument(closeDocument, documentSave, overwrite, formatt)
        print("success " + documentName)

    c4d.documents.CloseAllDocuments()
    print("done")


if __name__ == '__main__':
    main()
