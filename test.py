from flask import Flask, redirect, url_for, request, Response, render_template
import wikipedia

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('index.html')

@app.route('/search/<name>')
def success(message):
   return '%s' % message

@app.route('/search',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      message_body = request.form['searchkey']
      replyText = message_body    
#      print search_item['key']
      print "\n\nSearch input: ", message_body
      replyText,keyT = getReply(message_body)
#      print keyT
#      return redirect(url_for('success',name = 'aaa',message = 'csb'))
      return render_template('output.html', answer = replyText, key = keyT)
#      return '<p>' + 'Thanks for using the App, below is the response: '+ '</p>' + '<p>' + replyText + '</p>' + '<br>' + \
#         "<b><a href = '/'>click here to go back to Search</a></b>"
#      return Response(replyText, mimetype='text/plain')
   else:
      message_body = request.args.get('searchkey')
      replyText,keyT = getReply(message_body)
      return render_template('output.html', answer = replyText)


def removeHead(fromThis, removeThis):
    if fromThis.endswith(removeThis):
        fromThis = fromThis[:-len(removeThis)].strip()
    elif fromThis.startswith(removeThis):
        fromThis = fromThis[len(removeThis):].strip()    
    return fromThis

	
# Function to formulate a response based on message input.
def getReply(message):
    key = "None"
    # Make the message lower case and without spaces on the end for easier handling
    message = message.lower().strip()
    # This is the variable where we will store our response
    answer = ""
    
#    if "weather" in message:
#        answer = 'get the weather using a weather API'
            
    # is the keyword "wolfram" in the message? Ex: "wolfram integral of x + 1"
#    if "wolfram" in message:
#	  answer = 'get a response from the Wolfram Alpha API'
    
#    # is the keyword "wiki" in the message? Ex: "wiki donald trump"
#    elif "wiki" in message:
#	  answer = 'get a response from the Wikipedia API'
    # is the keyword "wiki" in the message? Ex: "wiki donald trump"
    if "wiki" in message:
        key = "wiki"
        # remove the keyword "wiki" from the message
        message = removeHead(message, "wiki")
        
        # Get the wikipedia summary for the request
        try:
	        # Get the summary off wikipedia
	        answer = wikipedia.summary(message)
        except:
            # handle errors or non specificity errors (ex: there are many people
            # named donald)
            answer = "Request was not found using wiki. Be more specific?"

    # is the keyword 'some_keyword' in the message? You can create your own custom  
    # requests! Ex: 'schedule Monday'
#    elif 'some_keyword' in message:
#	  answer = 'some response'

    # the message contains no keyword. Display a help prompt to identify possible 
    # commands
    else:
        answer = "\n Welcome! These are the commands you may use: \nWOLFRAM \"wolframalpha request\" \nWIKI \"wikipedia request\"\nWEATHER \"place\"\nSOME_KEYWORD \"some custom request\"\n"
    
    # Twilio can not send messages over 1600 characters in one message. Wikipedia
    # summaries may have way more than this. 
    # So shortening is required (1500 chars is a good bet):
#    if len(answer) > 1500:
#        answer = answer[0:1500] + "..."
    
    # return the formulated answer
    return answer, key



if __name__ == '__main__':
   app.run()
