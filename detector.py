import pickle
from trainer import preprocess
from trainer import encoder

class Detector:

    def __init__(self):
        # load models
        self.vect1 = pickle.load(open('models/vect1.pkl', 'rb'))
        self.vect2 = pickle.load(open('models/vect2.pkl', 'rb'))
        self.model1 = pickle.load(open('models/model1.pkl', 'rb'))
        self.model2 = pickle.load(open('models/model2.pkl', 'rb'))

    def predict(self, text):
        # Test predictions
        t1 = self.vect1.transform(preprocess([text]))
        t2 = self.vect2.transform(preprocess([text]))

        p1 = self.model1.predict(t1)
        p2 = self.model2.predict(t2)

        result = None

        if p1[0] != p2[0]:
            if p1[0] == 0:
                result = p2[0]
            else:
                result = p1[0]
        else:
            a = [0] * 17
            a[p1[0]] += 1
            a[p2[0]] += 1
            result = a.index(max(a))

        return encoder[result]