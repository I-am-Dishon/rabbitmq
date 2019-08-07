import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqp://ftvnnceb:x5EaT6FHyW2MUSKCnQNQUNiBxWUG302Z@whale.rmq.cloudamqp.com/ftvnnceb')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='pdfprocess') # Declare a queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello from the other side!')

channel.basic_publish(exchange='', routing_key='pdfprocess', body='User information')

print(" [x] Sent 'Hello World!'")
connection.close()