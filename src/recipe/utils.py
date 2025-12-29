from io import BytesIO 
import base64
import matplotlib
matplotlib.use('Agg')
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
    fig, ax = plt.subplots(figsize=(12,6))  # explicit figure and axes

    if chart_type == 'bar':
        ax.bar(data['name'], data['cooking_time'], color=plt.cm.tab20.colors)
        ax.set_xlabel('Recipe Name')
        ax.set_ylabel('Cooking Time (min)')
        ax.set_title('Cooking Time per Recipe')
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

    elif chart_type == 'pie':
        labels = kwargs.get('labels')
        ax.pie(data['count'], labels=labels, autopct='%1.1f%%', startangle=90)
        ax.set_title('Recipes per Difficulty')

    elif chart_type == 'line':
        ax.plot(data['name'], data['ingredients_count'], marker='o', color='#d35400')
        ax.set_xlabel('Recipe Name')
        ax.set_ylabel('Number Ingredients')
        ax.set_title('Number Ingredients Used per Recipe')
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

    plt.tight_layout()

    # Save figure to base64
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    plt.close(fig)  # important: close figure

    graph = base64.b64encode(image_png).decode('utf-8')
    return graph