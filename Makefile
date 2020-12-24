prod:
	@echo "Staring Up Production Server"
	gunicorn wsgi:application -b 0.0.0.0:5000 --workers=2 --access-logfile -

dev:
	@echo "Staring Up Dev Server"
	python manage.py run
