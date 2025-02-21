## Funcionalidades

- Criar, editar e deletar projetos (quadros).
- Criar, editar e deletar tarefas.
- Criar, editar e deletar etapas.

## Instruções para rodar o projeto

```bash
python3 -m venv venv  

source venv/bin/activate

cd server/newproject

pip install django djangorestframework django-cors-headers

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py runserver
```
