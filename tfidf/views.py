import math
import re
from django.shortcuts import render

from tfidf.forms import TFIDFForm


class ProcessText:
    def __init__(self, text: str):
        self.text = text.lower()

    def execute(self):
        tf = self.__get_tf()
        idf = self.__get_idf()

        result = self.__get_result(tf=tf, idf=idf, limit=50)
        return result

    def __get_tf(self) -> dict:
        words = re.findall(r'\b\w+\b', self.text)
        tf = {}
        for word in words:
            tf[word] = tf.get(word, 0) + 1
        return tf

    def __get_idf(self) -> dict:
        split_text = re.split(r'[.!?]+', self.text)
        sentences = [s.strip() for s in split_text if s.strip()]

        N = len(sentences) if sentences else 1

        df = {}
        for s in sentences:
            s_words = set(re.findall(r'\b\w+\b', s))
            for word in s_words:
                df[word] = df.get(word, 0) + 1

        # idf = log((N+1)/(df+1)) + 1
        idf = {}
        for word, freq in df.items():
            idf[word] = math.log((N + 1) / (freq + 1)) + 1

        return idf

    @staticmethod
    def __get_result(tf: dict, idf: dict, limit: int=50) -> list:
        result = []
        for word in tf:
            result.append((word, tf[word], idf.get(word, 1)))

        result = sorted(result, key=lambda x: (-x[2], -x[1]))
        return result[:limit]


def upload_file(request):
    if request.method == 'POST':
        form = TFIDFForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            text = file.read().decode('utf-8')
            words_data = ProcessText(text).execute()
            return render(request, 'tfidf/upload.html', {'form': form, 'words_data': words_data})
    else:
        form = TFIDFForm()
    return render(request, 'tfidf/upload.html', {'form': form})
