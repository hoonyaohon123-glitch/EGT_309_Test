from model import ModularPipelineLayoutLM

def useclass():
    processor = ModularPipelineLayoutLM()

    # 2. Define your file path and question
    file_path = "faceimg.jpeg"
    target_question = "INV-117_Naman.pdf"

    try:
        doc_image = processor.load_document(file_path)

        output = processor.ask(image=doc_image, question=target_question)
        
    except FileNotFoundError:
        print(f"\n[Error] Could not find the file '{file_path}'. Please provide a valid image path.")

if __name__ == "__main__":
    main()