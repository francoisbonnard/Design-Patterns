# cohesion & coupling

## loose coupling vs tight coupling

Des pratiques de conception telles que l'inversion de contrôle (IoC) et l'injection de dépendances (DI) sont utilisées pour réduire le couplage entre les composants d'une application.

Exemples d'utilisation de l'inversion de contrôle (IoC) et de l'injection de dépendances (DI) dans le cadre de Django/Python.

Dans Django, l'inversion de contrôle et l'injection de dépendances peuvent être atteintes à travers le système de configuration de Django, notamment en utilisant des fichiers de configuration et des paramètres.

### Exemple d'Inversion de Contrôle (IoC) avec Django :

Supposons que vous ayez une application Django appelée `myapp` avec un service qui effectue des opérations sur les données. Vous pouvez utiliser l'inversion de contrôle pour injecter ce service dans les vues.

1. **Service dans `services.py`** :

   ```python
   class DataService:
       def __init__(self, data_source):
           self.data_source = data_source

       def get_data(self):
           # Logique pour obtenir les données depuis la source de données
           return self.data_source.fetch_data()
   ```

2. **Source de données dans `data_sources.py`** :

   ```python
   class DataSource:
       def fetch_data(self):
           # Logique pour récupérer les données
           pass
   ```

3. **Configuration dans `settings.py` pour l'injection de dépendances** :

   ```python
   DATA_SOURCE = 'myapp.data_sources.DataSource'
   ```

4. **Vue dans `views.py` utilisant l'injection de dépendances** :

   ```python
   from django.conf import settings
   from django.shortcuts import HttpResponse
   from myapp.services import DataService

   def my_view(request):
       data_source_class = settings.DATA_SOURCE
       data_source = data_source_class()
       data_service = DataService(data_source)
       data = data_service.get_data()
       return HttpResponse(data)
   ```

Dans cet exemple, la classe `DataService` est injectée avec `DataSource` grâce à l'inversion de contrôle via `settings.DATA_SOURCE`.

### Exemple d'Injection de Dépendances (DI) avec Django :

Django prend en charge l'injection de dépendances via le système de vues basé sur les fonctions (Function-Based Views) et le système de classes de vues (Class-Based Views). Voici un exemple d'injection de dépendances avec les Class-Based Views :

1. **Service dans `services.py`** :

   ```python
   class DataService:
       def get_data(self):
           # Logique pour obtenir les données
           pass
   ```

2. **Vue basée sur les classes dans `views.py` utilisant l'injection de dépendances** :

   ```python
   from django.views import View
   from django.http import HttpResponse
   from myapp.services import DataService

   class MyView(View):
       def __init__(self, data_service=None, **kwargs):
           super().__init__(**kwargs)
           self.data_service = data_service or DataService()

       def get(self, request, *args, **kwargs):
           data = self.data_service.get_data()
           return HttpResponse(data)
   ```

Dans cet exemple, la classe `MyView` prend en paramètre un objet `data_service`, qui est une instance de `DataService`. Cela permet l'injection de dépendances, car vous pouvez fournir différentes implémentations de `DataService` lors de la création de l'objet `MyView`.

Ces exemples illustrent comment l'inversion de contrôle et l'injection de dépendances peuvent être utilisées dans Django pour réduire le couplage entre les composants de l'application. Cela rend votre code plus modulaire, réutilisable et facile à tester.