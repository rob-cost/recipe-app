from io import BytesIO 
import base64
import matplotlib.pyplot as plt

def get_graph():
   #create a BytesIO buffer for the image
   buffer = BytesIO()         

   #create a plot with a bytesIO object as a file-like object. Set format to png
   plt.savefig(buffer, format='png')

   #set cursor to the beginning of the stream
   buffer.seek(0)

   #retrieve the content of the file
   image_png=buffer.getvalue()

   #encode the bytes-like object
   graph=base64.b64encode(image_png)

   #decode to get the string as output
   graph=graph.decode('utf-8')

   #free up the memory of buffer
   buffer.close()

   #return the image/graph
   return graph

def get_chart(chart_type, data, **kwargs):
   #switch plot backend to AGG (Anti-Grain Geometry) - to write to file
   #AGG is preferred solution to write PNG files
    plt.switch_backend('AGG')

   #specify figure size
    fig=plt.figure(figsize=(12,6))

   #select chart_type based on user input from the form
    if chart_type == 'bar':
        plt.bar(data['name'], data['cooking_time'], color=plt.cm.tab20.colors)
        plt.xlabel('Recipe Name')
        plt.ylabel('Cooking Time (min)')
        plt.title('Cooking Time per Recipe')
        plt.xticks(rotation=45, ha='right')

    elif chart_type == 'pie':
        labels = kwargs.get('labels')
        plt.pie(data['price'], labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title('Recipes per Difficulty')

    elif chart_type == 'line':
        plt.plot(data['name'], data['cooking_time'], marker='o', color='#d35400')
        plt.xlabel('Recipe Name')
        plt.ylabel('Cooking Time (min)')
        plt.title('Cooking Time Trend')
        plt.xticks(rotation=45, ha='right')

    plt.tight_layout()
    return get_graph()    