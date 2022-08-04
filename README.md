Required Python Version: 3.10.5
# Install
```bash
# install poetry
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# install app dependencies
poetry install

# install pre-commit hooks
# includes: isort, black, flake8, mypy, and bandit
poetry run pre-commit install
```

# Set up database and seed data
```bash
poetry shell
prisma db push
python widgets/utils/seed_widgets.py
```

# Run Server
```bash
poetry run start
```

# Run Tests
```bash
poetry run pytest
```

# Docs
Once the server is running go to `/docs` to see Swagger docs

# OpenAPI
Once the server is running to go `/openapi.json` to see Open API Specs