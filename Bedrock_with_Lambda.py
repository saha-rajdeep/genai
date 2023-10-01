import json
import boto3

boto3_bedrock = boto3.client('bedrock-runtime')

def lambda_handler(event, context):
    # TODO implement
    #print("boto3 version:"+boto3.__version__)
    #prompt_data="What is AWS?"
    prompt_data='''Meeting transcript: 
                Miguel: Hi Brant, I want to discuss the workstream  for our new product launch 
                Brant: Sure Miguel, is there anything in particular you want to discuss? 
                Miguel: Yes, I want to talk about how users enter into the product. 
                Brant: Ok, in that case let me add in Namita. 
                Namita: Hey everyone 
                Brant: Hi Namita, Miguel wants to discuss how users enter into the product. 
                Miguel: its too complicated and we should remove friction.  for example, why do I need to fill out additional forms?  I also find it difficult to find where to access the product when I first land on the landing page. 
                Brant: I would also add that I think there are too many steps. 
                Namita: Ok, I can work on the landing page to make the product more discoverable but brant can you work on the additonal forms? 
                Brant: Yes but I would need to work with James from another team as he needs to unblock the sign up workflow.  Miguel can you document any other concerns so that I can discuss with James only once? 
                Miguel: Sure. 
                From the meeting transcript above, Create a list of action items for each person. '''
        
    #formatting body for Jurassic models
    #body = json.dumps({"prompt": prompt_data, "maxTokens":500})
    
    #formatting body for claude
    body = json.dumps({"prompt": "Human:"+prompt_data+"\nAssistant:", "max_tokens_to_sample":700})
    
    #set model
    #modelId='ai21.j2-ultra-v1'
    modelId='anthropic.claude-v2'
    accept = 'application/json'
    contentType = 'application/json'
    
    #invoke model
    response = boto3_bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    print(response_body)

    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Bedrock is awesome')
    }
