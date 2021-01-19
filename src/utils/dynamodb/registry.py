import inspect
from functools import cache
from importlib import import_module

from django.apps import apps
from django.utils.module_loading import module_has_submodule

from .nosql_models import BaseNoSQLModel

NOSQL_MODELS_MODULE_NAME = "nosql_models"


@cache
def get_nosql_models() -> dict[str, type[BaseNoSQLModel]]:
    nosql_models = {}
    for app_config in apps.app_configs.values():
        if module_has_submodule(app_config.module, NOSQL_MODELS_MODULE_NAME):
            nosql_models_module = import_module(
                f"{app_config.name}.{NOSQL_MODELS_MODULE_NAME}"
            )
            for attr_name, attr in nosql_models_module.__dict__.items():
                if inspect.isclass(attr) and issubclass(attr, BaseNoSQLModel):
                    if getattr(attr.Meta, "table_name", False):
                        nosql_models[attr_name] = attr

    return nosql_models
