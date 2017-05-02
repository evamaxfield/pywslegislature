#firebase
  documentInfo:
    documentClasses:
      0:  fill
      1:  fill
      2:  fill
      ...
      n:  fill
    documentStatus:
      0:  fill
      1:  fill
      2:  fill
      ...
      n:  fill
    documentActions:
      0:  fill
      1:  fill
      2:  fill
      ...
      n:  fill
    documentNaming:
      0:  fill
      1:  fill
      2:  fill
      ...
      n:  fill
    documents:
      #documentId:
        shortIdentifier:      fill(billId)
        longIdentifier:       fill(name)
        naming:               identity(split(billId)[0])
        shortName:            fill
        longName:             fill
        biennium:             fill
        description:          fill
        type:                 concat(originAgency + documentClass)
        class:                identity(documentClass)
        htmUrl:               fill
        htmCreateDate:        fill
        htmLastModifiedDate:  fill
        pdfUrl:               fill
        pdfCreateDate:        fill
        pdfLastModifiedDate:  fill
        status:               identity(status)
        events:
          #eventId:
            action:           identity(action)


...
  sessionInfo:
    sessions:
      #sessionId:
