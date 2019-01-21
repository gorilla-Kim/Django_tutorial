from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "wordcount/home.html")

def about(request):
    return render(request, "wordcount/about.html")

def result(request):
    # get data
    text = request.GET['text']
    # divide text
    words = text.split()
    # make dictionary
    word_dictionary = {}
    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word]=1
    print(word_dictionary)
    # make queryset
    context = {'text': text, 'words': words, 'total': len(words), 'dictionary':word_dictionary.items()}

    return render(request, "wordcount/result.html", context)