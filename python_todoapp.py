from flask import Flask, jsonify, request

app = Flask(__name__)

# todos = []
with open("private_key_argocd.txt", "r") as f:
    todos = f.read().strip()

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if 'task' in data:
        task = data['task']
        todos.append({'task': task})
        return jsonify({'message': 'Task added successfully'}), 201
    else:
        return jsonify({'error': 'Task field is required'}), 400

@app.route('/todos/<int:index>', methods=['DELETE'])
def delete_todo(index):
    if 0 <= index < len(todos):
        del todos[index]
        return jsonify({'message': 'Task deleted successfully'}), 200
    else:
        return jsonify({'error': 'Task not found'}), 404

@app.route('/todos/<int:index>', methods=['PUT'])
def update_todo(index):
    if 0 <= index < len(todos):
        data = request.get_json()
        if 'task' in data:
            todos[index]['task'] = data['task']
            return jsonify({'message': 'Task updated successfully'}), 200
        else:
            return jsonify({'error': 'Task field is required'}), 400
    else:
        return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
    # print(todos)   