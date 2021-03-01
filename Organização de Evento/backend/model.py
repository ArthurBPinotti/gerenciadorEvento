from config import *
from config import db

class EspacoCafe(db.Model):
    id_cafe = db.Column(db.Integer,primary_key=True)
    cafe_nome = db.Column(db.String(40), nullable = False)
    lot1 = db.Column(db.Integer, nullable=False, default = 0)
    lot2 = db.Column(db.Integer, nullable=False, default = 0)
    def __str__(self):
        return str(self.id_cafe) + ", " + str(self.cafe_nome) + ", " + str(self.lot1) + "," + str(self.lot2)
    
    def json(self):
        return {
            "id_cafe": self.id_cafe,
            "cafe_nome": self.cafe_nome,
            "lot1": self.lot1,
            "lot2": self.lot2,
        }

class Sala(db.Model):
    id_sala = db.Column(db.Integer,primary_key=True)
    s_nome = db.Column(db.String(40), nullable = False)
    lot1 = db.Column(db.Integer, nullable=False, default = 0)
    lot2 = db.Column(db.Integer, nullable=False, default = 0)
    def __str__(self):
        return str(self.id_sala) + ", " + str(self.s_nome) + ", "+ ", " + str(self.lot1) + "," + str(self.lot2)
    
    def json(self):
        return {
            "id_sala": self.id_sala,
            "s_nome": self.s_nome,
            "lot1": self.lot1,
            "lot2": self.lot2,
        }

class Pessoa(db.Model):
    id_pessoa = db.Column(db.Integer, primary_key=True)
    p_nome = db.Column(db.String(40), nullable = False)
    p_sobrenome = db.Column(db.String(40), nullable = False)
    sala_1_id = db.Column(db.Integer,db.ForeignKey(Sala.id_sala),nullable=False)
    sala_1 = db.relationship("Sala",foreign_keys=[sala_1_id])
    sala_2_id = db.Column(db.Integer,db.ForeignKey(Sala.id_sala),nullable=False)
    sala_2 = db.relationship("Sala",foreign_keys=[sala_2_id])
    ecafe_1_id = db.Column(db.Integer,db.ForeignKey(EspacoCafe.id_cafe),nullable=False)
    ecafe_1 = db.relationship("EspacoCafe",foreign_keys=[ecafe_1_id])
    ecafe_2_id = db.Column(db.Integer,db.ForeignKey(EspacoCafe.id_cafe),nullable=False)
    ecafe_2 = db.relationship("EspacoCafe",foreign_keys=[ecafe_2_id])

    def __str__(self):
        return str(self.id_pessoa)+", "+ str(self.p_nome)+", "+str(self.p_sobrenome)+", "+str(self.sala_1_id)+", "+ str(self.sala_1)+", " + str(self.sala_2_id)+", "+ str(self.sala_2) +", "+str(self.ecafe_1_id)+", "+ str(self.ecafe_1)+", "+str(self.ecafe_2_id)+", "+ str(self.ecafe_2)
    
    def json(self):
        return {
            "id_pessoa": self.id_pessoa,
            "p_nome": self.p_nome,
            "p_sobrenome": self.p_sobrenome,
            "sala_1_id": self.sala_1_id,
            "sala_1":self.sala_1.json(),
            "sala_2_id": self.sala_2_id,
            "sala_2":self.sala_2.json(),
            "ecafe_1_id": self.ecafe_1_id,
            "ecafe_1":self.ecafe_1.json(),
            "ecafe_2_id": self.ecafe_2_id,
            "ecafe_2":self.ecafe_2.json(),
        }

if __name__ == "__main__":


    print(EspacoCafe.query.get(1))
    print(Sala.query.get(1))
    print(Pessoa.query.get(1))

