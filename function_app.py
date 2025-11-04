import azure.functions as func
import logging
from blueprint import blueprint

app = func.FunctionApp()
app.register_functions(blueprint)

#@app.event_hub_message_trigger(arg_name="azeventhub", event_hub_name="test",
#                               connection="myeventhubnamespace") 
#def eventhub_trigger(azeventhub: func.EventHubEvent):
#    logging.info('My Python EventHub trigger processed an event: %s',
#                azeventhub.get_body().decode('utf-8'))


# This example uses SDK types to directly access the underlying EventData object provided by the Event Hubs trigger.
# To use, uncomment the section below and add azurefunctions-extensions-bindings-eventhub to your requirements.txt file
# import azurefunctions.extensions.bindings.eventhub as eh
# @app.event_hub_message_trigger(
#     arg_name="event", event_hub_name="myeventhub", connection="undefined"
# )
# def eventhub_trigger(event: eh.EventData):
#     logging.info(
#         "Python EventHub trigger processed an event %s",
#         event.body_as_str()
#     )



@app.queue_trigger(arg_name="azqueue", queue_name="test",
                               connection="AzureWebJobsStorage") 
def queue_trigger(azqueue: func.QueueMessage):
    logging.info('Python Queue trigger processed a message: %s',
                azqueue.get_body().decode('utf-8'))
