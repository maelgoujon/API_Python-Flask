from flask import Flask
from flask_restx import Api, Resource, fields
import db_produit

app = Flask(__name__)
api = Api(app, version='1.0', title='API boutiques en ligne',
    description='Cette API permet de créer, modifier et supprimer des produits. Elle permet également de rechercher et acheter des produits.',
)

ns_alimentaire = api.namespace('produit_alimentaire', description='Opérations liées aux produits alimentaires')
ns_techno = api.namespace('produit_techno', description='Opérations liées aux produits technologiques')


post_alimentaire = api.model('Produit Alimentaire', {
    'libelle': fields.String(required=True, description='Libellé du produit'),
    'categorie': fields.String(required=True, description='Catégorie du produit'),
    'prix': fields.Float(required=True, description='Prix du produit'),
})

get_alimentaire_one = api.model('Entité', {
    'id': fields.Integer(readOnly=True, description='Identifiant unique de l\'entité')
})

entity = api.model('Entité', {
    'id': fields.Integer(readOnly=True, description='Identifiant unique de l\'entité'),
    'libellé': fields.String(required=True, description='Libellé de l\'entité'),
    'categorie': fields.String(required=True, description='Catégorie de l\'entité'),
    'description': fields.String(required=True, description='Description de l\'entité'),
    'marque': fields.String(required=True, description='Marque de l\'entité'),
    'prix': fields.Float(required=True, description='Prix de l\'entité'),
})



@ns_alimentaire.route('/produit_alimentaire/')
class AlimentaireList(Resource):
    @ns_alimentaire.doc('list_entities', description='Permet de retourner toutes les entités')
    def get(self):
        return db_produit.obtenir_tout_alimentaire()

@ns_alimentaire.route('/produit_alimentaire/<int:id>')
class Alimentaire(Resource):
    @ns_alimentaire.doc('create_entity', description='Ajouter une nouvelle entité')
    @ns_alimentaire.expect(post_alimentaire)
    @ns_alimentaire.response(201, 'Entité créée')
    @ns_alimentaire.response(400, 'Mauvaise requête')
    def post(self, id):
        if 'libelle' in api.payload and 'categorie' in api.payload and 'prix' in api.payload:
            new_entity = api.payload
            db_produit.ajouter_alimentaire(id, new_entity['libelle'], new_entity['categorie'], new_entity['prix'])
            new_entity['id'] = id
            return new_entity, 201
        else:
            return 'Mauvaise requête', 400
    
    @ns_alimentaire.doc('get_entity', description='Permet de retourner l’entité dont l’id est spécifié en paramètre')
    @ns_alimentaire.marshal_with(get_alimentaire_one)
    def get(self, id):
        entity = db_produit.obtenir_alimentaire(id)
        if entity is None:
            api.abort(404)
        return entity

    @ns_alimentaire.doc('delete_entity', description='Permet de supprimer l’entité dont l’id est spécifié en paramètre')
    @ns_alimentaire.response(204, 'Entité supprimée')
    def delete(self, id):
        db_produit.supprimer_alimentaire(id)
        return '', 204

    @ns_alimentaire.expect(entity)
    @ns_alimentaire.marshal_with(entity)
    @ns_alimentaire.doc('update_entity', description='Permet de modifier les valeurs des champs de l’entité dont l’id est spécifié en paramètre')
    def put(self, id):
        updated_entity = api.payload
        if 'libelle' in updated_entity and 'categorie' in updated_entity and 'prix' in updated_entity:
            db_produit.mettre_a_jour_alimentaire(id, updated_entity['libelle'], updated_entity['categorie'], updated_entity['prix'])
            return updated_entity
        else:
            return 'Mauvaise requête', 400

@ns_techno.route('/produit_techno/')
class TechnoList(Resource):
    @ns_techno.doc('list_entities', description='Permet de retourner toutes les entités')
    @ns_techno.marshal_list_with(entity)
    def get(self):
        return db_produit.obtenir_tout_techno()

    @ns_techno.doc('create_entity', description='Permet d’ajouter une nouvelle entité')
    @ns_techno.expect(entity)
    @ns_techno.marshal_with(entity, code=201)
    def post(self):
        new_entity = api.payload
        if 'libelle' in new_entity and 'categorie' in new_entity and 'description' in new_entity and 'marque' in new_entity and 'prix' in new_entity:
            db_produit.ajouter_techno(new_entity['libelle'], new_entity['categorie'], new_entity['description'], new_entity['marque'], new_entity['prix'])
            return new_entity, 201
        else:
            return 'Mauvaise requête', 400
    

    @ns_techno.doc('get_entity', description='Permet de retourner l’entité dont l’id est spécifié en paramètre')
    @ns_techno.marshal_with(entity)
    def get(self, id):
        entity = db_produit.obtenir_techno(id)
        if entity is None:
            api.abort(404)
        return entity

    @ns_techno.doc('delete_entity', description='Permet de supprimer l’entité dont l’id est spécifié en paramètre')
    @ns_techno.response(204, 'Entité supprimée')
    def delete(self, id):
        db_produit.supprimer_techno(id)
        return '', 204

    @ns_techno.expect(entity)
    @ns_techno.marshal_with(entity)
    @ns_techno.doc('update_entity', description='Permet de modifier les valeurs des champs de l’entité dont l’id est spécifié en paramètre')
    def put(self, id):
        updated_entity = api.payload
        if 'libelle' in updated_entity and 'categorie' in updated_entity and 'description' in updated_entity and 'marque' in updated_entity and 'prix' in updated_entity:
            db_produit.mettre_a_jour_techno(id, updated_entity['libelle'], updated_entity['categorie'], updated_entity['description'], updated_entity['marque'], updated_entity['prix'])
            return updated_entity
        else:
            return 'Mauvaise requête', 400
    

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)