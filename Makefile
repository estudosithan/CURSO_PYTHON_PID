format:
	@echo "📌 Rodando Black..."
	@black .

	@echo "📌 Rodando isort..."
	@isort .

	@echo "📌 Rodando Flake8..."
	@flake8 . || exit /b 0  # Garante que o processo continue mesmo se Flake8 encontrar erros