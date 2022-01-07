# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

# import urllib library
from urllib.request import urlopen
import pandas
from datetime import datetime, timedelta
import json

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# parameter for urlopen
url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale-latest.json"
# store the response of URL
response = urlopen(url)
# storing the JSON response from url in data
data_json = json.loads(response.read())
bollettino_covid=data_json[0]

newurl=bollettino_covid['data'][:-9].replace('-','')  #sostituisco il trattino del formato data per avere 20211229
datetime_object = datetime.strptime(newurl, '%Y%m%d').date() #trasformo la stringa newurl in data
newurl2 = datetime_object - timedelta(days=1) #sottraggo un giorno alla data definita in newurl
newurl3=str(newurl2)[:10].replace('-','') #tolgo il trattino divisore del formato aaaa-mm-gg

url2 = 'https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale-'
url2=url2+newurl3+'.csv' #unisco la parte dell'url alla data del giorno precedente per avere il nuovo url
data = pandas.read_csv(url2)  #leggo il csv dal url del giorno precedente
tamponi_prec=(int(data['tamponi']))  #prendo il numero di tamponi del giorno precedente
tamponi_oggi=bollettino_covid['tamponi']-tamponi_prec
nuovi_casi=bollettino_covid['nuovi_positivi']
positivita=bollettino_covid['nuovi_positivi']/(bollettino_covid['tamponi']-tamponi_prec) #calcolo il tasso di positività nuovi/(differenza oggi e ieri dei tamponi)
positivita_percentage = "{:.2%}".format(positivita)     #trasformo il decimale in percentuale prima di stampare il risultato
terapia_intensiva=bollettino_covid['ingressi_terapia_intensiva']
deceduti_prec=(int(data['deceduti']))  #prendo il numero di decessi del giorno precedente
deceduti=bollettino_covid['deceduti']-deceduti_prec


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "I nuovi positivi in Italia per il giorno {datetime_object} sono {nuovi_casi}. Il numero di tamponi è pari a {tamponi_oggi}. Il tasso di positività è pari a {positivita_percentage}. Il numero di ingressi in terapia intensiva è {terapia_intensiva}. Il numero di decessi è {deceduti}. Questa skill riepiloga brevemente i numeri del bollettino giornaliero del Covid 19. Puoi chiedermi quanti nuovi casi ci sono stati oggi?. Qual'è il tasso di positività? Quanti decessi ci sono stati?".format(datetime_object=datetime_object, nuovi_casi=nuovi_casi, tamponi_oggi=tamponi_oggi, positivita_percentage=positivita_percentage, terapia_intensiva=terapia_intensiva, deceduti=deceduti)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Puoi chiedermi quanti nuovi casi ci sono stati oggi?. Qual'è il tasso di positività? Quanti decessi ci sono stati?")
                .response
        )

class CovidinfoHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("Covidinfo")(handler_input)

    def handle(self, handler_input):
        speak_output = "I nuovi positivi in Italia per il giorno {datetime_object} sono {nuovi_casi}. Il numero di tamponi è pari a {tamponi_oggi}. Il tasso di positività è pari a {positivita_percentage}. Il numero di ingressi in terapia intensiva è {terapia_intensiva}. Il numero di decessi è {deceduti}".format(datetime_object=datetime_object, nuovi_casi=nuovi_casi, tamponi_oggi=tamponi_oggi, positivita_percentage=positivita_percentage, terapia_intensiva=terapia_intensiva, deceduti=deceduti)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Puoi chiedermi quanti tamponi sono stati fatti oggi?. Quanti decessi ci sono stati?")
                .response
        )  

class tasso_positivitaHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("tasso_positivita")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Il tasso di positività è pari a {positivita_percentage}. Puoi chiedermi anche il numero di nuovi positivi o il numero di tamponi".format(positivita_percentage=positivita_percentage)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Puoi chiedermi anche il numero di nuovi positivi o il numero di tamponi")
                .response
        )
        
    
class tamponiHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Tamponi")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Il numero di tamponi è pari a {tamponi_oggi}. Puoi chiedermi anche il numero di persone in terapia intensiva o il numero di decessi".format(tamponi_oggi=tamponi_oggi)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Puoi chiedermi anche il numero di persone in terapia intensiva o il numero di decessi")
                .response
        )

class terapia_intensivaHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("terapia_intensiva")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Il numero di ingressi in terapia intensiva è {terapia_intensiva}. Puoi chiedermi anche il numero di nuovi positivi o il tasso di positività".format(terapia_intensiva=terapia_intensiva)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Puoi chiedermi anche il numero di nuovi positivi o il tasso di positività")
                .response
        )

class decessiHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("decessi")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Il numero di decessi secondo l'ultimo bollettino covid è {deceduti}. Puoi chiedermi anche il numero di tamponi effettuati oggi o il totale dei casi positivi".format(deceduti=deceduti)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Puoi chiedermi anche il numero di tamponi effettuati oggi o il totale dei casi positivi")
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Ciao, questa skill riepiloga brevemente i numeri del bollettino giornaliero del Covid 19. Puoi chiedermi quanti nuovi casi ci sono stati oggi?. Qual'è il tasso di positività? Quanti decessi ci sono stati?"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(" Puoi chiedermi quanti nuovi casi ci sono stati oggi?. Qual'è il tasso di positività?")
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Ciao, questa skill riepiloga brevemente i numeri del bollettino giornaliero del Covid 19. Puoi chiedermi quanti nuovi casi ci sono stati oggi?. Qual'è il tasso di positività? Quanti decessi ci sono stati?"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(" Puoi chiedermi quanti nuovi casi ci sono stati oggi?. Qual'è la sitauzione negli ospedali?")
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Arrivederci. Vieni a trovarmi sulla mia pagina Github Pymai73!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Non ho compreso. Prova a chiedermelo in altri termini. Puoi anche dire: chiedi a bollettino covid di oggi il numero di tamponi."
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Non ho capito. Prova chiedermi i numero di nuovi positivi o il tasso di positività. Puoi anche dire: chiedi a bollettino covid il numero di nuovi positivi"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask("Prova chiedermi i numero di nuovi positivi o il tasso di positività")
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(CovidinfoHandler())
sb.add_request_handler(tasso_positivitaHandler())
sb.add_request_handler(tamponiHandler())
sb.add_request_handler(terapia_intensivaHandler())
sb.add_request_handler(decessiHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()