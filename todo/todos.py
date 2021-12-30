from flask import request
from flask_restx import Resource, Api, Namespace, fields

todos = {}
count = 0

Todo = Namespace(
    name='todo',
    description='todo test'
)

todo_fields = Todo.model(
    'Todo', {
        'data': fields.String(
            description='a todo',
            required=True,
            example="code test"
        )
    }
)

todo_fields_with_id = Todo.inherit(
    'Todo with id',
    todo_fields,
    {
        'idx': fields.Integer(desription='a todo id')
    }
)

@Todo.route('')
class TodoPost(Resource):
    @Todo.expect(todo_fields)
    @Todo.response(200, 'success', todo_fields_with_id)
    def post(self):
        """
        create todos
        """
        global count
        global todos



        idx = count
        count+=1
        todos[idx] = request.json.get('data')

        return {
            'idx': idx,
            'data': todos[idx]
        }


@Todo.route('/<int:idx>')
@Todo.doc(params={
    'idx': 'index of todo'
})
class TodoSimple(Resource):
    @Todo.response(200, 'success', todo_fields_with_id)
    @Todo.response(500, 'failed')
    def get(self, idx):
        """
        get todos
        """
        return {
            'idx': idx,
            'data': todos[idx]
        }

    @Todo.response(202, 'success', todo_fields_with_id)
    @Todo.response(500, 'failed')
    def put(self, idx):
        """
        put todos
        """
        todos[idx] = request.json.get('data')

        return {
            'idx': idx,
            'data': todos[idx]
        }

    @Todo.response(202, 'success')
    @Todo.response(500, 'failed')
    def delete(self, idx):
        """
        delete todo
        """
        del todos[idx]

        return {
            'msg':'success',
            'status': 200
        }