from flask import Flask
from flask_restx import Api, Resource, fields
import db_client

app = Flask(__name__)
api = Api(app, version='1.0', title='Mon API',
    description='Cette API permet de créer, modifier et supprimer des entités',
)

ns = api.namespace('entite', description='Opérations liées à l\'entité')

entity = api.model('Entité', {
    'id': fields.Integer(readOnly=True, description='Identifiant unique de l\'entité'),
    'libellé_entité': fields.String(required=True, description='Libellé de l\'entité'),
})

@ns.route('/')
class EntityList(Resource):
    @ns.doc('list_entities', description='Permet de retourner toutes les entités')
    @ns.marshal_list_with(entity)
    def get(self):
        return db_client.obtenir_toutes_entite_bd()

    @ns.doc('create_entity', description='Permet d’ajouter une nouvelle entité')
    @ns.expect(entity)
    @ns.marshal_with(entity, code=201)
    def post(self):
        new_entity = api.payload
        db_client.ajouter_entite_bd(new_entity['id'], new_entity['libellé_entité'])
        return new_entity, 201

@ns.route('/<int:id>')
@ns.response(404, 'Entité non trouvée')
@ns.param('id', 'Identifiant de l\'entité')
class Entity(Resource):
    @ns.doc('get_entity', description='Permet de retourner l’entité dont l’id est spécifié en paramètre')
    @ns.marshal_with(entity)
    def get(self, id):
        entity = db_client.obtenir_entite_bd(id)
        if entity is None:
            api.abort(404)
        return entity

    @ns.doc('delete_entity', description='Permet de supprimer l’entité dont l’id est spécifié en paramètre')
    @ns.response(204, 'Entité supprimée')
    def delete(self, id):
        db_client.supprimer_entite_bd(id)
        return '', 204

    @ns.expect(entity)
    @ns.marshal_with(entity)
    @ns.doc('update_entity', description='Permet de modifier les valeurs des champs de l’entité dont l’id est spécifié en paramètre')
    def put(self, id):
        updated_entity = api.payload
        db_client.mettre_a_jour_entite_db(id, updated_entity['libellé_entité'])
        return updated_entity

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)