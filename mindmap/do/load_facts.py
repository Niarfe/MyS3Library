import hydraseq as hz
import pryzm as pz

dim = pz.Pryzm()._dim

def mssg(*args):
    dim("\t{}".format(" ".join(args)))

class Database:
    def __init__(self, hz_db):
        self.hydra= hz_db

    def get_seqs(self, col):
        return [nd.get_sequence() for nd in self.hydra.columns[col]]

    def list_seqs(self, col):
        if col not in self.hydra.columns.keys():
            mssg("{} not a column".format(col))
        else:
            for sequence in self.get_seqs(col):
                mssg("{}".format(sequence))
   
    def get_nexts(self, words):
        return [word for word in self.hydra.look_ahead(words).get_next_values()]

    def list_nexts(self, words):
        for word in self.get_nexts(words):
            mssg(word)



if __name__ == "__main__":
    hydra = hz.Hydraseq('lexicon')
    hydra.load_from_file('database/facts.txt')

    db = Database(hydra)






