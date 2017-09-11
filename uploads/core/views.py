from django.shortcuts import render, redirect, get_object_or_404
from uploads.core.models import Document
from uploads.core.forms import DocumentForm
import pandas as pd
import seaborn as sns


def home(request):
    documents = Document.objects.all()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            ds = pd.read_csv('./media/' + documents[0].document.name)
            viz = sns.heatmap(ds.corr())
            fig = viz.get_figure()
            fig.savefig('./uploads/core/static/image/plot.png')
            documents.delete()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/home.html', {'documents': documents, 'form': form})



