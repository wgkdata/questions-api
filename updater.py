import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Questions')

questions = ["Quem você fez sorrir hoje? Foi intencional?", "O que deixa você triste?", "Hoje foi um dia típico? Por que sim ou por que não?", "Em quem você confia mais?", "Qual seu próximo maior prazo? Pelo que é?", "O que teve no seu café da manhã hoje?", "Você tem algum arrependimento hoje?", "...me faz feliz.", "Quando foi a última vez que você dançou?", "Liste as pessoas com quem você vive.", "Que medos você teve hoje?", "O que faz você esquecer?", "Eu tenho fé que....", "Qual seu programa de TV favorito?", "Quem foi a última pessoa que você beijou?", "O que você vestiu hoje?", "O que está testando você?", "Liste cinco coisas que você deveria ter feito hoje.", "Onde você passou a maior parte do seu dia?", "Compartilhe uma citação favorita.", "Com o que você se preocupou hoje?", "Seu dia foi criativo hoje? De que forma?", "Qual a próxima grande aquisição que precisa/pretende fazer?"]

for number, question in enumerate(questions):
    # print(number+1, question)

    response = table.put_item(
        Item={
            'Id': number+1,
            'Text': question
        }
    )

    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        print(f"Question with id {number+1} created: {question}")